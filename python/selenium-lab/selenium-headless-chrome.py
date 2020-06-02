# -*- coding: utf-8 -*-

## References:
## [1] https://seleniumhq.github.io/selenium/docs/api/py/webdriver_chrome/selenium.webdriver.chrome.options.html
## [2] https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d
## [3] https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os, csv

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.example.com/")
soup = BeautifulSoup(driver.page_source,"lxml")
print(soup.prettify())
driver.quit()