# -*- coding: utf-8 -*-

import sys, re
import mailbox
from dateutil import parser

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " file_name.mbox")
    sys.exit(1)

mbox = mailbox.mbox(sys.argv[1])
print("date,count")
for message in mbox:
    date = parser.parse(message['Date']).strftime("%Y-%m-%dT%H:%M:%S")
    print(date + ",1")