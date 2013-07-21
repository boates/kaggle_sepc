#!/usr/bin/env python

class Probe(object):
    """
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name = name
        self.lat  = latitude
        self.long = longitude
        self.elev = elevation
        self.features = None

    def __repr__(self):
        s  = 'name: '+self.name+'\n'
        s += 'latitude: %s \n' % self.lat
        s += 'longitude: %s \n' % self.long
        s += 'elevation: %s \n' % self.elev
        return s
