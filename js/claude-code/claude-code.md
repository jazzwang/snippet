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

- some reference regarding those environment variables:
  - COREPACK_ENABLE_AUTO_PIN should default to 0 #485
    - https://github.com/nodejs/corepack/issues/485

## 2026-04-07

### 不懂程式碼也能當開發者？Claude Code 顛覆 AI 應用的 5 個驚人發現

- https://www.youtube.com/watch?v=kos_OsnuV24
> 這段影片旨在為無編程背景的初學者揭開 Claude Code 的神秘面紗，強調它不僅是開發者的工具，更是人人皆可使用的 AI 構建器。作者建議避開複雜的終端安裝，優先選擇桌面應用程式以整合聊天、協作與編碼功能，並透過輸入大白話提示詞來自動生成網頁或應用程式。核心教學涵蓋了利用 Opus 與 Sonnet 模型進行任務分配、透過截圖輔助設計，以及建立 claude.md 檔案來提供深層上下文的策略。最後，影片強調了 **氛圍編程（Vibe Coding）** 的疊代邏輯，並展示如何透過 MCP 插件與技能系統連接外部數據，實現從創意到產品的自動化轉化。

#### 引言：被「Code」這個詞嚇跑的人，正在錯過最強大的工具

在數位轉型的浪潮中，許多人一看到「Claude Code」這個名字，便會下意識地被「Code」這個詞勸退，想像中那是充滿冷冽終端機指令、只有工程師才能踏入的禁地。然而，這種心理畏懼正讓你與當前最具顛覆性的生產力工具失之交臂。這個名字其實是一個美麗的誤會，它隱藏了一個足以賦予平庸個體「數位超能力」的真相。

事實上，Claude Code 並非傳統意義上的程式編輯器，而是一個能讓任何人用「大白話」就能構建產品的 AI 引擎。它解構了長久以來將創意與執行隔絕的技術高牆，讓那些原本深藏於大腦中的點子，無需經過複雜的轉譯，就能直接在現實世界中落地。

#### 重點一：這不是程式編輯器，而是你的個人 AI 構建工廠

對於非技術背景的用戶來說，Claude Code 的出現標誌著「工具民主化」的終極階段。它不再只是在聊天視窗裡給你一段文字，而是實實在在地在你的電腦文件夾中「創造」物理文件。無論是一個美觀的產品落地頁、一套內部自動化工具，還是一個可視化的數據儀表板，它都能一手包辦。

更令人振奮的是，它支持「氛圍編程（Vibe Coding）」的概念：你只需要描述你想要的感覺和功能，AI 就會負責處理底層的邏輯架構。透過連接 Google 雲端硬碟或 Slack，它能跨平台存取數據，讓 AI 具備真正的執行力。

「你可以把它看作是一個可以實際給你創造東西的 AI 構建器，而你只需要用最簡單的大白話輸入你的要求。」

#### 重點二：桌面 App 才是最強形態，三位一體的效率神器

雖然 Claude Code 提供多種安裝方式，但真正能發揮「數位轉型專家」威力的，莫過於適配 Mac 與 Windows 的桌面端 App。這個設計不僅僅是為了方便，更是為了解決工作流的割裂感。在桌面版中，Claude 展現了「三位一體」的效率架構：

-   **Claude Chat（思考）：** 傳統的對話窗口，用於初步發想、文案撰寫與文件上傳。
-   **Claude Cowork（協作）：** 你的 AI 代理人（Agent），專注於協助執行跨應用的具體任務。
-   **Claude Code（構建）：** 核心構建功能，直接在本地環境執行開發與應用生成。

這種一站式的設計，讓用戶從點子萌芽（Chat）到細節輔助（Cowork），最後到產品落地（Code），都能在同一個介面中完成，徹底消除工具切換帶來的認知負荷。

#### 重點三：「計畫模式」：AI 把技術術語講成大白話

Claude Code 最能建立用戶信任的功能，莫過於其獨特的運作模式切換。對於非專業人士，AI 的決策過程往往像個「黑盒子」，而「計畫模式（Plan Mode）」正是打開黑盒子的鑰匙。

-   **始終詢問：** 謹慎派首選，每一步修改都需獲得用戶點頭。
-   **自動編輯：** 追求速度的默認模式，AI 會根據指令直接更動文件。
-   **計畫模式（Plan Mode）：** AI 在動手前會先撰寫一份詳盡的計畫書，將複雜的架構、顏色方案與動畫邏輯，翻譯成聽得懂的大白話。

**深度點評：** 這不只是功能，更是一種「信任機制」。透過計畫模式，用戶能在 AI 動手前進行「健康檢查（Sanity Check）」，如果發現顏色不對或邏輯有誤，在執行前就能即時否決。這種透明性讓非技術用戶也能掌控複雜項目的進度。

#### 重點四：別追求一蹴而就，迭代才是「氛圍編程」的真諦

在使用 AI 構建產品時，必須放棄「一次指令就完美」的幻想。真正的「氛圍編程」高手，懂得將 AI 視為一名需要溝通的初級夥伴，透過不斷的迭代來打磨成品。

**迭代優化的專業路徑：**

1.  **視覺參考：** 上傳一張你喜歡的網站截圖，讓 AI 捕捉品牌色調與設計品味，而非盲目猜測。
2.  **模型切換戰術：** 關鍵在於「先重後輕」。首版構建或複雜架構建議使用 **Opus 4.6**（重裝武力，完成度最高）；後續的微調與細部修改則切換到 **Sonnet**（輕裝快遞，節省積分）。
3.  **局部精準微調：** 利用內建工具選取特定元素（例如將兩行標題縮減為一行），進行精確點對點修改。

「好的成品通常是需要一點點迭代，你提出你的修改要求，查看 Claude 的輸出結果，然後繼續提出後續的指令。」

#### 重點五：`claude.md` 是賦予 AI 靈魂的「上下文祕笈」

若想讓 Claude Code 產出的內容不只是冷冰冰的代碼，而是具備你的風格與靈魂，`claude.md` 就是那份不可或缺的「心法」。這份文件定義了 AI 的行動準則，確保它能理解你的工作細節。

**高階技巧：** 不要自己手寫這份文件。建議在 Claude Chat 中發起一場「面試」，讓 AI 針對你的頻道或項目主動向你提問，最後再將對話轉化為 Markdown 格式存入 `claude.md`。

`**claude.md**` **應包含的關鍵要素：**

-   **定位與差異化：** 你的核心價值與競爭優勢。
-   **受眾畫像：** 產品是為誰而生？
-   **語言風格：** 專業、活潑還是冷幽默？
-   **禁用詞與寫作框架：** 哪些地雷不能踩？
-   **專案背景：** 例如抓取最新 AI 新聞的特定篩選標準。

#### 結語：從一件小事開始，構建你的 AI 體系

Claude Code 的出現，標誌著個人開發者時代的全面降臨。技術門檻不再是創新的枷鎖，而是一條通往想像力的捷徑。你不必具備高深的編程背景，只需要從一件小事開始：可能是做一個簡單的「午餐隨機選擇器」，或是一個屬於你自己的活動宣傳頁，在與 AI 互動的過程中，你會重新發現創造的樂趣。

當技術不再是創新的阻礙，我們與理想產品之間的距離，僅僅取決於我們如何與 AI 溝通。

**當技術門檻徹底消失後，唯一限制我們的是否只剩想像力？**