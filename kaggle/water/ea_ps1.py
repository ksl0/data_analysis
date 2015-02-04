# 01/15/2015
# Katie Li
# the intention of this is to get the hang of python and avoid Excel 
# and make a really simple graph
# readin file that takes discharge for cubic feet per second

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

df = pd.read_csv("nasa_temp.txt", header=4, delim_whitespace=True)

# create temporary variables
# to hold Year and mean temperature
# then concatenate them

dY = df.Year.convert_objects(convert_numeric=True).dropna()
dT = df['J-D'].convert_objects(convert_numeric=True).dropna()
df_simplified = pd.concat([dY, dT], axis=1)

## graph the first part
plt.cla()
plt.title("\n".join(wrap('Combined Surface Temperature Anomalies: Yearly Mean', 40)))
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Temperature Anomolies (degrees Celsius)', fontsize = 12, color='black')
plt.plot(df_simplified.Year, df_simplified['J-D'],color="#078ccc",marker='o')
plt.savefig('EA_assignments/yearly_mean.png')

plt.cla()
# calculate decale moving average
#shift to account for the excel formatting
temp_mva = pd.rolling_mean(df_simplified, window=10).shift(-2).dropna()


plt.title("\n".join(wrap('Combined Surface Temperature Anomalies: Moving Average', 40)))
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Temperature (degrees Celsius)', fontsize = 12, color='black')
plt.plot(temp_mva.Year, temp_mva['J-D'], color="#078ccc",marker='o')
plt.savefig('EA_assignments/moving_average.png')

plt.cla()
#now find the 5-year average for python
df_simplified['binned_year'] = (np.floor(df_simplified.dropna()*1./5)*5).Year
df_5year= df_simplified.groupby('binned_year').mean()

plt.title("\n".join(wrap('Combined Surface Temperature Anomalies: Five Year Average', 40)))
plt.xlabel('Year', fontsize=12, color='black')
plt.ylabel('Temperature (degrees Celsius)', fontsize = 12, color='black')
plt.plot(df_5year.Year, df_5year['J-D'], color="#078ccc",marker='o')
plt.savefig('EA_assignments/five_year.png')

plt.cla()


