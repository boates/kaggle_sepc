#!/usr/bin/env python

import globals

from geopy.point import Point
from geopy import distance

import heapq
import numpy as np
import copy


def find_distance(obj1, obj2, distance_method=distance.GreatCircleDistance):
    distance.distance = distance_method
    return distance.distance(Point(obj1.lat, obj1.lon), Point(obj2.lat, obj2.lon)).miles

def find_closest_coordinates(obj1, obj2_list, num_nearest=1, distance_method=distance.GreatCircleDistance):
    distances = [find_distance(obj1, obj2, distance_method) for obj2 in obj2_list]
    max_distance = np.max(heapq.nsmallest(num_nearest, distances))
    ret = [obj2_list[idx] for idx, dist in enumerate(distances) if dist<=max_distance]
    return ret


class Station(object):
    """
    Station class
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name  = name
        self.lat   = float(latitude)
        self.lon   = float(longitude)
        self.elev  = float(elevation)
        self.features = None

    def __str__(self):
        s  = 'name: %s\n' % self.name
        s += 'latitude: %s\n' % self.lat
        s += 'longitude: %s\n' % self.lon
        s += 'elevation: %s\n' % self.elev
        return s

    def __repr__(self):
        return self.__str__()

    def get_nearest_probe(self, probe_list):
        if len(probe_list)==0:
            return None
        nearest_probes = find_closest_coordinates(self, probe_list, num_nearest=1)
        if len(nearest_probes) > 0:
            return nearest_probes[0]
        else:
            return None

    def get_features(self):
        self.features = self.get_nearest_probe(globals.PROBES.values()).features
