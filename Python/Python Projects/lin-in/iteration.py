from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')
driver.get("https://www.google.com/")
driver.find_element_by_id("lst-ib").send_keys("search")
driver.submit()
driver.maximize_window()
pages=driver.find_elements_by_xpath("//*[@id='nav']/tbody/tr/td/a")
counter=1
for page in pages:
     pages=driver.find_elements_by_xpath("//*[@id='nav']/tbody/tr/td/a")
     counter+=1
     pages[counter].click()