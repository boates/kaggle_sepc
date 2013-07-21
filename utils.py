
import pandas as pd
import csv

from station import Station

# Global variables (for now)
STATIONS = {}
PROBES = {}


def _year(n):
    return str(n)[:4]

def _month(n):
    return str(n)[4:6]

def _day(n):
    return str(n)[6:]

def _datestring(n):
    return _year(n) + '-' + _month(n) + '-' + _day(n)

def datestring_index(date_int_list):
    return pd.to_datetime([_datestring(n) for n in date_int_list])

def populate_stations():
    station_file  = open('data/station_info.csv', "rb")
    station_data = csv.reader(station_file)
    for name, lat, lon, elev in station_data:
        station = Station(name, lat, long, elev)
        STATIONS[name] = station


def get_station(station_name):
    return STATIONS[station_name]


def get_features_from_station(station_name):
    return []


def get_features_at_location(lat, lon, elivation):
    station = get_closest_station(lat, lon, elivation)
    features = get_features_from_station(station)
    return features


def main():
    populate_stations()

if __name__ =="__main__":
    main()
    print STATION_INFO
