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
        s  = '(i, j): (%s,%s) \n' % (self.i, self.j)
        s += 'latitude: %s\n' % self.lat
        s += 'longitude: %s' % self.lon
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def _get_lat(self, lat_0=31):
        return lat_0 + self.i
    
    def _get_lon(self, lon_0=106):
        return -(lon_0 - self.j)
    

        
