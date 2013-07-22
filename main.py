#!/usr/bin/env python
"""
main.py
"""
import globals
import numpy as np
from utils import populate_stations
from utils import populate_probes
from utils import get_station
from utils import get_probe
from sklearn.ensemble import RandomForestRegressor
import ml

def main():
    
    # in this order...
    populate_probes()
    populate_stations()
    
    # Let's get a particular station
    station = get_station("ACME")
    print station.features.shape
    
    model = RandomForestRegressor(n_estimators=1000)
    
    remove_names = ['lat', 'lon', 'Date']
    feature_names = [c for c in station.features.columns if c not in remove_names]
    
    metric = ml.run_model(model, station.features[feature_names])    
    print metric
    
#    metrics = ml.run_models(10, model, station.features[feature_names])    
#    print np.mean(metrics)



if __name__ =="__main__":
    main()

