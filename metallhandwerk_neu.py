from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

url = 'https://www.metall-verband.de/fachbetriebe/'

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')

print(soup.prettify)


