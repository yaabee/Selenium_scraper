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

soup = BeautifulSoup(driver.page_source, "html.parser")

# print(soup.prettify())



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
            for x in meta.findAll('p', {'class': 'm-n p-n'}):
                block.append(x.text)

            #     # print(x.text)
            # for index,i in enumerate(block):
            #     try:
            #         if index%2 != 0:
            #             name = i
            #         if index % 2 == 0:
            #             inhalt = i
            #         print(inhalt)
            #     except IndexError:
            #         pass
            # print(block[1].strip())
            # print(block[3].strip())
            # print(block[5].strip())
            # print(block[7].strip())
            # print(block[9].strip())
            # print(block[11].strip())
            # print(block[13].strip())
            print(len(block))
            print('##################################')



            # datensatz = {
            #
            #     block[0]: block[1].strip(),
            #     block[2]: block[3].strip(),
            #     block[4]: block[5].strip(),
            #     block
            # }
            # print(datensatz)



            # for x in meta.findAll('p'):
            #     print(x.text)
            #     print('neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeext')


        # for name in soup2.findAll('div', {'class': 'col-xs-12 content'}):

        # for name in soup2.findAll('h1'):
        #     # print(name)
        #     print(name.text)
        #     print('######################')

        # for stuff in soup2.findAll('p', {'class': 'm-n p-n'}):
        #     print(stuff)
        #     print('######################')


        # for test in soup2.findAll('div', {'class': 'row'}):
        #     print(test)



#, {'class': 'm-n p-n'}