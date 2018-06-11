# -*- coding: utf-8 -*-

import mailbox
from bs4 import BeautifulSoup
from dateutil import parser

mbox = mailbox.mbox('Indeed.mbox')

for message in mbox:
	if message.is_multipart():
		content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
	else:
		content = message.get_payload(decode=True)
	
	dt = parser.parse(message['Date']).strftime("%Y-%m-%d")
	soup = BeautifulSoup(content, "lxml")
	for block in soup.select(".job_company"):
		print dt + ";" + block.text.encode('utf-8')
	for block in soup.find_all('span', 'sg-paragraph-large'):
		if block.find(class_='db'):
			continue
		else:
			print dt + ";" + block.text.encode('utf-8')
