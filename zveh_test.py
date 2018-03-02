# from bs4 import BeautifulSoup
# from selenium import webdriver
# import time
#
#
# # def insert_new_dataset_into_mdb(mdb_uri, datenbank, collection, datensatz):
# #     from pymongo import MongoClient
# #     client = MongoClient(mdb_uri, 27017, maxPoolSize=500)
# #     db = client[datenbank]
# #     collection = db[collection]
# #     collection.insert_one(datensatz)
#
#
# driver = webdriver.Chrome("chromedriver.exe")
# driver.implicitly_wait(3)
# driver.get('https://www.zveh.de/fachbetriebssuche.html?tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40extension%5D=EpFachbetriebsuche&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40vendor%5D=Kirchbergerknorr&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40controller%5D=CompanySearch&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40action%5D=show&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5Barguments%5D=YTo3OntzOjEwOiJzZWFyY2hXb3JkIjtzOjA6IiI7czoxMDoicG9zdGFsQ29kZSI7czo1OiI5NzA4NCI7czo4OiJkaXN0YW5jZSI7czozOiIxNTAiO3M6Njoic3VibWl0IjtzOjE4OiJGYWNoYmV0cmllYiBmaW5kZW4iO3M6MTA6ImF0dHJpYnV0ZXMiO3M6MDoiIjtzOjg6ImFjdGl2aXR5IjtzOjE6IjYiO3M6MTE6InN1YkFjdGl2aXR5IjtzOjI6IjU4Ijt9bcbd876d819e998e618644077bbf3f1110ebaa65&tx_epfachbetriebsuche_companysearch%5B__referrer%5D%5B%40request%5D=a%3A4%3A%7Bs%3A10%3A%22%40extension%22%3Bs%3A18%3A%22EpFachbetriebsuche%22%3Bs%3A11%3A%22%40controller%22%3Bs%3A13%3A%22CompanySearch%22%3Bs%3A7%3A%22%40action%22%3Bs%3A4%3A%22show%22%3Bs%3A7%3A%22%40vendor%22%3Bs%3A16%3A%22Kirchbergerknorr%22%3B%7D11efba3f9443acc074abfb36351cfc6738d3b0b2&tx_epfachbetriebsuche_companysearch%5B__trustedProperties%5D=a%3A7%3A%7Bs%3A10%3A%22searchWord%22%3Bi%3A1%3Bs%3A10%3A%22postalCode%22%3Bi%3A1%3Bs%3A8%3A%22distance%22%3Bi%3A1%3Bs%3A6%3A%22submit%22%3Bi%3A1%3Bs%3A10%3A%22attributes%22%3Ba%3A11%3A%7Bi%3A0%3Bi%3A1%3Bi%3A1%3Bi%3A1%3Bi%3A2%3Bi%3A1%3Bi%3A3%3Bi%3A1%3Bi%3A4%3Bi%3A1%3Bi%3A5%3Bi%3A1%3Bi%3A6%3Bi%3A1%3Bi%3A7%3Bi%3A1%3Bi%3A8%3Bi%3A1%3Bi%3A9%3Bi%3A1%3Bi%3A10%3Bi%3A1%3B%7Ds%3A8%3A%22activity%22%3Ba%3A1%3A%7Bs%3A10%3A%22__identity%22%3Bi%3A1%3B%7Ds%3A11%3A%22subActivity%22%3Ba%3A1%3A%7Bs%3A10%3A%22__identity%22%3Bi%3A1%3B%7D%7Da02daea287582fc5be99d6dab3942cb46d2309ef&tx_epfachbetriebsuche_companysearch%5BsearchWord%5D=&tx_epfachbetriebsuche_companysearch%5BpostalCode%5D=97074&tx_epfachbetriebsuche_companysearch%5Bdistance%5D=150&tx_epfachbetriebsuche_companysearch%5Bsubmit%5D=Fachbetrieb%20finden&tx_epfachbetriebsuche_companysearch%5Battributes%5D=&tx_epfachbetriebsuche_companysearch%5Bactivity%5D%5B__identity%5D=6&tx_epfachbetriebsuche_companysearch%5BsubActivity%5D%5B__identity%5D=58&tx_epfachbetriebsuche_companysearch%5B%40widget_0%5D%5BcurrentPage%5D=3&cHash=6564fbd625cf67bb7b36880304f2f7a3')
#
# soup = BeautifulSoup(driver.page_source, "html.parser")
#
# # print(soup)
# metainfo = soup.find_all('div', {'class': 'dates'})
#
# # print(metainfo)
#
# for x in metainfo:
#     print(x)
#     block = []
#     if x.has_attr('dates name'):
#         block.append(x)
#         print(block)
#         print('neeeeeeeeeew bloooooooooock')
#         time.sleep(0.5)
#         if x.has_attr('dates name'):
#             break
#     print('neeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeew')
#
#


block = []
for x in range(5):
    block.append(x)
print(block)