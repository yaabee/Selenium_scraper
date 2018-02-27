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
driver.implicitly_wait(5)
driver.get('http://www.metallhandwerk.de/fachbetriebe-vor-ort/')

#iframe ist inline Frame:= insert document inside current html document (test mit soup/prettify, sehe Inhalt von iframe)
frame = driver.find_element_by_id('advanced_iframe')
driver.switch_to.frame(frame)
select =  Select(driver.find_element_by_name('gewerk'))
select.select_by_index(1)
SubmitButton = driver.find_element_by_xpath('//*[@id="form2"]/table/tbody/tr[5]/td[2]/input[1]').click()
# print(soup.prettify())

# meta_info = soup.find_all('a', href=re.compile(r'detail.php?ClubID'))
# print(meta_info)


x = 1
maxSeiten = 706
while x < maxSeiten:

    soup = BeautifulSoup(driver.page_source, "html.parser")
    metainfo = soup.find_all('p')
    del metainfo[0]

    # if x == 1:
    #     del metainfo[0]
    for i in metainfo:

        #prepare data (entferne müll und check nach plz)
        naked_metainfo = i.text.split(';')
        naked_metainfo[0] = naked_metainfo[0].replace('»', '')
        naked_metainfo[0] = naked_metainfo[0].replace('\n', ' ')
        naked_metainfo[0] = naked_metainfo[0].replace('\t', ' ')
        naked_metainfo[3] = naked_metainfo[3].replace('\t', ' ')


        try:
            splitNaked_0 = naked_metainfo[0].split(' ')
            # reversed() läuft array rückwerts durch
            for index, j in enumerate(splitNaked_0):
                if len(j) == 5 and j.isdigit():

                    PLZ = j
                    Firmenname = splitNaked_0[:index -1]
                    Firmenname = ' '.join(Firmenname).strip()
                    Ort = splitNaked_0[index +1:]
                    Ort = ' '.join(Ort)
                    break


        except IndexError:
            Firmenname = 'K/A'
            Ort = 'K/A'
            PLZ = 'K/A'

        try:
            Straßenname = naked_metainfo[1].strip()
        except IndexError:
            Straßenname = 'K/A'

        try:
            Telenummer = naked_metainfo[2]
            if 'Tel.' in Telenummer:
                Telenummer = Telenummer.replace('Tel.', '').strip()
                Telenummer = Telenummer.replace('-', '')
                Telenummer = Telenummer.replace(' ', '')
        except IndexError:
            Telenummer = 'K/A'

        try:
            if 'E-Mail' in naked_metainfo[3]:
                Faxnummer = naked_metainfo[3].split('E-Mail')

                Faxnummer = Faxnummer[0:-1]
                Faxnummer = ''.join(Faxnummer)
                if 'Fax' in Faxnummer:
                    Faxnummer = Faxnummer.replace('Fax', '').strip()
                    Faxnummer = Faxnummer.replace('-', '')
                    Faxnummer = Faxnummer.replace(' ', '')
                    if len(Faxnummer) <2:
                        Faxnummer = 'K/A'

            else:
                Faxnummer= naked_metainfo[3]
                if 'Fax' in Faxnummer:
                    Faxnummer = Faxnummer.replace('Fax', '').strip()
                    Faxnummer = Faxnummer.replace('-', '')
                    Faxnummer = Faxnummer.replace(' ', '')
                    if len(Faxnummer) <2:
                        Faxnummer = 'K/A'
        except IndexError:
            Faxnummer = 'K/A'

        try:
            if ('E-Mail' in naked_metainfo[3]):
                Mailadresse = naked_metainfo[3].split('E-Mail')
                Mailadresse = Mailadresse[-1].strip()
            else:
                Mailadresse = 'K/A'

        except IndexError:
            Mailadresse = 'K/A'

        try:
            Internetseite = naked_metainfo[4].replace('Homepage', '')
        except IndexError:
            Internetseite = 'K/A'


        datensatz = {"Firma": Firmenname,
                     "Telefon": Telenummer,
                     "Faxnummer": Faxnummer,
                     "E-Mail": Mailadresse,
                     "Homepage": Internetseite,
                     "Straße": Straßenname,
                     "PLZ": PLZ,
                     "Ort": Ort

                     }

        print(datensatz)
        print(naked_metainfo)
        # print(splitNaked_0, index, j , Ort)
        # print(metainfo)
        insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='metallhandwerk_neu',
                                    datensatz=datensatz)
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



