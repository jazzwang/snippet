# -*- coding: utf-8 -*-

## References:
## [1] https://pypi.org/project/webdriver-manager/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.example.com/")
soup = BeautifulSoup(driver.page_source,"lxml")
print(soup.prettify())
driver.quit()