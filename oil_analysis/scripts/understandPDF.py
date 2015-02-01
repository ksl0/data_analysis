## 01-30-2015
## Purpose: to know how to better use dataframes

import pandas as pd

df = pd.read_csv('../csv/API_County_codes.csv', header=0, delim_whitespace=True)

headers = df.columns.get_values()

df_ = df[[headers[0], headers[1]]]
df__ = df[[headers[2], headers[3]]] 
df__.columns = [headers[0], headers[1]]

df3 = pd.concat([df_, df__])
  

  







