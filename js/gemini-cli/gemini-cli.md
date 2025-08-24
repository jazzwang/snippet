# Gemini CLI

- Git Repo
  - https://github.com/google-gemini/gemini-cli
- News
  - 2025-06-25: [Gemini CLI: your open-source AI agents](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
  - 2025-06-26: [Gemini CLI：你的開源 AI 代理](https://blog.google/intl/zh-tw/products/cloud/gemini-cli-your-open-source-ai-agent/)

## 2025-06-25

- See the news from [LargitData's LinkedIn Post](https://www.linkedin.com/feed/update/urn:li:activity:7343622985636827136/)

> Google 你這不要臉的傢伙，連 Claude Code 都抄，不過看在免費的份上，只好原諒你了！😤 
>
> Google 即將推出 Gemini CLI，a.k.a. Claude Code 的 Gemini 版本。🚀 
> 
> 💰 最大賣點 ，只需使用 Google 帳戶登入，即可獲得：
> 
> - Gemini 2.5 Pro 模型，含 100 萬 token 的超大上下文視窗
> - 每分鐘 60 次請求，每日最多 1,000 次請求
> 
> 代表幾乎完全免費！
>
> ⭐ Gemini CLI 還提供以下功能：
> 
> 🧠 智慧程式碼理解：深度理解程式碼，提供debug和最佳化建議
> 🔧 系統整合：透過自然語言直接操作檔案和執行系統命令
> 🔍 即時網路搜尋：內建 Google 搜尋功能！
> 🎛️ 高度可客製化：支援MCP、自訂提示和 GEMINI .md (連這也抄)
> 🤖 自動化整合：支援非同步呼叫，完美整合現有的工作流程
> 
> 好啦，大廠都下來卷了，猜猜我們的獨角獸 Cursor 還有多少光景好活？！😏 

- 看起來蠻值得花點時間測試一下。

## 2025-07-04

- ( 2025-07-04 12:13:19 )
- 參考：
  - 2025-06-27: 🌟 Gemini CLI 初探：讓 Gemini 進入你的終端機
  - https://vocus.cc/article/685dd5edfd897800010b06d3
- 環境：
  - Windows 11 Home x86_64
- 安裝：
```bash
~$ npm install -g @google/gemini-cli

added 432 packages in 23s
```
- 確認：
```bash
~$ which gemini
/c/Users/jazzw/scoop/apps/nvm/current/nodejs/nodejs/gemini
~$ gemini --help
Options:
  -m, --model                    Model      [string] [default: "gemini-2.5-pro"]
  -p, --prompt                   Prompt. Appended to input on stdin (if any).
                                                                        [string]
  -s, --sandbox                  Run in sandbox?                       [boolean]
      --sandbox-image            Sandbox image URI.                     [string]
  -d, --debug                    Run in debug mode?   [boolean] [default: false]
  -a, --all_files                Include ALL files in context?
                                                      [boolean] [default: false]
      --show_memory_usage        Show memory usage in status bar
                                                      [boolean] [default: false]
  -y, --yolo                     Automatically accept all actions (aka YOLO
                                 mode, see
                                 https://www.youtube.com/watch?v=xvFZjo5PgG0 for
                                 more details)?       [boolean] [default: false]
      --telemetry                Enable telemetry? This flag specifically
                                 controls if telemetry is sent. Other
                                 --telemetry-* flags set specific values but do
                                 not enable telemetry on their own.    [boolean]
      --telemetry-target         Set the telemetry target (local or gcp).
                                 Overrides settings files.
                                              [string] [choices: "local", "gcp"]
      --telemetry-otlp-endpoint  Set the OTLP endpoint for telemetry. Overrides
                                 environment variables and settings files.
                                                                        [string]
      --telemetry-log-prompts    Enable or disable logging of user prompts for
                                 telemetry. Overrides settings files.  [boolean]
  -c, --checkpointing            Enables checkpointing of file edits
                                                      [boolean] [default: false]
  -v, --version                  Show version number                   [boolean]
  -h, --help                     Show help                             [boolean]
~$ gemini -v
0.1.9
```
- 實測互動：
  - ![](20250704123324_gemini-cli_websearch_tool.png)
  - ![](20250704121805_gemini-cli_version.png)
  - ![](20250704123413_gemini-cli_tokens.png)
```
╭────────────╮
│  > /tools  │
╰────────────╯

ℹ Available Gemini CLI tools:

    - ReadFolder
    - ReadFile
    - SearchText
    - FindFiles
    - Edit
    - WriteFile
    - WebFetch
    - ReadManyFiles
    - Shell
    - Save Memory
    - GoogleSearch
```

- 初步感想：
  - Autocompletion 不像 Aider 可以用 TAB 自動補齊 `/{command}`，也許還有特定的 hotkey 要研究文件才會知道。
  - 相較於 Aider，Gemini CLI 只支援單一模型。
  - 相較於 Aider，目前 Aider 比較缺乏的部份應該就是 `/tools` 跟 `/mcp` 這兩塊吧～
    - Tools: 這部份理論上應該是 Model 本身是否支援 `Tool Calling`，但我有點不確定為什麼 Gemini 2.5 Pro 可以明確列出工具列表。其他支援 Tool 的模型(e.g. `Qwen 2.5`)並沒有
    - MCP: 雖然有人已經寫了讓 Aider 支援MCP 的外掛，但還是期待 Aider 有朝一日可以把這段補起來。
  - Aider 有實作 `cache` 來減少 token 用量，gemini-cli 看起來也有實作這一塊，不過<mark>僅限於 API Key 認證用戶</mark>。直接使用 Gmail OAuth 認證跟使用 Google Code Assistant 的用戶，還不支援快取節費(Token Caching and Cost Optimization)。當然科技大廠短期內應該就是砸錢養用量。先開放免費使用，養套殺策略。日久見人心，使用者會用腳投票。
    - 參考：
      - https://github.com/google-gemini/gemini-cli/blob/main/docs/troubleshooting.md
      > Q: Why don't I see <mark>cached token</mark> counts in my stats output?
      > A: Cached token information is only displayed when cached tokens are being used. <mark>This feature is available for **API key** users (Gemini API key or Vertex AI) but not for **OAuth** users (Google Personal/Enterprise accounts) at this time</mark>, as the Code Assist API does not support cached content creation. You can still view your total token usage with the `/stats` command.
      - https://github.com/google-gemini/gemini-cli/blob/main/docs/telemetry.md
      > gemini_cli.api_response: This event occurs upon receiving a response from Gemini API.
      > - Attributes:
      >   - model
      >     - status_code
      >     - duration_ms
      >     - error (optional)
      >     - input_token_count
      >     - output_token_count
      >     - <mark>cached_content_token_count</mark>
      >     - thoughts_token_count
      >     - tool_token_count
      >     - response_text (if applicable)
      - https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/token-caching.md
      > **Token Caching and Cost Optimization**
      > Gemini CLI automatically optimizes API costs through token caching when using API key authentication (Gemini API key or Vertex AI). This feature reuses previous system instructions and context to reduce the number of tokens processed in subsequent requests.
      >
      > - **Token caching is available for:**
      >   - API key users (Gemini API key)
      >   - Vertex AI users (with project and location setup)
      >
      > - **Token caching is not available for:**
      >   - OAuth users (Google Personal/Enterprise accounts) - the Code Assist API does not support cached content creation at this time
      >
      > You can view your token usage and cached token savings using the `/stats` command. When cached tokens are available, they will be displayed in the stats output.
- 商業策略觀察：
  - `Github Copilot` vs `Google Code Assistant`
  - `Claude Code` vs `Gemini CLI`

## 2025-08-20

- Gemini CLI for GitHub Actions
  - https://www.linkedin.com/feed/update/urn:li:activity:7358848236998041601/
- 2025-08-06:
  - Meet your new AI coding teammate: Gemini CLI GitHub Actions
  - https://blog.google/technology/developers/introducing-gemini-cli-github-actions/
  - https://github.com/google-github-actions/run-gemini-cli

## 2025-08-21

- 2025-06-29:
  - Conquering Google Login for Gemini CLI on Headless Servers
  - https://medium.com/@fourdollars/conquering-google-login-for-gemini-cli-on-headless-servers-3e9d2649790f
- 2025-07-05:
  - Gemini CLI in GCP Cloud Shell with Google login 小記
  - https://sakananote2.blogspot.com/2025/07/gemini-cli-in-gcp-cloud-shell-with.html