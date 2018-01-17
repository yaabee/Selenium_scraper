from bs4 import BeautifulSoup
import requests
import time
import lxml


target = 'https://www.gelbeseiten.de/fitness/berlin,,,,,umkreis-50000/s2'
page = requests.get(target)
soup = BeautifulSoup(page.content)
metainfo = soup.find_all("div", class_="table")

#print(metainfo)

del(metainfo[0])

#print(metainfo)

for tag in metainfo:

    naked_meta = tag.text.strip()

    #print(naked_meta)

    firma = []
    for line in naked_meta.split('\n'):
        line = line.strip()

        if line:
            firma.append(line)

            print(line)









    # if naked_meta:
    #     Firma.append(naked_meta)
    #
    #     try:
    #         Name = Firma[1]
    #     except IndexError:
    #         Name = 'K/A'
    #
    #     print(Name)









