#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
import mailbox
from bs4 import BeautifulSoup

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " file_name.mbox")
    sys.exit(1)

## References
## [1] https://docs.python.org/2/library/email.message.html
## [2] https://www.crummy.com/software/BeautifulSoup/bs4/doc/#get-text

mbox = mailbox.mbox(sys.argv[1])
for message in mbox:
    if message.is_multipart():
    	for part in message.get_payload():

    else:
        print(message.get_content_type())
        content = message.as_string()
    
    soup = BeautifulSoup(content,"lxml")
    print(soup.get_text())
