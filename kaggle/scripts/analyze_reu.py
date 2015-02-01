import pandas as pd
import numpy as np
import pylab as P
import re

# 01/22/2015
# GOAL: to analyze REU data, graph it, see the best place to be an intern
# REACH GOAL: develop web application wrapper that helps visualize the REU experience
# always use header=0 because the first row is the header
df = pd.read_csv('../csv/reu_ca.csv', header=0)

df_total = pd.read_csv('../csv/nsf-gov_researchExperienceSites.csv', header=0)
#takes in a keyword, string value
# returns the result, filtered the df into a new df
def reu_types(keyword):

    #df['Site Name'][map(lambda u: False, df['Site Name'])]
    return map(lambda u: re.search(keyword, u), df['Site Name'])
# how to plot with matplotlib

#
