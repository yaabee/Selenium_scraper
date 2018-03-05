from bs4 import BeautifulSoup
from selenium import webdriver
import time
import unicodedata


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(3)
# driver.get('https://www.zveh.de/fachbetriebssuche.html')
driver.get('https://www.zveh.de/fachbetriebssuche.html?tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40extension%5D=EpFachbetriebsuche&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40vendor%5D=Kirchbergerknorr&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40controller%5D=CompanySearch&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40action%5D=show&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5Barguments%5D=YTo3OntzOjEwOiJzZWFyY2hXb3JkIjtzOjA6IiI7czoxMDoicG9zdGFsQ29kZSI7czo1OiIxNjg0NSI7czo4OiJkaXN0YW5jZSI7czozOiIxNTAiO3M6MTA6ImF0dHJpYnV0ZXMiO3M6MDoiIjtzOjg6ImFjdGl2aXR5IjthOjE6e3M6MTA6Il9faWRlbnRpdHkiO3M6MToiMCI7fXM6Njoic3VibWl0IjtzOjc6IkZpbHRlcm4iO3M6OToiQHdpZGdldF8wIjthOjE6e3M6MTE6ImN1cnJlbnRQYWdlIjtzOjI6IjkzIjt9fQ%3D%3Db2dec4e56c11ea08c3ab816fa7ab9adda9fd14d4&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A18%3A%22EpFachbetriebsuche%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A13%3A%22CompanySearch%22%3Bs%3A7%3A%22%40action%22%3Bs%3A4%3A%22show%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A16%3A%22Kirchbergerknorr%22%3B%7D11efba3f9443acc074abfb36351cfc6738d3b0b2&tx_epfachbetriebsuche_companysearch%5B__trustedProperties%5D=a%3A7%3A%7Bs%3A10%3A%22searchWord%22%3Bi%3A1%3Bs%3A10%3A%22postalCode%22%3Bi%3A1%3Bs%3A8%3A%22distance%22%3Bi%3A1%3Bs%3A6%3A%22submit%22%3Bi%3A1%3Bs%3A10%3A%22attributes%22%3Ba%3A11%3A%7Bi%3A0%3Bi%3A1%3Bi%3A1%3Bi%3A1%3Bi%3A2%3Bi%3A1%3Bi%3A3%3Bi%3A1%3Bi%3A4%3Bi%3A1%3Bi%3A5%3Bi%3A1%3Bi%3A6%3Bi%3A1%3Bi%3A7%3Bi%3A1%3Bi%3A8%3Bi%3A1%3Bi%3A9%3Bi%3A1%3Bi%3A10%3Bi%3A1%3B%7Ds%3A8%3A%22activity%22%3Bi%3A1%3Bs%3A11%3A%22subActivity%22%3Bi%3A1%3B%7D634bd82564ac8398f7d9d96400e324a616383d15&tx_epfachbetriebsuche_companysearch%5BsearchWord%5D=&tx_epfachbetriebsuche_companysearch%5BpostalCode%5D=57462&tx_epfachbetriebsuche_companysearch%5Bdistance%5D=150&tx_epfachbetriebsuche_companysearch%5Battributes%5D=&tx_epfachbetriebsuche_companysearch%5Bactivity%5D=0&tx_epfachbetriebsuche_companysearch%5Bsubmit%5D=Filtern')



plzArray = ['27383', '16845', '57462', '09232', '74343', '84155']

y = 1
maxSeiten = 500
while y < maxSeiten:

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for meta in soup.findAll('div', {'class': 'block'}):


        block = []

        name = 'K/A'
        plz = 'K/A'
        strasse = 'K/A'
        ort = 'K/A'
        tele = 'K/A'
        fax = 'K/A'
        mail = 'K/A'


        for x in meta.findAll('div', {'class': 'dates'}):
            # print(x)

            if len(x.get('class')) is 2:
                name = x.text
                # print(name)

            for img in x.findAll('img'):
                if '/typo3conf/ext/ep_template/Resources/Public/Global2016/Images/SVG/Icons/pin-icon.svg' in img.get('src'):
                    Adresse = unicodedata.normalize("NFKD", x.text)
                    Adresse = Adresse.split(' ')

                    for index, j in enumerate(Adresse):
                        if len(j) == 5 and j.isdigit():
                            plz = j
                            strasse = Adresse[:index]
                            strasse = ' '.join(strasse).strip()
                            ort = Adresse[index + 1:]
                            ort = ' '.join(ort)
                            break

                if '/typo3conf/ext/ep_template/Resources/Public/Global2016/Images/SVG/Icons/tel-icon.svg' in img.get('src'):
                    tele = x.text
                    # print(tele)

                if '/typo3conf/ext/ep_template/Resources/Public/Global2016/Images/SVG/Icons/fax-icon.svg' in img.get('src'):
                    fax = x.text
                    # print(fax)

                if '/typo3conf/ext/ep_template/Resources/Public/Global2016/Images/SVG/Icons/mail-icon.svg' in img.get('src'):
                    mail = x.text

                    datensatz = {
                        'firma_name': name.strip(),
                        'firma_strasse': strasse.strip(),
                        "firma_plz": plz.strip(),
                        "firma_ort": ort.strip(),
                        "firma_telefon": tele.strip(),
                        "firma_fax": fax.strip(),
                        "firma_mail": mail.strip(),
                    }

                    print(datensatz)
                    print('neeeeeeeeeeeeew')

                    insert_new_dataset_into_mdb(mdb_uri="192.168.100.5", datenbank='yanghi', collection='zveh',
                                                datensatz=datensatz)
    y += 1
    prefix = 'https://www.zveh.de'
    link = soup.find('a', {'rel':'next'})
    href = link.get('href')
    driver.get(prefix + href)
    driver.implicitly_wait(2)