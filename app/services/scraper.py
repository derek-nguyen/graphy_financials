"""
USE THIS FILE TO STORE ALL WEB CRAWLER FUNCTIONS
"""

import requests
import pandas
from zipfile import ZipFile


url = "https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets/files/dera/data/crowdfunding-offerings-data-sets/2023q2_cf.zip"
req = requests.get(url)

filename = url.split('/')[-1]

print(filename)
