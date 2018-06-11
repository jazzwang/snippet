#!/usr/bin/python
# -*- coding: utf-8 -*-

import mailbox
from dateutil import parser

mbox = mailbox.mbox('Indeed.mbox')
for message in mbox:
	if message.is_multipart():
		content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
	else:
		content = message.get_payload(decode=True)
	dt = parser.parse(message['Date']).strftime("%Y-%m-%d")
	f1=open( dt + '.html', 'w+')
	f1.write(content)
	f1.close
