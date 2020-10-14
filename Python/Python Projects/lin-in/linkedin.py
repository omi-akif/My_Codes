#%%
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import itertools
import numpy as np
from selenium.common.exceptions import NoSuchElementException
import functools
import csv
#%%
alumFile = open('alum_link.csv', 'w')
csv_writer = csv.writer(alumFile)
with alumFile:
    csv_writer.writerow(['Name', 'Work', 'Working  at ','Experience', 'Company/Institution', 'Years/Years of experience', '(Voluntary) Years of experience','Education', 'Details of Education', 'Years', 'URL'])


driver = webdriver.Chrome('/mnt/d/Chrome_Driver/chromedriver.exe')
    #for bash terminal: /mnt/d/Chrome_Driver/chromedriver.exe
    #for cmd terminal: D:\Chrome_Driver\chromedriver.exe
sleep(2)
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
sleep(10)



def check_by_selector(css_xpath):
    try:
        driver.find_element_by_css_selector(css_xpath)
        if css_xpath:
            pass
    except NoSuchElementException:
        return False
    return True

def check_by_selectors(css):
    try:
        driver.find_elements_by_css_selector(css)
        if css:
            pass
    except NoSuchElementException:
        return False
    return True

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
sleep(10)


driver.execute_script("window.open('https://www.linkedin.com/search/results/people/?origin=DISCOVER_FROM_SEARCH_HOME');")
sleep(3)

driver.close()
driver.switch_to.window(driver.window_handles[-1])

#all_filters = driver.find_element_by_xpath('//*[@id="ember272"]/span')
#all_filters = driver.find_element_by_link_text('All Filters')

check_by_selector('//*[@id="ember33"]/input')

search = driver.find_element_by_xpath('//*[@id="ember33"]/input')
search.send_keys('East West University')
search.send_keys(Keys.ENTER)

#//*[@id="ember33"]/input
# class == search-filters-bar__all-filters flex-shrink-zero mr3 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view

def validate_field(field):
    if field:
        pass
    else:
        field = "No results"
    return field
        
#a = list(range(len(na_ames)))
#b = list(range(len(current_pos_txt)))
# result == '1234' 
def convert(li_st):
    res  = functools.reduce(lambda total, d: 10 * total + d, li_st, 0)
    return(str(res))


#[1, 2, 3, 4]
def rewind(str_ing):
    m = list(map(int, str_ing))
    return m


def con (stri):
    ret = list(convert(stri))
    return (ret) 



def find_odds(num_ber):
    if not num_ber:
        return []
    if num_ber[0]%2 == 1:
        return [num_ber[0]] + find_odds(num_ber[1:])
    return find_odds(num_ber[1:])





def matrix(a, b, match_score=3, gap_cost=2):
    H = np.zeros((len(a) + 1, len(b) + 1), np.int)

    for i, j in itertools.product(range(1, H.shape[0]), range(1, H.shape[1])):
        match = H[i-1, j-1] + (match_score if a[i-1] == b[j-1] else - match_score)
        delete = H[i - 1,j] - gap_cost
        insert = H[i, j - 1] - gap_cost
        H[i,j] = max(match, delete, insert, 0)

    return H

def traceback(H, b, b_='', old_i=0):
    H_flip = np.flip(np.flip(H,0), 1)
    i_, j_ = np.unravel_index(H_flip.argmax(), H_flip.shape)
    i, j = np.subtract(H.shape, (i_+ 1, j_+1))
    if H[i, j] == 0:
        return b_, j
    b_ = b[j - 1] + '_' + b_ if old_i - i > 1 else b[j - 1] + b_
    return traceback(H[0:i, 0:j], b, b_, i)

def smith_waterman(a, b, match_score=3, gap_cost=2):
    a, b = a.upper(), b.upper()
    H = matrix(a, b, match_score, gap_cost)
    b_, pos = traceback(H, b)
    return pos, pos + len(b_)


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

