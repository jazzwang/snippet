# screenpipe

> YC (S26) | Record your screen 24/7 and plug into your agents. Local, private, secure. Connect to OpenClaw, Hermes agent and 100+ apps

- Git Repo
  - https://github.com/screenpipe/screenpipe
- Website
  - https://screenpipe.com/

## 2026-08-07

- 研究 Plaude.AI 替代方案時發現的。
  - see [plaude-ai.md](../../md/genai/applications/dictation/plaude-ai.md)
- 這個專案的描述看起來也挺有『侵略性』的: 
> [!NOTE]
> Record your screen 24/7 and plug into your agents.
> 24/7 全天候把畫面錄起來給 AI Agent 用

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
could you give me more information about Screenpipe? does it support Windows and can use VLM locally?
</td></tr><tr><td>A:</td><td>

Yes, Screenpipe completely supports Windows and fully supports running Vision-Language Models (VLMs) locally. [1, 2] 

[Screenpipe](https://github.com/screenpipe/screenpipe) is specifically designed as a local-first, privacy-respecting alternative to closed-ecosystem tools like Microsoft Recall or Limitless. Because it is built on a highly optimized Rust core, it is light enough to log your screen and audio 24/7 while leaving plenty of processing headroom for local AI inference. [3, 4, 5, 6, 7] 

Here is exactly how Screenpipe operates on Windows and processes visual data locally. [4, 7, 8] 

### 1. Native Windows Support

Unlike many AI tools that favor macOS, [Screenpipe](https://screenpipe.com/) treats Windows as a first-class citizen: [9] 

* Windows Native APIs: On Windows, Screenpipe skips generic, heavy screen-capturing layers and uses [windows-rs](https://news.ycombinator.com/item?id=49024620) to communicate directly with native Windows Graphics Capture and Windows Accessibility APIs. [3, 7] 
* Local Windows OCR: Text on your screen is captured using the native Windows OCR engine. It handles data redaction (like hiding credit cards or passwords) directly on your device using Windows DirectML. [3, 7] 
* Low Overhead: It is explicitly optimized to consume less than 1% of your CPU and roughly 400 MB of RAM while running continuously in the background. [3] 

### 2. Running VLMs Locally with Screenpipe

Screenpipe does not force you to send your data to OpenAI or Anthropic. It features a built-in architecture to channel your 24/7 visual and audio logs directly into a local VLM pipeline: [10, 11, 12, 13] 

#### The Ollama Integration

The easiest way to use local VLMs with Screenpipe is through its native integration with Ollama. [10, 11, 14] 

   1. Screenpipe records your screen frames and audio timelines into a local SQLite database.
   2. You can pull an open-source visual model via Ollama (such as llava or moondream).
   3. You can use Screenpipe's plugin system (called Pipes) to auto-trigger scripts. For example, a local script can query your database, extract the last 10 screenshots from a Zoom meeting, and pass them to Ollama's local VLM endpoint to synthesize notes based on what was shown, not just what was said. [4, 10, 11, 15, 16] 

#### The Developer SDK & Model Flexibility

Because Screenpipe exposes a local REST API and an SDK, you can bypass Ollama entirely if you want more control. You can pipe raw frames into a Python script using local execution frameworks like Hugging Face Transformers or OpenVINO to process the images alongside text transcripts using models like Phi-3-Vision. [1, 4, 11, 17, 18] 

### 3. Screenpipe's "Pipes" (Note-Taking Automations)

Screenpipe includes an in-app plugin store called Pipes. These are small JavaScript/TypeScript applications that run locally inside the Screenpipe environment to turn your screen history into actionable notes. [4, 11, 19] 
Popular note-taking pipes include: [19] 

* Local Meeting Notes: Monitators your mic and system audio. The moment a meeting ends, it grabs the audio transcript, bundles it with keyframes of changing presentation slides, and builds a summary. [19, 20, 21] 
* Obsidian & Notion Sync: Automatically transfers your local multimodal meeting logs and visual notes straight into your Obsidian Vault or Notion Workspace. [19] 
* MCP Server Integration: It supports the Model Context Protocol (MCP). This means if you use an AI coding assistant like Claude Desktop, Cursor, or VS Code + Cline, your coding agent can safely query Screenpipe locally to see what you were just doing on your screen. [4, 19] 

### How to Get Started on Windows

   1. Download the app: Grab the Windows installer executable from the official Screenpipe Release Page.
   2. Install Ollama: If you want 100% local vision, download [Ollama for Windows](https://ollama.com/) and run ollama run llava in your command prompt.
   3. Configure the App: In the Screenpipe settings UI, switch your AI provider from OpenAI/Cloud over to Local / Ollama and point it to your model. [10, 22, 23, 24] 

If you plan to set this up, let me know what graphics card (GPU) your Windows machine has (so I can recommend the fastest local VLM for your hardware), or if you need help setting up a custom note-taking script!

- [1] [https://github.com](https://github.com/openvinotoolkit/openvino/discussions/34948)
- [2] [https://screenpipe.com](https://screenpipe.com/compare/limitless)
- [3] [https://news.ycombinator.com](https://news.ycombinator.com/item?id=49024620)
- [4] [https://daily.dev](https://daily.dev/posts/fbiz9smus)
- [5] [https://github.com](https://github.com/screenpipe/screenpipe)
- [6] [https://screenpipe.com](https://screenpipe.com/compare/limitless)
- [7] [https://www.reddit.com](https://www.reddit.com/r/windowsapps/comments/1r7i9al/i_built_an_opensource_app_that_records_your/)
- [8] [https://aiagentstore.ai](https://aiagentstore.ai/ai-agent/screenpipe)
- [9] https://screenpipe.com
- [10] [https://github.com](https://github.com/screenpipe/screenpipe)
- [11] [https://dev.to](https://dev.to/louis030195/how-to-create-an-ai-agent-powered-by-your-screen-mic-5g9b)
- [12] [https://skywork.ai](https://skywork.ai/skypage/en/screenpipe-mcp-ai-vision-memory/1978719521292800000)
- [13] [https://www.reddit.com](https://www.reddit.com/r/windowsapps/comments/1r7i9al/i_built_an_opensource_app_that_records_your/)
- [14] [https://github.com](https://github.com/NVIDIA-AI-IOT/live-vlm-webui/blob/main/docs/usage/list-of-vlms.md)
- [15] [https://towardsdatascience.com](https://towardsdatascience.com/running-local-llms-and-vlms-on-the-raspberry-pi-57bd0059c41a/)
- [16] [https://www.dreamhost.com](https://www.dreamhost.com/blog/local-ai-hosting/)
- [17] [https://www.youtube.com](https://www.youtube.com/watch?v=hnUmfHf-V4U)
- [18] [https://www.npmjs.com](https://www.npmjs.com/~screenpipe)
- [19] [https://github.com](https://github.com/screenpipe/awesome-screenpipe)
- [20] [https://screenpipe.com](https://screenpipe.com/blog/local-ai-meeting-notes-no-cloud)
- [21] [https://github.com](https://github.com/screenpipe/screenpipe)
- [22] [https://skywork.ai](https://skywork.ai/skypage/en/screenpipe-ai-digital-memory/1976832071869067264)
- [23] [https://collabnix.com](https://collabnix.com/running-ollama-on-windows-a-comprehensive-guide/)
- [24] [https://www.youtube.com](https://www.youtube.com/watch?v=46sTA8pUTxk)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
</table>