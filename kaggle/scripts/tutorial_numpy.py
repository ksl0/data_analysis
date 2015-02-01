# 01/14/2014
# A combination of notes and code from the python tutorial
# UC4P - 'uncomment for plot'
import csv as csv
import numpy as np

#readin data, the old way :/
data = []
csv_file_object = csv.reader(open('../csv/train.csv', 'rb'))
header = csv_file_object.next()

for row in csv_file_object:
    data.append(row)

#intersting, this would be like recursive? in haskell but actually it's just overwriting the value of data 
data = np.array(data)

# use pandas because the following line does not work....
#ages_onboard = data[0::, 5].astype(np.float)

import pandas as pd
# always use header=0 because the first row is the header
df = pd.read_csv('../csv/train.csv', header=0)
#df[df.Age < 3][['Sex', 'Age', 'Survived']]


# how to plot with matplotlib
import pylab as P

#df['Age'].hist()
# this command allows graph to show up on screen
#P.show()


#smaller bins
# the age may be positively skewed
# UC4P
# df['Age'].dropna().hist(bins=16, range = (0,80), alpha = 0.5)

P.show()
# add new columns
df['AgeFill'] = df.Age
df['Gender'] = df.Sex.map({'female': 0, 'male': 1} ).astype(int)


# fill the array
# fill in missing data using the medians from class and gender estimations

median_ages = np.zeros((2,3))

# find median ages
for i in range(0,2):
    for j in range(0,3):
        median_ages[i,j] = df[(df.Gender == i) & (df.Pclass == j+1)].Age.dropna().median()


for i in range(0, 2):
    for j in range(0, 3):
        df.loc[ (df.Age.isnull()) & (df.Gender == i) & (df.Pclass == j+1), 'AgeFill'] = median_ages[i,j]

df['AgeIsNull'] = pd.isnull(df.Age).astype(int)

# to find summary statistics, use 
# df.describe()


# Parch: parents and children onboard; SibSp: number of siblings+ spouses

df['FamilySize'] = df['SibSp'] + df['Parch']
# df.FamilySize.hist(bins=20, range = (0,20), alpha = .2), holy crap who had 10 family members?...
#  <-- 3rd class family, last name 'Sage' who all died

# probably some better iterative way to do this, but by making all nan values to zero 
# one can create a 'completed' age value

#EDIT: derp, you just set df['AgeFill'] to df['Age'] to fill up the numbers 
# and then don't need to do hacky stuff
#df['Age*Class'] = df.AgeFill.fillna(0) * df.Pclass + df.Age.fillna(0) * df.Pclass
df['Age*Class'] = df.AgeFill * df.Pclass 
df['Age*Class'].dropna().hist(bins=60, range = (0,240), alpha = 0.22)

# find what are objects, or in pandas...'string'

df.dtypes[df.dtypes.map(lambda x: x=='object')]

df = df.drop(['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'], axis=1)


df = df.drop['Age']
# if lazy: use df.dropna(), but a bad practice for real life

train_data = df.values



