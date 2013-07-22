
import random
from objects.probe import Probe

import numpy as np
import pandas as pd
from pandas import Series
from pandas import DataFrame
from pandas import read_csv

import pickle
import glob

import datetime

def get_probe_features(path='data/features/', start_date='19940101'):
    
    filepaths = glob.glob(path+'*.pkl')
    
    features = pd.DataFrame([])
    for f in filepaths:
        
        df = pickle.load(open(f))
        ens_names = df.columns[3:]
        
        feature_names = [f.split('/')[-1].split('.')[0]+'_'+ens for ens in ens_names]
        rename_dict = dict(zip(ens_names, feature_names))
        
        df = df.rename(columns=rename_dict)
        
        if len(features) == 0:
            features = df
        else:
            features = features.merge(df, on=('day_num', 'lat', 'lon'))
            
    start_date = datetime.datetime.strptime(str(start_date),'%Y%m%d')
    
    def day_num_to_datetime(i):
        return start_date + datetime.timedelta(days=int(i))
    
    features['Date'] = features['day_num'].map(day_num_to_datetime)
    del features['day_num']
    
    return features


def _get_datetime_from_station(date_string):
    return datetime.datetime.strptime(str(date_string),'%Y%m%d')


def get_station_targets():
    df = read_csv("data/train.csv")
    df['Date'] = df['Date'].map(_get_datetime_from_station)
    return df


def get_example_probe_features():

    data = DataFrame()

    features = {
        'apcp_sfc3' : random.random(),
        'dlwrf_sfcDownward' : random.random(),
        'dswrf_sfcDownward' : random.random(),
        'pres_mslAir' : random.random(),
        'pwat_eatmPrecipitable' : random.random(),
        'spfh_2mSpecific' : random.random(),
        'tcdc_eatmTotal' : random.random(),
        'tcolc_eatmTotal' : random.random(),
        'tmax_2m' : random.random(),
        'tmin_2m' : random.random(),
        'tmp_2m' : random.random(),
        'tmp_sfc' : random.random(),
        'ulwrf_sfc' : random.random(),
        'ulwrf_tatm' : random.random(),
        'uswrf_sfc' : random.random()}

    return DataFrame(features, index=range(1))


def get_example_probe(name):
    probe = Probe(name, 0.0, 0.0, 0.0)
    probe.features = get_example_probe_features()
    return probe


def main():
    df = get_station_targets()
    print df.head()
    print df['Date']

if __name__=="__main__":
    main()

