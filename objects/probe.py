#!/usr/bin/env python

class Probe(object):
    """
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name = name
        self.lat  = latitude
        self.long = longitude
        self.elev = elevation
    
    def __repr__(self):
        s  = 'name: '+self.name+'\n'
        s += 'latitude: '+self.lat+'\n'
        s += 'longitude: '+self.long+'\n'
        s += 'elevation: '+self.elev+'\n'
        return s