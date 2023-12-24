#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://member.readmoo.com/login")
input("Please enter to continue")
driver.get("https://readmoo.com/checkout/cart#wishlist")
soup = BeautifulSoup(driver.page_source,"lxml")
books = open('readmoo_wishlist.csv','w+', 512)
category = open('readmoo_wishlist_category.csv','w+', 512)
for link in soup.select('div.cart-item-detail div.item-detail-content div.item-title-link-box a.item-title-link'):
    book_url = link.get('href')
    print(book_url,file=books)
    driver.get(book_url)
    book_info        = BeautifulSoup(driver.page_source,"lxml")
    book_category    = book_info.select('div.rm-breadcrumb a span')[1].text
    book_subcategory = book_info.select('div.rm-breadcrumb a span')[2].text
    book_title       = book_info.select('div#price-btn-container')[0].get('data-title')
    book_price       = book_info.select('div#price-btn-container')[0].get('data-price')
    readmoo_id       = book_info.select('div#price-btn-container')[0].get('data-readmoo-id')
    print(book_url + ";" +  book_category + ";" +  book_subcategory + ";" + book_title + ";" + book_price + ";" + readmoo_id,file=category)
    print(book_url + ";" +  book_category + ";" +  book_subcategory + ";" + book_title + ";" + book_price + ";" + readmoo_id)
    category.flush()
    books.flush()
driver.quit()
books.close()
category.close()