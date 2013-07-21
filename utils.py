import pandas as pd

df = pd.read_csv('./data/train.csv')
def _year(n):
    return str(n)[:4]
def _month(n):
    return str(n)[4:6]
def _day(n):
    return str(n)[6:]
def datestring(n):
    return _year(n) + '-' + _month(n) + '-' + _day(n)


df.index = pd.to_datetime([datestring(n) for n in date_list])
