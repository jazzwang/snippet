# DASH-MPD CLI

A commandline application for downloading media content from a DASH MPD file, as used for on-demand replay of TV content and video streaming services.

> Download media content from a DASH-MPEG or DASH-WebM MPD manifest

- Website
  - https://emarsden.github.io/dash-mpd-cli/
- Git Repo
  - https://github.com/emarsden/dash-mpd-cli

## 2025-02-22

- Microsoft Stream 錄影是用 DASH MPD 格式傳給網頁播放軟體
- 試過 yt-dlp 會顯示檔案是 DRM 保護的
```bash
[02/22 11:44:12] yt-dlp "https://eastus1-mediap.svc.ms/transform/videomanifest?provider=spo&inputFormat=mp4&cs=fFNQTw&correlationId=61dd83a1-b07c-8000-318c-b25052308da8&docid=......略......"
```

### Similar tools

Similar commandline tools that are able to download content from a DASH manifest:

-   `yt-dlp <MPD-URL>`
-   `N_m3u8DL-RE <MPD-URL>`
-   `streamlink -o /tmp/output.mp4 <MPD-URL> worst`
-   `ffmpeg -i <MPD-URL> -vcodec copy /tmp/output.mp4`
-   `vlc <MPD-URL>`
-   `gst-launch-1.0 playbin uri=<MPD-URL>`

However, dash-mpd-cli (this application) is able to download content from certain streams that do not work with other applications:

-   streams using xHE-AAC codecs are currently unsupported by ffmpeg, streamlink, VLC, and gstreamer
-   streams in multi-period manifests
-   streams using XLink elements