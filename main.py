
from utils import *

from utils import populate_stations
from utils import populate_probes
from utils import get_station

import globals


def main():

    populate_stations()
    print globals.STATIONS

    populate_probes()
    print globals.PROBES

    # Let's make our feature set
    all_features = get_all_features(globals.STATIONS.values(), globals.PROBES.values())

    # Let's train a model
    model = train_model(all_features)

    # Let's get a particular station
    station = get_station("ACME")

    # Let's get the features for this station
    acme_features = get_features_for_station(station)

    # Now, let's try to classify
    classification = classify(model, acme_features)

    print classification


if __name__ =="__main__":
    main()

