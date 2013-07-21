

import pandas as pd
import csv

from station import Station
from geopy.point import Point
import heapq
import numpy as np

STATION_INFO = {}

def _year(n):
    return str(n)[:4]

def _month(n):
    return str(n)[4:6]

def _day(n):
    return str(n)[6:]

def _datestring(n):
    return _year(n) + '-' + _month(n) + '-' + _day(n)

#example usage: df.index = datestring_index(df.Date)
def datestring_index(date_int_list):
    pd.to_datetime([_datestring(n) for n in date_int_list])

def populate_stations():
    # load the csv

    station_file  = open('data/station_info.csv', "rb")
    station_data = csv.reader(station_file)
    #station_data = load_csv("data/station_info.csv")

    for name, lat, lon, elev in station_data:
        station = Station(name, lat, long, elev)
        STATION_INFO[name] = station

def get_station(station_name):
    return STATION_INFO[station_name]

def find_closest_coordinates(coord1, coord2_list, n=1, distanceMethod = distance.GreatCircleDistance):
    distance.distance = distanceMethod  
    distances = [distance.distance(Point(coord1['lat'], coord1['lon'],coord1['elev']), Point(coord2['lat'], coord2['lon'],coord2['elev'])).miles for idx, coord2 in coord2_list.iterrows()]
    maxd = np.max(heapq.nsmallest(n, distances))
    return coord2_list[(distances<=maxd)]

def main():
    populate_stations()

if __name__ =="__main__":
    main()
    print STATION_INFO

