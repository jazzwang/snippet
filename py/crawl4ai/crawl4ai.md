# crawl4ai

> Crawl4AI: Open-source LLM Friendly Web Crawler & Scraper

- Git Repo:
  - https://github.com/unclecode/crawl4ai
- Website:
  - https://crawl4ai.com/

## 2025-01-16

- 在 [Turn ANY Website into LLM Knowledge in SECONDS | 在幾秒鐘內將任何網站轉變為 LLM 知識](https://www.youtube.com/watch?v=JWfNLF_g_V0) 看到 `crawl4ai`
  - 範例程式：
    - https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent/crawl4AI-examples
    - 影片中的完整 Crawl4AI-agent 原始碼則在[上一層目錄](https://github.com/coleam00/ottomator-agents/tree/main/crawl4AI-agent/)
- 看了一下 crawl4ai 專案的 [requirements.txt](https://github.com/unclecode/crawl4ai/blob/main/requirements.txt) 觀察相依性，也做一個初步的逆向架構理解，紀錄一下幾個已知跟沒看過的專案。
  - litellm - 呼應 AI 的部份，用來串接不同的 LLM
  - playwright - 呼應 crawl 的部份，可以開不同的瀏覽器在背景(Headless Mode)來爬取資料
  - [tf-playwright-stealth](https://github.com/tinyfish-io/tf-playwright-stealth) - 讓 playwright 可以偽裝，避免爬蟲被偵測到而被擋掉。
  - [pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library
  - [snowballstemmer](https://pypi.org/project/snowballstemmer/) - 看起來是為了一些加速的目的（#TODO 待研究）

## 2025-01-18

- 安裝 Python 套件
```bash
@jazzwang ➜ /workspaces/snippet (master) $ pip install -U crawl4ai
... 略 ...
Successfully installed MarkupSafe-3.0.2 aiofiles-24.1.0 aiohappyeyeballs-2.4.4 aiohttp-3.11.11 aiosignal-1.3.2 aiosqlite-0.20.0 annotated-types-0.7.0 anyio-4.8.0 attrs-24.3.0 beautifulsoup4-4.12.3 certifi-2024.12.14 cffi-1.17.1 charset-normalizer-3.4.1 click-8.1.8 colorama-0.4.6 crawl4ai-0.4.247 cryptography-44.0.0 distro-1.9.0 fake-http-header-0.3.5 filelock-3.16.1 frozenlist-1.5.0 fsspec-2024.12.0 greenlet-3.1.1 h11-0.14.0 httpcore-1.0.7 httpx-0.27.2 huggingface-hub-0.27.1 idna-3.10 importlib-metadata-8.5.0 iniconfig-2.0.0 jinja2-3.1.5 jiter-0.8.2 joblib-1.4.2 jsonschema-4.23.0 jsonschema-specifications-2024.10.1 litellm-1.58.4 lxml-5.3.0 mockito-1.5.3 multidict-6.1.0 nltk-3.9.1 numpy-2.2.1 openai-1.59.8 packaging-24.2 pillow-10.4.0 playwright-1.49.1 pluggy-1.5.0 propcache-0.2.1 psutil-6.1.1 pyOpenSSL-25.0.0 pycparser-2.22 pydantic-2.10.5 pydantic-core-2.27.2 pyee-12.0.0 pytest-8.3.4 pytest-mockito-0.0.4 python-dotenv-1.0.1 pyyaml-6.0.2 rank-bm25-0.2.2 referencing-0.36.1 regex-2024.11.6 requests-2.32.3 rpds-py-0.22.3 sniffio-1.3.1 snowballstemmer-2.2.0 soupsieve-2.6 tf-playwright-stealth-1.1.0 tiktoken-0.8.0 tokenizers-0.21.0 tqdm-4.67.1 typing_extensions-4.12.2 urllib3-2.3.0 xxhash-3.5.0 yarl-1.18.3 zipp-3.21.0
```
- Post-Installation - 安裝套件後，還需要安裝 Playwright 支援的瀏覽器跟底層 Linux 作業系統相依的套件 (e.g. `xvfb`)
```bash
@jazzwang ➜ /workspaces/snippet (master) $ crawl4ai-setup
[INIT].... → Running post-installation setup...
[INIT].... → Installing Playwright browsers...

... 略 ...

[COMPLETE] ● Playwright installation completed successfully.
[INIT].... → Starting database initialization...
[COMPLETE] ● Database backup created at: /home/codespace/.crawl4ai/crawl4ai.db.backup_20250118_113122
[INIT].... → Starting database migration...
[COMPLETE] ● Migration completed. 0 records processed.
[COMPLETE] ● Database initialization completed successfully.
[COMPLETE] ● Post-installation setup completed!
```
- 驗證安裝結果
```bash
@jazzwang ➜ /workspaces/snippet (master) $ crawl4ai-doctor
[INIT].... → Running Crawl4AI health check...
[INIT].... → Crawl4AI 0.4.247
[TEST].... ℹ Testing crawling capabilities...
[EXPORT].. ℹ Exporting PDF and taking screenshot took 1.66s
[FETCH]... ↓ https://crawl4ai.com... | Status: True | Time: 3.36s
[SCRAPE].. ◆ Processed https://crawl4ai.com... | Time: 65ms
[COMPLETE] ● https://crawl4ai.com... | Status: True | Total: 3.42s
[COMPLETE] ● ✅ Crawling test passed!
@jazzwang ➜ /workspaces/snippet (master) $
```
- 測試一下單頁擷取成 Markdown 的範例 - https://github.com/coleam00/ottomator-agents/blob/main/crawl4AI-agent/crawl4AI-examples/1-crawl_single_page.py
```bash
@jazzwang ➜ /workspaces/snippet (master) $ wget https://raw.githubusercontent.com/coleam00/ottomator-agents/refs/heads/main/crawl4AI-agent/crawl4AI-examples/1-crawl_single_page.py
--2025-01-18 11:51:15--  https://raw.githubusercontent.com/coleam00/ottomator-agents/refs/heads/main/crawl4AI-agent/crawl4AI-examples/1-crawl_single_page.py
Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.108.133, 185.199.109.133, 185.199.110.133, ...
Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.108.133|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 275 [text/plain]
Saving to: ‘1-crawl_single_page.py’

1-crawl_single_page.py                             100%[=============================================================================================================>]     275  --.-KB/s    in 0s      

2025-01-18 11:51:15 (9.79 MB/s) - ‘1-crawl_single_page.py’ saved [275/275]

@jazzwang ➜ /workspaces/snippet (master) $ python3 1-crawl_single_page.py 
[INIT].... → Crawl4AI 0.4.247
[FETCH]... ↓ https://ai.pydantic.dev/... | Status: True | Time: 2.04s
[SCRAPE].. ◆ Processed https://ai.pydantic.dev/... | Time: 135ms
[COMPLETE] ● https://ai.pydantic.dev/... | Status: True | Total: 2.23s

... 略 ... 因為 Markdown 格式輸出會影響到這篇筆記 ...

@jazzwang ➜ /workspaces/snippet (master) $ 
@jazzwang ➜ /workspaces/snippet (master) $ 
```

- 測試一下多頁平行擷取 - https://github.com/coleam00/ottomator-agents/blob/main/crawl4AI-agent/crawl4AI-examples/3-crawl_docs_FAST.py

```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ wget https://raw.githubusercontent.com/coleam00/ottomator-agents/refs/heads/main/crawl4AI-agent/crawl4AI-examples/3-crawl_docs_FAST.py

2025-01-18 12:05:03 (40.8 MB/s) - ‘3-crawl_docs_FAST.py’ saved [4231/4231]

@jazzwang ➜ /tmp $ python3 3-crawl_docs_FAST.py 
Found 49 URLs to crawl

=== Parallel Crawling with Browser Reuse + Memory Check ===
Before batch 1:  Current Memory: 83 MB, Peak: 83 MB
After batch 1:  Current Memory: 97 MB, Peak: 97 MB
Before batch 2:  Current Memory: 97 MB, Peak: 97 MB
After batch 2:  Current Memory: 118 MB, Peak: 118 MB
Before batch 3:  Current Memory: 118 MB, Peak: 118 MB
After batch 3:  Current Memory: 118 MB, Peak: 118 MB
Before batch 4:  Current Memory: 118 MB, Peak: 118 MB
After batch 4:  Current Memory: 117 MB, Peak: 118 MB
Before batch 5:  Current Memory: 117 MB, Peak: 118 MB
After batch 5:  Current Memory: 117 MB, Peak: 118 MB

Summary:
  - Successfully crawled: 49
  - Failed: 0

Closing crawler...
Final:  Current Memory: 117 MB, Peak: 118 MB

Peak memory usage (MB): 118
@jazzwang ➜ /tmp $ 
```
- 閱讀程式碼 https://github.com/coleam00/ottomator-agents/blob/main/crawl4AI-agent/crawl4AI-examples/2-crawl_docs_sequential.py

### Lesson Learned #1 -- 解析 `sitemap.xml`

```python
def get_pydantic_ai_docs_urls():
    """
    Fetches all URLs from the Pydantic AI documentation.
    Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
    
    Returns:
        List[str]: List of URLs
    """            
    sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
    try:
        response = requests.get(sitemap_url)
        response.raise_for_status()
        
        # Parse the XML
        root = ElementTree.fromstring(response.content)
        
        # Extract all URLs from the sitemap
        # The namespace is usually defined in the root element
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
        
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []
```
- 用 `ipython3` 觀察
```python
@jazzwang ➜ /workspaces/snippet (master) $ ipython3
Python 3.12.1 (main, Dec 12 2024, 22:30:56) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.31.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import requests

In [2]: from xml.etree import ElementTree

In [3]: sitemap_url = "https://ai.pydantic.dev/sitemap.xml"

In [4]: response = requests.get(sitemap_url)

In [5]: response.raise_for_status()

In [6]: root = ElementTree.fromstring(response.content)

In [7]: print(f"${response.text}")
$<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
         <loc>https://ai.pydantic.dev/</loc>
         <lastmod>2025-01-16</lastmod>
    </url>
    <url>
         <loc>https://ai.pydantic.dev/agents/</loc>
         <lastmod>2025-01-16</lastmod>
    </url>
    <url>
         <loc>https://ai.pydantic.dev/contributing/</loc>

... 略 ...
```
- 看了一下 [xml.etree.ElementTree 筆記](https://hackmd.io/@top30339/rJYlKYpml?type=view)，感覺用 array 的方式比 `findall()` 來得容易理解。
```python
In [14]: root[0]
Out[14]: <Element '{http://www.sitemaps.org/schemas/sitemap/0.9}url' at 0x7139e499dc60>

In [15]: root[0][1]
Out[15]: <Element '{http://www.sitemaps.org/schemas/sitemap/0.9}lastmod' at 0x7139e499e430>

In [16]: root[0][1].text
Out[16]: '2025-01-16'

In [17]: root[0][0].text
Out[17]: 'https://ai.pydantic.dev/'

In [18]: root[1][0].text
Out[18]: 'https://ai.pydantic.dev/agents/'

In [19]: root[2][0].text
Out[19]: 'https://ai.pydantic.dev/contributing/'

In [20]: len(root)
Out[20]: 49
```
- 所以要取得 sitemap.xml 中的所有 url 可以用 python 的一行語法達成：
```python
In [24]: urls = [ element[0].text for element in root ]
```

### Lesson Learned #2 - 各種抓取與解析 Site Map 的狀況

- <span style='padding:3px; background-color:red; color: white;'>題外話：寫爬蟲真是一個很挑戰的工作啊～</span>
- 例如：想抓 Databricks 文件的 Site Map
  - Site Map 會是 `槽狀結構` (nested sitemap)
  - 還要避免刻意的網址誤導 e.g. https://docs.databricks.com/api/gcp//workspace/libraries/allclusterlibrarystatuses 實際上應該是 https://docs.databricks.com/api/gcp/workspace/libraries/allclusterlibrarystatuses
```python
In [18]: urls = site_map("https://docs.databricks.com/en/sitemap.xml")

In [19]: urls
Out[19]:
['https://docs.databricks.com/en/doc-sitemap.xml',
 'https://docs.databricks.com/en/doc-sitemap-pt.xml',
 'https://docs.databricks.com/en/doc-sitemap-ja.xml',
 'https://docs.databricks.com/api/sitemap.xml']

In [20]: urls = []
    ...: for url in site_map("https://docs.databricks.com/en/sitemap.xml"):
    ...:     urls.extend(site_map(url))
    ...:

In [21]: len(urls)
Out[21]: 10530

In [22]: urls[10000]
Out[22]: 'https://docs.databricks.com/api/gcp//workspace/libraries/allclusterlibrarystatuses'
```
- 例如想抓愛料理的 sitemap 就更神了～
  - 重新導向
  - 轉不同的 domain
  - sitemap 是 gz 壓縮檔
  - 槽狀結構
```bash
jazzw@JazzBook:~$ curl https://icook.tw/sitemap.xml
Redirecting to <a href="https://tokyo-kitchen.icook.network/sitemaps/sitemap.xml.gz">https://tokyo-kitchen.icook.network/sitemaps/sitemap.xml.gz</a>
jazzw@JazzBook:~$ curl -s https://tokyo-kitchen.icook.network/sitemaps/sitemap.xml.gz --output - | zcat | xmllint --format -
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/siteindex.xsd">
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap1.xml.gz</loc>
    <lastmod>2025-01-18T00:00:33+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap2.xml.gz</loc>
    <lastmod>2025-01-18T00:00:33+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap3.xml.gz</loc>
    <lastmod>2025-01-18T00:00:49+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap4.xml.gz</loc>
    <lastmod>2025-01-18T00:01:12+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap5.xml.gz</loc>
    <lastmod>2025-01-18T00:01:42+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap6.xml.gz</loc>
    <lastmod>2025-01-18T00:02:35+00:00</lastmod>
  </sitemap>
  <sitemap>
    <loc>https://tokyo-kitchen.icook.network/sitemaps/sitemap7.xml.gz</loc>
    <lastmod>2025-01-18T00:04:35+00:00</lastmod>
  </sitemap>
</sitemapindex>
jazzw@JazzBook:~$ curl -s https://tokyo-kitchen.icook.network/sitemaps/sitemap7.xml.gz --output - | zcat | xmllint --format - | head
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1" xmlns:video="http://www.google.com/schemas/sitemap-video/1.1" xmlns:news="http://www.google.com/schemas/sitemap-news/0.9" xmlns:mobile="http://www.google.com/schemas/sitemap-mobile/1.0" xmlns:pagemap="http://www.google.com/schemas/sitemap-pagemap/1.0" xmlns:xhtml="http://www.w3.org/1999/xhtml" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
  <url>
    <loc>https://icook.tw/users/mrpark</loc>
    <lastmod>2025-01-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://icook.tw/users/foreolive</loc>
```
- 從 `robots.txt` 看得出來，已經請 OpenAI (ChatGPT), Anthropic(Claude), Google (Gemini) 不要再爬了！當然，這真的就回歸各家爬蟲機器人到底有沒有『尊重』 `robots.txt`，再看有沒有能力解析各網站提供的 `sitemap.xml`
```bash
jazzw@JazzBook:~$ curl https://icook.tw/robots.txt
User-agent: GPTBot
Disallow: /

User-agent: ChatGPT-User
Disallow: /

User-agent: CCBot
Disallow: /

User-agent: anthropic-ai
Disallow: /

User-agent: Claude-Web
Disallow: /

User-agent: Google-Extended
Disallow: /

User-agent: *
Disallow: /stickers/*
Disallow: /recipes/search/*
Disallow: /recipes/*/print
Disallow: /recipes/*/dishes/new
Disallow: /recipes/*/edit
Disallow: /recipes/new
Disallow: /recipes/*.json
Disallow: /search/%E9%A3%9F%E6%9D%90%EF%BC%9A*
Disallow: /users/*/stickers
Disallow: /users/*/entries
Disallow: /users/*/followers
Disallow: /users/*/notifications
Disallow: /campaigns/panasonicilovecookingbakers
Disallow: /campaigns/hawdii_curry
Disallow: /.well-known/amphtml/apikey.pub
Disallow: /metrics/*
Disallow: /login
Disallow: /signup

User-agent: grapeshot
Disallow:

Sitemap: http://tokyo-kitchen.icook.network/sitemaps/sitemap.xml.gz
```

### Lesson Learned #3 - Crawl4ai 的 "AI" 是用在產生 Markdown

## 2025-03-04

- 評估可否擷取結構化網站文件當 RAG 的知識庫。