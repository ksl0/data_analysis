import requests
import urllib
import urllib2
import json
import urllib
import urllib2
import urlparse
import time

# see https://cogcc.state.co.us/COGIS_Help/API_County_codes.pdf
timeStart = time.time()
url = 'http://cogcc.state.co.us/cogis/IncidentSearch2.asp'
maxrec = 2500
countyCode = 013 #boulder

values = {
 'itype': 'insp', 
  'ApiCountyCode': countyCode,
  'ApiSequenceCode': '', 
  'Complainant':'', 
  'Operator': '',
  'operator_name_number': 'name',
  'Facility_Lease':'',
  'facility_name_number': 'name',
  'qtrqtr': '',
  'sec': '', 
  'twp': '', 
  'rng': '', 
  'project_num': '', 
  'document_num': '', 
  'maxrec': maxrec,
  'Button1': 'Submit',
} 

headers={'Content-type': 'application/x-www-form-urlencoded'}
data = urllib.urlencode(values) 
req  = urllib2.Request(url, data, headers)
r = urllib2.urlopen(req)

timeEnd = time.time()
total_time = timeEnd - timeStart

print total_time 
print r.read()
## the opening of files for later
"""
predictions_file = open('../csv/output.csv', 'wb')
p = csv.writer(predictions_file)
p.writerow(["PassengerId", "Survived"])
test_file.close()
predictions_file.close() """

