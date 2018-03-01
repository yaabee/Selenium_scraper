from bs4 import BeautifulSoup
from selenium import webdriver


def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
    from pymongo import MongoClient
    client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
    db = client[datenbank]
    collection = db[collection]
    collection.insert_one(datensatz)


driver = webdriver.Chrome("chromedriver.exe")
driver.get('https://www.zveh.de/fachbetriebssuche.html?tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40extension%5D=EpFachbetriebsuche&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40vendor%5D=Kirchbergerknorr&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40controller%5D=CompanySearch&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40action%5D=show&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5Barguments%5D=YTo3OntzOjEwOiJzZWFyY2hXb3JkIjtzOjA6IiI7czoxMDoicG9zdGFsQ29kZSI7czo1OiI5NzA4NCI7czo4OiJkaXN0YW5jZSI7czozOiIxNTAiO3M6Njoic3VibWl0IjtzOjE4OiJGYWNoYmV0cmllYiBmaW5kZW4iO3M6MTA6ImF0dHJpYnV0ZXMiO3M6MDoiIjtzOjg6ImFjdGl2aXR5IjtzOjE6IjYiO3M6MTE6InN1YkFjdGl2aXR5IjtzOjI6IjU4Ijt9bcbd876d819e998e618644077bbf3f1110ebaa65&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A18%3A%22EpFachbetriebsuche%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A13%3A%22CompanySearch%22%3Bs%3A7%3A%22%40action%22%3Bs%3A4%3A%22show%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A16%3A%22Kirchbergerknorr%22%3B%7D11efba3f9443acc074abfb36351cfc6738d3b0b2&tx_epfachbetriebsuche_companysearch%5B__trustedProperties%5D=a%3A7%3A%7Bs%3A10%3A%22searchWord%22%3Bi%3A1%3Bs%3A10%3A%22postalCode%22%3Bi%3A1%3Bs%3A8%3A%22distance%22%3Bi%3A1%3Bs%3A6%3A%22submit%22%3Bi%3A1%3Bs%3A10%3A%22attributes%22%3Ba%3A11%3A%7Bi%3A0%3Bi%3A1%3Bi%3A1%3Bi%3A1%3Bi%3A2%3Bi%3A1%3Bi%3A3%3Bi%3A1%3Bi%3A4%3Bi%3A1%3Bi%3A5%3Bi%3A1%3Bi%3A6%3Bi%3A1%3Bi%3A7%3Bi%3A1%3Bi%3A8%3Bi%3A1%3Bi%3A9%3Bi%3A1%3Bi%3A10%3Bi%3A1%3B%7Ds%3A8%3A%22activity%22%3Ba%3A1%3A%7Bs%3A10%3A%22__identity%22%3Bi%3A1%3B%7Ds%3A11%3A%22subActivity%22%3Ba%3A1%3A%7Bs%3A10%3A%22__identity%22%3Bi%3A1%3B%7D%7Da02daea287582fc5be99d6dab3942cb46d2309ef&tx_epfachbetriebsuche_companysearch%5BsearchWord%5D=&tx_epfachbetriebsuche_companysearch%5BpostalCode%5D=97074&tx_epfachbetriebsuche_companysearch%5Bdistance%5D=150&tx_epfachbetriebsuche_companysearch%5Bsubmit%5D=Fachbetrieb+finden&tx_epfachbetriebsuche_companysearch%5Battributes%5D=&tx_epfachbetriebsuche_companysearch%5Bactivity%5D%5B__identity%5D=6&tx_epfachbetriebsuche_companysearch%5BsubActivity%5D%5B__identity%5D=58')

soup = BeautifulSoup(driver.page_source, "html.parser")
# # print(soup.prettify())

#Zeile eins_Name
firmenname = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname2 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname3 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#Zeile zwei_name
firmenname4 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname5 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname6 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile drei_name
firmenname7 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname8 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname9 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile vier_name
firmenname10 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname11 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname12 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile fünf_name
firmenname13 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname14 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname15 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile 6_name
firmenname16 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname17 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname18 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile 7_name
firmenname19 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname20 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname21 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[1]/p/b').text