#%%
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

    na_ames = driver.find_elements_by_css_selector('span.name.actor-name')

    linkedin_urls = driver.find_elements_by_css_selector('a.search-result__result-link.ember-view')
    #for i in range(len(na_ames)):
    #current_pos[i] = driver.find_element_by_css_selector('p.search-result__snippets.mt2.t-12.t-black--light.t-normal')

    
    #for i in range(len(na_ames)):
        
    current_pos = driver.find_elements_by_css_selector('p.search-result__snippets.mt2.t-12.t-black--light.t-normal')
    
    #name_1 = [url.text for url in linkedin_urls]
    current_pos_txt = [ul.text for ul in current_pos]


    #f = open('output.html', 'w')
    #driver.page_source = f
    le_ngth = len(current_pos_txt)


    sleep(5)

    #driver.close()
    for i in range(len(na_ames)):
        odd_find = find_odds(range(len(linkedin_urls)))
        l = linkedin_urls[odd_find[i-len(na_ames)]].get_attribute('href')
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

        #current_pos = current_pos_txt[len(current_pos_txt)]
        #current position/work

        a = list(range(len(na_ames)))
        b = list(range(len(current_pos_txt)))





        #le_ngth-=1

        #if not (current_pos_txt[-(len(current_pos_txt)-le_ngth)]) == []:
        #    c_position = current_pos_txt[-(len(current_pos_txt)-le_ngth)]
        #else:
        #    c_position = "Empty Cell"

        #c_position = current_pos_txt[-(len(current_pos_txt)-le_ngth)]
        #To find if the candidate has any details of his past

        
        #degree

        #document.querySelector(".example");

        exper_ience = driver.find_elements_by_css_selector('h3.t-16.t-black.t-bold')
        experience = [exp.text for exp in exper_ience]
        if experience:
            experience = [i.strip() for i in experience] 
        experience = str(experience)

        #working_at_ = check_by_selectors('span.pv-entity__secondary-title')
        #working_at = driver.find_element_by_css_selector('span.pv-entity__secondary-title')
        #working_at =  working_at.get_attribute('innerHTML')
        
        comp = driver.find_elements_by_css_selector('span.pv-entity__secondary-title')
        company_institutation = [com.get_attribute('innerHTML') for com in comp]
        if company_institutation:
            company_institutation = [i.strip() for i in company_institutation]
        company_institutation = str(company_institutation)



        yea_expe_rience = driver.find_elements_by_css_selector('span.pv-entity__bullet-item-v2')
        years_experience = [yea.get_attribute('innerHTML') for yea in yea_expe_rience]
        if years_experience:
            years_experience = [i.strip() for i in years_experience]
        years_experience = str(years_experience)

        vol_years_exp_erience = driver.find_elements_by_css_selector('span.pv-entity__bullet-item')
        vol_years_experience = [yea.text for yea in vol_years_exp_erience]
        vol_years_experience = str(vol_years_experience)


        edu_cation = driver.find_elements_by_css_selector('h3.pv-entity__school-name.t-16.t-black.t-bold')
        education = [edu.get_attribute('innerHTML') for edu in edu_cation]
        if education:
            education=[i.strip() for i in education]
        education = str(education)

        edu_details_ = driver.find_elements_by_css_selector('span.pv-entity__comma-item')
        edu_details = [edud.get_attribute('innerHTML') for edud in edu_details_]
        if edu_details:
            edu_details =  [i.strip() for i in edu_details]
        edu_details = str(edu_details)
        

        ye_ars = driver.find_elements_by_tag_name('time') 
        yea = [y.text for y in ye_ars] 
        years = str(yea)


        #pv-entity__comma-item



        #pv-entity__school-name t-16 t-black t-bold

        #pv-entity__bullet-item-v2

        #pv-entity__secondary-title
        

        #pv-entity__secondary-title


        #'h3.t-16.t-black.t-bold'

        #replaced with innerHTML
        #education = [deg.text for deg in deg_ree] 

        #degree = sel.css('span.pv-entity__comma-item').extract_first()
        #if degree:
        #    degree = degree.strip()
        
        #pv-entity__school-name t-16 t-black t-bold

        #university = sel.css('h3.pv-entity__school-name.t-16.t-black.t-bold')

        #year
         

        #url of the 
        link_url = driver.current_url

        #name
        #work
        #experience
        #company_institutation
        #years_experience
        #education
        #edu_details_
        #years


        name = validate_field(name)
        work = validate_field(work)

        experience = validate_field(experience)
        company_institutation = validate_field(company_institutation)
        years_experience = validate_field(years_experience)
        vol_years_experience = validate_field(vol_years_experience)
        education = validate_field(education)
        edu_details = validate_field(edu_details)
        years = validate_field(years)
        link_url = validate_field(link_url)
        
        #c_position = validate_field(c_position)


        print('\n')
        print('Name: ' + name)
        
        if ' at ' in work:
            print(work.split(' at ')[0])
            print(work.split(' at ')[1:])
        else:
            print(work)
        
        print('Work: ' + work.split(' at ')[0])
        print('Working Experience' + str(work.split(' at ')[1:]))
        print('Experience: ' + experience)
        print('Company/Institution: ' + company_institutation)
        print('Years/Years of experience: ' + years_experience)
        print('(Voluntary) Years of experience: ' + vol_years_experience)
        print('Education: ' + education)
        print('Details of Education: ' + edu_details)
        print('Years ' + years)
        print('URL ' + link_url)
        #print('Past or Current' + c_position)

        alumFile = open('alum_link.csv', 'a')
        csv_writer = csv.writer(alumFile)

        if ' at ' in work:
            work_1 = work.split(' at ')[0]
            work_1 = str(work_1)
            work_2 = work.split(' at ')[1:]
            work_2 = str(work_2)
        else:
            work_1 = work
            work_2 = "Nothing"

        with alumFile:
            #csv_writer.writerow(['Name', 'Work', 'Working  at ','Experience', 'Company/Institution', 'Years/Years of experience', '(Voluntary) Years of experience','Education', 'Details of Education', 'Years', 'URL'])
            csv_writer.writerow([name.encode('utf-8'), work_1.encode('utf-8'), work_2.encode('utf-8'), experience.encode('utf-8'), company_institutation.encode('utf-8'), years_experience.encode('utf-8'), vol_years_experience.encode('utf-8'), education.encode('utf-8'), edu_details.encode('utf-8'), years.encode('utf-8'), link_url.encode('utf-8')])
            #c_position.encode('utf-8')])


        driver.close()
        driver.switch_to.window(driver.window_handles[-1])

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