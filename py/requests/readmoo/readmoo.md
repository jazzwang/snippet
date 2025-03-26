## 2024-12-19

- 以下擷取自 aider 幫忙做 code review 跟 `--watch-files` 的紀錄
- from `.aider.chat.history.md`

-------------------------------------------------

```
# aider chat started at 2024-12-19 17:13:42

> /home/codespace/.python/current/bin/aider --mini --watch-files get-readmoo-wishlist.py
> Aider v0.69.1
> Model: gpt-4o-mini with whole edit format
> Git repo: ../../../.git with 1,061 files
> Warning: For large repos, consider using --subtree-only and .aiderignore
> See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
> Repo-map: disabled
> Added py/requests/readmoo-wishlist/get-readmoo-wishlist.py to the chat.
> Note: in-chat filenames are always relative to the git working dir, not the current working dir.
> Cur working dir: /workspaces/snippet/py/requests/readmoo-wishlist
> Git working dir: /workspaces/snippet

#### /tokens
> Approximate context window usage for gpt-4o-mini, in tokens:
> $ 0.0001      542 system messages
> $ 0.0001      702 py/requests/readmoo-wishlist/get-readmoo-wishlist.py /drop to remove
> ==================
> $ 0.0002    1,244 tokens total
> 126,756 tokens remaining in context window
> 128,000 tokens max context window size
> Added py/aider/MEMO.md to the chat
> End your comment with AI! to request changes or AI? to ask questions

#### /drop py/aider/MEMO.md
> Removed py/aider/MEMO.md from the chat

#### could you code review get-readmoo-wishlist.py and give me suggestions to improve?

Here are some suggestions to improve the `get-readmoo-wishlist.py` file:

1. **Use Context Managers**: Instead of manually opening and closing files, use context managers (`with` statement) for better resource management.
2. **Error Handling**: Improve error handling by specifying the exception type and providing more informative error messages.
3. **Function Decomposition**: Break down the `main` function into smaller functions for better readability and maintainability.
4. **Use Constants**: Define constants for the CSV headers and other repeated strings to avoid magic strings in the code.
5. **Logging**: Consider using the `logging` module instead of print statements for better control over logging levels and outputs.

Here is the updated code with these improvements:

py/requests/readmoo-wishlist/get-readmoo-wishlist.py
```
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import argparse
from bs4 import BeautifulSoup
import logging

# Constants
CSV_HEADER = "book_url;book_category;book_subcategory;book_title;book_price;readmoo_id"

def get_link(line):
    (url, title) = line.strip().split(';')
    return url

def fetch_book_info(link):
    r = requests.get(link)
    book_info = BeautifulSoup(r.text, "lxml")
    try:
        book_category = book_info.select('div.rm-breadcrumb a span')[1].text
        book_subcategory = book_info.select('div.rm-breadcrumb a span')[2].text
        book_title = book_info.select('div#price-btn-container')[0].get('data-title')
        book_price = book_info.select('div#price-btn-container')[0].get('data-price')
        readmoo_id = book_info.select('div#price-btn-container')[0].get('data-readmoo-id')
    except IndexError as e:
        logging.error(f"Error fetching book info for {link}: {e}")
        book_category = book_subcategory = book_title = "已下架"
        book_price = readmoo_id = "0"

    return link, book_category, book_subcategory, book_title, book_price, readmoo_id

def main():
    # parsing CLI arguments
    parser = argparse.ArgumentParser(description="Download book category from Readmoo based on CSV input.")
    parser.add_argument("--input", "-i", help="input CSV file, delimiter: ';', first column should be 'readmoo url'.", required=True)
    parser.add_argument("--output", "-o", help="output CSV file, delimiter: ';'", required=True)
    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    links = list(map(get_link, content))

    with open(output_file, 'w+', encoding='utf-8') as category:
        print(CSV_HEADER, file=category)
        for link in links:
            book_info = fetch_book_info(link)
            print(';'.join(book_info), file=category)
            category.flush()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
```
```
> Tokens: 1.4k sent, 673 received. Cost: $0.00062 message, $0.00062 session.
> Applied edit to py/requests/readmoo-wishlist/get-readmoo-wishlist.py
> Commit 418fee4 refactor: Improve code structure and error handling in wishlist script
> You can use /undo to undo and discard each aider commit.
```

<span style="background-color:#00875a;; border-color: #ff0000; color: #ffffff; padding: 5px;">備註: 在 `get-readmoo-wishlist.py` 加入 `## is this better for readability? AI?` 的註解，因為有啟用 `--watch-files` 所以觸發了底下的回答（因為是 `AI?` 所以等於 `/ask`）</span>

```
> Processing your request...

#### Find the "AI" comments below (marked with █) in the code files I've shared with you.
#### They contain your questions you need to answer and other instructions.
####
#### py/requests/readmoo-wishlist/get-readmoo-wishlist.py:
#### ⋮...
#### │def fetch_book_info(link):
#### │    r = requests.get(link)
#### │    book_info = BeautifulSoup(r.text, "lxml")
#### │    try:
#### ⋮...
#### │        readmoo_id = book_info.select('div#price-btn-container')[0].get('data-readmoo-id')
#### │    except IndexError as e:
#### │        logging.error(f"Error fetching book info for {link}: {e}")
#### █        ## is this better for readability? AI?
#### │        book_category = book_subcategory = book_title = "已下架"
#### │        book_price = readmoo_id = "0"
#### │
#### ⋮...
```
The comment you highlighted asks whether the way the code handles the error case is better for readability.

