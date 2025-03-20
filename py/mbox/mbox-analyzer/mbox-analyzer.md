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

## 2020-08-31

每次都要匯出成 mbox 格式，感覺有點小麻煩。所以實驗一下改用 IMAP 只掃過指定的搜尋條件。

- https://github.com/martinrusev/imbox
- https://github.com/mjs/imapclient/

初步先實驗一下 [imbox](https://github.com/martinrusev/imbox)

- 跟 Gmail 整合時，第一個要先產生 app-specific password
   - https://myaccount.google.com/apppasswords
```
error: If you're not using an app-specific password, 
grab one here: https://myaccount.google.com/apppasswords
```
   - 必須啟用兩階段認證才可以啟用應用程式密碼
   - https://support.google.com/accounts/answer/185833?hl=zh-Hant

- 參考 https://hant-kb.kutu66.com/python/post_1398329
   - 使用 `imaplib` 還是無法認證通過

- 看樣子要改用 Google 提供的 Gmail API
   - https://developers.google.com/gmail/api/quickstart/python

## 2020-11-06

- https://github.com/mjs/imapclient/
   - https://stackoverflow.com/a/57518241

看了一下 Stackoverflow 的討論，2019 年有人可以用 imapclient 套件登入 Outlook