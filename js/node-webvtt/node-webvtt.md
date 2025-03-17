# node-webvtt

> A command line interface and npm package for the WebVTT JavaScript parser.

- Git Repo:
  - https://github.com/humphd/node-webvtt

## 2025-03-16

### 緣起

- 詳見 [subsrt](../subsrt/subsrt.md)

### Install 安裝

```bash
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ pnpm i -g webvtt

   ╭──────────────────────────────────────────────────────────────────╮
   │                                                                  │
   │                Update available! 10.6.1 → 10.6.3.                │
   │   Changelog: https://github.com/pnpm/pnpm/releases/tag/v10.6.3   │
   │                Run "pnpm self-update" to update.                 │
   │                                                                  │
   ╰──────────────────────────────────────────────────────────────────╯

Packages: +3
+++
Progress: resolved 408, reused 405, downloaded 3, added 3, done

C:\Users\jazzw\AppData\Local\pnpm\global\5:
+ webvtt 0.0.2

Done in 2.6s using pnpm v10.6.1
```

### 

- ( 2025-03-17 09:10:00 )
- 確認命令列工具路徑
```bash
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ which webvtt
/c/Users/jazzw/AppData/Local/pnpm/webvtt
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ webvtt -h

  Usage: webvtt.js [options] <file...>

  Options:

    -h, --help     output usage information
    -V, --version  output the version number
    -s, --silent   don't print errors messages
```
- ( 2025-03-17 09:10:32 )
- 檢驗 WebVTT 格式的正確性
```bash
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ webvtt sample.vtt
jazzw@JazzBook:~/git/snippet/js/node-webvtt$
```
- 如果驗證格式正確的話，不會有錯誤訊息。
- 刻意拿掉開頭的 `WEBVTT` 跟第二行空白行的話
```bash
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ webvtt sample.vtt
sample.vtt:1.0: No valid signature. (File needs to start with "WEBVTT".)
sample.vtt:2.0: No blank line after the signature.
```
- 刻意拿掉最後一行，也不會抱怨。
- 再拿掉一行時間的話，就會抱怨有錯了
```bash
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ tail -n 5 sample.vtt
f377dd1a-3271-4bb4-80e3-bacbcfe56495/3071-0
00:23:56.598 --> 00:23:56.958
<v Chan, XXXXXX>Thank you.</v>

f377dd1a-3271-4bb4-80e3-bacbcfe56495/3073-0
jazzw@JazzBook:~/git/snippet/js/node-webvtt$ webvtt sample.vtt
sample.vtt:1868.0: Cue identifier cannot be standalone.
```