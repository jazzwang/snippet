# Development MEMO

## MBox headers

```python
In [1]: import sys, re
   ...: import mailbox
   ...: from dateutil import parser
   ...: mbox = mailbox.mbox("AutoRule.mbox")

In [2]: message = mbox[0]

In [3]: message.keys()
Out[3]:
['X-GM-THRID',
 'X-Gmail-Labels',
 'Delivered-To',
 'Received',
 'X-Received',
 'ARC-Seal',
 'ARC-Message-Signature',
 'ARC-Authentication-Results',
 'Return-Path',
 'Received',
 'Received-SPF',
 'Authentication-Results',
 'DKIM-Signature',
 'X-Google-DKIM-Signature',
 'X-Gm-Message-State',
 'X-Google-Smtp-Source',
 'MIME-Version',
 'X-Received',
 'Reply-To',
 'Auto-Submitted',
 'Message-ID',
 'Date',
 'Subject',
 'From',
 'To',
 'Content-Type']
```
