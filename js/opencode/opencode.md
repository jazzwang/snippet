# opencode

- Git Repo
  - https://github.com/sst/opencode

## 2025-10-08

- https://opencode.ai/zen

## 2026-02-04

- 緣起：
  - 不想要被 Claude Code / Gemini CLI 單一模型綁架，
  想起了 HuggingFace 推薦的 OpenCode
- 看了這篇，更覺得該動手試試看：
  - https://hackmd.io/@BASHCAT/B1zktAnNZx
- 高見龍推薦可以在加上 superpowers 來強制套用一些「好習慣」
  - https://kaochenlong.com/ai-superpowers-skills

## 2026-02-23

- 生態系
  - https://opencode.ai/docs/ecosystem/
    - https://github.com/darrenhinde/OpenAgentsControl
    - https://github.com/Cluster444/agentic
    - https://github.com/zenobi-us/opencode-skillful
  - https://www.opencode.cafe/
    - 在這個網站可以查到 opencode 的 plugin, slash command, theme, MCP server, Tools.
    - source code - https://github.com/R44VC0RP/opencode.cafe
    - 例如：
      - https://www.opencode.cafe/plugin/opencode-tokenscope
      - 這個 Tool 可以統計/最佳化 token 使用量
      - https://github.com/ramtinJ95/opencode-tokenscope
- Ollama 整合 opencode
  - https://github.com/p-lemonish/ollama-x-opencode
  - https://www.reddit.com/r/opencodeCLI/comments/1ngd18t/anyone_using_opencode_with_ollama/

## 2026-02-25

- 感興趣的 opencode plugin
  - opencode-browser
    - https://www.opencode.cafe/plugin/opencode-browser
    - https://github.com/different-ai/opencode-browser
  - opencode-lmstudio
    - https://www.opencode.cafe/plugin/lmstudio
    - https://github.com/agustif/opencode-lmstudio
  - oh-my-opencode
    - https://www.opencode.cafe/plugin/oh-my-opencode
    - https://github.com/code-yeongyu/oh-my-opencode
    - README 介紹中提到 
    > Anthropic blocked OpenCode because of us. Yes this is true. They want you locked in. Claude Code's a nice prison, but it's still a prison.
  - opencode-md-table-formatter
    - https://www.opencode.cafe/plugin/opencode-md-table-formatter
    - https://github.com/franlol/opencode-md-table-formatter
  - opencode-websearch-cited
    - https://www.opencode.cafe/plugin/opencode-websearch-cited
    - https://github.com/ghoulr/opencode-websearch-cited
  - agentic
    > An agentic workflow tool that provides context engineering support for opencode
    - https://github.com/Cluster444/agentic
  - OpenAgentsControl
    > AI agent framework for plan-first development workflows with approval-based execution. Multi-language support (TypeScript, Python, Go, Rust) with automatic testing, code review, and validation built for OpenCode
    - https://github.com/darrenhinde/OpenAgentsControl
    - 感覺有點像高見龍推薦的 superpower
- 更多 opencode 生態系
  - https://github.com/awesome-opencode/awesome-opencode

## 2026-04-06

- 緣起：想要改用 `scoop install opencode`
- 搜尋如何反安裝，查到可以用 `opencode uninstall`
```bash
@jazzwang ➜ /workspaces/snippet (master) $ opencode uninstall

                                   ▄
  █▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
  █  █ █  █ █▀▀▀ █  █ █    █  █ █  █ █▀▀▀
  ▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀

┌  Uninstall OpenCode
│
●  Installation method: curl
│
│  The following will be removed:
│
●    ✓ Data: ~/.local/share/opencode (28.2 MB)
│
●    ✓ Cache: ~/.cache/opencode (4.2 MB)
│
●    ✓ Config: ~/.config/opencode (4.2 MB)
│
●    ✓ State: ~/.local/state/opencode (2.6 KB)
│
●    ✓ Binary: ~/.opencode/bin/opencode
│
●    ✓ Shell PATH in ~/.bashrc
│
◆  Are you sure you want to uninstall?
│  ○ Yes / ● No
```
- 若是使用 `scoop install opencode` 的話，會顯示以下結果
```bash
~/git/snippet/js/opencode$ opencode uninstall
Performing one time database migration, may take a few minutes...
Database migration complete.

                                   ▄
  █▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
  █  █ █  █ █▀▀▀ █  █ █    █  █ █  █ █▀▀▀
  ▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀

┌  Uninstall OpenCode
│
●  Installation method: scoop
│
│  The following will be removed:
│
●    ✓ Data: ~\.local\share\opencode (189.3 KB)
│
●    ✓ Cache: ~\.cache\opencode (1.7 MB)
│
●    ✓ Config: ~\.config\opencode (0 B)
│
●    ✓ State: ~\.local\state\opencode (0 B)
│
●    ✓ Package: scoop uninstall opencode
│
◆  Are you sure you want to uninstall?
│  ○ Yes / ● No
└
```
- 大致看起來，需要備份的主要是 `~\.local\share\opencode` 跟 `~\.config\opencode`

