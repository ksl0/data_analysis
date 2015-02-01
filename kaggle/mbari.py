import pandas as pd
import numpy as np

# For .read_csv, always use header=0 when you know row 0 is the header row
df = pd.read_csv('chlorophyll_data.csv', header=0)

# this would make the chlorophyll okay :D, eliminates -99999 data :D 
#df[df['chlorophyll[unit="mg.m-3"]'] > -999999]
# df2 = df[df['chlorophyll[unit="mg.m-3"]'] > 0][["date", 'chlorophyll[unit="mg.m-3"]']]
