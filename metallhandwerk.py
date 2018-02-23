from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver import ActionChains
import time
import re

driver = webdriver.Chrome('chromedriver.exe')
driver.implicitly_wait(5)
driver.get('http://www.metallhandwerk.de/fachbetriebe-vor-ort/')

#iframe ist inline Frame:= insert document inside current html document (test mit soup/prettify, sehe Inhalt von iframe)
frame = driver.find_element_by_id('advanced_iframe')
driver.switch_to.frame(frame)
select =  Select(driver.find_element_by_name('gewerk'))
select.select_by_index(1)
SubmitButton = driver.find_element_by_xpath('//*[@id="form2"]/table/tbody/tr[5]/td[2]/input[1]').click()


soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup.prettify())

# meta_info = soup.find_all('a', href=re.compile(r'detail.php?ClubID'))
# print(meta_info)


metainfo = soup.find_all('p')

x = 1
maxSeiten = 704
while x < maxSeiten:

    if x == 1:
        del metainfo[0]
    for i in metainfo:

        #prepare data (entferne müll und check nach plz)
        naked_metainfo = i.text.split(';')
        naked_metainfo[0] = naked_metainfo[0].replace('\n', ' ')
        naked_metainfo[0] = naked_metainfo[0].replace('\t', ' ')
        naked_metainfo[3] = naked_metainfo[3].replace('\t', ' ')




        try:
            splitNaked0 = naked_metainfo[0].split(' ')
            # reversed() läuft array rückwerts durch
            for index, j in enumerate(splitNaked0):
                if len(j) == 5 and j.isdigit():
                    PLZ = j
                    Firmenname = splitNaked0[:index - 1]
                    Firmenname = ' '.join(Firmenname)
                    Ort = splitNaked0[index + 1:]
                    Ort = ' '.join(Ort)
                    break

        except IndexError:
            Firmenname = 'K/A'
            Ort = 'K/A'
            PLZ = 'K/A'

        try:
            Straßenname = naked_metainfo[1]
        except IndexError:
            Straßenname = 'K/A'

        try:
            Telenummer = naked_metainfo[2]
        except IndexError:
            Telenummer = 'K/A'

        try:
            if 'E-Mail' in naked_metainfo[3]:
                Faxnummer = naked_metainfo[3].split('E-Mail')

                Faxnummer = Faxnummer[0:-1]
                Faxnummer = ' '.join(Faxnummer)
            else:
                Faxnummer= naked_metainfo[3]
        except IndexError:
            Faxnummer = 'K/A'

        try:
            if ('E-Mail' in naked_metainfo[3]):
                Mailadresse = naked_metainfo[3].split('E-Mail')
                Mailadresse = Mailadresse[-1]

        except IndexError:
            Mailadresse = 'K/A'

        try:
            Internetseite = naked_metainfo[4].replace('Homepage', '')
        except IndexError:
            Internetseite = 'K/A'

        # try:
        #     PLZ = naked_metainfo[0].split(' ')
        #     PLZ = PLZ[-2]
        # except IndexError:
        #     PLZ = 'K/A'
        #
        # try:
        #     Ort = naked_metainfo[0].split(' ')
        #     Ort = Ort[-1]
        # except IndexError:
        #     Ort = 'K/A'

        datensatz = {"Firma": Firmenname,
                     "Straße": Straßenname,
                     "Telefon": Telenummer,
                     "Faxnummer": Faxnummer,
                     "Mail": Mailadresse,
                     "Homepage": Internetseite,
                     "PLZ": PLZ,
                     "Ort": Ort

                     }

        print(datensatz)
        print(naked_metainfo)
        print('########################################')
        time.sleep(0.5)
    x = x +1

    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr[2]/td[4]/a').click()

    driver.implicitly_wait(2)

    search_field = driver.find_element_by_name("seite")
    search_field.clear()
    search_field.send_keys(str(x))
    search_field.send_keys(Keys.RETURN)
    print('Seeeeeeeeeeeeeeeeeeeeite')



