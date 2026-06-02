# streamlink

- Git Repo
  - https://github.com/streamlink/streamlink
- Website
  - https://streamlink.github.io/install.html#windows

## 2026-06-02

- 緣起：
  - 把 uv 搬到 rust 目錄以後，注意到先前看到的 `dash-mpd-cli` 可能可以拿來下載 Microsoft Streams 影片
  - 在 https://github.com/emarsden/dash-mpd-cli#similar-tools 有提到 `Streamlink`
- 安裝：
  - sqoop
  ```cmd
  scoop bucket add extras
  scoop install streamlink
  ```
  - winget
  ```cmd
  winget install streamlink
  ```
- 實測：<font color='red'>失敗</font>
```bash
~/git/snippet$ scoop install streamlink
```
- 在 Chrome DevTool 的 Network Tab 搜尋 videomaifest 可以看到 MPD 的 response 
```
~$ streamlink -o test.mp4 "https://southcentralus1-mediap.svc.ms/transform/videomanifest?provider=spo&farmid=207079&inputFormat=mp4&......
error: No plugin can handle URL: https://southcentralus1-mediap.svc.ms/transform/videomanifest?provider=spo&farmid=207079&inputFormat=mp4&......
```
- 用 Microsoft Streams 上抓到的 MPD 檔案，用 `python -m http.server` 跑起來，再用 streamlink 去抓，還是失敗。跟 `yt-dlp` 一樣。
```
~/git/snippet$ streamlink -o test.mp4 http://127.0.0.1:8000/test.mpd
[cli][info] Found matching plugin dash for URL http://127.0.0.1:8000/test.mpd
error: http://127.0.0.1:8000/test.mpd is protected by DRM
```