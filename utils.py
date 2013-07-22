import numpy as np
import pandas as pd
import csv
import globals
from objects.station import Station
from geopy.point import Point
from geopy import distance
import heapq
import numpy as np
import copy
from data_pipeline import get_example_probe
from objects.station import Station
from objects.probe import Probe

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


def load_stations():
    station_file  = open('data/station_info.csv', "rb")
    station_data = csv.reader(station_file)
    stations = {}
    for name, lat, lon, elev in station_data:
        station = Station(name, lat, lon, elev)
        stations[name] = station
    return stations


def populate_stations():
    globals.STATIONS = load_stations()


def get_station(station_name):
    return globals.STATIONS[station_name]


def populate_probes():
    """
    This is just all BS for now until
    we can actually load the real probes
    """
    for i in range(10):
        name = '%s' % i
        globals.PROBES[name] = get_example_probe(name)


def get_features_at_location(lat, lon, elivation):
    station = get_closest_station(lat, lon, elivation)
    features = get_features_from_station(station)
    return features


def get_all_features(stations, probes):
    print "DUMMY 'get_all_features'"
    print probes
    return [probe.features for probe in probes]


def get_features_for_station(station):
    print "DUMMY 'get_all_features'"
    return globals.PROBES['0'].features


def train_model(features):
    print "DUMMY 'train_model'"
    return None


def find_closest_coordinates(obj1, obj2_list, num_nearest=1, distance_method=distance.GreatCircleDistance):
    distances = [find_distance(obj1, obj2, distance_method) for obj2 in obj2_list]
    max_distance = np.max(heapq.nsmallest(num_nearest, distances))
    ret = [obj2_list[idx] for idx, dist in enumerate(distances) if dist<=max_distance]
    return ret
    
def find_distance(obj1, obj2, distance_method=distance.GreatCircleDistance):
    distance.distance = distance_method
    return distance.distance(Point(obj1.lat, obj1.lon), Point(obj2.lat, obj2.lon)).miles


def classify(model, features):
    print "DUMMY 'classify'"
    return None
