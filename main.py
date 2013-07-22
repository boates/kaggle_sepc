#!/usr/bin/env python
"""
main.py
"""
import globals
from utils import populate_stations
from utils import populate_probes
from utils import get_station
from utils import get_all_features
from utils import train_model
#from utils import get_features_for_station
from utils import classify
from utils import get_probe


def main():

    populate_probes()
    print globals.PROBES

    populate_stations()
    print globals.STATIONS

    # Let's make our feature set
    # Eventually we'll pick the probe by station
    # Right now we're just hard coding the 0, 0 probe
    #all_features = get_all_features(globals.STATIONS.values(), globals.PROBES.values())
    probe = get_probe(0, 0)
    all_features = probe.features

    # Let's train a model
    model = train_model(all_features)

    # Let's get a particular station
    station = get_station("ACME")

    # Let's get the features for this station
    acme_features = station.features #get_features_for_station(station)

    # Now, let's try to classify
    classification = classify(model, acme_features)

    print classification


if __name__ =="__main__":
    main()

