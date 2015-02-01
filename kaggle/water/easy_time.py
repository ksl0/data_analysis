# 01/15/2015
# the intention of this is to get the hang of python 
# and make a really simple graph
# readin file that takes discharge for cubic feet per second

import pandas as pd
import numpy as np
import pylab as P
import matplotlib.pyplot as plt

df = pd.read_csv("10_year_water_data.txt", header=26, delim_whitespace=True)
df['discharge'] = df['04_00060_00003']

# find the local max

local_max = df[df.discharge > 4700] 


pp = df.discharge.plot(lw=2, color="#078CCC")

plt.annotate('Colorado 2014 Floods', xy = (3163, local_max.discharge), xytext = (1500, local_max.discharge -700), arrowprops = dict(facecolor="black", shrink=0.05),)


plt.savefig('North_Boulder_Stream_Flows.png')