#zeile 8_name
firmenname22 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[1]/p/b').text
firmenname23 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[1]/p/b').text
firmenname24 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[1]/p/b').text


# print(firmenname)
# print(firmenname2)
# print(firmenname3)
# print(firmenname4)
# print(firmenname5)
# print(firmenname6)
# print(firmenname7)
# print(firmenname8)
# print(firmenname9)
# print(firmenname10)
# print(firmenname11)
# print(firmenname12)
# print(firmenname13)
# print(firmenname14)
# print(firmenname15)
# print(firmenname16)
# print(firmenname17)
# print(firmenname18)
# print(firmenname19)
# print(firmenname20)
# print(firmenname21)
# print(firmenname22)
# print(firmenname23)
# print(firmenname24)


#zeile 1
Adresse1 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse2 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse3 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 2
Adresse4 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse5 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse6 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 3
Adresse7 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse8 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse9 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 4
Adresse10 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse11 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse12 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 5
Adresse13 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse14 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse15 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 6
Adresse16 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse17 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse18 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 7
Adresse19 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse20 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse21 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[2]/p').text

#zeile 8
Adresse22 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[2]/p').text
Adresse23 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[2]/p').text
Adresse24 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[2]/p').text




try:
    Adresse1 = Adresse1.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse1):
        if len(j) == 5 and j.isdigit():
            PLZ1 = j
            #index [von : bis] geht bis einen vor index (quasi -1 (wegen index geht bei 0 los?))
            straße1 = Adresse1[:index]
            straße1 = ' '.join(straße1).strip()
            Ort1 = Adresse1[index + 1:]
            Ort1 = ' '.join(Ort1)
            break
except IndexError:
    Adresse1 = 'K/A'
    Ort1 = 'K/A'
    PLZ11 = 'K/A'

try:
    Adresse2 = Adresse2.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse2):
        if len(j) == 5 and j.isdigit():
            PLZ2 = j
            straße2 = Adresse2[:index]
            straße2 = ' '.join(straße2).strip()
            Ort4 = Adresse2[index + 1:]
            Ort4 = ' '.join(Ort4)
            break
except IndexError:
    Adresse2 = 'K/A'
    Ort4 = 'K/A'
    PLZ2 = 'K/A'

try:
    Adresse3 = Adresse3.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse3):
        if len(j) == 5 and j.isdigit():
            PLZ3 = j
            straße3 = Adresse3[:index]
            straße3 = ' '.join(straße3).strip()
            Ort3 = Adresse3[index + 1:]
            Ort3 = ' '.join(Ort3)
            break
except IndexError:
    Adresse3 = 'K/A'
    Ort3 = 'K/A'
    PLZ3 = 'K/A'

try:
    Adresse4 = Adresse4.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse4):
        if len(j) == 5 and j.isdigit():
            PLZ4 = j
            straße4 = Adresse4[:index]
            straße4 = ' '.join(straße4).strip()
            Ort4 = Adresse4[index + 1:]
            Ort4 = ' '.join(Ort4)
            break
except IndexError:
    Adresse4 = 'K/A'
    Ort4 = 'K/A'
    PLZ4 = 'K/A'

try:
    Adresse5 = Adresse5.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse5):
        if len(j) == 5 and j.isdigit():
            PLZ5 = j
            straße5 = Adresse5[:index]
            straße5 = ' '.join(straße5).strip()
            Ort5 = Adresse5[index + 1:]
            Ort5 = ' '.join(Ort5)
            break
except IndexError:
    Adresse5 = 'K/A'
    Ort5 = 'K/A'
    PLZ5 = 'K/A'

try:
    Adresse6 = Adresse6.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse6):
        if len(j) == 5 and j.isdigit():
            PLZ6 = j
            straße6 = Adresse6[:index]
            straße6 = ' '.join(straße6).strip()
            Ort6 = Adresse6[index + 1:]
            Ort6 = ' '.join(Ort6)
            break
except IndexError:
    Adresse6 = 'K/A'
    Ort6 = 'K/A'
    PLZ6 = 'K/A'

