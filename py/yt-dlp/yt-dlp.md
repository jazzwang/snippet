# yt-dlp = YouTube Download

- PyPI
  - https://pypi.org/project/yt-dlp
- Git Repo
  - https://github.com/yt-dlp/yt-dlp

- 紀錄一些使用上的小技巧

## 2025-07-09

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me a command line example to extract subtitle from YouTube using yt-dlp?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

To extract subtitles from a YouTube video using `yt-dlp`, you can use various command-line options depending on your specific needs. Here are several examples:

**Basic Extraction (Auto-generated and Available Subtitles):**

This command will download all available subtitles (including auto-generated ones if available) in all languages for the specified video.

```bash
yt-dlp --write-subs --all-subs --skip-download "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

```

* `--write-subs`: Instructs `yt-dlp` to download the subtitles.
* `--all-subs`: Downloads all available subtitle tracks for the video.
* `--skip-download`: Prevents `yt-dlp` from downloading the video itself, only downloading the subtitles.
* `"https://www.youtube.com/watch?v=YOUR_VIDEO_ID"`: Replace `YOUR_VIDEO_ID` with the actual ID or full URL of the YouTube video.

**Extracting Specific Languages:**

If you only want subtitles in certain languages (e.g., English and Spanish):

```bash
yt-dlp --write-subs --sub-langs en,es --skip-download "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

```

* `--sub-langs en,es`: Specifies the desired subtitle languages. You can use their two-letter ISO 639-1 codes.

**Extracting Auto-generated Subtitles Only:**

To specifically get auto-generated subtitles (often marked with `.orig` in the filename):

```bash
yt-dlp --write-auto-subs --skip-download "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

```

* `--write-auto-subs`: Only downloads auto-generated subtitles.

**Specifying Subtitle Format (e.g., SRT, VTT):**

You can specify the preferred output format for the subtitles. SRT and VTT are common choices.

```bash
yt-dlp --write-subs --all-subs --sub-format srt --skip-download "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

```

* `--sub-format srt`: Saves the subtitles in SRT format. Other common options include `vtt`, `ass`, `lrc`.

**Embedding Subtitles into the Video (if downloading the video):**

If you *are* downloading the video and want to embed the subtitles directly into the video file:

```bash
yt-dlp --write-subs --all-subs --embed-subs "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

* `--embed-subs`: Embeds the downloaded subtitles into the video file. This usually requires a video format that supports embedded subtitles (like MP4 or MKV) and often remuxing or re-encoding.

**Listing Available Subtitle Tracks (before downloading):**

To see which subtitle tracks are available for a video before downloading them, use the `--list-subs` option:

```bash
yt-dlp --list-subs "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

This will output a list like:

```
[info] Available subtitles for YOUR_VIDEO_ID:
Language formats
en       vtt, srv3, ttml, ass, srt, json3
es       vtt, srv3, ttml, ass, srt, json3
```

**Saving Subtitles to a Specific Directory:**

```bash
yt-dlp --write-subs --all-subs --skip-download -o "~/Downloads/subtitles/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```

* `-o "~/Downloads/subtitles/%(title)s.%(ext)s"`: Specifies the output template.
* `~/Downloads/subtitles/`: The directory where you want to save the subtitles.
* `%(title)s`: Replaced by the video's title.
* `%(ext)s`: Replaced by the subtitle file extension (e.g., `srt`, `vtt`).

**Important Notes:**

* **Install `yt-dlp`:** If you haven't already, install `yt-dlp`. The recommended way is via `pip`:
```bash
pip install -U yt-dlp
```

* **Update `yt-dlp` Regularly:** YouTube frequently changes its website, which can break `yt-dlp`. Keep it updated for the best performance:
```bash
yt-dlp -U

```

* **Replace `YOUR_VIDEO_ID`:** Always replace `"https://www.youtube.com/watch?v=YOUR_VIDEO_ID"` with the actual URL of the YouTube video you want to process.
* **Check `yt-dlp --help`:** For a complete list of options and more advanced usage, refer to the `yt-dlp` help documentation: `yt-dlp --help`.
</td></tr></table>

## 2025-09-25

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
how can I download transcript of specific youtube link using yt-dlp?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

To download the transcript for a specific YouTube video using yt-dlp, you'll use a command-line interface with a few key options. The most important options are those that tell yt-dlp to download subtitles/captions and to skip downloading the video itself.

### Command for Downloading Transcripts

The basic command structure is as follows:

```bash
yt-dlp --skip-download --write-subs --sub-lang <language_code> "<video_url>"
```

* `yt-dlp`: The name of the program you're running.
* `--skip-download`: This is crucial. It tells yt-dlp to **not** download the video file, which is the default behavior. It will only download the supplementary files, like the transcript.
* `--write-subs`: This command instructs yt-dlp to download the subtitles created by the uploader.
* `--sub-lang <language_code>`: This option specifies the language of the transcript you want to download. Replace `<language_code>` with the two-letter ISO 639-1 code for the language (e.g., **`en`** for English, **`es`** for Spanish, **`fr`** for French).

---

### Additional Options

You can combine the base command with other options to get the exact transcript you need.

#### Downloading Auto-Generated Transcripts

