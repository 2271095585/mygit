#-*-encoding:utf-8-*-
import requests
from bs4 import *
url = 'https://www.gebiz.gov.sg/ptn/opportunity/BOListing.xhtml?origin=menu'
r = requests.get(url)
print r
print r.cookies
for c in r.cookies:
    print c

