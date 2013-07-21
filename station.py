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
        s += 'latitude: '+str(self.latitude)
        s += 'longitude: '+str(self.longitude)
        s += 'elevation: '+str(self.elevation)
        return s
