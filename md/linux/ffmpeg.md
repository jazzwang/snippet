# ffmpeg

## 2025-11-10

- 紀錄一下常用的 ffmpeg 指令。
- 用途一：轉檔 (e.g. m4a 格式，轉成 mp3 格式)
```bash
ffmpeg -i input.m4a output.mp3
```
  - 原本是用 `avconv` 指令，也有用過 `mencoder` 不過後來都不容易找到安裝套件，還好可以容易安裝 ffmpeg (on Linux or Windows)
```bash
avconv -i input.m4a output.mp3
```
- 用途二：忽略開頭的秒數(e.g. 一些 webinar 直播前面有一段時間在等演講開始）
  - Reference:
    - Is it possible to use ffmpeg to trim off X seconds from the beginning of a video with an unspecified length?
    - https://superuser.com/a/269960
```bash
ffmpeg -i input.m4a -ss 15:40 output.mp3 ## 忽略 15 分 40 秒
```
