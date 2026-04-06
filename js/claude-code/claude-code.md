# Claude Code

> Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows - all through natural language commands.

- Git Repo:
  - https://github.com/anthropics/claude-code
- Document:
  - https://docs.anthropic.com/s/claude-code
  - https://docs.anthropic.com/en/docs/claude-code/overview
  - https://docs.anthropic.com/en/docs/claude-code/quickstart
- News:
  - 2025-02-25: 發佈 Claude Code
    - https://www.anthropic.com/news/claude-3-7-sonnet
  - 2025-04-18: Claude Code: Best practices for agentic coding
    - https://www.anthropic.com/engineering/claude-code-best-practices

## 2025-08-26

- 安裝：
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```

## 2025-08-27

- 緣起：
  - 可以讓 Claude Code 支援其他 Local LLM 嗎？
- 解法一：（已失效）
  - https://www.shawnmayzes.com/product-engineering/running-claude-code-with-local-llm/
- 解法二： AnyClaude
  - https://github.com/coder/anyclaude
- 關於 Claude Code 跟 Aider 的一些比較跟討論
  - https://news.ycombinator.com/item?id=43254351
    - https://github.com/ai-christianson/RA.Aid (可以整合 Aider)

## 2025-10-09

- 緣起：
  - 因為看到 Github Spec Kit 支援 Claude Code, Gemini CLI 卻沒有支援 Aider
  - 回到先前想研究 Claude Code 是否支援其他 Local LLM
- 解法三：Term-Code
  - https://github.com/Ishuin/term-code
  - 2025-03-08
    - From Claude to Ollama: How I Hacked Together an AI Coding Assistant in 2 Days (With Zero TypeScript Knowledge)
    - https://medium.com/@ishu.kumars/from-claude-to-ollama-how-i-hacked-together-an-ai-coding-assistant-in-2-days-with-zero-typescript-712191d6f66e
  - 2025-03-09
    - From Claude to Ollama: Building a Local AI Coding Assistant
    - https://dev.to/ishu_kumar/from-claude-to-ollama-building-a-local-ai-coding-assistant-3c46
- 解法四：
  - https://github.com/musistudio/claude-code-router
- 另類思路：告訴 Claude 用 Ollama + Local LLM 來生成 Web App
  - 2025-06-30
    - From Prompt to Production: Vibe Coding Local AI Apps with Claude + Ollama
    - https://blog.greenflux.us/from-prompt-to-production-vibe-coding-local-ai-apps-with-claude-ollama/

## 2026-03-28

- 測試 Ollama 整合 Claude Code
  - https://docs.ollama.com/integrations/claude-code
- 已安裝 Claude Code
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
- 測試使用 kimi-k2.5:cloud 但看起來要 ollama 訂閱，使用本機的 `qwen3:8b` 抱怨找不到 `git-bash`
```bash
~/git/snippet$ ollama launch claude --model kimi-k2.5:cloud
Warning: ignoring --model kimi-k2.5:cloud because cloud is disabled
~/git/snippet$ ollama launch claude