try:
    Adresse7 = Adresse7.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse7):
        if len(j) == 5 and j.isdigit():
            PLZ7 = j
            straße7 = Adresse7[:index]
            straße7 = ' '.join(straße7).strip()
            Ort7 = Adresse7[index + 1:]
            Ort7 = ' '.join(Ort7)
            break
except IndexError:
    Adresse7 = 'K/A'
    Ort7 = 'K/A'
    PLZ7 = 'K/A'

try:
    Adresse8 = Adresse8.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse8):
        if len(j) == 5 and j.isdigit():
            PLZ8 = j
            straße8 = Adresse8[:index]
            straße8 = ' '.join(straße8).strip()
            Ort8 = Adresse8[index + 1:]
            Ort8 = ' '.join(Ort8)
            break
except IndexError:
    Adresse8 = 'K/A'
    Ort8 = 'K/A'
    PLZ8 = 'K/A'

try:
    Adresse9 = Adresse9.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse9):
        if len(j) == 5 and j.isdigit():
            PLZ9 = j
            straße9 = Adresse9[:index]
            straße9 = ' '.join(straße9).strip()
            Ort9 = Adresse9[index + 1:]
            Ort9 = ' '.join(Ort9)
            break
except IndexError:
    Adresse9 = 'K/A'
    Ort9 = 'K/A'
    PLZ9 = 'K/A'

try:
    Adresse10 = Adresse10.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse10):
        if len(j) == 5 and j.isdigit():
            PLZ10 = j
            straße10 = Adresse10[:index]
            straße10 = ' '.join(straße10).strip()
            Ort10 = Adresse10[index + 1:]
            Ort10 = ' '.join(Ort10)
            break
except IndexError:
    Adresse10 = 'K/A'
    Ort10 = 'K/A'
    PLZ10 = 'K/A'

try:
    Adresse11 = Adresse11.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse11):
        if len(j) == 5 and j.isdigit():
            PLZ11 = j
            straße11 = Adresse11[:index]
            straße11 = ' '.join(straße11).strip()
            Ort11 = Adresse11[index + 1:]
            Ort11 = ' '.join(Ort11)
            break
except IndexError:
    Adresse11 = 'K/A'
    Ort11 = 'K/A'
    PLZ11 = 'K/A'

try:
    Adresse12 = Adresse12.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse12):
        if len(j) == 5 and j.isdigit():
            PLZ12 = j
            straße12 = Adresse12[:index]
            straße12 = ' '.join(straße12).strip()
            Ort12 = Adresse12[index + 1:]
            Ort12 = ' '.join(Ort12)
            break
except IndexError:
    Adresse12 = 'K/A'
    Ort12 = 'K/A'
    PLZ12 = 'K/A'

try:
    Adresse13 = Adresse13.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse13):
        if len(j) == 5 and j.isdigit():
            PLZ13 = j
            straße13 = Adresse13[:index]
            straße13 = ' '.join(straße13).strip()
            Ort13 = Adresse13[index + 1:]
            Ort13 = ' '.join(Ort13)
            break
except IndexError:
    Adresse13 = 'K/A'
    Ort13 = 'K/A'
    PLZ13 = 'K/A'

try:
    Adresse14 = Adresse14.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse14):
        if len(j) == 5 and j.isdigit():
            PLZ14 = j
            straße14 = Adresse14[:index]
            straße14 = ' '.join(straße14).strip()
            Ort14 = Adresse14[index + 1:]
            Ort14 = ' '.join(Ort14)
            break
except IndexError:
    Adresse14 = 'K/A'
    Ort14 = 'K/A'
    PLZ14 = 'K/A'

try:
    Adresse15 = Adresse15.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse15):
        if len(j) == 5 and j.isdigit():
            PLZ15 = j
            straße15 = Adresse15[:index]
            straße15 = ' '.join(straße15).strip()
            Ort15 = Adresse15[index + 1:]
            Ort15 = ' '.join(Ort15)
            break
