#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup

## initial Chrome webdriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(60) # seconds
driver.maximize_window()
driver.set_page_load_timeout(60)

## login readmoo
driver.get("https://member.readmoo.com/login")
input("Please enter to continue")

## fetch wishlist
driver.get("https://readmoo.com/checkout/cart#wishlist")
### waiting 10 seconds for loading wishlist
WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-purchase"))
    )

### convert wishlist page into lxml
soup = BeautifulSoup(driver.page_source,"lxml")
books = open('readmoo_wishlist.csv','w+', 512)
for link in soup.select('div.cart-item-detail div.item-detail-content div.item-title-link-box a.item-title-link'):
    print(link.get('href'))
    print(book_url,file=books)
    books.flush()
## close Chrome webdriver
driver.quit()
## close wishlist book url file
books.close()

## create wishlist book category file
category = open('readmoo_wishlist_category.csv','w+', 512)
print("book_url;book_category;book_subcategory;book_title;book_price;readmoo_id",file=category)
for link in soup.select('div.cart-item-detail div.item-detail-content div.item-title-link-box a.item-title-link'):
    book_url = link.get('href')
    r = requests.get(book_url)
    book_info        = BeautifulSoup(r.text,"lxml")
    try:
        book_category    = book_info.select('div.rm-breadcrumb a span')[1].text
        book_subcategory = book_info.select('div.rm-breadcrumb a span')[2].text
        book_title       = book_info.select('div#price-btn-container')[0].get('data-title')
        book_price       = book_info.select('div#price-btn-container')[0].get('data-price')
        readmoo_id       = book_info.select('div#price-btn-container')[0].get('data-readmoo-id')
    except:
        book_category    = "已下架"
        book_subcategory = "已下架"
        book_title       = "已下架"
        book_price       = "0"
        readmoo_id       = "0"

    print(book_url + ";" +  book_category + ";" +  book_subcategory + ";" + book_title + ";" + book_price + ";" + readmoo_id,file=category)
    print(book_url + ";" +  book_category + ";" +  book_subcategory + ";" + book_title + ";" + book_price + ";" + readmoo_id)
    category.flush()
    
category.close()
