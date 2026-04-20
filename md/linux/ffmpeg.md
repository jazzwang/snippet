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

## 2026-04-19

- 需求：把兩個多小時的 YouTube 影片擷取出想要的片段
- Prompt:
> how can I use ffmpeg to cut a clip from given start and end timestamp?
- Gemini 3 Response:

Cutting a video with `ffmpeg` is one of its most common use cases. Depending on whether you want speed or frame-perfect accuracy, there are two main ways to handle it.

### 1\. The Basic Command (Fastest)

If you want to cut a clip without re-encoding the video (which is near-instant), use the `-c copy` flag.


```Bash
ffmpeg -ss 00:01:30 -to 00:02:00 -i input.mp4 -c copy output.mp4
```

#### Breakdown of the flags:

-   **`-ss` (Start Seek):** The start timestamp (Format: `HH:MM:SS` or seconds).
-   **`-to` (End Position):** The end timestamp (Format: `HH:MM:SS` or seconds).
-   **`-i`:** Your input file.
-   **`-c copy`:** Tells ffmpeg to copy the video and audio streams directly without re-encoding. It's lightning fast but can occasionally be slightly off if the cut doesn't land on a "keyframe."

### 2\. Using Duration Instead of End Time

If you know the start time and you just want the next 30 seconds (rather than calculating the end timestamp), use `-t`.

```bash
ffmpeg -ss 00:01:30 -t 30 -i input.mp4 -c copy output.mp4
```

-   **`-t` (Duration):** How long the clip should be (in this case, 30 seconds).

### 3\. The "Frame Accurate" Method

If you notice your video starts with a few seconds of black screen or "frozen" frames when using the commands above, it's because of the `-c copy` flag missing a keyframe. To fix this, you have to let `ffmpeg` re-encode the clip:

```Bash
ffmpeg -i input.mp4 -ss 00:01:30 -to 00:02:00 output.mp4
```

> **Note the order:** By putting `-i` **before** the `-ss` flag, `ffmpeg` will decode the video and find the exact frame you requested. This is slower but much more precise.

### Summary Table

| **Feature** | **Command Flag** | **Example** |
| --- |  --- |  --- |
| **Start Time** | `-ss` | `00:00:10` |
| **End Time** | `-to` | `00:00:25` |
| **Duration** | `-t` | `15` (seconds) |
| **Stream Copy** | `-c copy` | Fast, no quality loss |
| **Re-encode** | (Omit `-c copy`) | Slower, frame-accurate |

#### Pro Tip: Input vs. Output Seeking

- **Input Seeking (Fast):** `ffmpeg -ss [time] -i [input] ...`
  - It jumps to the timestamp immediately. Use this for long videos.
- **Output Seeking (Accurate):** `ffmpeg -i [input] -ss [time] ...`
  - It processes the video from the beginning until it reaches the timestamp. Slower, but ensures the cut is exactly where you want it.

- 實際執行
```bash
  [04/20 00:41:47] ~$ ffmpeg -ss 2:33:01 -t 315 -i source.webm -c copy target.webm
```