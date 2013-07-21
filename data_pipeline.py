
from probes import Probe

from pandas import Series, DataFrame

def get_example_probe_features():

    data = DataFrame()

    features = {
        'apcp_sfc3' : Series(0),
        'dlwrf_sfcDownward' : Series(0),
        'dswrf_sfcDownward' : Series(0),
        'pres_mslAir' : Series(0),
        'pwat_eatmPrecipitable' : Series(0),
        'spfh_2mSpecific' : Series(0),
        'tcdc_eatmTotal' : Series(0),
        'tcolc_eatmTotal' : Series(0),
        'tmax_2m' : Series(0),
        'tmin_2m' : Series(0),
        'tmp_2m' : Series(0),
        'tmp_sfc' : Series(0),
        'ulwrf_sfc' : Series(0),
        'ulwrf_tatm' : Series(0),
        'uswrf_sfc' : Series(0)}

    return DataFrame(features, index=range(1))


def get_example_probe(name):
    probe = Probe(name, 0.0, 0.0, 0.0)
    probe.features = get_example_probe_features()
    return probe
