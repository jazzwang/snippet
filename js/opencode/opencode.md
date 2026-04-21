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
