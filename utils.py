import numpy as np
import pandas as pd
import csv
import globals
import pandas
from objects.station import Station

from data_pipeline import get_example_probe
from data_pipeline import get_probe_features
from data_pipeline import get_station_targets

from objects.station import Station
from objects.probe import Probe

N_LAT = 9
N_LON = 16

def _year(n):
    return str(n)[:4]


def _month(n):
    return str(n)[4:6]


def _day(n):
    return str(n)[6:]


def _datestring(n):
    return _year(n) + '-' + _month(n) + '-' + _day(n)


def datestring_index(date_int_list):
    """
    Takes a list of date integers and returns a pandas time series. Useful for adding a time series index to a pandas
    dataframe.

    Example Usage: df.index = datestring_index(df.Date)


    A date integer is an integer of the form yyyymmdd
    """
    return pd.to_datetime([_datestring(n) for n in date_int_list])


def load_stations(path='data/station_info.csv'):
    df = pandas.read_csv(path)
    stations = {}

    # Load the targets for all stations
    targets = get_station_targets()
    for idx, (name, lat, lon, elev) in df.iterrows():
        station = Station(name, lat, lon, elev)
        station.get_features()
        print station.features.shape
        print targets[name].shape
        
        station.features = station.features.merge(targets, on=('Date'))
#        station.features[globals.TARGET] = targets[name]
        stations[name] = station
    return stations


def populate_stations():
    globals.STATIONS = load_stations()


def get_station(station_name):
    return globals.STATIONS[station_name]


def populate_probes():
    """
    Returns the i, jth probe
    """
    # Get the dataframe for all features
    all_features = get_probe_features()
    for lat in range(N_LON):
        for lon in range(N_LAT):
            probe_features = all_features[(all_features['lat']==lat) & (all_features['lon']==lon)]
            probe = Probe(lat, lon)
            probe.features = probe_features
            globals.PROBES[(lat, lon)] = probe


def get_probe(i, j):
    return globals.PROBES[(i, j)]


def get_features_at_location(lat, lon, elivation):
    station = get_closest_station(lat, lon, elivation)
    features = get_features_from_station(station)
    return features


def get_all_features(stations, probes):
    print "DUMMY 'get_all_features'"
    print probes
    return [probe.features for probe in probes]


def train_model(features):
    print "DUMMY 'train_model'"
    return None

def classify(model, features):
    print "DUMMY 'classify'"
    return None



