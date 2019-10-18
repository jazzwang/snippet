import mailbox
from lxml import html

mbox = mailbox.mbox('Indeed.mbox')
for message in mbox:
	if message.is_multipart():
		content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
	else:
		content = message.get_payload(decode=True)
	
	print message['Date']
	tree = html.fromstring(content)
	companies = tree.xpath('//span[@class="job_company"]/text()')
	jobs = tree.xpath('//a[@class="jobtitle tap_item_link"]/text()')
	print companies
	print jobs
