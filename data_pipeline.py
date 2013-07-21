import random
from objects.probe import Probe
from pandas import Series
from pandas import DataFrame

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
