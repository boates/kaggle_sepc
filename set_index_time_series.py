import pandas as pd

df = pd.read_csv('./data/train.csv')
def year(n):
    return str(n /10000)
def month(n):
    return str(n % 10000 / 100)
def day(n):
    return str(n % 100)
def datestring(n):
    return year(n) + '-' + month(n) + '-' + day(n)
df.index = pd.to_datetime([datestring(n) for n in df.Date])
