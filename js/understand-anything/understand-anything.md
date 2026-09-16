# Understand Anything

> Graphs that teach > graphs that impress. Turn any code into an interactive knowledge graph you can explore, search, and ask questions about. Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.

- Git Repo
  - https://github.com/Lum1104/Understand-Anything
- Website
  - https://understand-anything.com/

## 2026-05-31

- Demo 看起來很適合拿來理解程式碼 (Legacy Code)
  - https://understand-anything.com/demo/
- Q: 背後需要相依特定 LLM?
- A:
  - 原生是 Claude Code Plugin，但 README.md 有提到 `install.sh opencode`
    所以應該可以適應不同的語言模型。

## 2026-09-16

- 參考：
  - 2026-06-03
    - 橫向對決：Understand-Anything vs. GitNexus vs. CodeGraph vs. graphify
    - https://altsol.tw/understand-anything-gitnexus-codegraph-comparison
  - 2026-06-01
    - 解構多智能體流水線：Understand-Anything 如何自動繪製程式碼知識地圖
    - https://altsol.tw/understand-anything-multi-agent-pipeline-architecture

> [!QUOTE]
> 如果痛點是「新人看不懂遺留系統」：選擇 `Understand-Anything`。它提供的互動式儀表板是最友好的學習入口。

## 實測

- 使用 `curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash -s pi` 安裝成 Pi 跟 OpenCode 都可以用的 Skill
```bash
~$ curl -fsSL https://raw.githubusercontent.com/Egonex-AI/Understand-Anything/main/install.sh | bash -s pi
→ Cloning https://github.com/Egonex-AI/Understand-Anything.git → /c/Users/jazzw/.understand-anything/repo
Cloning into 'C:/Users/jazzw/.understand-anything/repo'...
remote: Enumerating objects: 7743, done.
remote: Counting objects: 100% (450/450), done.
remote: Compressing objects: 100% (153/153), done.
remote: Total 7743 (delta 344), reused 297 (delta 297), pack-reused 7293 (from 3)
Receiving objects: 100% (7743/7743), 34.66 MiB | 1.26 MiB/s, done.
Resolving deltas: 100% (4801/4801), done.
→ Linking skills for pi (per-skill → /c/Users/jazzw/.agents/skills)
  ✓ /c/Users/jazzw/.agents/skills/understand → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand
  ✓ /c/Users/jazzw/.agents/skills/understand-chat → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-chat
  ✓ /c/Users/jazzw/.agents/skills/understand-dashboard → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-dashboard
  ✓ /c/Users/jazzw/.agents/skills/understand-diff → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-diff
  ✓ /c/Users/jazzw/.agents/skills/understand-domain → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-domain
  ✓ /c/Users/jazzw/.agents/skills/understand-explain → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-explain
  ✓ /c/Users/jazzw/.agents/skills/understand-figma → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-figma
  ✓ /c/Users/jazzw/.agents/skills/understand-knowledge → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-knowledge
  ✓ /c/Users/jazzw/.agents/skills/understand-onboard → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin/skills/understand-onboard
→ Linking universal plugin root
  ✓ /c/Users/jazzw/.understand-anything-plugin → /c/Users/jazzw/.understand-anything/repo/understand-anything-plugin

✓ Installed Understand-Anything for pi
  Restart your CLI or IDE to pick up the skills.
```
- 驗證：進入 `pi` 會看到多了 `understand, understand-chat, understand-dashboard, understand-diff,
understand-domain, understand-explain, understand-figma, understand-knowledge, understand-onboard` 這麼多新的 Skill
```bash
~$ pi
 pi v0.85.1
 escape interrupt · ctrl+c/ctrl+d clear/exit · / commands · ! bash · ctrl+o more
 Press ctrl+o to show full startup help and loaded resources.

 Pi can explain its own features and look up its docs. Ask it how to use or extend Pi.

[Skills]
  context7, docx, find-skills, grill-me, pdf, pptx, skill-creator, speak-human-tw, understand, understand-chat, understand-dashboard, understand-diff,
understand-domain, understand-explain, understand-figma, understand-knowledge, understand-onboard, xlsx

[Extensions]
  pi-opencode-zen, pi-web-access


────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
~
$0.000 (sub) 0.0%/1.0M (auto)                                                                                        (github-copilot) gpt-5.3-codex • medium
```