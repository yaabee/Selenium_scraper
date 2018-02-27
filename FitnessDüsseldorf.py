from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
import time



def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


x = 1
maxSeiten = 111
while x <= maxSeiten:

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.gelbeseiten.de/fitness/duesseldorf,,,,,umkreis-50000/s' + str(x))
    driver.implicitly_wait(1.5)


    soup = BeautifulSoup(driver.page_source, "html.parser")
    for link in soup.findAll('a', {'class','m08_teilnehmername teilnehmername entry' }):
        href = link.get('href')
        # print(href)
        page = requests.get(href)
        clean_text = page.text
        soup2 =BeautifulSoup(clean_text, "html.parser")
        # print(soup2.prettify())

        try:
            for name in soup2.find('h1', {'class': 'mod-TeilnehmerKopf__name'}):
                print(name)

        except TypeError:
            name = 'K/A'

        try:
            for Straße in soup2.find('span', {'itemprop':'streetAddress'}):
                print(Straße)
        except TypeError:
            Straße = 'K/A'
        try:
            for PLZ in soup2.find('span', {'itemprop': 'postalCode'}):
                print(PLZ)
        except TypeError:
            PLZ = 'K/A'
        try:
            for Ort in soup2.find('span', {'itemprop': 'addressLocality'}):
                print(Ort)
        except TypeError:
            Ort = 'K/A'
        try:
            for telenummer in soup2.find('span', {'class': 'mod-TeilnehmerKopf--secret_suffix'}):
                telenummer = telenummer.replace('(','')
                telenummer = telenummer.replace(')', '/')
                telenummer = telenummer.replace(' ', '')
                telenummer = telenummer.replace('-', '')
                print(telenummer)
        except TypeError:
            telenummer = 'K/A'


        datensatz = { "Firma":name,
                      "Straße":Straße,
                      "PLZ": PLZ,
                      "Ort": Ort,
                      "Telefon": telenummer
        }

        print(datensatz)
        print('##########################################')
        time.sleep(0.5)
        insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='FitnessDüsseldorf_neu',
                                    datensatz=datensatz)

    x = x + 1


    print('neue Seeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeite')
