from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import re



search_field = driver.find_element_by_id("plz_ort")
search_field.clear()
search_field.send_keys("49685")
search_field.send_keys(Keys.RETURN)