In this context, the code assigns default values to multiple variables in a single line when an `IndexError` occurs. While this approach can be concise, it may reduce readability for some developers, especially those who prefer clarity over brevity.

### Suggestions for Improved Readability:

1. **Separate Assignments**: Instead of assigning multiple variables in one line, you could assign them one by one. This makes it clearer what each variable represents and can be easier to read:

   ```python
   book_category = "已下架"
   book_subcategory = "已下架"
   book_title = "已下架"
   book_price = "0"
   readmoo_id = "0"
   ```

2. **Commenting**: Adding a comment explaining why these default values are being assigned can also enhance readability. For example:

   ```python
   # Assign default values if book information is not available
   ```

3. **Use of Constants**: If "已下架" and "0" are used in multiple places, consider defining them as constants at the top of your file. This way, if you need to change them later, you only have to do it in one place.

In summary, while the current approach is functional, separating the assignments and adding comments can improve readability and maintainability of the code.

```
> Tokens: 1.6k sent, 297 received. Cost: $0.00041 message, $0.0010 session.
> Added py/aider/MEMO.md to the chat
> End your comment with AI! to request changes or AI? to ask questions
```

## 2024-12-20

- ( 2024-12-20 10:30:41 )
- 綜整這些紀錄，看起來有一些可以嘗試的作法：
  - 修改 `.aiderignore`： 讓 `aider` 不要 `watch` 像是 `MEMO.md` 這樣的文件檔裡面出現的 `AI?` 或 `AI.`
- 評點：
  - 實際上 `Code Review` 改的建議還算容易理解，改得比較模組化一點，每個函數比較短。也幫我改更明確指定 `IndexError` 這個 Exception，並改用 `logger` 來顯示 Error Message。
```diff
- except:
+ except IndexError as e:
+         logging.error(f"Error fetching book info for {link}: {e}")
```

## 2025-03-26

- ( 2025-03-26 21:43:50 )
- 測試用 `uv tool` 安裝這個小工具
- 參考：
  - [httpx 的 pyproject.toml](https://github.com/encode/httpx/blob/master/pyproject.toml)
  - [yt-dlp 的 pyproject.toml](https://github.com/yt-dlp/yt-dlp/blob/master/pyproject.toml)
  - 本來想學著用 `hatchling` 因為 `httpx` 跟 `yt-dlp` 都用這個。
  - 而 `webvtt-to-json` 則只採用 `setup.py`
- 在 `httpx` 的 `pyproject.toml` 裡學到 `dependencies` 的寫法，所以根據 readmoo.py 會用到的套件，加上三個相依套件（沒特別指定版本）：
```
dependencies = [
    "requests",
    "bs4",
    "lxml"
]
```
- 其他小改動，對比範例 `hello-tool` 的 `pyproject.toml`
```diff
--- ../uv/hello-tool/pyproject.toml     2025-03-26 21:21:40.017132700 +0800
+++ readmoo/pyproject.toml      2025-03-26 21:42:32.125589500 +0800
@@ -3,18 +3,23 @@
 build-backend = "setuptools.build_meta"

 [project]
-name = "hello-tool"
+name = "readmoo"
 version = "0.1.0"
 authors = [
-  { name="Your Name", email="your.email@example.com" },
+  { name="Jazz Wang", email="jazz.wang@example.com" },
 ]
-description = "A simple hello world tool"
-requires-python = ">=3.7"
+description = "Fetch Readmoo book category, price, rating info"
+requires-python = ">=3.12"
 classifiers = [
     "Programming Language :: Python :: 3",
     "License :: OSI Approved :: MIT License",
     "Operating System :: OS Independent",
 ]
+dependencies = [
+    "requests",
+    "bs4",
+    "lxml"
+]

 [project.scripts]
-hello = "hello_tool:main"
+readmoo = "readmoo:main"
```
- ( 2025-03-26 21:52:31 )
- 測試安裝：
```bash
jazzw@JazzBook:~/git/snippet/py/requests$ uv tool install ./readmoo/
Resolved 11 packages in 633ms
      Built readmoo @ file:///C:/Users/jazzw/git/snippet/py/requests/readmoo
Prepared 1 package in 2.68s
Installed 11 packages in 93ms
 + beautifulsoup4==4.13.3
 + bs4==0.0.2
 + certifi==2025.1.31
 + charset-normalizer==3.4.1
 + idna==3.10
 + lxml==5.3.1
 + readmoo==0.1.0 (from file:///C:/Users/jazzw/git/snippet/py/requests/readmoo)
 + requests==2.32.3
 + soupsieve==2.6
 + typing-extensions==4.13.0
 + urllib3==2.3.0
Installed 1 executable: readmoo.exe
```
- ( 2025-03-26 21:55:11 )
- 確認可以動
```bash
jazzw@JazzBook:~/git/snippet/py/requests$ which readmoo
/c/Users/jazzw/.local/bin/readmoo
jazzw@JazzBook:~/git/snippet/py/requests$ readmoo
usage: readmoo [-h] --input INPUT --output OUTPUT
readmoo: error: the following arguments are required: --input/-i, --output/-o
```