except IndexError:
    Adresse15 = 'K/A'
    Ort15 = 'K/A'
    PLZ15 = 'K/A'

try:
    Adresse16 = Adresse16.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse16):
        if len(j) == 5 and j.isdigit():
            PLZ16 = j
            straße16 = Adresse16[:index]
            straße16 = ' '.join(straße16).strip()
            Ort16 = Adresse16[index + 1:]
            Ort16 = ' '.join(Ort16)
            break
except IndexError:
    Adresse16 = 'K/A'
    Ort16 = 'K/A'
    PLZ16 = 'K/A'

try:
    Adresse17 = Adresse17.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse17):
        if len(j) == 5 and j.isdigit():
            PLZ17 = j
            straße17 = Adresse17[:index]
            straße17 = ' '.join(straße17).strip()
            Ort17 = Adresse17[index + 1:]
            Ort17 = ' '.join(Ort17)
            break
except IndexError:
    Adresse17 = 'K/A'
    Ort17 = 'K/A'
    PLZ17 = 'K/A'

try:
    Adresse18 = Adresse18.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse18):
        if len(j) == 5 and j.isdigit():
            PLZ18 = j
            straße18 = Adresse18[:index]
            straße18 = ' '.join(straße18).strip()
            Ort18 = Adresse18[index + 1:]
            Ort18 = ' '.join(Ort18)
            break
except IndexError:
    Adresse18 = 'K/A'
    Ort18 = 'K/A'
    PLZ18 = 'K/A'

try:
    Adresse19 = Adresse19.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse19):
        if len(j) == 5 and j.isdigit():
            PLZ19 = j
            straße19 = Adresse19[:index]
            straße19 = ' '.join(straße19).strip()
            Ort19 = Adresse19[index + 1:]
            Ort19 = ' '.join(Ort19)
            break
except IndexError:
    Adresse19 = 'K/A'
    Ort19 = 'K/A'
    PLZ19 = 'K/A'

try:
    Adresse20 = Adresse20.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse20):
        if len(j) == 5 and j.isdigit():
            PLZ20 = j
            straße20 = Adresse20[:index]
            straße20 = ' '.join(straße20).strip()
            Ort20 = Adresse20[index + 1:]
            Ort20 = ' '.join(Ort20)
            break
except IndexError:
    Adresse20 = 'K/A'
    Ort20 = 'K/A'
    PLZ20 = 'K/A'

try:
    Adresse21 = Adresse21.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse21):
        if len(j) == 5 and j.isdigit():
            PLZ21 = j
            straße21 = Adresse21[:index]
            straße21 = ' '.join(straße21).strip()
            Ort21 = Adresse21[index + 1:]
            Ort21 = ' '.join(Ort21)
            break
except IndexError:
    Adresse21 = 'K/A'
    Ort21 = 'K/A'
    PLZ21 = 'K/A'

try:
    Adresse22 = Adresse22.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse22):
        if len(j) == 5 and j.isdigit():
            PLZ22 = j
            straße22 = Adresse22[:index]
            straße22 = ' '.join(straße22).strip()
            Ort22 = Adresse22[index + 1:]
            Ort22 = ' '.join(Ort22)
            break
except IndexError:
    Adresse22 = 'K/A'
    Ort22 = 'K/A'
    PLZ22 = 'K/A'

try:
    Adresse23 = Adresse23.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse23):
        if len(j) == 5 and j.isdigit():
            PLZ23 = j
            straße23 = Adresse23[:index]
            straße23 = ' '.join(straße23).strip()
            Ort23 = Adresse23[index + 1:]
            Ort23 = ' '.join(Ort23)
            break
except IndexError:
    Adresse23 = 'K/A'
    Ort23 = 'K/A'
    PLZ23 = 'K/A'

try:
    Adresse24 = Adresse24.replace('\n', ' ').split(' ')
    # reversed() läuft array rückwerts durch
    for index, j in enumerate(Adresse24):
        if len(j) == 5 and j.isdigit():
            PLZ24 = j
            straße24 = Adresse24[:index]
            straße24 = ' '.join(straße24).strip()
            Ort24 = Adresse24[index + 1:]
            Ort24 = ' '.join(Ort24)
            break
