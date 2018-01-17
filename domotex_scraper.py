from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
#     from pymongo import MongoClient
#     client = MongoClient(mdb_uri, 27017, maxPoolSize=50)
#     db = client[datenbank]
#     collection = db[collection]
#     collection.insert_one(datensatz)


driver = webdriver.Chrome("chromedriver.exe")
driver.get('http://www.domotex.de/de/messe/aussteller-produkte/ausstellerverzeichnis/index-2.xhtml')

Detaillierte_Liste = driver.find_element_by_class_name('M014-02__text-element')
Detaillierte_Liste.click()

time.sleep(0.5)


soup = BeautifulSoup(driver.page_source)
metainfo = soup.find_all("a", class_="search-link")


for tag in metainfo:

    clean_meta = tag.text.strip()


    Firma = []
    for line in clean_meta.split('\n'):
        line = line.strip()


        print(line)

        if line:
            Firma.append(line)

            try:
                Name = Firma[1]
            except IndexError:
                Name = 'K/A'

            try:
                Land = Firma[2]
            except IndexError:
                Land= 'K/A'

            try:
               Stadt  = Firma[3]
            except IndexError:
                Stadt = 'K/A'

            try:
                Halle = Firma[:-2]
            except IndexError:
                Fax = 'K/A'


        Datensatz = {'Name': Name,
                     'Land': Land,
                     'Stadt': Stadt,
                     'Halle': Halle
                     }

        print(Datensatz)
        time.sleep(0.5)

    # clean_meta.replace('    ', '')





    # print(Firma)
    # time.sleep(0.5)
    #




    #insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank= 'yanghi', collection='domotex',datensatz=datensatz)


# print(clean_meta)
# time.sleep(0.5)