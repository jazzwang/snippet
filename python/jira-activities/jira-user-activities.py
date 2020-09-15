# -*- coding: utf-8 -*-
import os, sys, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

try:
    base_url  = os.environ["BASE_URL"]
except:
    print("Please define environment variable 'BASE_URL'.")
    print("Ex: if your user profile can be found at ")
    print("    https://issues.apache.org/jira/secure/ViewProfile.jspa")
    print("    then please define")
    print("    BASE_URL  = https://issues.apache.org/jira")
    exit(1)

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " Username")
    exit(1)
else:
    user_id = sys.argv[1]

options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(30)
## https://selenium-python.readthedocs.io/waits.html#implicit-waits
driver.implicitly_wait(10)

driver.get(base_url + "/login.jsp")
input("Press Enter to continue...")

driver.get(base_url + "/secure/ViewProfile.jspa?name=" + user_id)
soup = BeautifulSoup(driver.page_source,"lxml")
driver.get(soup.find('iframe').get('src'))
time.sleep(3)
more_pages = True
while more_pages:
    try:
        ## If there are div with "jira-activity-item" class
        if(driver.find_element_by_class_name("jira-activity-item")):
            csv_output = open(user_id + ".csv","w+")
            soup = BeautifulSoup(driver.page_source,"lxml")
            for item in soup.select('.jira-activity-item'):
                issue = item.select('.activity-item-summary')[0].select('a')[1].get("href")
                item.select('.activity-item-summary')[0].select('a')[0].decompose()
                summary=' '.join(item.select('.activity-item-summary')[0].text.replace('\n','').split())
                timestamp=item.select('.timestamp')[0].get('datetime')
                print(timestamp + ";" + issue + ";" + summary, file=csv_output)
    except:
        more_pages = False
    ## click if "activity-stream-show-more" is not 'hidden' or 'loading'
    if(driver.find_element_by_id("activity-stream-show-more").get_attribute("class") == ''):
        driver.find_element_by_id("activity-stream-show-more").click()
    if(driver.find_element_by_id("activity-stream-show-more").get_attribute("class") == 'hidden'):
        more_pages = False
    else:
        time.sleep(5)

soup = BeautifulSoup(driver.page_source,"lxml")
activity = open( user_id + '.html','w+')
print(soup.prettify(), file=activity)

input("Press Enter to continue...")
driver.close()