Launching Claude Code with qwen3:8b...
Claude Code on Windows requires git-bash (https://git-scm.com/downloads/win). If installed but not in PATH, set environment variable pointing to your bash.exe, similar to: CLAUDE_CODE_GIT_BASH_PATH=C:\Program Files\Git\bin\bash.exe
Error: exit status 1
```
- 切到 `cmd` 加入環境變數
```cmd
C:\Users\jazzw>where bash
C:\Users\jazzw\scoop\shims\bash.exe
C:\Users\jazzw\AppData\Local\Microsoft\WindowsApps\bash.exe

C:\Users\jazzw>setx CLAUDE_CODE_GIT_BASH_PATH "C:\Users\jazzw\scoop\shims\bash.exe"

SUCCESS: Specified value was saved.
```

## 2026-04-06

- 測試 `ollama launch claude --model gemma4:e4b` 並將環境變數存成檔案
```bash
~/git/snippet/js/claude-code$ ollama launch claude --model gemma4:e4b

Launching Claude Code with gemma4:e4b...
╭─── Claude Code v2.1.92 ────────────────────────────────────────────────────────────────────────────────╮
│                                    │ Tips for getting started                                          │
│            Welcome back!           │ Run /init to create a CLAUDE.md file with instructions for Claude │
│                                    │ ───────────────────────────────────────────────────────────────── │
│               ▐▛███▜▌            │ Recent activity                                                   │
│              ▝▜█████▛▘          │ No recent activity                                                │
│                ▘▘ ▝▝               │                                                                   │
│                                    │                                                                   │
│   gemma4:e4b · API Usage Billing   │                                                                   │
│    ~\git\snippet\js\claude-code    │                                                                   │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────╯

! env | sort -n | tee ollama_launch_claude

❯ /stats

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
   Status   Config   Usage   Stats

    Overview   Models


      Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr
      ····················································
  Mon ··················································▒▓
      ···················································
  Wed ···················································
      ···················································
  Fri ···················································
      ···················································

      Less ░ ▒ ▓ █ More

  All time · Last 7 days · Last 30 days

  Favorite model: gemma4:e4b      Total tokens: 81.1k

  Sessions: 9                     Longest session: 1h 3m 39s
  Active days: 3/10               Longest streak: 2 days
  Most active day: Apr 6          Current streak: 2 days

  You've used ~2x more tokens than A Christmas Carol

    ↓ stats · r to cycle dates · ctrl+s to copy
```
- 比對沒有執行 `ollama launch claude` 的環境變數
```bash
~/git/snippet/js/claude-code$ ls
claude-code.md  ollama_launch_claude
~/git/snippet/js/claude-code$ env | sort -n > git-bash
~/git/snippet/js/claude-code$ diff -Naur git-bash ollama_launch_claude
```
```diff
--- git-bash    2026-04-06 22:29:21.132186600 +0800
+++ ollama_launch_claude        2026-04-06 22:24:03.622063000 +0800
@@ -3,16 +3,29 @@
 ACSvcPort=17532
 AIDER_EDITOR=code --wait
 ALLUSERSPROFILE=C:\ProgramData
+ANTHROPIC_API_KEY=
+ANTHROPIC_AUTH_TOKEN=ollama
+ANTHROPIC_BASE_URL=http://127.0.0.1:11434
+ANTHROPIC_DEFAULT_HAIKU_MODEL=gemma4:e4b
+ANTHROPIC_DEFAULT_OPUS_MODEL=gemma4:e4b
+ANTHROPIC_DEFAULT_SONNET_MODEL=gemma4:e4b
 APPDATA=C:\Users\jazzw\AppData\Roaming
+CLAUDE_CODE_ATTRIBUTION_HEADER=0
+CLAUDE_CODE_ENTRYPOINT=cli
+CLAUDE_CODE_EXECPATH=C:\Users\jazzw\scoop\apps\nvm\current\nodejs\nodejs\node.exe
 CLAUDE_CODE_GIT_BASH_PATH=C:\Users\jazzw\scoop\shims\bash.exe
+CLAUDE_CODE_SUBAGENT_MODEL=gemma4:e4b
+CLAUDECODE=1
 CommonProgramFiles(x86)=C:\Program Files (x86)\Common Files
 COMMONPROGRAMFILES=C:\Program Files\Common Files
 CommonProgramW6432=C:\Program Files\Common Files
 COMPUTERNAME=JAZZBOOK
 COMSPEC=C:\WINDOWS\system32\cmd.exe
+COREPACK_ENABLE_AUTO_PIN=0
 DriverData=C:\Windows\System32\Drivers\DriverData
 EnableLog=INFO
 EXEPATH=C:\Users\jazzw\scoop\apps\git\2.53.0.2\bin
+GIT_EDITOR=true
 GIT_INSTALL_ROOT=C:\Users\jazzw\scoop\apps\git\current
 HISTTIMEFORMAT=[%m/%d %T]
 HOME=/c/Users/jazzw
@@ -30,14 +43,16 @@
 LOGONSERVER=\\JAZZBOOK
 LS_COLORS=rs=0:di=01;34:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:mi=00:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arc=01;31:*.arj=01;31:*.taz=01;31:*.lha=01;31:*.lz4=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.tzo=01;31:*.t7z=01;31:*.zip=01;31:*.z=01;31:*.dz=01;31:*.gz=01;31:*.lrz=01;31:*.lz=01;31:*.lzo=01;31:*.xz=01;31:*.zst=01;31:*.tzst=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.alz=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.cab=01;31:*.wim=01;31:*.swm=01;31:*.dwm=01;31:*.esd=01;31:*.jpg=01;35:*.jpeg=01;35:*.mjpg=01;35:*.mjpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.webp=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.m4a=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.oga=00;36:*.opus=00;36:*.spx=00;36:*.xspf=00;36:
 MSYSTEM=MINGW64
+NoDefaultCurrentDirectoryInExePath=1
 NUMBER_OF_PROCESSORS=16
 NVM_HOME=C:\Users\jazzw\scoop\apps\nvm\current
 NVM_SYMLINK=C:\Users\jazzw\scoop\persist\nvm\nodejs\nodejs
-OLDPWD=/c/Users/jazzw/git/snippet
+OLDPWD=C:/Users/jazzw/git/snippet
 OLLAMA_API_BASE=http://127.0.0.1:11434
 OneDrive=C:\Users\jazzw\OneDrive
 OS=Windows_NT
+OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
 PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
 PLINK_PROTOCOL=ssh
 PROCESSOR_ARCHITECTURE=AMD64
@@ -48,7 +63,7 @@
 ProgramFiles(x86)=C:\Program Files (x86)
 PROGRAMFILES=C:\Program Files
 ProgramW6432=C:\Program Files
-PS1=\[\e]0;\u@\h: \w\a\]\[\033[01;34m\]\w\[\033[00m\]\$
+PROMPT=$P$G
 PSModulePath=C:\Users\jazzw\scoop\modules;C:\Users\jazzw\Documents\WindowsPowerShell\Modules
 PUBLIC=C:\Users\Public
 PWD=/c/Users/jazzw/git/snippet/js/claude-code
@@ -58,7 +73,8 @@
 SFTP_HOST=sftp2.dmotorworks.com
 SFTP_PASSWD=niko212
 SFTP_USER=cust_demo
-SHLVL=1
+SHELL=/c/Users/jazzw/scoop/shims/bash.exe
+SHLVL=2
 SYSTEMDRIVE=C:
 SYSTEMROOT=C:\WINDOWS
 TEMP=/tmp
```
- 透過這個觀察結果，設定以下環境變數，目標是讓 Claude Code 使用 OpenCode Zen 的模型
```bash
ANTHROPIC_API_KEY=
ANTHROPIC_AUTH_TOKEN=sk-xxxxxxxxxxx ## 這個換成真實的 OpenCode Zen Token
## https://opencode.ai/docs/zen/#endpoints
ANTHROPIC_BASE_URL=https://opencode.ai/zen/v1/chat/completions
ANTHROPIC_DEFAULT_HAIKU_MODEL=minimax-m2.5-free
ANTHROPIC_DEFAULT_OPUS_MODEL=minimax-m2.5-free
ANTHROPIC_DEFAULT_SONNET_MODEL=minimax-m2.5-free
CLAUDE_CODE_ATTRIBUTION_HEADER=0
CLAUDE_CODE_ENTRYPOINT=cli
CLAUDE_CODE_SUBAGENT_MODEL=minimax-m2.5-free
CLAUDECODE=1
COREPACK_ENABLE_AUTO_PIN=0
GIT_EDITOR=true
NoDefaultCurrentDirectoryInExePath=1
OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```
- 讓 Claude Code 使用 OpenCode Zen 的 MiniMax M2.5。不過實測結果有錯誤，沒辦法正常呼叫 OpenCode Zen 的模型。
```
╭─── Claude Code v2.1.92 ───────────────────────────────────────────────────────────────────────────────────────────╮
│                                               │ Tips for getting started                                          │
│                 Welcome back!                 │ Run /init to create a CLAUDE.md file with instructions for Claude │
│                                               │ ───────────────────────────────────────────────────────────────── │
│                    ▐▛███▜▌                    │ Recent activity                                                   │
│                   ▝▜█████▛▘                   │ No recent activity                                                │
│                     ▘▘ ▝▝                     │                                                                   │
│                                               │                                                                   │
│   minimax-m2.5-free[1m] · API Usage Billing   │                                                                   │
│           ~\git\snippet\js\openspec           │                                                                   │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

❯ /model
  ⎿  Kept model as minimax-m2.5-free (default)

! pwd
  ⎿  /c/Users/jazzw/git/snippet/js/openspec

❯ /plugin marketplace add https://github.com/challengepost/devpost-curriculum
  ⎿  Successfully added marketplace: devpost-curriculum

❯ /plugin install hackathon-in-a-plugin@devpost-curriculum
  ⎿  ✓ Installed hackathon-in-a-plugin. Run /reload-plugins to apply.

❯ /reload-plugins
  ⎿  Reloaded: 1 plugin · 0 skills · 5 agents · 0 hooks · 0 plugin MCP servers · 0 plugin LSP servers

❯ /exit
  ⎿  Goodbye!

❯ /hackathon-in-a-plugin:onboard

● There's an issue with the selected model (minimax-m2.5-free). It may not exist or you may not have access to it. Run /model to pick a different model.

❯ /context
  ⎿  Context Usage
     ⛀ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   minimax-m2.5-free
                           498/200k tokens (0%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶
                           Estimated usage by category
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛁ Skills: 498 tokens (0.2%)
                           ⛶ Free space: 166.5k (83.3%)
     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶   ⛝ Autocompact buffer: 33k tokens (16.5%)

     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶

     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶

     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶

     ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶ ⛶

     ⛶ ⛶ ⛶ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝

     ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝ ⛝

     Skills · /skills

     Plugin
     └ hackathon-guide: 107 tokens
     └ onboard: 42 tokens

❯ /copy
  ⎿  Copied to clipboard (22 characters, 1 lines)
     Also written to C:\Users\jazzw\AppData\Local\Temp\claude\response.md

❯ /copy 5
  ⎿  Only 1 assistant message available to copy

❯ /doctor
  ⎿  Claude Code diagnostics dismissed

❯ /config
  ⎿  Config dialog dismissed

❯ /agents
  ⎿  Agents dialog dismissed

❯ /copy 5
  ⎿  Only 1 assistant message available to copy

❯ /copy
  ⎿  Copied to clipboard (22 characters, 1 lines)
     Also written to C:\Users\jazzw\AppData\Local\Temp\claude\response.md

❯ /hackathon-in-a-plugin:onboard

● There's an issue with the selected model (minimax-m2.5-free). It may not exist or you may not have access to it. Run /model to pick a different model.

✻ Brewed for 1m 1s

❯ /hackathon-in-a-plugin:spec

● There's an issue with the selected model (minimax-m2.5-free). It may not exist or you may not have access to it. Run /model to pick a different model.

❯ /model
  ⎿  Set model to minimax-m2.5-free[1m]

❯ /hackathon-in-a-plugin:spec

● There's an issue with the selected model (minimax-m2.5-free[1m]). It may not exist or you may not have access to it. Run /model to pick a different model.
                                                                                                                                                   (\__/)
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────   ( ◉  ◉ )
❯                                                                                                                                                =(  ..  )=
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────   (")__(")
  ? for shortcuts                                                                                                                                   Soup
```