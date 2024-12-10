- https://requests.readthedocs.io/en/master/user/quickstart/
- https://realpython.com/python-requests/

## 2024-12-10

- ( 2024-12-10 14:49:45 )
- 現在很多網頁都會做登入的保護措施，因此撰寫 Python Request 程式時，往往需要確認身份認證完成後，是存在 Cookie 或者有固定的 JWT token 等。
- 舉 https://member.readmoo.com/login 為例，原始碼中寫到
> <small>此頁面受 Google reCAPTCHA 保護，以確認您不是機器人。</small>
- 而 HTML 原始碼中
  - https://www.google.com/recaptcha/api.js?render=6LfOROAZAAAAAJDSw27C97LvhIMV0lYF_hdLn2sF -- 使用 `Google reCAPTCHA` API javascript
  - "https://cdn.readmoo.com/wp/member/js/w-member-login.bundle.js?version=20241210103916" -- GPT-4o-mini 說這是 commonJS 的 bundle
```bash
jazzw@JazzBook:~/git/snippet/py/requests$ curl -s https://member.readmoo.com/login | grep "\.js"
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  } (window,document,'script','https://cdn.qgr.ph/qgraph.22c6932429d7219472ff.js');
<script src="https://cdn.readmoo.com/js/default_js.js" charset="utf-8"></script>
'https://connect.facebook.net/en_US/fbevents.js');
<!-- Global site tag (gtag.js) - Google AdWords: 824240233 -->
<script src="https://www.google.com/recaptcha/api.js?render=6LfOROAZAAAAAJDSw27C97LvhIMV0lYF_hdLn2sF"></script>
    <script type="text/javascript" src="https://cdn.readmoo.com/wp/member/js/w-member-login.bundle.js?version=20241210103916" charset="utf-8"></script>
```
- ( 2024-12-10 15:56:27 )
- 解析 `w-member-login.bundle.js` 來找出為何 Network Traffic 中 login 會帶多個參數 `email`, `password`, `token` 跟 `version`
```bash
jazzw@JazzBook:~/git/snippet/js$ snippet ssh
```
- 用 `js/chrome-devtools/oreilly-cookie.js` 改寫成 `js/chrome-devtools/readmoo-cookie.js`，把 readmoo.com 登入後的 cookie 下載存成 `readmoo-cookie.json`
- 用 `ipython` 驗證是否可以查詢 readmoo wishlist -- <span style="background-color:#ff0011; color:#ffffff; padding: 3px;">[ 失敗 ]</span>
```python
## https://g.co/gemini/share/3cc2f36f2939
import json
import requests
from bs4 import BeautifulSoup

with open("readmoo-cookie.json","r") as f:
    cookies = json.load(f)
session = requests.Session()
session.cookies.update(cookies)
r1 = session.get("https://readmoo.com/checkout/cart#wishlist")
r1.status_code
print(r1.text)
```
- 結果是 Status Code `200` 但內容是「未登入」。
```html
<!DOCTYPE html>
<html class="no-js" lang="zh-TW">
<head>
<title>登入帳號 | Readmoo 讀墨電子書</title>
... 略 ...
```