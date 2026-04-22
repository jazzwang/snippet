# remotion

> Make videos programmatically with React

Tags: #animation #GIF

- Github Repo:
  - https://github.com/remotion-dev/remotion
- Document:
  - https://www.remotion.dev/docs/

## 2024-12-04

- ( 2024-12-04 23:00:39 )
- 緣起：
  - 原本想找 Webassembly 的專案，想起 [bolt.new](https://github.com/stackblitz/bolt.new)
  - 結果 [bolt.new](https://github.com/stackblitz/bolt.new) 是用 [WebContainer](https://webcontainers.io/) (非 Open Source)
  - 在 [bolt.new](https://github.com/stackblitz/bolt.new) 的界面上看到一個 `Code a video with Remotion`
  - 挺有趣的，居然用 React.js 來產生 Video
- 一些 Example Showcase
  - https://remotion.dev/showcase
- Get started 還蠻簡單的，就用 `npx`
```bash
npx create-video@latest
```

## 2026-04-21 (1)

- 參考：
  - https://www.remotion.dev/prompts/travel-route-on-map-with-3d-landmarks
- 實驗：用 `OpenCode` 加上 `Remotion Best Practive Skill`，使用 `MiniMax M2.5 Free` 模型，只給簡單的 Prompt `use remotion best practices. make a new composition and add a map and zoom out of LA while staying focused on it. once done, animate a line from LA to NY and make the camera follow it.`
- 結果：可以用 Remotion Studio 預覽，但沒辦法正常匯出 MP4 或 GIF
- 對話：[la-to-ny.md](la-to-ny.md)
- 學到：
  - 創建空的專案 `la-to-ny`
  ```bash
  npx create-video@latest --yes --blank la-to-ny
  ```
  - 檢查 TypeScript -- `npx tsc --noEmit`
  ```json
  {
    "command": "npx tsc --noEmit",
    "description": "TypeScript check",
    "timeout": 60000,
    "workdir": "C:\\Users\\jazzw\\git\\snippet\\js\\remotion\\la-to-ny"
  }
  ```

## 2026-04-21 (2)

- 參考：
  - https://x.com/itsolelehmann/status/2014740993208188959
  - https://medium.com/@creativeaininja/making-videos-with-code-the-complete-guide-to-remotion-and-claude-code-82892e21d022
- 實驗：

```bash
~/git/snippet/js/remotion$ npx create-video@latest
Welcome to Remotion!
√ Choose a template: » Hello World A playground with a simple animation
√ Directory to create your project ... my-video
√ You are already inside a Git repo (C:\Users\jazzw\git\snippet).
A new project will be created without initializing a new Git repository. Do you want to continue? ... No / Yes
√ Add TailwindCSS? ... No / Yes
√ Add agent skills? ... No / Yes

███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
███████╗█████╔╝ ██║██║     ██║     ███████╗
╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
███████║██║  ██╗██║███████╗███████╗███████║
╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝

┌   skills
│
◇  Source: https://github.com/remotion-dev/skills.git
│
◇  Repository cloned
│
◇  Found 1 skill
│
●  Skill: remotion-best-practices
│
│  Best practices for Remotion - Video creation in React
│
◇  Detected 4 agents
│
◇  Install to
│  Same as last time (Recommended)
│
◇  Installation scope
│  Project
│
◇  Installation method
│  Symlink (Recommended)

│
◇  Installation Summary ──────────────────────────────────────────────────────╮
│                                                                             │
│  ~\git\snippet\js\remotion\my-video\.agents\skills\remotion-best-practices  │
│    symlink → Gemini CLI, GitHub Copilot, OpenCode                           │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────╯
│
◇  Proceed with installation?
│  Yes
│
◇  Installation complete

│
◇  Installed 1 skill to 3 agents ───────────────────────────────────────────────╮
│                                                                               │
│  ✓ ~\git\snippet\js\remotion\my-video\.agents\skills\remotion-best-practices  │
│    symlink → Gemini CLI, GitHub Copilot, OpenCode                             │
│                                                                               │
├───────────────────────────────────────────────────────────────────────────────╯

│
└  Done!


Copied to my-video.

Get started by running:
 cd my-video
 npm i
 npm run dev

To render a video, run:
 npx remotion render

Links to get you started:
 https://www.remotion.dev/docs
 https://www.remotion.dev/prompts

Remotion is free for teams of up to 3.
Adopting Remotion in your company? Visit https://www.remotion.pro/license

√ 💻 Open in VS Code? ... No / Yes

~/git/snippet/js/remotion$ cd my-video/
~/git/snippet/js/remotion/my-video$ npm i
npm warn deprecated source-map@0.8.0-beta.0: The work that was done in this beta branch won't be included in future versions
npm warn deprecated source-map@0.8.0-beta.0: The work that was done in this beta branch won't be included in future versions
npm warn deprecated source-map@0.8.0-beta.0: The work that was done in this beta branch won't be included in future versions
npm warn deprecated source-map@0.8.0-beta.0: The work that was done in this beta branch won't be included in future versions

added 346 packages, and audited 347 packages in 1m

66 packages are looking for funding
  run `npm fund` for details

2 low severity vulnerabilities

To address all issues, run:
  npm audit fix --force

Run `npm audit` for details.
~/git/snippet/js/remotion/my-video$ npm run dev

> my-video@1.0.0 dev
> remotion studio

-------------
Version mismatch:
- On version: 4.0.449
  - @remotion/bundler node_modules\@remotion\bundler\package.json
  - @remotion/media-utils node_modules\@remotion\media-utils\package.json
  - @remotion/player node_modules\@remotion\player\package.json
  - @remotion/renderer node_modules\@remotion\renderer\package.json
  - @remotion/studio-server node_modules\@remotion\studio-server\package.json

- On version: 4.0.450
  - @remotion/cli node_modules\@remotion\cli\package.json
  - remotion node_modules\remotion\package.json
  - @remotion/eslint-config-flat node_modules\@remotion\eslint-config-flat\package.json
  - @remotion/tailwind-v4 node_modules\@remotion\tailwind-v4\package.json
  - @remotion/zod-types node_modules\@remotion\zod-types\package.json

- On version: 4.0.448
  - @remotion/compositor-win32-x64-msvc node_modules\@remotion\compositor-win32-x64-msvc\package.json
  - @remotion/licensing node_modules\@remotion\licensing\package.json
  - @remotion/streaming node_modules\@remotion\streaming\package.json
  - @remotion/studio-shared node_modules\@remotion\studio-shared\package.json
  - @remotion/studio node_modules\@remotion\studio\package.json
  - @remotion/media-parser node_modules\@remotion\media-parser\package.json
  - @remotion/web-renderer node_modules\@remotion\web-renderer\package.json

You may experience breakages such as:
- React context and hooks not working
- Type errors and feature incompatibilities
- Failed renders and unclear errors

To resolve:
- Make sure your package.json has all Remotion packages pointing to the same version.
- Remove the `^` character in front of a version to pin a package.
- Run `npx remotion versions --log=verbose` to see the path of the modules resolved.
-------------

Server ready - Local: http://localhost:3000, Network: http://10.2.102.47:3000
Building...
Built in 6290ms


~/git/snippet/js/remotion/my-video$ opencode
```
- 結果：
  - [hello-world.md](hello-world.md)
- 探索：
  - 除了 `Blank`, `Hello World` 之外，還有 `Prompt to Video` 的範本可以用。
  ```bash
  ~/git/snippet/js/remotion$ npx create-video@latest -h
  Welcome to Remotion!
  ? Choose a template: » - Use arrow-keys. Return to submit.
    ↑ Next.js (Vercel Sandbox) Render videos on-demand using Vercel Sandbox
      Next.js (No Tailwind) SaaS template for video generation apps
      Next.js (Pages dir) SaaS template for video generation apps
      Recorder A video production tool built entirely in JavaScript
      Prompt to Motion Graphics SaaS Starter Kit SaaS template for AI-powered animation generation
      Hello World (JavaScript) The default starter template in plain JS
      Render Server An Express.js server for rendering videos with Remotion
      Electron Render Remotion videos from a desktop app
      React Router SaaS template for video generation apps
      React Three Fiber Remotion + React Three Fiber Starter Template
      Still images Dynamic PNG/JPEG template with built-in server
      Audiogram Text and waveform visualization for podcasts
      Music Visualization Text and waveform visualization for podcasts
  >   Prompt to Video Create a story with images and voiceover from a prompt
      Skia React Native Skia starter
      Overlay Overlays for video editing software
      Code Hike Beautiful code animations
      Stargazer Celebrate your repo stars with a video
      TikTok Generate animated word-by-word captions
      Editor Starter (Paid) A boilerplate for starting a video editor
  ```

## 2026-04-22

- \#TODO: 待測試 Initializes a Remotion AI workspace with OpenCode
  - https://github.com/the-langston-co/remotion-workspace-setup

