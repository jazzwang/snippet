#!/usr/bin/env python
# -*- coding: utf-8 -*-
## References:
## [1] https://pypi.org/project/webdriver-manager/
## [2] https://www.edureka.co/community/6398/there-way-pass-the-options-flags-selenium-scripting-python
## [3] https://stackoverflow.com/questions/60352003/how-to-download-webpage-as-mhtml
## [4] https://stackoverflow.com/questions/12211781/how-to-maximize-window-in-chrome-using-webdriver-python
## [5] https://stackoverflow.com/questions/10089442/whats-the-best-way-to-handle-platform-specific-keys-in-selenium-webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--save-page-as-mhtml")    # [2][3]
options.add_argument("--start-maximized")       # [4]
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.get("https://www.example.com/")
driver.quit()