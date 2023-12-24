#!/usr/bin/env python
# -*- coding: utf-8 -*-
## References:
## [1] https://pypi.org/project/webdriver-manager/
## [2] https://medium.com/@pyzzled/running-headless-chrome-with-selenium-in-python-3f42d1f5ff1d
## [3] https://chromium.googlesource.com/chromium/src/+/master/docs/design/sandbox.md
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

## https://www.selenium.dev/blog/2023/headless-is-going-away/
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.example.com/")
soup = BeautifulSoup(driver.page_source,"lxml")
print(soup.prettify())
driver.quit()