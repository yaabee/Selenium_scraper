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
driver.get('https://www.hwk-ulm.de/handwerkersuche/')

suche = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div[1]/div[2]/div[1]/form/div/div[1]/div/div/div[2]/div/button/span[1]/span')
suche.click()



# print(soup.prettify())

y = 1
maxSeiten = 160
while y < maxSeiten:

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for tag in soup.findAll('div',{'class': 'searchhit-header'}):
        # print(tag)
        for a in tag.find_all('a'):
            # print(a.get('href'))
            href = a.get('href')
            page = requests.get(href)
            clean_text = page.text
            soup2 = BeautifulSoup(clean_text, 'html.parser')
            # print(soup2.prettify())


            # block = []
            #
            # for meta in soup2.findAll('section', {'id': 'section-1'}):
            #     # print(meta)
            #     block.append([x.text for x in meta.findAll('p')])
            # print(block)
            # print('########################################################')


            for meta in soup2.findAll('section', {'id': 'section-1'}):
                block = []
                print(meta)
                for x in meta.findAll('p', {'class': 'm-n p-n'}):
                    block.append(x.text)

                strasse = 'K/A'
                plz = 'K/A'
                ort = 'K/A'
                tele = 'K/A'
                handy = 'K/A'
                fax = 'K/A'
                mail = 'K/A'
                homepage = 'K/A'
                branche = 'K/A'

                # hier sind die werte in paaren => immer ein index weiter ist gesuchter wert
                for index, i in enumerate(block):
                    if 'Name:' in block[index]:
                        name = block[index + 1].strip()
                        # print(name)
                        # print(index)
                        continue
                    if 'Straße:' in block[index]:
                        strasse = block[index + 1].strip()
                        # print(strasse)
                        # print(index)
                        continue
                    if 'Postleitzahl' in block[index]:
                        plz = block[index + 1].strip()
                        # print(plz)
                        # print(index)
                        continue
                    if 'Stadt:' in block[index]:
                        ort = block[index + 1].strip()
                        # print(ort)
                        # print(index)
                        continue
                    if 'Telefon:' in block[index]:
                        tele = block[index + 1].strip()
                        # print(tele)
                        # print(index)
                        continue
                    if 'Mobil' in block[index]:
                        handy = block[index + 1].strip()
                        # print(handy)
                        # print(index)
                        continue
                    if 'Fax:' in block[index]:
                        fax = block[index + 1].strip()
                        # print(fax)
                        # print(index)
                        continue
                    if 'E-Mail' in block[index]:
                        mail = block[index + 1].strip()
                        # print(mail)
                        # print(index)
                        continue
                    if 'Internet:' in block[index]:
                        homepage = block[index + 1].strip()
                        # print(homepage)
                        # print(index)
                        continue
                    if 'Gewerk' in block[index]:
                        branche = block[index + 1:]
                        branche = ' '.join(branche)
                        # print(branche)
                        # print(index)
                        continue
                datensatz = {
                    'firma_name': name,
                    'firma_strasse': strasse,
                    "firma_plz": plz,
                    "firma_ort": ort,
                    "firma_telefon": tele,
                    "firma_handy": handy,
                    "firma_fax": fax,
                    "firma_mail": mail,
                    "firma_branche": branche
                }

                # print(datensatz)
                #
                # print(block)
                # # print(len(block))
                # print('##################################')
                # insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi',
                #                             collection='hwk_ulm',
                #                             datensatz=datensatz)
    y += 1
    print('neueSeiteeeeeee', y)
    button = driver.find_element_by_class_name('next')
    button.click()
    driver.implicitly_wait(3)



