from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')
driver.get('https://www.google.com')

# //*[@id="identifierId"]
# driver.find_element_by_xpath('//*[@id="identifierId"]')
# Next button google account login == //*[@id="identifierNext"]/content/span

search_query = driver.find_element_by_name('q')

search_query.send_keys('site:linkedin.com/in/ AND "East West University" AND "Bangladesh"')

search_query.submit()
sleep(120)

linkedin_urls = driver.find_elements_by_class_name('iUh30')

links = [url.text for url in linkedin_urls]

print(links)
driver.quit()