# tutorial2, getting started with python
# 10 January 2014

import csv as csv
import numpy as np

csv_file_object = csv.reader(open('train.csv', 'rb'))
header = csv_file_object.next()

data = []
for row in csv_file_object:
    data.append(row)
data = np.array(data)

# size() function counts the number of passangers

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived/number_passengers

#use the following variables as a 'mask' for the data
#see index of women or men

women_only_stats = data[0::,4] == "female"
men_only_stats = data[0::,4] != "female"

women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats, 1].astype(np.float)

proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)

proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

print "women survived: %s" % proportion_women_survived
print "men survived: %s" % proportion_men_survived

# readin test data
test_file = open('test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next() 

prediction_file = open("genderbasedmodel2.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object: #for every row in test.csv
    if row[3] == "female":
        prediction_file_object.writerow([row[0], '1']) 
    else:
        prediction_file_object.writerow([row[0],'0'])

test_file.close()
prediction_file.close()

#### second submission
fare_ceiling = 40
## everythng that is above 40 put it in the 30 - 39 bin 
data[ data[0::,9].astype(np.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling/fare_bracket_size

#find the number of classes on board: 1st, 2nd, 3rd
number_of_classes = len(np.unique(data[0::,2]))

# make survival table...all zeros
survival_table = np.zeros((2,number_of_classes, number_of_price_brackets))

# search with passengers that are binned based on their class and ticket price

for i in xrange(number_of_classes):
    for j in xrange(number_of_price_brackets):
    
        women_only_stats = data[ (data[0::,4] == "female") & (data[0::,2].astype(np.float) == i+1) & (data[0::,9].astype(np.float) >= j*fare_bracket_size) & (data[0::,9].astype(np.float) < (j+1)*fare_bracket_size), 1]

        men_only_stats = data[(data[0::,4] != "female") & (data[0::,2].astype(np.float) == i+1) & (data[0::,9].astype(np.float) >= j*fare_bracket_size) & (data[0::,9].astype(np.float) < (j+1)*fare_bracket_size), 1]


survival_table[0,i,j] = np.mean(women_only_stats.astype(np.float))
survival_table[1,i,j] = np.mean(men_only_stats.astype(np.float))  

#remove the NAN's because there are no women who paid 
# less than $10 for her fair ticket
survival_table[survival_table != survival_table ] = 0

print survival_table