except IndexError:
    Adresse24 = 'K/A'
    Ort24 = 'K/A'
    PLZ24 = 'K/A'

# print(Adresse1)
# print(Adresse2)
# print(Adresse3)
# print(Adresse4)
# print(Adresse6)
# print(Adresse7)
# print(Adresse8)
# print(Adresse9)
# print(Adresse10)
# print(Adresse11)
# print(Adresse12)
# print(Adresse13)
# print(Adresse14)
# print(Adresse15)
# print(Adresse16)
# print(Adresse17)
# print(Adresse18)
# print(Adresse19)
# print(Adresse20)
# print(Adresse21)
# print(Adresse22)
# print(Adresse23)
# print(Adresse24)

#tele 1
Telenummer1 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer2 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer3 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 2
Telenummer4 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer5 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer6 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 3
Telenummer7 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer8 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer9 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 4
Telenummer10 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer11 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer12 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 5
Telenummer13 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer14 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer15 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 6
Telenummer16 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer17 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer18 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 7
Telenummer19 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer20 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer21 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[3]/p').text

#tele 8
Telenummer22 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[3]/p').text
Telenummer23 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[3]/p').text
Telenummer24 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[3]/p').text


# print(Telenummer1)
# print(Telenummer2)
# print(Telenummer3)
# print(Telenummer4)
# print(Telenummer5)
# print(Telenummer6)
# print(Telenummer7)
# print(Telenummer8)
# print(Telenummer9)
# print(Telenummer10)
# print(Telenummer11)
# print(Telenummer12)
# print(Telenummer13)
# print(Telenummer14)
# print(Telenummer15)
# print(Telenummer16)
# print(Telenummer17)
# print(Telenummer18)
# print(Telenummer19)
# print(Telenummer20)
# print(Telenummer21)
# print(Telenummer22)
# print(Telenummer23)
# print(Telenummer24)

#fax 1
fax1 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax2 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax3 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 2
fax4 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax5 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax6 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 3
fax7 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax8 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax9 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 4
fax10 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax11 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax12 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 5
fax13 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax14 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax15 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 6
fax16 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax17 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax18 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 7
fax19 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax20 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax21 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[4]/p').text

#fax 8
fax22 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[4]/p').text
fax23 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[4]/p').text
fax24 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[4]/p').text

# print(fax1)
# print(fax2)
# print(fax3)
# print(fax4)
# print(fax5)
# print(fax6)
# print(fax7)
# print(fax8)
# print(fax9)
# print(fax10)
# print(fax11)
# print(fax12)
# print(fax13)
# print(fax14)
# print(fax15)
# print(fax16)
# print(fax17)
# print(fax18)
# print(fax19)
# print(fax20)
# print(fax21)
# print(fax22)
# print(fax23)
# print(fax24)

#mail 1
mail1 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail2 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail3= driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[1]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 2
mail4 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail5 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail6 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[2]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 3
mail7 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail8 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail9 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[3]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 4
mail10 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail11 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail12 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[4]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 5
mail13 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail14 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail15 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[5]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 6
mail16 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail17 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail18 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[6]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 7
mail19 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail20 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail21 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[7]/div[3]/div/div[1]/div[2]/div[5]/p/a').text

#mail 8
mail22 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[1]/div/div[1]/div[2]/div[5]/p/a').text
mail23 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[2]/div/div[1]/div[2]/div[5]/p/a').text
mail24 = driver.find_element_by_xpath('//*[@id="c68651"]/div[3]/div[8]/div[3]/div/div[1]/div[2]/div[5]/p/a').text


# print(mail1)
# print(mail2)
# print(mail3)
# print(mail4)
# print(mail5)
# print(mail6)
# print(mail7)
# print(mail8)
# print(mail9)
# print(mail10)
# print(mail11)
# print(mail12)
# print(mail13)
# print(mail14)
# print(mail15)
# print(mail16)
# print(mail17)
# print(mail18)
# print(mail19)
# print(mail20)
# print(mail21)
# print(mail22)
# print(mail23)
# print(mail24)

