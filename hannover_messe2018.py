from bs4 import BeautifulSoup
from selenium import webdriver
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
driver.get('http://www.hannovermesse.de/de/ausstellung/aussteller-produkte/ausstellerverzeichnis/index.xhtml')

select = Select(driver.find_element_by_id('j_idt100:j_idt104:j_idt107:0:r'))
select.select_by_index(1)




y = 1
maxSeiten = 29
while y < maxSeiten:
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup.prettify())

    for meta in soup.findAll('div',{ 'class':'nested l-nested12 m-nested12 s-nested12'}):

        for name in meta('h2'):
            name = name.text
            print(name)

        for ort in meta('div', {'itemprop': 'country'}):
            ort = ort.text
            ort = ort.replace('\n', '')
            ort = ort.replace('D - ', '')
            print(ort)

        for halle in meta('p', {'itemprop': 'location'}):
            halle = halle.text
            halle = halle.replace('\n', '')
            halle = halle.replace('\t', '')
            print(halle)


        datensatz = {

            'firma_name': name,
            'firma_ort': ort,
            'messe_halle': halle
        }

        print(datensatz)
        insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='hannover_messe2018',
                                    datensatz=datensatz)
        print('########################################')

    y += 1
    driver.find_element_by_class_name('next-page').click()
    print('neueseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeite')



