import requests
import urllib
import urllib2

# the following successfully posts to the form on stackoverflow

url = "http://stackoverflow.com"
data = {
  'd': '[python]'
}

r = requests.post(url, params=data)

print r.text

