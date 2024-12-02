#!/usr/bin/env python
# -*- coding: utf-8 -*-
## References:
## [1] https://pypi.org/project/webdriver-manager/
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.example.com/")
soup = BeautifulSoup(driver.page_source,"lxml")
print(soup.prettify())
driver.quit()