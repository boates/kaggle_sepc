#!/usr/bin/env python

import globals

import numpy as np
import pandas as pd

from geopy.point import Point
from geopy import distance

import heapq
import copy


def find_distance(a, b, distance_method=distance.GreatCircleDistance):
    distance.distance = distance_method
    return distance.distance(Point(a.lat, a.lon), Point(b.lat, b.lon)).miles

def find_closest_coordinates(obj1, obj2_list, num_nearest=1, distance_method=distance.GreatCircleDistance):
    distances = [find_distance(obj1, obj2, distance_method) for obj2 in obj2_list]
    max_distance = np.max(heapq.nsmallest(num_nearest, distances))
    ret = [obj2_list[idx] for idx, dist in enumerate(distances) if dist <= max_distance]
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
        self.features = pd.DataFrame([])

    def __str__(self):
        s  = 'name: %s\n' % self.name
        s += 'latitude: %s\n' % self.lat
        s += 'longitude: %s\n' % self.lon
        s += 'elevation: %s' % self.elev
        return s

    def __repr__(self):
        return self.__str__()

    def get_nearest_probe(self, probe_list):
        if len(probe_list) == 0:
            return None
        nearest_probes = find_closest_coordinates(self, probe_list, num_nearest=1)
        if len(nearest_probes) > 0:
            return nearest_probes[0]
        else:
            return None

    def get_nearest_features(self):
        probe_list = globals.PROBES.values()
        nearest_probe = self.get_nearest_probe(probe_list)
        self.features = nearest_probe.features
        
    def get_features(self):
        self.get_nearest_features()
#        for (i,j), probe in globals.PROBES.iteritems():
            
#            if len(self.features) == 0:
#                self.features = pd.DataFrame(index=range(len(probe.features)))
                
#            for feature_name in [c for c in probe.features.columns if c not in globals.IGNORE_FEATURES]:
#                self.features[feature_name+'_%s_%s' % (i, j)] = probe.features[feature_name]
    
        
        
        
        
        
        
