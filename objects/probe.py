#!/usr/bin/env python

class Probe(object):
    """
    Probe class
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name = name
        self.lat  = latitude
        self.lon  = longitude
        self.elev = elevation
        self.features = None

    def __str__(self):
        s  = 'name: '+self.name+'\n'
        s += 'latitude: '+self.lat+'\n'
        s += 'longitude: '+self.lon+'\n'
        s += 'elevation: '+self.elev+'\n'
        return s
    
    def __repr__(self):
        return self.__str__()
    
