
import random
from objects.probe import Probe

from pandas import Series
from pandas import DataFrame
from pandas import read_csv

import pickle

from datetime import datetime


def get_probe_features():

    file = open('data/features/Minimum_temperature.pkl')
    df1 = pickle.load(file)

    file = open('data/features/Maximum_temperature.pkl')
    df2 = pickle.load(file)

    #return all_features = df1.merge(df2, on=('day_num', 'lat', 'lon'))
    return df1.merge(df2, on=('day_num', 'lat', 'lon'))



    #return df1

"""
    feature_files = ['Minimum_temperature', 'Maximum_temperature']

    features = None

    for file in feature_files:
        file = open('data/features/%s.pkl' % file)
        df = pickle.load(file)
        if features=None:
            features = df
        else:
            features.merge(df, on)

        return df
"""

def _get_datetime_from_station(date_string):
    return datetime.strptime(str(date_string),'%Y%m%d')


def get_station_targets():
    df = read_csv("data/train.csv")
    df['Date'] = df['Date'].map(_get_datetime_from_station) #datestring_index(df['Date']) #.map(_convert_station_date_to_datetime)
    return df


def get_example_probe_features():

    data = DataFrame()

    features = {
        'apcp_sfc3' : random.random(),
        'dlwrf_sfcDownward' : random.random(),
        'dswrf_sfcDownward' : random.random(),
        'pres_mslAir' : random.random(),
        'pwat_eatmPrecipitable' : random.random(),
        'spfh_2mSpecific' : random.random(),
        'tcdc_eatmTotal' : random.random(),
        'tcolc_eatmTotal' : random.random(),
        'tmax_2m' : random.random(),
        'tmin_2m' : random.random(),
        'tmp_2m' : random.random(),
        'tmp_sfc' : random.random(),
        'ulwrf_sfc' : random.random(),
        'ulwrf_tatm' : random.random(),
        'uswrf_sfc' : random.random()}

    return DataFrame(features, index=range(1))


def get_example_probe(name):
    probe = Probe(name, 0.0, 0.0, 0.0)
    probe.features = get_example_probe_features()
    return probe


def main():
    df = get_station_targets()
    print df.head()
    print df['Date']

if __name__=="__main__":
    main()

