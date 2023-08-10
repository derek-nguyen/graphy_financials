"""
USE THIS FILE TO STORE ALL WEB CRAWLER FUNCTIONS
"""

import requests
import pandas
from bs4 import BeautifulSoup
from zipfile import ZipFile

zip_links = []

def get_zip_links(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    for link in soup.find_all("a"):
        try:
            if link.get("href").endswith(".zip") == True:
                zip_links.append(link.get("href"))
        except AttributeError:
            print('Not a string')
            

    # return zip_links


# data = get_zip_links("https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets")

get_zip_links("https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets")

print(zip_links[0])