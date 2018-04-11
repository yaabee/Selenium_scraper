from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://hwk-heilbronn-service.de/apps/services/modules/hws/index.php')

landkreis = driver.find_element_by_id('hwr_ort1')

# ActionChains(driver).move_to_element(landkreis).click().send_keys(Keys.TAB).send_keys(Keys.DOWN).perform()


action = ActionChains(driver)
action.move_to_element(landkreis)
action.click()
action.send_keys(Keys.TAB)
action.send_keys(Keys.DOWN)
action.send_keys(Keys.ENTER)
action.perform()


# metaBlock = driver.find_element_by_class_name('list-group')


driver.find_element_by_xpath('//*[@id="results_container_content"]')







# ladida = driver.window_handles[0]
# print(ladida)




# driver.switch_to.window(driver.window_handles[-1])
#
# soup = BeautifulSoup(driver.page_source, "html.parser")
#
# for meta in soup.findAll('div', {'class': 'listgroup-text'}):
#     print(meta)

# print(soup)






# driver.implicitly_wait(3)
#
# print(ladi)


# soup = BeautifulSoup(driver.page_source, "html.parser")
# # print(soup.prettify())
#
# for meta in  soup.findAll('a', {'href':'#'}):
#     print(meta)


