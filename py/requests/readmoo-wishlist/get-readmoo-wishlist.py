#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import argparse
from bs4 import BeautifulSoup
import logging

# Constants
CSV_HEADER = "book_url;book_category;book_subcategory;book_title;book_price;readmoo_id"

def get_link(line):
    (url, title) = line.strip().split(';')
    return url

def fetch_book_info(link):
    r = requests.get(link)
    book_info = BeautifulSoup(r.text, "lxml")
    try:
        book_category = book_info.select('div.rm-breadcrumb a span')[1].text
        book_subcategory = book_info.select('div.rm-breadcrumb a span')[2].text
        book_title = book_info.select('div#price-btn-container')[0].get('data-title')
        book_price = book_info.select('div#price-btn-container')[0].get('data-price')
        readmoo_id = book_info.select('div#price-btn-container')[0].get('data-readmoo-id')
    except IndexError as e:
        logging.error(f"Error fetching book info for {link}: {e}")
        book_category = book_subcategory = book_title = "已下架"
        book_price = readmoo_id = "0"
    
    return link, book_category, book_subcategory, book_title, book_price, readmoo_id

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Download book category from Readmoo based on CSV input.")
    parser.add_argument("--input", "-i", help="input CSV file, delimiter: ';', first column should be 'readmoo url'.", required=True)
    parser.add_argument("--output", "-o", help="output CSV file, delimiter: ';'", required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    links = list(map(get_link, content))

    with open(output_file, 'w+', encoding='utf-8') as category:
        print(CSV_HEADER, file=category)
        for link in links:
            book_info = fetch_book_info(link)
            print(';'.join(book_info), file=category)
            category.flush()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