firma = {"firma_name": firmenname,
              "firma_strasse" : straße1,
              "firma_plz" : PLZ1,
              "firma_ort": Ort1,
              "firma_telefon": Telenummer1,
              "firma_fax":fax1,
              "firma_mail" :mail1}

firma2 = {"firma_name": firmenname2,
              "firma_strasse" : straße2,
              "firma_plz" : PLZ2,
              "firma_ort": Ort4,
              "firma_telefon": Telenummer2,
              "firma_fax":fax2,
              "firma_mail" :mail2}

firma3 = {"firma_name": firmenname3,
              "firma_strasse" : straße3,
              "firma_plz" : PLZ3,
              "firma_ort": Ort3,
              "firma_telefon": Telenummer3,
              "firma_fax":fax3,
              "firma_mail" :mail3}

firma4 = {"firma_name": firmenname4,
              "firma_strasse" : straße4,
              "firma_plz" : PLZ4,
              "firma_ort": Ort4,
              "firma_telefon": Telenummer4,
              "firma_fax":fax4,
              "firma_mail" :mail4}

firma5 = {"firma_name": firmenname5,
              "firma_strasse" : straße5,
              "firma_plz" : PLZ5,
              "firma_ort": Ort5,
              "firma_telefon": Telenummer5,
              "firma_fax":fax5,
              "firma_mail" :mail5}

firma6 = {"firma_name": firmenname6,
              "firma_strasse" : straße6,
              "firma_plz" : PLZ6,
              "firma_ort": Ort6,
              "firma_telefon": Telenummer6,
              "firma_fax":fax6,
              "firma_mail" :mail6}

firma7 = {"firma_name": firmenname7,
              "firma_strasse" : straße7,
              "firma_plz" : PLZ7,
              "firma_ort": Ort7,
              "firma_telefon": Telenummer7,
              "firma_fax":fax7,
              "firma_mail" :mail7}

firma8 = {"firma_name": firmenname,
              "firma_strasse" : straße8,
              "firma_plz" : PLZ8,
              "firma_ort": Ort8,
              "firma_telefon": Telenummer8,
              "firma_fax":fax8,
              "firma_mail" :mail8}

firma9 = {"firma_name": firmenname9,
              "firma_strasse" : straße9,
              "firma_plz" : PLZ9,
              "firma_ort": Ort9,
              "firma_telefon": Telenummer9,
              "firma_fax":fax9,
              "firma_mail" :mail9}

firma10 = {"firma_name": firmenname10,
              "firma_strasse" : straße10,
              "firma_plz" : PLZ10,
              "firma_ort": Ort10,
              "firma_telefon": Telenummer10,
              "firma_fax":fax10,
              "firma_mail" :mail10}

firma11 = {"firma_name": firmenname11,
              "firma_strasse" : straße11,
              "firma_plz" : PLZ11,
              "firma_ort": Ort11,
              "firma_telefon": Telenummer11,
              "firma_fax":fax11,
              "firma_mail" :mail11}

firma12 = {"firma_name": firmenname12,
              "firma_strasse" : straße12,
              "firma_plz" : PLZ12,
              "firma_ort": Ort12,
              "firma_telefon": Telenummer12,
              "firma_fax":fax12,
              "firma_mail" :mail12}

firma13 = {"firma_name": firmenname13,
              "firma_strasse" : straße13,
              "firma_plz" : PLZ13,
              "firma_ort": Ort13,
              "firma_telefon": Telenummer13,
              "firma_fax":fax13,
              "firma_mail" :mail13}

firma14 = {"firma_name": firmenname14,
              "firma_strasse" : straße14,
              "firma_plz" : PLZ14,
              "firma_ort": Ort14,
              "firma_telefon": Telenummer14,
              "firma_fax":fax14,
              "firma_mail" :mail14}

