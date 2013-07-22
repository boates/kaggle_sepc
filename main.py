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
    print station.features['target'].values

    model = RandomForestRegressor(n_estimators=10, max_depth=10)
    mae = ml.run_model(model, station.features)
    
    print mae




if __name__ =="__main__":
    main()

