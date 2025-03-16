# subsrt

- npm package
  - https://www.npmjs.com/package/subsrt
- Git Repo
  - https://github.com/papnkukn/subsrt

## 2025-03-16

- 緣起：
  - 為了快速理解多個 Microsoft Teams 錄影，下載了對應的 vtt 格式字幕檔。
  - 但要餵給 LLM 或者當 fine-tine 資料的話，結構化的 JSON 格式會比較好。
  - 而且 JSON 格式有助於把同一個發言人的內容合併成同一個長字串。可以拿來去除贅字，讓句子更容易閱讀。
- 工具蒐集：
  - 問 Bing Copilot

<table>
<tr><td>Q:</td><td><b>Are there tools to convert transcript vtt format file to json format?</b></td></tr>
<tr><td>A:</td><td>
Yes, there are several tools available online that can convert VTT (WebVTT) subtitle files to JSON format. Here are a couple of options:

1. **SubtitleGen**: This free online tool allows you to convert VTT files to JSON easily. You just need to upload your VTT file, select JSON as the output format, and click "Convert" [[1]](https://subtitlegen.com/tools/convert-vtt-to-json).

2. **EditingTools.io**: This platform offers a variety of subtitle conversion tools, including the ability to convert VTT files to JSON. It also provides additional features for checking, repairing, and correcting subtitles [[2]](https://editingtools.io/subtitles/).

These tools should help you convert your VTT files to JSON format without any hassle. If you need any further assistance, feel free to ask!
</td></tr>
<tr><td colspan="2">考量不合適上傳到 Public Cloud Service，改問有沒有本地的命令列工具：</td></tr>
<tr><td>Q:</td><td><b>Are there <mark>command line tools</mark> to convert transcript vtt format file to json format?</b></td></tr>
<tr><td>A:</td><td>
Yes, there are several command line tools available for converting VTT files to JSON format. Here are a couple of options:

1. **vtt-json**: This tool can parse and serialize VTT files to JSON format. You can use it directly from the command line. Here's an example of how to use it:
   ```bash
   vtt-json parse input.vtt --output=output.json
   ```
   You can find more details on its [GitHub page](https://github.com/linclark/vtt-json) [[1]](https://github.com/linclark/vtt-json).

2. **subsrt**: This is a versatile subtitle converter that supports various formats, including VTT to JSON. You can install it via npm and use it from the command line:
   ```bash
   npm install -g subsrt
   subsrt parse input.vtt --json output.json
   ```
   More information is available on its [npm page](https://www.npmjs.com/package/subsrt) [[2]](https://www.npmjs.com/package/subsrt).

These tools should help you convert your VTT files to JSON format efficiently. If you need any further assistance, feel free to ask!
</td></tr>
</table>

### Install 安裝

- ( 2025-03-16 12:50:03 )
- install using `pnpm`
```bash
jazzw@JazzBook:~/git/snippet/js/subsrt$ pnpm i -g subsrt
Packages: +1
+
Progress: resolved 405, reused 404, downloaded 1, added 1, done

C:\Users\jazzw\AppData\Local\pnpm\global\5:
+ subsrt 1.1.1

Done in 2.6s using pnpm v10.6.1
```
- 查看是否有對應的指令
```
jazzw@JazzBook:~/git/snippet/js/subsrt$ which subsrt
/c/Users/jazzw/AppData/Local/pnpm/subsrt
```

### Convert VTT to JSON

- ( 2025-03-16 12:53:57 )
```bash
jazzw@JazzBook:~/git/snippet/js/subsrt$ wc sample.vtt
 1868  5888 59564 sample.vtt
jazzw@JazzBook:~/git/snippet/js/subsrt$ subsrt convert sample.vtt sample.json
```
- ( 2025-03-16 12:56:29 )
- 檢驗轉換結果：
  - 原始 VTT 取樣：
    ```bash
    jazzw@JazzBook:~/git/snippet/js/subsrt$ head sample.vtt
    WEBVTT

    f377dd1a-3271-4bb4-80e3-bacbcfe56495/47-0
    00:00:03.878 --> 00:00:09.967
    <v Chan, XXXXXXXX>So first party's like, finally,
    I got a permission and the predation to</v>

    f377dd1a-3271-4bb4-80e3-bacbcfe56495/47-1
    00:00:09.967 --> 00:00:14.280
    <v Chan, XXXXXXXX>get into it,
    ```
  - 結果 JSON 取樣：
    ```bash
    jazzw@JazzBook:~/git/snippet/js/subsrt$ cat sample.json | jq .[1]
    {
        "type": "caption",
        "index": 1,
        "cue": "f377dd1a-3271-4bb4-80e3-bacbcfe56495/47-0",
        "start": 3878,
        "end": 9967,
        "duration": 6089,
        "content": "<v Chan, XXXXXXXX>So first party's like, finally,\r\nI got a permission and the predation to</v>",
        "text": "So first party's like, finally,\r\nI got a permission and the predation to"
    }
    ```
  - 照這樣的邏輯來看，如果我想要根據「發言人」(出現在 `content` 裡的 `<v .....>`) 把發言內容整合在一起，還需要做一些額外的處理。