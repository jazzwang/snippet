#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_link(line):
    (url, title) = line.strip().split(';')
    return url

## create wishlist book category file
category = open('readmoo-wishlist-category.csv','w+', 512, encoding='utf-8')
print("book_url;book_category;book_subcategory;book_title;book_price;readmoo_id",file=category)

## input file: readmoo-wishlist.csv (generated from `js/chrome-devtools/readmoo-wishlist.js` )
with open('readmoo-wishlist.csv', 'r', encoding='utf-8') as file:
    content = file.readlines()

## https://g.co/gemini/share/32f97a6c8367
## - use map() function to get link from each line. 
## - use list() to convert map object o list object.
links = list(map(get_link, content))

for link in links:
    r = requests.get(link)
    book_info        = BeautifulSoup(r.text, "lxml")
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

    print(f"{link};{book_category};{book_subcategory};{book_title};{book_price};{readmoo_id}",file=category)
    print(f"{link};{book_category};{book_subcategory};{book_title};{book_price};{readmoo_id}")
    category.flush()
    
category.close()
