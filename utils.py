import numpy as np
import pandas as pd
import csv


from objects.station import Station


from geopy.point import Point
from geopy import distance
import heapq
import numpy as np
import copy

from data_pipeline import get_example_probe
from objects.station import Station
from objects.probe import Probe
import globals


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
        station = Station(name, lat, long, elev)
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


#def get_features_from_station(station_name):
#    return []


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

def find_closest_coordinates(coord1, coord2_list, n=1, distanceMethod = distance.GreatCircleDistance, getDistances = False):
    distance.distance = distanceMethod  
    distances = [distance.distance(Point(coord1['lat'], coord1['lon'],coord1['elev']), Point(coord2['lat'], coord2['lon'],coord2['elev'])).miles for idx, coord2 in coord2_list.iterrows()]
    maxd = np.max(heapq.nsmallest(n, distances))
    if getDistances:
        df_ret = copy.deepcopy(coord2_list)
        df_ret['dist'] = distances
        return df_ret[df_ret['dist']<=maxd]
    else:
        return coord2_list[(distances<=maxd)]

def classify(model, features):
    print "DUMMY 'classify'"
    return None
