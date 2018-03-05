from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get('https://www.hwk-karlsruhe.de/betriebe/suche-63,0,bdbsearch.html?search-searchterm=&search-filter-zipcode=bayern&search-filter-radius=20&search-filter-jobnr=&search-job=&search-filter-training=')#

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup.prettify())

for alleLinks in soup.findAll('div', {'class': 'col-md-5 col-sm-12'}):
    # del(alleLinks[0])
    # del(alleLinks[1])
    # print(alleLinks)

    #hier href mit partial link ("wegen <a href="#" >
    for a in alleLinks.select('a[href*="/betriebe/"]'):
        # print(a)
        urlPrefix = 'https://www.hwk-karlsruhe.de'
        href = a.get('href')
        # print(href)
        page = requests.get( urlPrefix + href)
        clean_text = page.text
        soup2 = BeautifulSoup(clean_text, 'html.parser')
        # print(soup2.prettify())

        section = soup2.find('section')
        print(section)