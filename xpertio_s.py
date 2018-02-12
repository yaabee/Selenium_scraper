from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import requests
import time



def get_new_plz():




def xpertio_spider(max_pages):

    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://www.xpertio.net/')

    Plz_feld = driver.find_element_by_id('cphContainer_csbHome_tbZipOrCity')
    Plz_feld.send_keys('97080')
    Plz_feld.send_keys(Keys.RETURN)

    time.sleep(3)



    seite = 1
    while seite <= max_pages:

        soup = BeautifulSoup(driver.page_source, "html.parser")
        for link in soup.findAll('a', {'class': 'content-box lv-search-item margin-top20' }):
            href = link.get('href')
            #print(href)
            page = requests.get(href)
            clean_text = page.text
            soup2 = BeautifulSoup(clean_text, "html.parser")
            #print(soup2.prettify)


            #mal gucken wie if funktion den find() inhalt tauschen könnte.
            try:
                for name in soup2.find('h1', {'class': 'h2'}):
                            print(name)
            except TypeError:
                        name = 'KA'
                        print(name)
            try:
                for address in soup2.find('a', {'id':'cphContainer_cphMain_cBusinessCard_hlAddress'}):
                    print(address)
            except TypeError:
                    address = 'KA'
                    print(address)

            try:
                for tele in soup2.find('span', {'id': 'cphContainer_cphMain_cBusinessCard_lbPhone'}):
                    print(tele, '####################################')
            except TypeError:
                    tele = 'KA'
                    print(tele)

            Datensatz = {
                "Firmenname": name,
                "Adresse": address,
                "Telefon": tele
            }

        num = seite + 1
        if num == 20:
            break

        click_next_seite = driver.find_element_by_link_text('Nächste Seite').click()
        print(num)
        seite += 1



xpertio_spider(20)