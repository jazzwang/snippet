# Windows Live Caption Saver

- 2022-08-08: [Is it possible to save a transcript of live captions in Windows 11?](https://answers.microsoft.com/en-us/windows/forum/all/is-it-possible-to-save-a-transcript-of-live/3474cc04-1d34-4e51-bf99-aa7dc0e0fdd0)

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there a way to save Windows Live Caption as output file?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Currently, **Windows Live Captions does not natively support saving or exporting transcripts** to a file. The captions are generated in real-time and are not stored on disk or in any accessible log file by default [1](https://answers.microsoft.com/en-us/windows/forum/all/is-it-possible-to-save-a-transcript-of-live/3474cc04-1d34-4e51-bf99-aa7dc0e0fdd0).

However, there is a **third-party solution** available:

### 🛠 GitHub Project: `get-livecaptions`
A community-developed tool written in Rust, [**get-livecaptions**](https://github.com/msftwarelab/get-livecaptions), can:
- Capture Windows 11 Live Captions in real-time.
- Save them to a specified text file at regular intervals.
- Provide a user interface for viewing and copying captions.
- Optionally integrate with OpenAI for querying the captured text.

#### Requirements:
- Windows 11 with Live Captions enabled.
- Rust installed on your system.
- Basic command-line usage.

#### Example usage:
```bash
cargo run -- --file output.txt --interval 1
```
This command captures captions every second and writes them to `output.txt`.

Would you like help setting this up or exploring alternative methods like screen recording with OCR?
</td></tr></table>
