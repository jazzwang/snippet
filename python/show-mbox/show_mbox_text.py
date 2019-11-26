# -*- coding: utf-8 -*-

import mailbox

mbox = mailbox.mbox('Indeed.mbox')
for message in mbox:
	if message.is_multipart():
		content = ''.join(part.get_payload(decode=True) for part in message.get_payload())
	else:
		content = message.get_payload(decode=True)
	print content
