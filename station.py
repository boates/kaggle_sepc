#!/usr/bin/env python

class Station(object):
    """
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name  = name
        self.lat   = latitude
        self.long  = longitude
        self. elev = elevation
        
    def __repr__(self):
        s  = 'name: '+str(self.name)
        s += 'latitude: '+str(self.lat)
        s += 'longitude: '+str(self.long)
        s += 'elevation: '+str(self.elev)
        return s
