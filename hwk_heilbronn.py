from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

import requests
import time
import _pickle as cPickle


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)

'''
select class ließ sich mit driverFindElementById nicht finden:
stattdessen funktionierte aber Select von selenium ums zu finden
anschließend ein input feld anvisiert und mit actoinchains -> enter
'''

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://hwk-heilbronn-service.de/apps/services/modules/hws/index.php')

# landkreis = driver.find_element_by_id('hwr_landkreis')
# landkreis.click()

try:

    select = Select(driver.find_element_by_id('hwr_landkreis'))     #didnt work with loop, select is perfect for drop-down(option/list)
    select.select_by_index(1)                                       #select option number (index)
    # landkreis.click()
except:
    pass

hwr_ort1 = driver.find_element_by_id('hwr_ort1')


#press enter
actions = ActionChains(driver)
actions.move_to_element(hwr_ort1)
actions.send_keys(Keys.RETURN)
actions.perform()

# WebDriverWait(driver, 5).until(lambda d: len(d.window_handles) ==2)
# driver.switch_to_window(driver.window_handles[0])
# driver.switch_to.window(driver.window_handles[1])


'''
Die Ergebnisse lassen sich nicht richtig anvisieren,
aber get requests sind angegeben und lasse loop drüber laufen.
check suchergebnis nach aktueller 'guid_nummer' ob änderung vorliegt
pro Session kann man gleiche guid_nummer benutzen
'''



# element = driver.find_element_by_css_selector('div.col.col-xs-12.col-sm-12.col-md-12.list-group')
# print(element.text)


# frame = driver.find_element_by_css_selector('#content')
# print(frame.text)
#
# driver.switch_to.frame(frame)
# link = driver.find_element_by_class_name('list-group-item')
# print(link.text)



id1 = "https://hwk-heilbronn-service.de/apps/services/modules/hws/details.php?id="
id2 = 0
id3 = input("HALLO")

id = id1 + str(id2) + id3

Page = driver.get(id)

time.sleep(1)


x= 0
Seite = 5

while x < Seite:

    id = id1 + str(x) + id3

    Page = driver.get(id)



    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # print(soup.prettify())
    time.sleep(1)
    print(x)

    block = soup.find_all(class_="block")
    print(block)
    print(type(block))


    # meta = block.find_all(class_='row')
    # for row in meta:
    #     print('row',row)
    #
    #     for span in row.find_all('span'):
    #         print('span',span)




    x += 1



