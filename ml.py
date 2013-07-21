#!/usr/bin/env python
"""
ml.py

Machine learning tools
"""
import numpy as np
import pandas as pd
import random
from sklearn.base import clone
from sklearn.ensemble import RandomForestRegressor

def mean_absolute_error(predictions, target):
    """
    return: float | mean absolute error (per example)
    params:
       predictions | 1D array of predicted values
            target | 1D array of actual values
    """
    return np.sum( abs(predictions - target) ) / float(len(target))


def evaluation_metric(predictions, target, metric_fnc=mean_absolute_error):
    """
    return: float | evaluation metric
                    (i.e. mean absolute error 
                    per prediction example)
    params:
       predictions | 1D array of predicted values
            target | 1D array of actual values
        metric_fnc | method returning an evaluation metric as a float
    """
    return metric_fnc(predictions, target)


def split_data(df, train_frac=0.70, shuffle=True):
    """
    return: df_train, df_predict | pd.DataFrame's
    
    params:
              df: pd.DataFrame | entire training data
      train_frac: float        | fraction of data for training (default=0.70)
                               | (fraction of prediction data is 1-train_frac)
    """
    N = len(df)
    indices = range(N)
    if shuffle:
        random.shuffle(indices)
        
    train_len = int(N*train_frac)
        
    df_train   = df.ix[indices[:train_len]]
    df_predict = df.ix[indices[train_len:]]
    
    return df_train, df_predict


def train_model(model, df_train, target_name='target'):
    """
    return:
        trained model object
    params:
            model: model object | (i.e. sklearn.ensemble.RandomForestRegressor)
         df_train: pd.DataFrame | feature & target data to train on
      target_name: string       | name of target column in df
    """
    feature_names = [c for c in df_train.columns if c != target_name]
    return model.fit(df_train[feature_names].values, df_train[target_name])


def make_predictions(trained_model, df_predict, target_name='target'):
    """
    return:
        trained model object
    params:
      trained_model: trained model object | (i.e. sklearn.ensemble.RandomForestRegressor)
         df_predict: pd.DataFrame | feature data for predicting
        target_name: string       | name of target column in df
    """
    feature_names = [c for c in df_predict.columns if c != target_name]
    return trained_model.predict(df_predict[feature_names].values)


def run_model(model, df, target_name='target', **kwargs):
    """
    Train a model and make predictions, return a metric
    
    return:
        float | evaluation metric (i.e. mean absolute error)
    params:
            model: model object | (i.e. sklearn.ensemble.RandomForestRegressor)
               df: pd.DataFrame | feature & target data to train and predict on
      target_name: string       | name of target column in df
         **kwargs: optional args
    """
    df_train, df_predict = split_data(df, **kwargs)
    
    trained_model = train_model(model, df_train)
    
    predictions = make_predictions(trained_model, df_predict)
    
    return evaluation_metric(predictions, df_predict[target_name].values)


def run_models(n_runs, model, df, target_name='target', **kwargs):
    """
    Run several models to accumulate evaluation statistics
    
    return:
    
    params:
           n_runs: int          | number of experiments to run
            model: model object | (i.e. sklearn.ensemble.RandomForestRegressor)
               df: pd.DataFrame | feature & target data to train and predict on
      target_name: string       | name of target column in df
         **kwargs: optional args
    """
    metrics = []
    for i in range(n_runs):
        model_clone = clone(model)
        metrics.append( run_model(model_clone, df, **kwargs) )
    return metrics


def main():
    
    # Generate fake data
    N = 100
    df = pd.DataFrame(index=range(N))
    df['feature1'] = np.random.rand(N)*N
    df['feature2'] = (np.random.rand(N)*N)**0.5
    df['feature3'] = (np.random.rand(N)*N)**2
    df['feature4'] = np.log(np.random.rand(N)*N)
    df['target']   = np.arange(N)
    
    # Evaluate the models built on fake data
    model = RandomForestRegressor(n_estimators=10, max_depth=10)
    metrics = run_models(10, model, df)
    
    # report the average metric
    print 'You got: ', np.mean(metrics),
    print '- This should be around 25 or 30'

    
if __name__ == '__main__':
    main()
