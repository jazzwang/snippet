# oh-my-openagent (was `oh-my-opencode`)

> omo; the best agent harness - previously oh-my-opencode

- Git Repo
  - https://github.com/code-yeongyu/oh-my-openagent
- Website
  - https://ohmyopenagent.com/

## 2026-05-15

### 實測

- 安裝步驟還蠻單純的，就是改 `~/.config/opencode/opencode.json`

>  [05/15 15:49:30] vi ~/.config/opencode/opencode.json

```diff
~/.config/opencode$ diff -Naur opencode.json.1 opencode.json
--- opencode.json.1     2026-04-06 23:24:45.128471300 +0800
+++ opencode.json       2026-05-15 15:51:56.245193400 +0800
@@ -1,7 +1,7 @@
 {
   "$schema": "https://opencode.ai/config.json",
   "plugin": [
-    "superpowers@git+https://github.com/obra/superpowers.git"
+    "oh-my-openagent"
   ],
   "provider": {
     "ollama": {
```

- 重新啟動 opencode 以後，會發現原本的兩個 Agent (`Plan` 跟 `Build`) 變成四個 Agent ，加了三個 MCP
- 初步跑了 `/skill-creator`，覺得 token 用量相對兇(48,076 token, 23% used, MiniMax M2.5 Free | OpenCode Zen)。