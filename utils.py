import pandas as pd

def _year(n):
    return str(n)[:4]
    
def _month(n):
    return str(n)[4:6]
    
def _day(n):
    return str(n)[6:]
    
def _datestring(n):
    return _year(n) + '-' + _month(n) + '-' + _day(n)

#example usage: df.index = datestring_index(df.Date)
def datestring_index(date_int_list):
    pd.to_datetime([_datestring(n) for n in date_int_list])
