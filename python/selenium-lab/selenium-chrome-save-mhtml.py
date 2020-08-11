# -*- coding: utf-8 -*-

## References:
## [1] https://www.edureka.co/community/6398/there-way-pass-the-options-flags-selenium-scripting-python
## [2] https://stackoverflow.com/questions/60352003/how-to-download-webpage-as-mhtml
## [3] https://stackoverflow.com/questions/12211781/how-to-maximize-window-in-chrome-using-webdriver-python
## [4] https://stackoverflow.com/questions/10089442/whats-the-best-way-to-handle-platform-specific-keys-in-selenium-webdriver

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--save-page-as-mhtml")    # [1][2]
options.add_argument("--start-maximized")       # [3]
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.example.com/")

