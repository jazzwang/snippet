# MEMO

## 2022-08-01

- ( 2022-08-01 00:05:00 )
```
jazzwang:~/git/snippet/python/top945-mp3$ source ~/venv/bin/activate
(venv) jazzwang:~/git/snippet/python/top945-mp3$ pip3 install selenium webdriver-manager bs4 lxml pandas
(venv) jazzwang:~/git/snippet/python/top945-mp3$ ipython3
Python 3.8.9 (default, Oct 26 2021, 07:25:54)
Type 'copyright', 'credits' or 'license' for more information
IPython 8.3.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```
```
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
url="https://www.top945.com.tw/service/mp3A/index.asp?TheGUID=" + GUID
options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.set_page_load_timeout(30)
driver.get(url)
soup = BeautifulSoup(driver.page_source,"lxml")
mp3_url = soup.select("#jp_audio_0")[0].get('src')
mp3_name = soup.select("#jp_audio_0")[0].get('title')
print("wget -o \"" + mp3_name + ".mp3\" \"" + mp3_url + "\"")
```
- ( 2022-08-01 00:31:26 )