# httpx

- Web
  - https://www.python-httpx.org/
- Git Repo
  - https://github.com/encode/httpx/

> A next generation HTTP client for Python. 🦋

## 2025-03-19

- aider 提到會用 `httpx` 來擷取 web 頁面。但複雜的內容則會用 playwright 來做。
- 實測 `aider` 的 `/web` 指令，發現還會裝 `pydantic` (不確定對不對，但畫面上一閃而過)

### install

- ( 2025-03-19 00:53:49 )
```bash
(env) jazzw@JazzBook:~/git/snippet/py$ pip install 'httpx[cli]'
```
- ( 2025-03-26 18:14:04 )
- 也可以用 `uv tool` 安裝，會比較省硬碟空間，也比較不會裝一堆相依套件在 pip 裡。
```bash
jazzw@JazzBook:~$ uv tool install --force --python python3.12 httpx[cli]
Resolved 14 packages in 645ms
Uninstalled 1 package in 12ms
Installed 7 packages in 268ms
 + click==8.1.8
 + colorama==0.4.6
 ~ httpx==0.28.1
 + markdown-it-py==3.0.0
 + mdurl==0.1.2
 + pygments==2.19.1
 + rich==13.9.4
Installed 1 executable: httpx.exe
```

### test

- ( 2025-03-19 00:53:56 )
```bash
(env) jazzw@JazzBook:~/git/snippet/py$ httpx https://www.example.com
HTTP/1.1 200 OK
Accept-Ranges: bytes
Content-Type: text/html
ETag: "84238dfc8092e5d9c0dac8ef93371a07:1736799080.121134"
Last-Modified: Mon, 13 Jan 2025 20:11:20 GMT
Vary: Accept-Encoding
Content-Encoding: gzip
Cache-Control: max-age=3417
Date: Tue, 18 Mar 2025 16:54:56 GMT
Alt-Svc: h3=":443"; ma=93600,h3-29=":443"; ma=93600,quic=":443"; ma=93600; v="43"
Content-Length: 648
Connection: keep-alive

<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
- ( 2025-03-19 00:55:21 )
- 看起來可以跟 `markdownify` 一起搭配著用