import numpy as np
import pandas as pd
import globals
import pickle
import glob
import datetime

from objects.station import Station
from objects.probe import Probe

def get_station_targets(path='data/train.csv'):
    df = pd.read_csv(path)
    df['Date'] = df['Date'].map(lambda x: datetime.datetime.strptime(str(x),'%Y%m%d').date())
    return df


def load_stations(path='data/station_info.csv'):
    df = pd.read_csv(path)
    stations = {}
    
    targets = get_station_targets()
    targets = targets[(targets['Date'] <= datetime.date(1994, 4, 10))]
    
    for idx, (name, lat, lon, elev) in df.iterrows():
        station = Station(name, lat, lon, elev)
        station.get_features()
        station.features[globals.TARGET] = targets[name]
        stations[name] = station
    return stations


def populate_stations():
    globals.STATIONS = load_stations()

def get_station(station_name):
    return globals.STATIONS[station_name]


def get_probe_features(path='data/features/', start_date='19940101'):
    
    filepaths = glob.glob(path+'*.pkl')
    
    features = pd.DataFrame([])
    for f in filepaths:
        
        df = pickle.load(open(f))
        ens_names = df.columns[3:]
        feature_name = f.split('/')[-1].split('.')[0]
        
        df2 = df[['day_num', 'lat', 'lon']]
        df2[feature_name+'_mean'] = df[ens_names].mean(axis=1)
        df = df2
        
#        feature_names = [feature_name+'_'+ens for ens in ens_names]
#        rename_dict = dict(zip(ens_names, feature_names))        
#        df = df.rename(columns=rename_dict)
        
        if len(features) == 0:
            features = df
        else:
            features = features.merge(df, on=('day_num', 'lat', 'lon'))
            
    start_date = datetime.datetime.strptime(str(start_date),'%Y%m%d')
    
    def day_num_to_datetime(i):
        return (start_date + datetime.timedelta(days=int(i))).date()
    
    features['Date'] = features['day_num'].map(day_num_to_datetime)
    del features['day_num']
    
    return features


def populate_probes():
    all_features = get_probe_features()
    for lat in range(globals.N_LON):
        for lon in range(globals.N_LAT):
            probe_features = all_features[(all_features['lat']==lat) & (all_features['lon']==lon)]
            probe = Probe(lat, lon)
            probe.features = probe_features
            probe.features.index = range(len(probe.features))
            globals.PROBES[(lat, lon)] = probe


def get_probe(i, j):
    return globals.PROBES[(i, j)]


def main():
    pass


if __name__=="__main__":
    main()


