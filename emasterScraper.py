from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.e-masters.de/e-masters-fachbetriebe.html')


Land_auswahl = driver.find_element_by_id("staat_auswahl")
Land_auswahl.click()
select = Select(driver.find_element_by_id('staat_auswahl'))     #didnt work with loop, select is perfect for drop-down(option/list)
select.select_by_index(1)                                       #select option number (index)
Land_auswahl.click()


Radius_auswahl = driver.find_element_by_id("radius_auswahl")
Radius_auswahl.click()
select2 = Select(driver.find_element_by_id("radius_auswahl"))
select2.select_by_index(9)
Radius_auswahl.click()


#get the search textbox (für PLZ)
search_field = driver.find_element_by_id("plz_ort")
search_field.clear()
search_field.send_keys("49685")
search_field.send_keys(Keys.RETURN)                             #press "enter"


driver.implicitly_wait(12)


soup = BeautifulSoup(driver.page_source)
metainfo = soup.find_all("tr")                                  #every tag should be from <tr> to </tr> in metainfo
#print(soup.prettify())


del(metainfo[0])                                                #erstes element hatte eine liste mit einem element (out of bound error)

import time
for tag in metainfo:
    firma = []
    naked_metainfo = tag.text.split(':')                           #(strip) since all tags are printed separatly, all tags have own line

    try:
        Firmenname = naked_metainfo[0].replace("Straße", "")
        Firmenname = Firmenname.split('D')[0]
    except IndexError:
        Firmenname = 'K/A'

    try:
        Straßenname = naked_metainfo[1].replace("Telefon","")
    except IndexError:
        Straßenname = Straßenname

    try:
        Telenummer = naked_metainfo[2].replace("Telefax", "")
    except IndexError:
        Telenummer = 'K/A'

    try:
        Faxnummer = naked_metainfo[3].replace("E-Mail", "")
    except IndexError:
        Faxnummer = 'K/A'
    try:
        Mailadresse = naked_metainfo[4].replace("Internet", "")
    except IndexError:
        Mailadresse = 'K/A'

    try:
        #internetseite und plz werden gesplitted und als liste in der "tag-list" als eigene list eingefügt
        internetseite = naked_metainfo[5].split('D-')[0]
    except IndexError:
        internetseite = 'K/A'

    try:
        Ort_PLZ = naked_metainfo[5].split('D-')[1]
        #splits string into numbers/letters
        Ort_PLZ = re.split('(\D+)', Ort_PLZ)
        PLZ = Ort_PLZ[0]
        Ort = Ort_PLZ[1]

    except IndexError:
        Ort = "K/A"
        PLZ = "K/A"
        Ort_PLZ = 'K/A'

    datensatz = { "Firma": Firmenname,
                  "Straße": Straßenname,
                  "Telefon": Telenummer,
                  "Faxnummer":Faxnummer,
                  "Mail": Mailadresse,
                  "Internet": internetseite,
                  "PLZ": PLZ,
                  "Ort": Ort

                  }

    print(datensatz)
    # print(Firmenname)
    # print(naked_metainfo)
    insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='emaster', datensatz=datensatz)
    print("Nächste Firma.....*************************************************")