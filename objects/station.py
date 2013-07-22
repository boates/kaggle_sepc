#!/usr/bin/env python

import globals

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

    def get_nearest_probe(self, probe_list = globals.PROBES):
        nearest_probes =  find_closest_coordinates(self, probe_list, num_nearest)
        if len(nearest_probes)>0:
            return nearest_probes[0]
        else:
            return None
    
