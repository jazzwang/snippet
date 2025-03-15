# mcpm-aider

- Git Repo
  - https://github.com/lutzleonhardt/mcpm-aider
- YouTube
  - https://www.youtube.com/watch?v=OM1h4YDPjRU

## 2025-03-15

### MCP 跟 aider 整合 -- `mcpm-aider`

- ( 2025-03-15 21:05:49 )
- 想法： `aider` 目前並沒有支援可以呼叫外部工具的作法，像是可否請 `aider` 的 `/ask` 模式做 web search 並彙整到 Markdown
- 搜尋：找到一個 YouTube 影片 [Use MCP Servers and Tools in Aider](https://www.youtube.com/watch?v=OM1h4YDPjRU) 提到他寫了一個工具，可以讓 `aider` 知道有 MCP Tool

### 安裝

- ( 2025-03-15 21:45:05 )
- test installation with `pnpm`
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ pnpm i -g @poai/mcpm-aider

   ╭──────────────────────────────────────────────────────────────────╮
   │                                                                  │
   │                Update available! 10.6.1 → 10.6.3.                │
   │   Changelog: https://github.com/pnpm/pnpm/releases/tag/v10.6.3   │
   │                Run "pnpm self-update" to update.                 │
   │                                                                  │
   ╰──────────────────────────────────────────────────────────────────╯

Packages: +88
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Progress: resolved 404, reused 316, downloaded 88, added 88, done

C:\Users\jazzw\AppData\Local\pnpm\global\5:
+ @poai/mcpm-aider 1.0.4

Done in 13.3s using pnpm v10.6.1

jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ which mcpm-aider
/c/Users/jazzw/AppData/Local/pnpm/mcpm-aider

jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider search web

📦 Found 24 packages matching "web"

Pagespeed-Mcp-Server (@PhialsBasement/Pagespeed-MCP-Server)
  A Model Context Protocol (MCP) server that integrates PageSpeed Insights functionality, enabling AI assistants to perform detailed web performance analysis.
  #AI #PageSpeed Insights #Server

Tavily (@RamXX/mcp-tavily)
  A Model Context Protocol server enabling AI-powered web searches, direct Q&A, and recent news retrieval using Tavily's API.
  #AI #web-search #MCP-server

Mcp-Searxng (@SecretiveShell/MCP-searxng)
  An MCP server for integrating agentic systems with web search functionality using searXNG.
  #MCP #searXNG #web-search

... 後略 ...
```

### 設定

- ( 2025-03-15 22:00:47 )
- 根據文件，要先創一個 Claude config，因為我習慣跑 git-bash，先試試 `~/.config/claude/claude.json`
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
[2025-03-15T14:23:14.738Z] [ERROR] Claude config not found
No MCP servers found
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mkdir -p ~/.config/claude/
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ touch ~/.config/claude/claude.json
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
[2025-03-15T14:25:30.336Z] [ERROR] Claude config not found
No MCP servers found
```
- 看樣子要試試
```cmd
Microsoft Windows [Version 10.0.26100.3476]
(c) Microsoft Corporation. All rights reserved.

C:\Users\jazzw>echo %APPDATA%
C:\Users\jazzw\AppData\Roaming
```
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mkdir ~/AppData/Roaming/claude/
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ touch ~/AppData/Roaming/claude/claude.json
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
[2025-03-15T14:29:30.871Z] [ERROR] Claude config not found
No MCP servers found
```
- 還是有錯誤訊息，改用 YouTube 影片裡的設定檔
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ cat > ~/.config/claude/claude_desktop_config.json << EOF
> {
>   "mcpServers": {}
> }
> EOF
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ cat  ~/.config/claude/claude_desktop_config.json
{
  "mcpServers": {}
}
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
[2025-03-15T14:31:35.317Z] [ERROR] Claude config not found
No MCP servers found
```
- 最後一個組合
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ cp ~/.config/claude/claude_desktop_config.json ~/AppData/Roaming/claude/
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
No MCP servers found
```
- 搞定！

### 啟動 MCP Server

- ( 2025-03-15 23:04:55 )
- 把 `mcpm-aider` 自己變成 MCP Server
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider add --self
MCPM CLI added successfully
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider list
Your MCP Servers:

mcpm
  ✓ Enabled
  Command: mcpm
  Args: mcp
  Source: self
```
- 啟動 MCP Server
```bash
jazzw@JazzBook:~/git/snippet/js/mcpm-aider$ mcpm-aider mcp
MCPM MCP Server running on stdio
```
- ( 2025-03-15 23:09:36 )
- 根據 YouTube 影片的操作，實測一下 `aider`
```bash
jazzw@JazzBook:~/git/snippet$ export OLLAMA_API_BASE=http://127.0.0.1:11434
jazzw@JazzBook:~/git/snippet$ ollama list
NAME                            ID              SIZE      MODIFIED
gemma-3-12b-it:q4_k_m           56a4b304a208    7.3 GB    35 hours ago
qwen25-7b-instruct-1m:q4_k_m    80b818033c9f    4.7 GB    7 days ago
qwen2.5-coder:latest            2b0496514337    4.7 GB    2 weeks ago
deepseek-r1:8b                  28f8fd6cdc67    4.9 GB    5 weeks ago
jazzw@JazzBook:~/git/snippet$ aider --model ollama/qwen2.5-coder:latest
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Aider v0.75.1
Model: ollama/qwen2.5-coder:latest with whole edit format
Git repo: .git with 1,201 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 4096.0 tokens, auto refresh
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /tokens

Initial repo scan can be slow in larger repos, but only happens once.
Scanning repo:   0%|                                                                                                              | 0/1201 [00:00<?, ?it/s]Repo-map can't include C:\Users\jazzw\git\snippet\c#\c-sharp-basics
Has it been deleted from the file system but not from git?
Repo-map can't include C:\Users\jazzw\git\snippet\go\go-workshop-practical
Has it been deleted from the file system but not from git?
Scanning repo: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████| 1201/1201 [00:02<00:00, 544.12it/s]

Approximate context window usage for ollama/qwen2.5-coder:latest, in tokens:

$ 0.0000      463 system messages
$ 0.0000    7,921 repository map  use --map-tokens to resize
==================
$ 0.0000    8,384 tokens total
           24,384 tokens remaining in context window
           32,768 tokens max context window size
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /code

Aider v0.75.1
Model: ollama/qwen2.5-coder:latest with whole edit format
Git repo: .git with 1,201 files
Warning: For large repos, consider using --subtree-only and .aiderignore
See: https://aider.chat/docs/faq.html#can-i-use-aider-in-a-large-mono-repo
Repo-map: using 4096.0 tokens, auto refresh
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> /run mcpm-aider toom

error: unknown command 'toom'
Add 0.0k tokens of command output to the chat? (Y)es/(N)o [Yes]:
Added 1 line of output to the chat.
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
> What's wrong? Fix

It seems like the command mcpm-aider toom is not recognized. To help you further, I need more context about what you are trying to achieve with this
command. Could you please provide more details or specify the task you want to accomplish? Once I understand your request, I can suggest the appropriate
files that might need changes and then wait for your approval before making any updates.


Tokens: 10k sent, 80 received.
> /run mcpm-aider toolprompt

# Available Tools

When this prompt is loaded, always say to the user EXACTLY THIS:
"I am aware of MCP Tools!"

## *Usage*
If you decide to call a function of a tool, please execute this bash command.
**Do not include unescaped ' or line breaks in <parameters as jsonstring>, because it is passed as a cli argument oneliner!**

```bash
mcpm-aider call <tool> <function> '<parameters as jsonstring>'
```

## *Example*

```bash
mcpm-aider call @calclavia/mcp-obsidian read_notes '{"paths": ["path/to/notes"]}'
```
## tool: mcpm


**ERROR**: spawn mcpm ENOENT

Add 0.2k tokens of command output to the chat? (Y)es/(N)o [Yes]:
Added 20 lines of output to the chat.
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
>
```

- 測試了一下，請 `aider` 用 `mcpm` 做 `websearch` 還真的有模有樣的。雖然我覺得寫出來的 code 有點怪怪的，就不紀錄在這邊。
- 初步看起來可行，如果安裝 `@RamXX/mcp-tavily` 應該有機會可以讓 `aider` 做 web search

```
Tavily (@RamXX/mcp-tavily)
  A Model Context Protocol server enabling AI-powered web searches, direct Q&A, and recent news retrieval using Tavily's API.
  #AI #web-search #MCP-server
```