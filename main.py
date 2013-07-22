#!/usr/bin/env python
"""
main.py
"""
import globals
import numpy as np
from utils import populate_stations
from utils import populate_probes
from utils import get_station
from utils import get_all_features
from utils import train_model
#from utils import get_features_for_station
from utils import classify
from utils import get_probe
from sklearn.ensemble import RandomForestRegressor
import ml

def main():
    
    # in this order...
    populate_probes()
#    print globals.PROBES
    populate_stations()
#    print globals.STATIONS

    # Let's make our feature set
    # Eventually we'll pick the probe by station
    # Right now we're just hard coding the 0, 0 probe
    #all_features = get_all_features(globals.STATIONS.values(), globals.PROBES.values())
#    probe = get_probe(0, 0)
#    all_features = probe.features

    # Let's train a model
#    model = train_model(all_features)

    # Let's get a particular station
    station = get_station("ACME")
    print station.features.shape
    print station.features['target'].values

    model = RandomForestRegressor(n_estimators=10, max_depth=10)
    mae = ml.run_model(model, station.features)
    
    print mae




if __name__ =="__main__":
    main()

