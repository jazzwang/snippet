#!/usr/bin/env python3
## Reference:
## https://requests.readthedocs.io/en/latest/user/quickstart/

import sys, requests
import getpass
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

user_id = input("ID: ")
password = getpass.getpass("Password: ")

login_url = "https://webpac.hcml.gov.tw/personalization/memberLoginAct.do"
login_data = {  'goVar': '-1',
                'returnxItem': '',
                'account2': user_id,
                'txtps': password}
session = requests.Session()
r1 = session.post(login_url, data=login_data)

booklist_url = "https://webpac.hcml.gov.tw/personalization/MyLendList.do?order=Marc_Detail.title-desc&pageSize=50"
r2 = session.get(booklist_url)

# Parse the HTML content using BeautifulSoup to extract the table
soup = BeautifulSoup(r2.text, "lxml")

# Find the table by its HTML tag (e.g., <table>)
table = soup.find('table')

# Read the table into a Pandas DataFrame
df = pd.read_html(str(table))[0].sort_values(by="到期日")  # Assuming there's only one table on the page

# Now, you have the table data in a Pandas DataFrame (df)
formatted_table = tabulate(df[['到期日', '題名', '索書號', '借書日期']], headers='keys', tablefmt='plain')
print(formatted_table)
