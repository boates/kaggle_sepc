#!/usr/bin/env python
import itertools
import pandas as pd
import os
import pickle as pkl

from netCDF4 import Dataset

for filename in os.listdir('./data/train/'):
  data = Dataset('/Users/kkwteh/Development/kaggle_sepc/data/train/' + filename, 'r', format='NETCDF4')

  var_name = data.variables.keys()[-1]
  v = data.variables[var_name]

  columns = ['day_num', 'lat', 'lon']
  columns.extend(["ens%02d" % i for i in range(11)])
  it = itertools.product(range(100), range(v.shape[3]), range(v.shape[4]))
  rows = []
  for a,b,c in it:
    row = [a,b,c]
    row.extend([v[a,i,0,b,c] for i in range(11)])
    rows.append(row)

  df = pd.DataFrame(rows, columns=columns)

  with open('./data/train_pkl/{0}.pkl'.format(var_name), 'wb') as f:
    pkl.dump(df,f)
