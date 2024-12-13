# Selenium

## 2024-12-13

- ( 2024-12-13 23:19:20 )
- 緣起：
  - 想要備份一些 Confluence Wiki 成 MHTML 格式。
- 測試了一下先前寫的 `selenium-chrome-save-mhtml.py` 其實並沒有寫完
- 後來測了一下 https://gist.github.com/vane/76aa72737809e091bc5732015c1867f3 的實作，透過 `driver.execute_cdp_cmd('Page.captureSnapshot', {})` 取得的內容，並無法正常顯示。
```python
def save_mhtml(driver: selenium.webdriver.chrome.webdriver.WebDriver, fname: str):
    with open(fname, 'w+') as f:
        page_source = driver.execute_cdp_cmd('Page.captureSnapshot', {})
        f.write(page_source['data'])
```
```bash
jazzw@JazzBook:~/git/snippet/py/selenium$ wget https://gist.githubusercontent.com/vane/76aa72737809e091bc5732015c1867f3/raw/2854342b4d1b7d2430f410d5f021b58bf3fd154b/selenium-scrap.py
jazzw@JazzBook:~/git/snippet/py/selenium$ chmod a+x selenium-scrap.py
jazzw@JazzBook:~/git/snippet/py/selenium$ ./selenium-scrap.py -u https://www.google.com -m test
```
- 測試 `selenium-scrap.py` 產生的 MTHML 內容看起來很像 Email 格式。
```html
From: <Saved by Blink>^M
Snapshot-Content-Location: https://www.google.com/^M
Subject: Google^M
Date: Fri, 13 Dec 2024 23:38:06 +0800^M
MIME-Version: 1.0^M
Content-Type: multipart/related;^M
        type="text/html";^M
        boundary="----MultipartBoundary--AMvf9xUfwu8a4FOAR3po8YLP3hh2OqR8bq3eLfN8D8----"^M
^M
^M
------MultipartBoundary--AMvf9xUfwu8a4FOAR3po8YLP3hh2OqR8bq3eLfN8D8----^M
Content-Type: text/html^M
Content-ID: <frame-F6923F886C014A50E678BF1B0A09C5DD@mhtml.blink>^M
Content-Transfer-Encoding: quoted-printable^M
Content-Location: https://www.google.com/^M
^M
<!DOCTYPE html><html itemscope=3D"" itemtype=3D"http://schema.org/WebPage" =^M
lang=3D"zh-TW"><head><meta http-equiv=3D"Content-Type" content=3D"text/html=^M
; charset=3DUTF-8"><link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:c=^M
ss-69671035-02e4-4680-88f0-f63ddda40b5c@mhtml.blink" /><link rel=3D"stylesh=^M
eet" type=3D"text/css" href=3D"cid:css-3aee24fa-d5b7-4e18-9acb-e9bc77af3fcd=^M
@mhtml.blink" /><link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-=^M
0dd5f7f2-b7e7-4120-a38c-8ce8fd77b9e5@mhtml.blink" /><link rel=3D"stylesheet=^M
" type=3D"text/css" href=3D"cid:css-cc249db0-26b5-4981-af1a-1673a210786b@mh=^M
tml.blink" /><link rel=3D"stylesheet" type=3D"text/css" href=3D"cid:css-51a=^M
cef6e-924d-4643-9ace-40132ff121c3@mhtml.blink" /><link rel=3D"stylesheet" t=^M
ype=3D"text/css" href=3D"cid:css-5b86f105-d380-4821-bd65-f5795111c6db@mhtml=^M

... 略 ...
```