from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')
    #for bash terminal: /mnt/d/Chrome_Driver/chromedriver.exe
    #for cmd terminal: D:\Chrome_Driver\chromedriver.exe
sleep(2)
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
sleep(3)

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
sleep(4)


driver.execute_script("window.open('https://www.linkedin.com/search/results/people/?origin=DISCOVER_FROM_SEARCH_HOME');")
sleep(3)

driver.close()
driver.switch_to.window(driver.window_handles[-1])

#all_filters = driver.find_element_by_xpath('//*[@id="ember272"]/span')
#all_filters = driver.find_element_by_link_text('All Filters')

search = driver.find_element_by_xpath('//*[@id="ember33"]/input')
search.send_keys('East West University')
search.send_keys(Keys.ENTER)

#//*[@id="ember33"]/input
# class == search-filters-bar__all-filters flex-shrink-zero mr3 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view

def find_odds(num_ber):
    if not num_ber:
        return []
    if num_ber[0]%2 == 1:
        return [num_ber[0]] + find_odds(num_ber[1:])
    return find_odds(num_ber[1:])

def find_people(li):
    for i in range(len(li)):
        odd_find = find_odds(range(len(linkedin_urls)))
        l = linkedin_urls[odd_find[i-len(li)]].get_attribute('href')
        #l = linkedin_urls[i].get_attribute('href')
        driver.execute_script("window.open(arguments[0]);", l)
        sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        
        #driver.get(linkedin_urls[i])
        sleep(5)
        
        driver.execute_script("window.scrollTo(0,811.495);")
        sleep(0.5)
        driver.execute_script("window.scrollTo(811.495,1622.99);")
        sleep(0.5)
        driver.execute_script("window.scrollTo(1622.99,2434.485);")
        sleep(0.5)
        driver.execute_script("window.scrollTo(2434.485,3254.98);")
        sleep(0.5)

        #sel = Selector(text=driver.page_source)

        #to match against the provided name
        #re_name = name_1[i]

        name_2 = driver.find_element_by_css_selector('li.inline.t-24.t-black.t-normal.break-words')
        name = name_2.get_attribute('innerHTML')
        if name:
            name = name.strip()

        wo_rk = driver.find_element_by_css_selector('h2.mt1.inline-block.t-18.t-black.t-normal')
        work = wo_rk.get_attribute('innerHTML')
        if work:
            work = work.strip()

        
        #current position/work
        #c_position = current_pos_txt[i]
        #To find if the candidate has any details of his past

        if current_pos_txt == "":
            print("As per work")
        
        #degree

        deg_ree = driver.find_element_by_css_selector('span.pv-entity__comma-item')
        degree = deg_ree.get_attribute('innerHTML')
        if degree:
            degree = degree.strip()

        #replaced with innerHTML
        #education = [deg.text for deg in deg_ree] 

        #degree = sel.css('span.pv-entity__comma-item').extract_first()
        #if degree:
        #    degree = degree.strip()
        
        #pv-entity__school-name t-16 t-black t-bold

        #university = sel.css('h3.pv-entity__school-name.t-16.t-black.t-bold')

        uni_ver = driver.find_element_by_css_selector('h3.pv-entity__school-name.t-16.t-black.t-bold')
        university = uni_ver.get_attribute('innerHTML')
        if university:
            university = university.strip()

        #year
        ye_ars = driver.find_element_by_tag_name('time') 
        years = [y.text for y in ye_ars]  

        #url of the 
        link_url = driver.current_url

        print('\n')
        print('Name: ' + name)
        print('Work: ' + work)
        print('Degree: ' + degree)
        print('Years ' + str(years))
        print('URL ' + link_url)

        driver.close()
        driver.switch_to_window(driver.window_handles[-1])

        return name, work, degree, years, link_url



# Find the object to interact with.
#driver.find_element_by_class_name("foo").click()

# New tabs will be the last object in window_handles
#driver.switch_to.window(driver.window_handles[-1])

# close the tab
#driver.close()

#search_query = driver.find_element_by_name('q')
#search_query.send_keys('site:linkedin.com/in/ AND "East West University" AND "Bangladesh"')
#sleep(0.5)

#search_query.submit()
#sleep(3)


counter = 1
#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

#actionChains = ActionChains(driver)

while True:
    driver.execute_script("window.scrollTo(0,557);")
    sleep(0.5)
    driver.execute_script("window.scrollTo(557,1114);")
    sleep(0.5)
    driver.execute_script("window.scrollTo(1114,1671);")
    sleep(0.5)
    driver.execute_script("window.scrollTo(1671,2229);")
    sleep(0.5)

    li = driver.find_elements_by_class_name('span.name.actor-name')

    linkedin_urls = driver.find_elements_by_css_selector('a.search-result__result-link.ember-view')
    current_pos = driver.find_elements_by_css_selector('p.search-result__snippets.mt2.t-12.t-black--light.t-normal')
    
    #name_1 = [url.text for url in linkedin_urls]
    current_pos_txt = [ul.text for ul in current_pos]


    #f = open('output.html', 'w')
    #driver.page_source = f


    sleep(5)

    #driver.close()


        #a = driver.page_source
        #file = open('ist.html', 'w', encoding='utf-8')
        #file.write(a)
        #file.close()

    counter+=1

    driver.get("https://www.linkedin.com/search/results/people/?keywords=East%%20West%%20University&origin=GLOBAL_SEARCH_HEADER&page=%d" % counter)


    if linkedin_urls[0] == linkedin_urls[-1]:
        break

    sleep(0.5)


sleep(0.5)

driver.quit()