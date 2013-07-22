#!/usr/bin/env python

class Station(object):
    """
    Station class
    """
    def __init__(self, name, latitude, longitude, elevation):
        self.name  = name
        self.lat   = latitude
        self.lon   = longitude
        self.elev  = elevation

    def __str__(self):
        s  = 'name: '+str(self.name)+'\n'
        s += 'latitude: '+str(self.lat)+'\n'
        s += 'longitude: '+str(self.lon)+'\n'
        s += 'elevation: '+str(self.elev)+'\n'
        return s
    
    def __repr__(self):
        return self.__str__()
    
