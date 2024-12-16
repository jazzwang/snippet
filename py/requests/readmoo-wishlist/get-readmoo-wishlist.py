#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import argparse
from bs4 import BeautifulSoup

def get_link(line):
    (url, title) = line.strip().split(';')
    return url

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Download book category from Readmoo based on CSV input.")
    parser.add_argument("--input", "-i", help="input CSV file, delimiter: ';', first column should be 'readmoo url'.")
    parser.add_argument("--output", "-o", help="output CSV file, delimiter: ';'")
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    ## create wishlist book category file
    category = open(output_file,'w+', 512, encoding='utf-8')
    print("book_url;book_category;book_subcategory;book_title;book_price;readmoo_id",file=category)
    print("book_url;book_category;book_subcategory;book_title;book_price;readmoo_id")

    ## input file: readmoo-wishlist.csv (generated from `js/chrome-devtools/readmoo-wishlist.js` )
    ## e.g.
    ## https://readmoo.com/book/210274853000101;高效團隊都在用的奇蹟式提問
    ## https://readmoo.com/book/210263905000101;最少話的最強說明法
    with open(input_file, 'r', encoding='utf-8') as file:
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

if __name__ == "__main__":
    main()