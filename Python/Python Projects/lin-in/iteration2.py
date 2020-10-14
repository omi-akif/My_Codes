from time import sleep
from selenium import webdriver

#path to the chromedriver
driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')

driver.get('https://www.google.com')

#locate search form by name
search_query = driver.find_element_by_name('q')

#Input search words
search_query.send_keys('X-Men')

#Simulate return key
search_query.submit()

Xmen_urls = driver.find_elements_by_class_name('iUh30')

for page in range(0,3):
    Xmen_urls = [url.text for url in Xmen_urls]

    #loop to iterate through all links in the google search query
    for Xmen_url in Xmen_urls:
         driver.get(Xmen_url)
         sel = Selector(text = driver.page_source)

    #Go back to google search
    driver.get('https://www.gooogle.com') 

    #locate search form by name
    search_query = driver.find_element_by_name('q')

    #Input search words
    search_query.send_keys('X-Men')

    #Simulate return key
    search_query.submit()

    #find next page icon in Google search
    Next_Google_page = driver.find_element_by_link_text("Next").click()

    page += 1