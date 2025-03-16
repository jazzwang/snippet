# webvtt-to-json

- Git Repo
  - https://github.com/simonw/webvtt-to-json

## 2025-03-16

### Motivation 緣起

- 詳見 [subsrt](../../js/subsrt/subsrt.md) 的紀錄

### Install 安裝

```bash
(env) jazzw@JazzBook:~/git/snippet/py$ pip install webvtt-to-json
```

### Test 測試

```bash
(env) jazzw@JazzBook:~/git/snippet/py/webvtt-to-json$ which webvtt-to-json
/c/Users/jazzw/git/confluence-insight/env/Scripts/webvtt-to-json
(env) jazzw@JazzBook:~/git/snippet/py/webvtt-to-json$ webvtt-to-json.exe sample.vtt
[
  {
    "start": "00:00:03.878",
    "end": "00:00:09.967",
    "lines": [
      "<v Chan, XXXXXXXX>So first party's like, finally,",
      "I got a permission and the predation to</v>"
    ]
  },
... 略 ...
```
- 測試 deduplication (-d) 跟 single (-s) 參數
```bash
(env) jazzw@JazzBook:~/git/snippet/py/webvtt-to-json$ webvtt-to-json -d -s sample.vtt
[
  {
    "start": "00:00:03.878",
    "end": "00:00:09.967",
    "line": "<v Chan, XXXXXXXX>So first party's like, finally,\nI got a permission and the predation to</v>"
  },
  {
    "start": "00:00:09.967",
    "end": "00:00:14.280",
    "line": "<v Chan, XXXXXXXX>get into it,\nand I spend some time took it to look</v>"
  },
... 略 ...
```
- 整體感覺比 [subsrt](../../js/subsrt/subsrt.md) 的效果好一些。當然有些地方，像是換行符號(`\n`)，可能要替換成空白。如果後續想要把同一個與會者的發言內容串成一整個段落。