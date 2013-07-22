#!/usr/bin/env python
"""
main.py
"""
import globals
import numpy as np
import time
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
    
    t0 = time.time()
    station_metrics = {}
    for station in globals.STATIONS.values():
    
        model = RandomForestRegressor(n_estimators=globals.N_ESTIMATORS)    
        feature_names = [c for c in station.features.columns if c not in globals.IGNORE_FEATURES]
    
        metric = ml.run_model(model, station.features[feature_names])    
        station_metrics[station.name] = metric
    
        print station.name, time.time() - t0

#        metrics = ml.run_models(10, model, station.features[feature_names])    
#        print np.mean(metrics)

    print np.mean(station_metrics.values())


if __name__ =="__main__":
    main()

