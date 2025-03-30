# MHTMLconverter
- Git Repo:
  - https://github.com/AScriver/MHTMLExtractor
- PyPI:
  - https://pypi.org/project/MHTMLconverter/

## 2024-12-15
- ( 2024-12-15 01:57:38 )
- 測試 HTML <-> MHTML 轉換工具
- 安裝：

```bash
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ pip3 install mhtmlconverter
```

- 看起來有三種工具
  - `html2mtml`
  - `md2mtml`
  - `mhtml2html`
- 看一下 `--help` 顯示的用法：
```bash
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ html2mhtml --help
Usage: html2mhtml [OPTIONS]

  HTML to MHTML converter

Options:
  -i, --input TEXT   html input filename  [required]
  -o, --output TEXT  mhtml output filename
  --help             Show this message and exit.
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ md2mhtml --help
Usage: md2mhtml [OPTIONS]

  MD to MHTML converter

Options:
  -i, --input TEXT   md input filename  [required]
  -o, --output TEXT  mhtml output filename
  --help             Show this message and exit.
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ md2mhtml --help
Usage: md2mhtml [OPTIONS]

  MD to MHTML converter

Options:
  -i, --input TEXT   md input filename  [required]
  -o, --output TEXT  mhtml output filename
  --help             Show this message and exit.
```

- ( 2024-12-15 02:10:22 )
- 測試把 `mhtmlconverter.md` 轉成 `mhtmlconverter.mhtml` 

```bash
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ md2mhtml -i mhtmlconverter.md -o mhtmlconverter.mhtml 
```

- 下載下來看，用 Chrome 顯示為空白。但 File Explorer 能正常顯示。

- 測試將 MTHML 轉成 HTML
```bash
@jazzwang ➜ /workspaces/snippet/py/mhtmlconverter (master) $ mhtml2html -i mhtmlconverter.mhtml -o mhtmlconverter.html
 fileutility.py >  get_content :  mhtmlconverter.mhtml
mhtmlconverter.mhtml
```