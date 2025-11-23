# jq

- Git Repo
  - https://github.com/jqlang/jq
- Website
  - https://jqlang.org/

## 2025-11-23

- 緣起：
  - 想分析 HAR 檔跟 Zoom 錄影某個 JSON 檔的 Schema
- 參考：
  - https://stackoverflow.com/questions/43379692/extract-schema-of-nested-json-object
- 解法一：
  - https://stackoverflow.com/a/43380040
    ```bash
    jq 'paths(scalars) | map(tostring) | join(".")' sample.json
    ```
- 解法二：
  - https://stackoverflow.com/a/57261588
  - 這個作法必須把 https://gist.github.com/pkoppstein/a5abb4ebef3b0f72a6ed 存成 `schema.jq`
  - 然後再用指令呼叫
    ```bash
    jq 'include "schema"; schema' sample.json
    ```
- 解法三：
  - https://stackoverflow.com/a/43379886
  - https://raw.githubusercontent.com/ilyash/show-struct/refs/heads/master/show_struct.py
  - 這個作法比較簡單，蠻方便拿來做 `jq` 查詢語法的參考
    ```bash
    ~/bin$ wget https://raw.githubusercontent.com/ilyash/show-struct/refs/heads/master/show_struct.py
    ~/bin$ chmod a+x show_struct.py
    ~/bin$ cd ~/Downloads
    ~/Downloads$ show_struct.py sample.har | awk -F' -- ' '{ print $1 }'
    .log
    .log.creator
    .log.creator.name
    .log.creator.version
    .log.entries
    .log.entries[]
    .log.entries[]._connectionId
    .log.entries[]._initiator
    .log.entries[]._initiator.stack
    .log.entries[]._initiator.stack.callFrames
    .log.entries[]._initiator.stack.callFrames[]
    .log.entries[]._initiator.stack.callFrames[].columnNumber
    .log.entries[]._initiator.stack.callFrames[].functionName
    .log.entries[]._initiator.stack.callFrames[].lineNumber
    .log.entries[]._initiator.stack.callFrames[].scriptId
    .log.entries[]._initiator.stack.callFrames[].url
    .log.entries[]._initiator.stack.parent
    .log.entries[]._initiator.stack.parent.callFrames
    .log.entries[]._initiator.stack.parent.callFrames[]
    .log.entries[]._initiator.stack.parent.callFrames[].columnNumber
    .log.entries[]._initiator.stack.parent.callFrames[].functionName
    .log.entries[]._initiator.stack.parent.callFrames[].lineNumber
    .log.entries[]._initiator.stack.parent.callFrames[].scriptId
    .log.entries[]._initiator.stack.parent.callFrames[].url
    .log.entries[]._initiator.stack.parent.description
    .log.entries[]._initiator.type
    .log.entries[]._priority
    .log.entries[]._resourceType
    .log.entries[].cache
    .log.entries[].connection
    .log.entries[].pageref
    .log.entries[].request
    .log.entries[].request.bodySize
    .log.entries[].request.cookies
    .log.entries[].request.headers
    .log.entries[].request.headersSize
    .log.entries[].request.headers[]
    .log.entries[].request.headers[].name
    .log.entries[].request.headers[].value
    .log.entries[].request.httpVersion
    .log.entries[].request.method
    .log.entries[].request.queryString
    .log.entries[].request.queryString[]
    .log.entries[].request.queryString[].name
    .log.entries[].request.queryString[].value
    .log.entries[].request.url
    .log.entries[].response
    .log.entries[].response._error
    .log.entries[].response._fetchedViaServiceWorker
    .log.entries[].response._transferSize
    .log.entries[].response.bodySize
    .log.entries[].response.content
    .log.entries[].response.content.mimeType
    .log.entries[].response.content.size
    .log.entries[].response.content.text
    .log.entries[].response.cookies
    .log.entries[].response.headers
    .log.entries[].response.headersSize
    .log.entries[].response.headers[]
    .log.entries[].response.headers[].name
    .log.entries[].response.headers[].value
    .log.entries[].response.httpVersion
    .log.entries[].response.redirectURL
    .log.entries[].response.status
    .log.entries[].response.statusText
    .log.entries[].serverIPAddress
    .log.entries[].startedDateTime
    .log.entries[].time
    .log.entries[].timings
    .log.entries[].timings._blocked_queueing
    .log.entries[].timings._workerFetchStart
    .log.entries[].timings._workerReady
    .log.entries[].timings._workerRespondWithSettled
    .log.entries[].timings._workerStart
    .log.entries[].timings.blocked
    .log.entries[].timings.connect
    .log.entries[].timings.dns
    .log.entries[].timings.receive
    .log.entries[].timings.send
    .log.entries[].timings.ssl
    .log.entries[].timings.wait
    .log.pages
    .log.pages[]
    .log.pages[].id
    .log.pages[].pageTimings
    .log.pages[].pageTimings.onContentLoad
    .log.pages[].pageTimings.onLoad
    .log.pages[].startedDateTime
    .log.pages[].title
    .log.version
    ```
  - 備註：需要處理一下「字集」的問題
    ```bash
    ~/Downloads$ show_struct.py From_Lakehouse_to_Intelligent_Data_Infrastructure.json
    Traceback (most recent call last):
    File "C:\Users\jazzw\bin\show_struct.py", line 60, in <module>
        data = json.loads(f.read())
                        ^^^^^^^^
    File "C:\Users\jazzw\scoop\apps\python\current\Lib\encodings\cp1252.py", line 23, in decode
        return codecs.charmap_decode(input,self.errors,decoding_table)[0]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    UnicodeDecodeError: 'charmap' codec can't decode byte 0x8d in position 686: character maps to <undefined>
    ```
    ```bash
    ~/Downloads$ json-schema From_Lakehouse_to_Intelligent_Data_Infrastructure.json | sed 's# -- .*##'
    Traceback (most recent call last):
      File "C:\Users\jazzw\bin\json-schema", line 69, in <module>
        print("{0} -- {1}".format(path['path'], path['values'][0]))
      File "C:\Users\jazzw\scoop\apps\python\current\Lib\encodings\cp1252.py", line 19, in encode
        return codecs.charmap_encode(input,self.errors,encoding_table)[0]
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    UnicodeEncodeError: 'charmap' codec can't encode character '\u5e74' in position 40: character maps to <undefined>
    ```
  - 修正：
    ```diff
    --- show_struct.py      2025-11-23 20:10:22.185025400 +0800
    +++ json-schema 2025-11-23 20:09:22.076243900 +0800
    @@ -1,4 +1,5 @@
    #!/usr/bin/env python
    +# coding: utf-8
    # vim: ts=4 sw=4 et

    # https://github.com/ilyash/show-struct.git
    @@ -8,6 +9,7 @@
    import json
    import sys

    +sys.stdout.reconfigure(encoding='utf-8')

    class Outliner(object):

    @@ -56,7 +58,7 @@
        if args.file == "-":
            data = json.loads(sys.stdin.read())
        else:
    -        with open(args.file) as f:
    +        with open(args.file, 'r', encoding='utf-8') as f:
                data = json.loads(f.read())

        outline = Outliner().outline(data)
    ```