YouTube often generates automatic captions when no human-created ones are available. To download these, use the `--write-auto-subs` option. You can combine it with `--write-subs` to download both human-created and auto-generated transcripts, with a preference for the human-created ones.

```bash
yt-dlp --skip-download --write-subs --write-auto-subs --sub-lang en "<video_url>"
```

#### Listing Available Transcripts

If you aren't sure what languages are available for a video, you can list them with the `--list-subs` option. This will show you all available human-generated and auto-generated subtitles without downloading anything.

```bash
yt-dlp --list-subs "<video_url>"
```

The output will display the language code and format for each available transcript.

#### Specifying the Transcript Format

By default, yt-dlp will download the transcript in the VTT format. If you need a different format, like SRT, use the `--sub-format` option.

```bash
yt-dlp --skip-download --write-subs --sub-lang en --sub-format srt "<video_url>"
```

#### Example

Here's a full example command to download the English transcript in SRT format from a specific YouTube link, without downloading the video itself.

```bash
yt-dlp --skip-download --write-auto-subs --sub-lang en --sub-format srt "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
</td></tr></table>

## 2026-01-02

### 增加 header

- 加上 `--add-headers` (允許多個)

```
yt-dlp --add-headers referer:https://example.com/ --add-headers origin:https://example.com https://exampe.com/test.m3u8
```

### 列舉影音格式

- 加上 `-F`

```bash
yt-dlp -F https://www.youtube.com/watch?v=OQXkkbbhp4Y
```
```bash
~/git/snippet$ yt-dlp -F https://www.youtube.com/watch?v=OQXkkbbhp4Y
[youtube] Extracting URL: https://www.youtube.com/watch?v=OQXkkbbhp4Y
[youtube] OQXkkbbhp4Y: Downloading webpage
[youtube] OQXkkbbhp4Y: Downloading android sdkless player API JSON
[youtube] OQXkkbbhp4Y: Downloading tv client config
[youtube] OQXkkbbhp4Y: Downloading tv player API JSON
[youtube] OQXkkbbhp4Y: Downloading web safari player API JSON
[youtube] OQXkkbbhp4Y: Downloading player 50cc0679-main
WARNING: [youtube] Falling back to generic n function search
         player = https://www.youtube.com/s/player/50cc0679/player_ias.vflset/en_US/base.js
WARNING: [youtube] OQXkkbbhp4Y: nsig extraction failed: Some formats may be missing
         n = _YAA3YEKbZLwX4qCUU ; player = https://www.youtube.com/s/player/50cc0679/player_ias.vflset/en_US/base.js
         Please report this issue on  https://github.com/yt-dlp/yt-dlp/issues?q= , filling out the appropriate issue template. Confirm you are on the latest version using  yt-dlp -U
WARNING: [youtube] OQXkkbbhp4Y: Some web_safari client https formats have been skipped as they are missing a url. YouTube is forcing SABR streaming for this client. See  https://github.com/yt-dlp/yt-dlp/issues/12482  for more details
WARNING: [youtube] OQXkkbbhp4Y: Some web client https formats have been skipped as they are missing a url. YouTube is forcing SABR streaming for this client. See  https://github.com/yt-dlp/yt-dlp/issues/12482  for more details
[youtube] OQXkkbbhp4Y: Downloading m3u8 information
[info] Available formats for OQXkkbbhp4Y:
ID  EXT   RESOLUTION FPS CH │   FILESIZE   TBR PROTO │ VCODEC       VBR ACODEC      ABR ASR MORE INFO
─────────────────────────────────────────────────────────────────────────────────────────────────────────────
sb3 mhtml 48x27        2    │                  mhtml │ images                               storyboard
sb2 mhtml 60x45        1    │                  mhtml │ images                               storyboard
sb1 mhtml 120x90       1    │                  mhtml │ images                               storyboard
sb0 mhtml 240x180      1    │                  mhtml │ images                               storyboard
139 m4a   audio only      2 │  347.27KiB   49k https │ audio only       mp4a.40.5   49k 22k low, m4a_dash
140 m4a   audio only      2 │  919.31KiB  130k https │ audio only       mp4a.40.2  130k 44k medium, m4a_dash
251 webm  audio only      2 │  858.09KiB  121k https │ audio only       opus       121k 48k medium, webm_dash
91  mp4   192x144     30    │ ~  1.06MiB  154k m3u8  │ avc1.4D400C      mp4a.40.5
160 mp4   192x144     30    │  589.61KiB   83k https │ avc1.4d400c  83k video only          144p, mp4_dash
93  mp4   480x360     30    │ ~  4.41MiB  637k m3u8  │ avc1.4D401E      mp4a.40.2
134 mp4   480x360     30    │    1.68MiB  243k https │ avc1.4d401e 243k video only          360p, mp4_dash
18  mp4   480x360     30  2 │ ≈  2.57MiB  371k https │ avc1.42001E      mp4a.40.2       44k 360p
94  mp4   640x480     30    │ ~  7.26MiB 1050k m3u8  │ avc1.4D401E      mp4a.40.2
135 mp4   640x480     30    │    3.23MiB  467k https │ avc1.4d401e 467k video only          480p, mp4_dash
```