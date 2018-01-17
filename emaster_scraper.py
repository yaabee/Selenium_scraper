import urllib3
from bs4 import BeautifulSoup
import time

target = 'https://www.e-masters.de/e-masters-fachbetriebe.html'

http = urllib3.PoolManager()                            #von urllib3, hol seite (für request war die url zu lang)
page = http.request('GET', target)
time.sleep(10)
soup = BeautifulSoup(page.data.decode())                #collection of tag objects := <class 'bs4.element.ResultSet'>

#metainfo = soup.find_all("li", class_="odd")

print(soup.prettify())