### opencode uninstall

To uninstall OpenCode, use the CLI command opencode uninstall. Alternatively, remove it via npm using `npm uninstall -g opencode-ai`. For a complete removal, manually delete the configuration folder, typically located at `~/.config/opencode` on Linux/macOS or within `%USERPROFILE%\.config\opencode\` on Windows.

**Uninstallation Methods**

- **CLI Method:** Run `opencode uninstall` in your terminal to remove the application and associated files.
- **NPM Method:** Run `npm uninstall -g opencode-ai`.
- **Manual Removal (Windows):** Open command prompt as admin, run `where opencode` to find the path, and delete the `opencode` folder.
- **Manual Removal (macOS/Linux):** Run `rm -rf ~/.config/opencode` and `rm -rf ~/.opencode`.

**Cleaning Up**

To ensure a complete removal, you may also need to:

- Remove plugins by editing `~/.config/opencode/opencode.jsonc`.
- Remove local skills using `npx skills remove [skill-name]`.

### 新增 `superpower` plugin

- 參考：
  - https://github.com/obra/superpowers/blob/main/.opencode/INSTALL.md
- 修改 `~/.config/opencode/opencode.json`
```diff
--- opencode.json.old   2026-03-24 21:09:38.000000000 +0800
+++ opencode.json       2026-04-06 23:13:18.815155600 +0800
@@ -1,18 +1,26 @@
 {
   "$schema": "https://opencode.ai/config.json",
+  "plugin": [
+    "superpowers@git+https://github.com/obra/superpowers.git"
+  ],
   "provider": {
     "ollama": {
       "models": {
+        "gemma4:e4b": {
+          "_launch": true,
+          "name": "gemma4:e4b"
+        },
         "qwen25-coder:7b": {
           "_launch": true,
           "name": "qwen25-coder:7b"
         },
-        "qwen3:8b": {
+        "qwen35:9b": {
           "_launch": true,
-          "name": "qwen3:8b"
+          "name": "qwen35:9b"
         }
       },
-      "name": "Ollama (local)",
+      "name": "Ollama",
       "npm": "@ai-sdk/openai-compatible",
       "options": {
         "baseURL": "http://127.0.0.1:11434/v1"
```

### 新增 `devpost-curriculum` plugin

```diff
--- opencode.json.1     2026-04-06 23:24:45.128471300 +0800
+++ opencode.json       2026-04-06 23:21:06.666461300 +0800
@@ -1,7 +1,8 @@
 {
   "$schema": "https://opencode.ai/config.json",
   "plugin": [
-    "superpowers@git+https://github.com/obra/superpowers.git"
+    "superpowers@git+https://github.com/obra/superpowers.git",
+    "devpost-curriculum@git+https://github.com/challengepost/devpost-curriculum.git"
   ],
   "provider": {
     "ollama": {
```
- 看起來沒有生效，因為讀了其他 opencode plugin 都有定義 `package.json`，所以 `@git+https://` 前面放的應該是 `package name`
- 改用以下步驟測試：
```bash
/tmp$ mkdir devpost
/tmp$ cd devpost/
/tmp/devpost$ mkdir .opencode
/tmp/devpost$ cd .opencode/
/tmp/devpost/.opencode$ rsync -avzrP ~/git/devpost-curriculum/plugins/hackathon-in-a-plugin/skills .
/tmp/devpost/.opencode$ tree
.
└── skills
    ├── build
    │   └── SKILL.md
    ├── checklist
    │   └── SKILL.md
    ├── hackathon-guide
    │   ├── references
    │   │   ├── eval-rubric.md
    │   │   ├── prd-guide.md
    │   │   └── spec-patterns.md
    │   ├── SKILL.md
    │   └── templates
    │       ├── checklist-template.md
    │       ├── learner-profile-template.md
    │       ├── prd-template.md
    │       ├── reflection-template.md
    │       ├── scope-template.md
    │       └── spec-template.md
    ├── iterate
    │   └── SKILL.md
    ├── onboard
    │   └── SKILL.md
    ├── prd
    │   └── SKILL.md
    ├── reflect
    │   └── SKILL.md
    ├── scope
    │   └── SKILL.md
    └── spec
        └── SKILL.md

13 directories, 18 files
/tmp/devpost/.opencode$ cd ..
/tmp/devpost$ opencode
                                   ▄
  █▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
  █  █ █  █ █▀▀▀ █  █ █    █  █ █  █ █▀▀▀
  ▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀

  Session   Onboard: Learner wellness and scope kickoff
  Continue  opencode -s ses_29c5a0976ffeTqUWXXltTiDqQp

/tmp/devpost$ ls
docs  process-notes.md
```

## 2026-04-21

- https://opencodeguide.com/
  - Master your local coding agent.
  > OpenCode is the offline-first, plugin-driven alternative to cloud coding assistants. Learn how to run it with Ollama, connect via Model Context Protocol (MCP), and integrate with Neovim.

## 2026-06-06

- OpenCode基本功 EP01：免費 AI Agent 啟手式_免費仔必看！三師爸手把手教你用開源OpenCode打造專屬AI Agent！
- https://www.youtube.com/watch?v=lB7Pl8Dl_Rw
```
還在為了每個月20美金的AI訂閱費傷腦筋，又覺得傳統生成式AI不夠聰明、無法應付連續任務嗎 ？
這支影片將顛覆你對工具使用的既定想像，由三師爸現場實測，手把手帶你跨入免費AI Agent的全新世界 ！  
Harness Engineering架構解密：用電腦硬體妙喻AI Agent，帶你秒懂作業系統、CPU與記憶體的協同原理，不再只盲目追求單一模型能力 。  
OpenCode免費用法實操：現場示範如何下載與設定開源Harness桌面版，並透過OpenRouter完美、安全地串接雲端免費頂級模型 。  
多模態任務自動化工作流：實測串接NotebookLM與聯網搜尋，讓免費AI分身幫你搞定日常瑣碎的行政與勞務工作 。  
想知道如何用最低成本發揮AI的最大威力、建立流暢的自動化工作流嗎 ？
立刻觀看影片，並記得訂閱頻道、開啟小鈴鐺，在評論區留下你的測試心得，讓我們一起解鎖最強生產力！
```
- 快轉看了一下，這個主要是介紹 OpenCode Desktop 版本。至於串接 NotebookLM 是透過 MCP
- 懶人包路徑: https://github.com/mathruffian-dot/claude-code-lazy-packs

```bash
◇  Security Risk Assessments ─────────────────────────────────────────────────╮
│                                                                             │
│                          Gen               Socket            Snyk           │
│  claude-code-lazy-packs  Safe              3 alerts          Critical Risk  │
│                                                                             │
│  Details: https://skills.sh/mathruffian-dot/claude-code-lazy-packs          │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────╯
│
◇  Proceed with installation?
│  No
└  Installation cancelled
```
* 這些 Skill 有一個嚴重 Snyk 的資安風險，先緩緩～
- 另外注意到有用到一個 Exa Web Search
  - https://exa.ai/
- 在懶人包裡面找不到對應的關鍵字，或許是其他相依的工具安裝的。

## 2026-06-11

<table><tr style="background-color:lightgreen;"><td>Tool:</td><td>
Google Search - AI Mode
</td></tr><tr style="background-color:lightyellow;"><td>Q:</td><td>
opencode 支援排程執行工作嗎
</td></tr><tr><td>A:</td><td>

是的，OpenCode 支援排程執行工作。 它身為一個靈活的開源 AI 編碼代理，除了傳統在終端機與開發者即時協作（TUI 模式）外，也能透過多種官方或社群擴充方式來進行週期性與自動化的排程任務。 [1, 2, 3, 4, 5] 
以下是 OpenCode 實現排程執行的三種主要方式：

## 1. 透過 GitHub Actions 定時觸發 (官方支援)

OpenCode 整合了 GitHub 自動化工作流程。你可以在專案中建立 .github/workflows/opencode-scheduled.yml 檔案，利用標準的 Cron 語法 定時啟動 OpenCode 執行特定任務（例如：每週一早上自動審查程式碼並建立 Issue）。 [5, 6] 
（此處省略具體的 YAML 設定範例內容，使用者可在原參考文檔中找到完整代碼。） [5] 

## 2. 使用社群擴充套件 opencode-scheduler

在 OpenCode 生態系中，[opencode-scheduler](https://opencode.ai/docs/zh-tw/ecosystem/) 套件支援透過 Cron 語法，整合底層系統（如 Mac 的 launchd 或 Linux 的 systemd）在本地進行定時排程。 [2] 

## 3. CLI 搭配系統工具

利用 OpenCode 強大的 命令列介面 (CLI)，可將 opencode --prompt "任務內容" 指令封裝為 Shell 腳本，並搭配系統原生工具（如 Windows 工作排程器、macOS/Linux 的 crontab）來執行任務。 [7] 

若需更自主的長駐自動化，可搭配 OpenClaw。如有具體應用情境（本地或雲端、執行任務類型），可進一步提供更精確的設定建議。 [3] 

[1] [https://opencode.ai](https://opencode.ai/zht)
[2] [https://opencode.ai](https://opencode.ai/docs/zh-tw/ecosystem/)
[3] [https://www.meta-intelligence.tech](https://www.meta-intelligence.tech/insight-openclaw-opencode)
[4] [https://www.webdong.dev](https://www.webdong.dev/zh-tw/shortpost/opencode/)
[5] [https://opencode.ai](https://opencode.ai/docs/zh-tw/github/)
[6] [https://opencode.ai](https://opencode.ai/docs/zh-tw/github/)
[7] [https://www.runoob.com](https://www.runoob.com/opencode/opencode-cli.html)

</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
<tr style="background-color:lightyellow;"><td>Q:</td><td>
</td></tr><tr><td>A:</td><td>
</td></tr>
</table>
