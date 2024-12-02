# -*- coding: utf-8 -*-

## 這是一個簡單的小程式，用來根據 CSV 欄位裡的數值來產生 HTML 檔案，透過 mailto 語法來產生寄給不同 E-Mail 的信件內容

import csv
import sys
import urllib.parse

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " input_file_name.csv")
    sys.exit(1)

input_file_name = sys.argv[1]

def read_file_to_string(input_filename):
  """Reads the contents of a file into a single string.

  Args:
    input_filename: The name of the file to read.

  Returns:
    A string containing the contents of the file, or None if there is an error.
  """

  try:
    # Open the file in read mode with a context manager
    with open(input_filename, 'r') as input_file:
      # Read the entire file content into a string
      output_string = input_file.read()
  except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
    return None
  except PermissionError:
    print(f"Error: Permission denied reading file '{input_filename}'.")
    return None
  else:
    return output_string

## main()

subject = read_file_to_string("mail_subject")
subject_encoded = urllib.parse.quote(subject, encoding="UTF-8")
body = read_file_to_string("mail_template.tpl")
link = "<li><a target='_blank' href='mailto:{}?subject={}&body={}'>{}</a></li>"

print("<html><body><ol>")

with open( input_file_name ,"r") as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        name = row["NAME"]
        email = row["EMAIL"]
        shorten_url = row["SURL"]
        body_encoded = urllib.parse.quote(body.format(name,shorten_url),encoding="UTF-8")
        print(link.format(email,subject_encoded,body_encoded,name))

print("</ol></body></html>")