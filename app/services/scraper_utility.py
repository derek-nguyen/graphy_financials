"""
USE THIS FILE TO STORE ALL WEB CRAWLER FUNCTIONS
"""

import requests
import pandas
import os
from bs4 import BeautifulSoup
from zipfile import ZipFile


def get_zip_href(url: str) -> list:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    zip_links = []
    for link in soup.find_all("a"):
        try:
            if link.get("href").endswith(".zip") == True:
                zip_links.append(link.get("href"))
        except AttributeError:
            pass

    return zip_links


def zip_extract_download(zip_url: str, download_folder: str):
    zip_response = requests.get(zip_url)
    zip_filename = zip_url.split("/")[-1]
    zip_path = os.path.join(download_folder, zip_filename)

    with open(zip_path, "wb") as zip_file:
        zip_file.write(zip_response.content)

    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(download_folder)

    os.remove(zip_path)

    return


# data = get_zip_links("https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets")


zip_list = get_zip_href(
    "https://www.sec.gov/dera/data/crowdfunding-offerings-data-sets"
)
# test_url = cf_sec_url + zip_list[0]
# zip_extract_download(
#     test_url, "/Users/derek/Documents/Github_Repos/graphy_financials/data"
# )

for zip_link in zip_list:
    cf_sec_url = "https://www.sec.gov/"
    zip_url = cf_sec_url + zip_link

    data_folder_path = "/Users/derek/Documents/Github_Repos/graphy_financials/data"
    
    try: 
        zip_extract_download(zip_url, data_folder_path)
    except:
        print('Error downloading file')