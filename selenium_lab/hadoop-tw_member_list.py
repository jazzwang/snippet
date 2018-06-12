#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
import time, re
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
driver.implicitly_wait(3)
driver.get("https://www.facebook.com/groups/hadoop.tw/members/")
driver.implicitly_wait(30)
for i in range(1,600):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

soup = BeautifulSoup(driver.page_source,"lxml")
for block in soup.select("._60rj"):
	print block.text.rstrip().lstrip().encode('utf-8')
driver.close()