firma15 = {"firma_name": firmenname15,
              "firma_strasse" : straße15,
              "firma_plz" : PLZ15,
              "firma_ort": Ort15,
              "firma_telefon": Telenummer15,
              "firma_fax":fax15,
              "firma_mail" :mail15}

firma16 = {"firma_name": firmenname16,
              "firma_strasse" : straße16,
              "firma_plz" : PLZ16,
              "firma_ort": Ort16,
              "firma_telefon": Telenummer16,
              "firma_fax":fax16,
              "firma_mail" :mail16}

firma17 = {"firma_name": firmenname17,
              "firma_strasse" : straße17,
              "firma_plz" : PLZ17,
              "firma_ort": Ort17,
              "firma_telefon": Telenummer17,
              "firma_fax":fax17,
              "firma_mail" :mail17}

firma18 = {"firma_name": firmenname18,
              "firma_strasse" : straße18,
              "firma_plz" : PLZ18,
              "firma_ort": Ort18,
              "firma_telefon": Telenummer18,
              "firma_fax":fax18,
              "firma_mail" :mail18}

firma19 = {"firma_name": firmenname19,
              "firma_strasse" : straße19,
              "firma_plz" : PLZ19,
              "firma_ort": Ort19,
              "firma_telefon": Telenummer19,
              "firma_fax":fax19,
              "firma_mail" :mail19}

firma20 = {"firma_name": firmenname20,
              "firma_strasse" : straße20,
              "firma_plz" : PLZ20,
              "firma_ort": Ort20,
              "firma_telefon": Telenummer20,
              "firma_fax":fax20,
              "firma_mail" :mail20}

firma21 = {"firma_name": firmenname21,
              "firma_strasse" : straße21,
              "firma_plz" : PLZ21,
              "firma_ort": Ort21,
              "firma_telefon": Telenummer21,
              "firma_fax":fax21,
              "firma_mail" :mail21}

firma22 = {"firma_name": firmenname22,
              "firma_strasse" : straße22,
              "firma_plz" : PLZ22,
              "firma_ort": Ort22,
              "firma_telefon": Telenummer22,
              "firma_fax":fax22,
              "firma_mail" :mail22}

firma23 = {"firma_name": firmenname23,
              "firma_strasse" : straße23,
              "firma_plz" : PLZ23,
              "firma_ort": Ort23,
              "firma_telefon": Telenummer23,
              "firma_fax":fax23,
              "firma_mail" :mail23}

firma24 = {"firma_name": firmenname24,
              "firma_strasse" : straße24,
              "firma_plz" : PLZ24,
              "firma_ort": Ort24,
              "firma_telefon": Telenummer24,
              "firma_fax":fax24,
              "firma_mail" :mail24}


print(firma)
print(firma2)
print(firma3)
print(firma4)
print(firma5)
print(firma6)
print(firma7)
print(firma8)
print(firma9)
print(firma10)
print(firma11)
print(firma12)
print(firma13)
print(firma14)
print(firma15)
print(firma16)
print(firma17)
print(firma18)
print(firma19)
print(firma20)
print(firma21)
print(firma22)
print(firma23)
print(firma24)

from pymongo import MongoClient
client = MongoClient("192.168.100.5", 27017, maxPoolSize=50)
db = client['yanghi']  # mz durch die entsprechende Datenbank ersetzen
collection = db['zveh']  # db durch entsprechende DB ersetzen
collection.insert_one(firma)
collection.insert_one(firma2)
collection.insert_one(firma3)
collection.insert_one(firma4)
collection.insert_one(firma5)
collection.insert_one(firma6)
collection.insert_one(firma7)
collection.insert_one(firma8)
collection.insert_one(firma9)
collection.insert_one(firma10)
collection.insert_one(firma11)
collection.insert_one(firma12)
collection.insert_one(firma13)
collection.insert_one(firma14)
collection.insert_one(firma15)
collection.insert_one(firma16)
collection.insert_one(firma17)
collection.insert_one(firma18)
collection.insert_one(firma19)
collection.insert_one(firma20)
collection.insert_one(firma21)
collection.insert_one(firma22)
collection.insert_one(firma23)
collection.insert_one(firma24)
