from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

#username authentication
username = driver.find_element_by_id('username')
username.send_keys('omiakif@gmail.com')
sleep(0.5)

#password authentication
password = driver.find_element_by_id('password')
password.send_keys('m911springfieldm911')
sleep(0.5)

#login
log_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
log_in_button.click()
sleep(0.5)

driver.execute_script("window.open('https://www.google.com/');")
sleep(3)

driver.close()
driver.switch_to.window(driver.window_handles[-1])

# Find the object to interact with.
#driver.find_element_by_class_name("foo").click()

# New tabs will be the last object in window_handles
#driver.switch_to.window(driver.window_handles[-1])

# close the tab
#driver.close()

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "East West University" AND "Bangladesh"')
sleep(0.5)

search_query.submit()
sleep(3)


counter = 1


while True:
    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    links = [url.text for url in linkedin_urls]
    print(links)
    counter+=1
    continue_link = driver.find_element_by_link_text('%d' % counter)
    continue_link.click()
    #s = input("press 's' to stop?")
    # require mvcrt module

    sleep(0.5)
    

# links = [url.text for url in linkedin_urls]
#print(links)
#//*[@id="nav"]/tbody/tr/td[2]/a

#page1 == //*[@id="nav"]/tbody/tr/td[2]/a
#page2 == //*[@id="nav"]/tbody/tr/td[3]/a
#page3 == //*[@id="nav"]/tbody/tr/td[4]/a
#page4 == //*[@id="nav"]/tbody/tr/td[5]/a
#page5 == //*[@id="nav"]/tbody/tr/td[6]/a

sleep(0.5)

driver.quit()