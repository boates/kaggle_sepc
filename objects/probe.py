#!/usr/bin/env python

class Probe(object):
    """
    Probe class
    """
    def __init__(self, i, j):
        self.i   = i
        self.j   = j
        self.lat = self._get_lat()
        self.lon = self._get_lon()
        self.features = None
    
    def __str__(self):
        s  = '(i, j): ('+self.i+','+self.j+')'+'\n'
        s += 'latitude: '+self.lat+'\n'
        s += 'longitude: '+self.lon+'\n'
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def _get_lat(lat_0=31):
        return lat_0 + self.i
    
    def _get_lon(lon_0=106):
        return lon_0 - self.j
    

        