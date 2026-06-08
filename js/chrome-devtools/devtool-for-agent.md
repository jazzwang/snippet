# Chrome DevTools for Agents

- YouTube: 
  - Supercharge your AI coding workflow with Chrome DevTools for agents
  - https://www.youtube.com/watch?v=1AD81ZselPk
- Reference:
  - https://developer.chrome.com/blog/devtools-for-agents-v1?hl=en
  - https://developer.chrome.com/blog/new-in-devtools-149/#devtools-for-agents
  - https://developer.chrome.com/docs/devtools/ai-assistance/chat#auto-workspace
  - https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/tool-reference.md#third-party
  - https://github.com/ChromeDevTools/chrome-devtools-mcp
  - https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/docs/cli.md

## 告別 AI 瞎子摸象：Chrome DevTools for agents 如何賦予 AI 真正的「開發者之眼」

### 前言

身為資深開發者，你一定體驗過這種挫敗感：當前的 AI 代理（Coding Agents）雖然具備強大的代碼生成能力，但一旦面對複雜的運行時錯誤（Runtime Errors）或細微的 CSS 佈局調整，它們往往會陷入「嘗試修正、刷新、失敗」的死循環。究其原因，是因為 AI 處於一種「盲視」狀態------它能看見源代碼，卻看不見瀏覽器中真實發生的狀況。

Google 最近發布了 **Chrome DevTools for agents**，這不僅僅是一個新工具，更是 Google 填補「靜態推理」與「運行時執行」之間鴻溝的關鍵橋樑。它為 AI 代理提供了核心的「閉環回饋（Closed Feedback Loop）」，讓 AI 能夠像真人開發者一樣直接與開發者工具互動，徹底重塑 AI 輔助編程的遊戲規則。

### 核心重點一：打破「盲目開發」-- AI 的閉環回饋循環

回顧每位開發者的成長歷程，我們並非單靠閱讀代碼來理解網頁。資深開發者 Matthias Rohmer 指出，他真正理解靜態 HTML 如何轉化為動態 DOM，是透過在 Elements 面板中不斷點擊與修改實現的。對於 AI 來說，需求完全一致：若要讓 AI 從「代碼生成器」進化為真正的「問題解決者」，它必須具備觀察力。

Chrome DevTools for agents 基於成熟的 **Puppeteer** 與 **Chrome for Testing** 架構，為 AI 提供了穩定的環境感知能力。這讓 AI 不再只是根據機率猜測源代碼，而是能直接檢查運行中的頁面並進行即時調試。

「對我而言，DevTools 在我的學習旅程中實現了閉環回饋。透過 DevTools，我可以檢查我正在開發的活動頁面、進行微調、嘗試破壞事物並調試問題。」

### 核心重點二：運行時數據（Runtime Data）才是除錯的關鍵

許多開發者常遇到一種困境：錯誤訊息僅顯示在用戶界面，而源代碼中完全找不到線索。Matthias 在案例中展示了一個名為 **Showtime** 的內部身份驗證提供者。當註冊失敗時，系統僅拋出 `APP_ERR_1003` 這種神祕代碼。

由於 Showtime 是內部系統且缺乏公開文件，任何 AI 模型都無法在預訓練階段掌握它。傳統 AI 代理會在地毯式搜索源代碼後陷入崩潰，但具備 DevTools 能力的 AI 會直接查看 Network 面板。透過獲取 Response 中的具體錯誤細節，AI 即使面對完全未經文件紀錄的系統，也能依賴「運行時數據」進行精準修復。這在處理企業內部老舊系統或未公開 API 時，展現了巨大的實戰價值。

### 核心重點三：規模化專業知識 -- 從 Lighthouse 到效能分析

這套工具最深遠的意義在於「規模化專家技能」。它目前內建了六大核心技能組：**疑難排解 (Troubleshooting)**、**CLI 腳本編寫**、**無障礙 (Accessibility) 調試**、**記憶體洩漏 (Memory Leaks)**、**LCP 優化**以及 **Chrome DevTools 基礎操作**。

這意味著開發者不再需要親自成為效能專家。以日本公司 **CyberAgent** 的案例為例，他們利用此技術讓 AI 代理在短短一小時內，針對 Storybook 中 32 個組件的 **230 個 Stories** 進行了完整的自動化審計。AI 不再是隨機優化，而是能主動執行 Performance Trace，根據量測數據精準出擊。

「這套技能組將在未來幾個月內擴展，以幫助您的代理人調試網頁的最新功能......這讓您的編碼代理人表現得像該領域的專家。」

### 核心重點四：`autoConnect` -- 人機協作的無縫銜接

`autoConnect` 功能徹底降低了開發者的認知負擔。想像你已經在瀏覽器中手動重現了一個極難觸發的 bug，現在你不需要撰寫冗長的 Prompt 來解釋環境，只需讓 AI 「接手」即可。

要啟用此功能，只需簡單三步：在瀏覽器中選擇 **Inspect (檢查)** -> **Remote Debugging (遠端偵錯)** -> 勾選 **Allow Remote Debugging (允許此瀏覽器實例進行遠端偵錯)**。

關於安全性，資深開發者最關心的隱私問題也有明確保障：DevTools for agents **無法存取** Chrome 密碼管理器中儲存的密碼。不過，Matthias 仍幽默地提醒：當你將 AI 連接到個人 Profile 時要格外小心。如果你在已登入的電商頁面下令，AI 可能會真的幫你下單買了 999 個彩色氣球送到門口。

### 核心重點五：從對話到腳本 -- 動作持久化

除了透過 MCP (Model Context Protocol) 服務進行對話式交互，Chrome DevTools for agents 提供的 CLI 工具具備更高的 **Token 效率 (Token-efficient)**。

AI 在 DevTools 中執行的一系列複雜操作（如：模擬不同視窗大小、檢查導航列可見性、截圖對比），可以透過 CLI 指令**將 AI 的動作持久化為工程資產 (Engineering Assets)**------即自動生成可重複執行的 Shell 腳本。這將一次性的 AI 調試過程，轉化為長期可用的自動化測試腳本，對於追求效能與成本平衡的團隊來說，這才是大規模應用的終極形態。

### 結論與展望

Chrome DevTools for agents 的問世，標誌著 AI 輔助編程從單純的「文本生成」正式跨越到了「環境感知」的新紀元。這套工具目前已發布 **1.0 穩定版**，這是一個成熟且隨時可投入生產環境的里程碑。

當 AI 代理擁有了與人類開發者完全相同的工具視角與操作能力時，我們必須思考：未來的開發流程將如何被重構？或許，我們的工作重心將從「編寫代碼」轉變為「審核 AI 產出的調試腳本與自動化資產」。

**現在，就去試試看吧！讓你的 AI 代理睜開雙眼。**

## (A) Mindmap

```markmap
# Chrome DevTools for Agents
## Introduction
- Purpose: Deep dive on announcements, what it is, usefulness, getting started.
- DevTools opens when right-click in Chrome -> Inspect.
- New UI surface in September last year: Chrome DevTools for agents.
## Overview
- What it is: DevTools for coding agents.
- Where it lives: NPM package.
- How it relates to other tools: Integrates with coding agents (Antigravity, Gemini CLI, etc.).
- How agents use it: Enables a closed feedback loop for agents, similar to human developers.
## Foundational Technologies
### Chrome for Testing
### Puppeteer
- Library from the Chrome tooling team.
- Layer between DevTools for agents and Chrome.
- Gives DevTools for agents its capabilities.
- Security Considerations:
    - Does NOT have access to passwords saved in Chrome's password manager.
    - Uses a separate, anonymous browser profile by default.
    - Emphasizes: Critical to protect personal data; carefully decide what agents have access to.
## Architecture & Capabilities
### DevTools for Agents as an NPM package
- Installable on any machine with a recent Node.js version.
- Used by coding agents.
- Components:
    - MCP server
    - CLI (can be more token-efficient than MCP server)
    - Set of skills
### Skills (Total of six)
- Categories:
    - Troubleshooting & Chrome DevTools & Chrome DevTools CLI (help agents understand key capabilities and general usage).
    - Accessibility debugging (includes expert knowledge).
    - Memory leak debugging (includes expert knowledge).
    - Optimized LCP (includes expert knowledge).
- Skill set will expand over coming months (as part of Modern Web Guidance).
### Agent Tools (Wrapped Puppeteer Capabilities)
- Divided into six overall categories.
- Tools from multiple categories can be combined to fulfill user prompts.
### Use Cases / Examples
#### Closed Feedback Loop
- Agents can inspect live pages, fiddle, break things, debug issues.
- Contrast with agents relying only on source code (e.g., APP_ERR_1003 debugging example).
- Agent can find solutions in runtime data (e.g., Network panel response).
#### Fix Complex UI Flows
- Example: Debugging and fixing a sign-up error.
- CyberAgent case study: Audited 230 Storybook stories across 32 components in 1 hour.
#### One-off Bug Validation
- Combines Emulation tools (viewport resize) and Debugging tools (screenshot).
- Example prompt: "Check the same navigation items are visible on desktop, tablet, and mobile viewports."
- Agent resizes viewport, takes screenshots, interacts (e.g., burger menu), cross-checks.
- Automates testing journey across viewports and nested menus.
#### Scale Expertise (Performance, Accessibility, SEO)
- Agents can act as experts in areas where the user lacks knowledge.
- Example: "Improve the performance of this project" with DevTools for agents avoids token burn and focuses on real issues.
- Tools: Performance traces, analyze insights, Lighthouse audits (accessibility, best practices, SEO, agentic browser agent).
#### Persist Actions to Shell Scripts
- Allows actions performed by the agent to be saved as reusable CLI scripts.
- Example script for validating navigation: opens page, emulates viewports, takes screenshots.
- Human user would be responsible for comparing results from the script.
## Configuration
### For MCP server users
- Configure in MCP server's config file (e.g., `.gemini/settings.json` for Gemini CLI, `.mcp.json` for Cloud).
- Add entry to the `args` array.
### For CLI users
- Explicitly include desired option in the prompt.
### Common Configuration Options
- `channel`: Specify Chrome channel (e.g., Stable).
- `experimentalScreencast`: Enable experimental screencast support.
- Turn off certain tool categories (MCP server specific, to save tokens).
### autoConnect (Highlighted Feature)
- Allows agent to connect to an already running Chrome instance.
- Functionality: Agent picks up where the human user left off; "sharing your screen with your coding agent."
- How to enable: Chrome -> Inspect -> Remote Debugging -> Toggle "Allow Remote Debugging for This Browser Instance" checkbox.
- Usage: Set `autoConnect` in MCP JSON config or explicitly prompt for it in CLI.
## Getting Started & Resources
### Stable Release
- Version 1.0 (currently ~1.0.1) released.
### Documentation & Install Instructions
- `developer.chrome.com` provides install instructions for over 20 coding agents, more use cases, and in-depth documentation.
### Video Tutorial
- "google/dtasetup" on YouTube for setting up DevTools for agents (beginning of a series).
### Open-Source Project
- Available on GitHub for contributions, feature discussions, and issue reporting.
```

## (B) Action Items
*   [ ] Install Chrome DevTools for agents NPM package on any machine with a recent Node.js version.
*   [ ] When using a coding agent for runtime debugging, tweak your prompt to ask the agent to look at the runtime instead of specific files.
*   [ ] Ensure your coding agent has access to the DevTools CLI and the related skill when persisting actions to scripts.
*   [ ] For MCP server users, find the config file (`.gemini/settings.json` or `.mcp.json`) to configure DevTools for agents.
*   [ ] For CLI users, explicitly include desired configuration options in your prompt.
*   [ ] To use `autoConnect`, go to Chrome, then Inspect, select Remote Debugging in the sidebar, and toggle the "Allow Remote Debugging for This Browser Instance" checkbox.
*   [ ] Once remote debugging is enabled, use `autoConnect` in your MCP JSON config or explicitly prompt for it when using the CLI.
*   [ ] Visit `developer.chrome.com` for install instructions, more use cases, and documentation.
*   [ ] Watch the video tutorial at `google/dtasetup` on YouTube for setup guidance.
*   [ ] Visit the DevTools for agents project on GitHub to contribute, view feature discussions, or report issues.

## (C) Help Needed
*   The team is seeking user feedback on particular use cases or areas where users want to learn more; reach out on social media with ideas.
*   Contributions to the open-source project are welcome (e.g., reporting issues, participating in feature discussions, submitting code).

## (D) Potential Risk
*   **Data Security with `autoConnect`**:
    *   Using `autoConnect` with a personal Chrome profile (instead of the anonymous default) puts personal data at risk.
    *   An agent connected to a personal profile could execute unintended actions (e.g., ordering items online, incurring costs) if logged into sites.
    *   Always carefully decide what agents have access to, especially when using `autoConnect` with a personal profile, to protect personal data and prevent unintended consequences.
*   **Inefficient Token Usage (without DevTools for agents for certain tasks)**:
    *   Without DevTools for agents, a generic prompt (e.g., "Improve performance") might lead an agent to burn through token budget by reading all project files and making random fixes, without actually improving the website's performance.

## (E) Overview and Chapters

This presentation by Matthias Rohmer at Google I/O introduces "Chrome DevTools for agents," a new UI surface and NPM package designed to give coding agents access to the powerful debugging and inspection capabilities of Chrome DevTools. The core idea is to enable a "closed feedback loop" for AI agents, similar to how human developers use DevTools for learning and debugging. The talk covers the foundational technologies, key capabilities through various use cases, configuration options, and resources for getting started.

The presentation is structured into the following main chapters:

*   **Introduction to Chrome DevTools for Agents:** What it is, where it lives, its relation to other tools, and how agents can use it.
*   **Foundational Technologies:** A deep dive into Chrome for testing and Puppeteer as the underlying technologies.
*   **Capabilities and Use Cases:** Exploring various examples of what DevTools for agents can do across different tool categories.
*   **Configuration Options:** How to tailor DevTools for agents to specific needs, including `autoConnect`.
*   **Getting Started:** Resources for installation, learning, and contributing to the open-source project.
*   **Release Announcement:** Confirmation of the first stable release, version 1.0.

## (F) Detailed summary based on different attendees

The presentation, delivered by Matthias Rohmer, focused entirely on the new Chrome DevTools for Agents. As the primary speaker and presenter, Matthias outlined a compelling vision for extending web development tools to AI coding agents.

**Matthias's Perspective and Key Takeaways:**

*   **The Problem:** Matthias started by reflecting on his own learning journey in web development, emphasizing how Chrome DevTools provided an essential "closed feedback loop" for inspection, fiddling, and debugging. He highlighted that current AI coding agents, despite their advancements, lack this critical feedback loop because they don't interact with DevTools. This leads to agents hitting "dead ends" when debugging runtime issues that aren't apparent from source code alone.
*   **The Solution: DevTools for Agents:** Introduced as a new UI surface for DevTools, this solution aims to provide agents with the same inspection and debugging capabilities human developers enjoy. It was announced in September of the previous year (relative to the talk).
*   **How it Works:** Matthias detailed that DevTools for agents is an NPM package that agents (like Antigravity or Gemini CLI) can use via an MCP server or a CLI. It's built on the "solid and longstanding foundation" of Chrome for testing and Puppeteer. Key to its functionality are "skills" which teach the agent how and when to use DevTools for agents. Initially, there are six skills, categorized into general troubleshooting and expert knowledge areas (like accessibility, memory leaks, and LCP debugging).
*   **Core Capabilities through Use Cases:**
    *   **Automating Complex UI Flows:** Demonstrated with a sign-up form error (`APP_ERR_1003`). The agent navigated to a page, filled a form, captured network requests (where the real error message resided), fixed the code, and validated its own fix. This combines input automation, network, and navigation. He cited CyberAgent's success in auditing over 230 Storybook stories in an hour using this approach.
    *   **One-off Bug Validation:** Showcased how agents can validate UI responsiveness across different viewports (desktop, tablet, mobile). The agent used emulation tools to resize the viewport and debugging tools to take screenshots, then interacted with elements like a burger menu to verify consistent navigation items.
    *   **Scaling Expertise:** Matthias explained that instead of agents "burning through token budgets" with generic prompts, DevTools for agents allows them to "test for known problems" using specialized tools like performance traces and Lighthouse audits. This enables agents to genuinely improve performance, accessibility, or SEO even if the developer (or agent) lacks inherent expertise in those areas.
    *   **Persisting Actions to Scripts:** For users wanting to integrate agent actions into existing workflows, the CLI allows persisting DevTools actions into reusable shell scripts, such as setting up viewports and taking screenshots.
*   **Security Considerations:** Matthias addressed security concerns directly, clarifying that DevTools for agents uses a separate, anonymous browser profile by default and does not have access to Chrome's password manager. However, he emphasized caution when using `autoConnect` with a personal Chrome profile, as it could lead to unintended consequences (e.g., ordering items online if the agent connects to a logged-in shopping site).
*   **Configuration:** Users can configure the tool via MCP server settings files (e.g., `.gemini/settings.json`) or by including options in CLI prompts. Important options include specifying the Chrome `channel`, enabling `experimentalScreencast`, and turning off tool categories to save tokens. `autoConnect` was highlighted as a useful feature allowing agents to connect to an already running Chrome instance, requiring the user to enable "Allow Remote Debugging" in Chrome.
*   **Getting Started & Release:** He announced the first stable release (version 1.0 or ~1.01) and provided resources: developer.chrome.com for installation and documentation, a YouTube video series (`google/dtasetup`), and the GitHub repository for contributions.

In essence, Matthias presented Chrome DevTools for Agents as a transformative tool that empowers AI agents to become more effective web developers by providing them with crucial runtime context and interactive debugging capabilities, ultimately saving human developers time and effort.

## (G) Action Items

*   - [ ] Install Chrome DevTools for agents via NPM package on a machine with a recent Node.js version.
*   - [ ] Explore the documentation on developer.chrome.com for install instructions, use cases, and in-depth information.
*   - [ ] Watch the video tutorial series on YouTube (start at `google/dtasetup`) for setting up and understanding use cases.
*   - [ ] Experiment with prompts like "Go to localhost, signup, debug and fix the error when signing up with test and 1234" with a coding agent enabled with DevTools for agents.
*   - [ ] Test the bug validation use case with a prompt like "go to developer.chrome.com. Check the same navigation items are visible on desktop, tablet, and mobile viewports."
*   - [ ] Run performance traces or Lighthouse audits with a prompt such as "Go to localhost, run a performance trace, and act on all findings" to scale web performance expertise.
*   - [ ] Practice persisting agent actions to shell scripts using the DevTools CLI with a prompt like "Persist your previous actions in DevTools to a well-named script file using the DevTools CLI."
*   - [ ] Configure DevTools for agents by modifying the `args` array in MCP server settings (e.g., `.gemini/settings.json`) or by including options in CLI prompts.
*   - [ ] Try the `autoConnect` feature: enable "Allow Remote Debugging for This Browser Instance" in Chrome (Inspect > Remote Debugging sidebar) and then prompt your agent to connect to the running instance.
*   - [ ] Be mindful of security when using `autoConnect` with a personal Chrome profile; carefully consider what you give agents access to.
*   - [ ] Review the open-source project on GitHub for feature discussions, issues, or to contribute.
*   - [ ] Reach out to Matthias on social media with ideas for particular use cases or topics for future video tutorials.

## (H) 50 single select Quiz questions

1.  What was the primary announcement Matthias Rohmer discussed at Google I/O?
    a) New CSS properties
    b) Chrome DevTools for agents
    c) Updates to Lighthouse audits
    d) A new version of Puppeteer
    **Correct Answer: b) Chrome DevTools for agents**

2.  When was Chrome DevTools for agents announced (relative to the talk)?
    a) In September of the current year
    b) Last month
    c) In September last year
    d) Three years ago
    **Correct Answer: c) In September last year**

3.  According to Matthias, what does DevTools enable for human developers during their learning journey?
    a) Faster code compilation
    b) A closed feedback loop
    c) Automated testing suites
    d) Remote server access
    **Correct Answer: b) A closed feedback loop**

4.  What type of data does a typical out-of-the-box coding agent struggle to access when debugging?
    a) Source code
    b) Training data
    c) Runtime data
    d) Configuration files
    **Correct Answer: c) Runtime data**

5.  In the sign-up form debugging example, where was the additional useful error message found?
    a) In the source code comments
    b) In the Network panel of DevTools
    c) In the agent's training data
    d) In the browser's local storage
    **Correct Answer: b) In the Network panel of DevTools**

6.  Which command did Matthias suggest for the agent to debug the sign-up error, leveraging DevTools for agents?
    a) "Please fix APP_ERR_1003 in @SignUpForm.tsx"
    b) "Search for all network requests related to sign-up"
    c) "Go to localhost, signup, debug and fix the error when signing up with test and 1234."
    d) "Inspect console logs for APP_ERR_1003"
    **Correct Answer: c) "Go to localhost, signup, debug and fix the error when signing up with test and 1234."**

7.  What are the two foundational technologies upon which DevTools for agents is built?
    a) Chrome OS and React
    b) Chrome for testing and Puppeteer
    c) Node.js and npm
    d) Gemini CLI and Antigravity
    **Correct Answer: b) Chrome for testing and Puppeteer**

8.  DevTools for agents ships as what type of software package?
    a) A standalone executable
    b) A browser extension
    c) An NPM package
    d) A Docker image
    **Correct Answer: c) An NPM package**

9.  Which of these is NOT a core component through which your coding agent might use DevTools for agents?
    a) MCP server
    b) CLI
    c) Puppeteer directly
    d) Skills
    **Correct Answer: c) Puppeteer directly**

10. How many total skills does Chrome DevTools for agents initially ship with?
    a) Three
    b) Four
    c) Six
    d) Ten
    **Correct Answer: c) Six**

11. The skills for DevTools for agents are roughly put into how many categories?
    a) One
    b) Two
    c) Three
    d) Four
    **Correct Answer: b) Two**

12. Which of the following is an example of an "expert knowledge" skill category mentioned?
    a) General usage
    b) Troubleshooting
    c) Memory leak debugging
    d) CLI scripting
    **Correct Answer: c) Memory leak debugging**

13. DevTools for agents uses Puppeteer as an intermediary layer. What is a key security aspect related to this?
    a) It has full access to Chrome's saved passwords.
    b) It always uses the user's personal Chrome profile.
    c) It uses a vetted and tested set of tools, not exposing password manager access.
    d) It is not designed for security-sensitive operations.
    **Correct Answer: c) It uses a vetted and tested set of tools, not exposing password manager access.**

14. By default, what kind of browser profile does DevTools for agents use?
    a) The user's primary personal profile
    b) A shared corporate profile
    c) A separate, anonymous browser profile
    d) A read-only browser profile
    **Correct Answer: c) A separate, anonymous browser profile**

15. What was the name of the coding agent used in the screencasts by Matthias?
    a) Gemini
    b) Antigravity
    c) Showtime
    d) Lighthouse
    **Correct Answer: b) Antigravity**

16. The first example use case for DevTools for agents combined which categories of tools?
    a) Performance and accessibility
    b) Emulation and debugging
    c) Input automation, network, and navigation automation
    d) CLI scripting and configuration
    **Correct Answer: c) Input automation, network, and navigation automation**

17. What did CyberAgent achieve using DevTools for agents as a partner case study?
    a) Developed a new AI model for web development.
    b) Audited over 230 stories in Storybook across 32 components in one hour.
    c) Fixed critical security vulnerabilities in a web application.
    d) Optimized server-side performance by 50%.
    **Correct Answer: b) Audited over 230 stories in Storybook across 32 components in one hour.**

18. What types of tools were combined for the "one-off bug validation" use case (e.g., checking navigation items on different viewports)?
    a) CLI scripting and performance tools
    b) Emulation tools and debugging tools (like screenshots)
    c) Network tools and input automation
    d) Navigation tools and configuration options
    **Correct Answer: b) Emulation tools and debugging tools (like screenshots)**

19. What was the example prompt for validating navigation items across viewports?
    a) "Run a Lighthouse audit for responsiveness."
    b) "Check device compatibility for developer.chrome.com."
    c) "go to developer.chrome.com. Check the same navigation items are visible on desktop, tablet, and mobile viewports."
    d) "Take screenshots of developer.chrome.com on all mobile devices."
    **Correct Answer: c) "go to developer.chrome.com. Check the same navigation items are visible on desktop, tablet, and mobile viewports."**

20. What is the benefit of scaling expertise with DevTools for agents?
    a) It allows agents to guess problems from source code more effectively.
    b) It only works for developers already familiar with web performance.
    c) It enables improvement in areas like performance or accessibility by testing for known problems.
    d) It replaces the need for human experts in web development.
    **Correct Answer: c) It enables improvement in areas like performance or accessibility by testing for known problems.**

21. Which tool can DevTools for agents use to measure current performance and analyze insights?
    a) `console.log()`
    b) Performance traces
    c) Network monitor
    d) DOM inspector
    **Correct Answer: b) Performance traces**

22. What specific audit tool was mentioned for improving accessibility, best practices, and SEO?
    a) WebPageTest
    b) PageSpeed Insights
    c) Lighthouse
    d) Google Search Console
    **Correct Answer: c) Lighthouse**

23. Which use case is particularly well-suited for the CLI because it can run outside of an agent loop?
    a) Fixing complex UI flows
    b) Scaling expertise
    c) Persisting actions to shell scripts
    d) One-off bug validation
    **Correct Answer: c) Persisting actions to shell scripts**

24. What does the prompt "Persist your previous actions in DevTools to a well-named script file using the DevTools CLI" aim to create?
    a) A new agent skill
    b) A configuration file for the MCP server
    c) Shell scripts that can be rerun
    d) A detailed performance report
    **Correct Answer: c) Shell scripts that can be rerun**

25. When using DevTools for agents as an MCP server, where would you typically find the configuration file?
    a) `package.json`
    b) `.gitignore`
    c) `.gemini/settings.json` or `.mcp.json`
    d) `chrome-devtools-config.yaml`
    **Correct Answer: c) `.gemini/settings.json` or `.mcp.json`**

26. If you're using DevTools for agents through the CLI, how do you include desired configuration options?
    a) Through environment variables
    b) By explicitly including them in the prompt
    c) By modifying a global configuration file
    d) CLI usage does not support configuration options
    **Correct Answer: b) By explicitly including them in the prompt**

27. Which configuration option allows you to specify whether Chrome DevTools for agents should connect to a Chrome channel other than Stable?
    a) `browserChannel`
    b) `targetChannel`
    c) `channel`
    d) `chromeVersion`
    **Correct Answer: c) `channel`**

28. Which experimental option was mentioned that enables experimental support for screencasts?
    a) `enableScreencasts`
    b) `screencastFeature`
    c) `experimentalScreencast`
    d) `captureScreen`
    **Correct Answer: c) `experimentalScreencast`**

29. For MCP server users, what is a configuration option mentioned to save tokens?
    a) Increasing agent verbosity
    b) Disabling source map access
    c) Turning off certain tool categories
    d) Reducing the number of skills
    **Correct Answer: c) Turning off certain tool categories**

30. What is the purpose of the `autoConnect` configuration option?
    a) To automatically install browser updates
    b) To allow the coding agent to connect to an already running Chrome instance
    c) To connect to a remote server automatically
    d) To automatically generate prompts for the agent
    **Correct Answer: b) To allow the coding agent to connect to an already running Chrome instance**

31. To enable `autoConnect` for a human-operated Chrome instance, what setting must be toggled in Chrome DevTools?
    a) "Enable JavaScript debugging"
    b) "Allow Remote Debugging for This Browser Instance"
    c) "Connect to Localhost"
    d) "Record Network Activity"
    **Correct Answer: b) "Allow Remote Debugging for This Browser Instance"**

32. What is the potential security risk highlighted when using `autoConnect` with a personal Chrome profile?
    a) It might expose your IP address.
    b) It could delete browser history.
    c) The agent might incur unintended costs or consequences (e.g., ordering items).
    d) It slows down browser performance significantly.
    **Correct Answer: c) The agent might incur unintended costs or consequences (e.g., ordering items).**

33. What was the version number of the first stable release of DevTools for agents?
    a) 0.5
    b) 1.0
    c) 2.0
    d) Beta
    **Correct Answer: b) 1.0**

34. Where can users find install instructions, more use cases, and in-depth documentation?
    a) google.com
    b) developer.chrome.com
    c) github.com/chromedevtools
    d) npmjs.com
    **Correct Answer: b) developer.chrome.com**

35. What is the YouTube URL mentioned for a video tutorial on setting up DevTools for agents?
    a) youtube.com/chromedevtools
    b) youtube.com/google/dtasetup
    c) youtube.com/webdev
    d) youtube.com/devtoolsforagents
    **Correct Answer: b) youtube.com/google/dtasetup**

36. How is DevTools for agents described in terms of its development model?
    a) A closed-source Google project
    b) A thriving open-source project
    c) A commercial product with paid licenses
    d) A research-only initiative
    **Correct Answer: b) A thriving open-source project**

37. Where can users contribute to the DevTools for agents project or find feature discussions?
    a) Stack Overflow
    b) The developer.chrome.com forums
    c) GitHub
    d) Google Groups
    **Correct Answer: c) GitHub**

38. Matthias mentioned that the DevTools for agents skill set will expand over time to help debug which types of features?
    a) Obsolete web features
    b) Back-end API issues
    c) Modern web capabilities
    d) Mobile application features
    **Correct Answer: c) Modern web capabilities**

39. What did Matthias compare the agent's ability to debug using DevTools to for human learning?
    a) Learning by memorization
    b) Trial and error
    c) Blindly following advice
    d) Theoretical study
    **Correct Answer: b) Trial and error**

40. What is the primary language environment required for the DevTools for agents NPM package?
    a) Python
    b) Java
    c) Node.js
    d) Go
    **Correct Answer: c) Node.js**

41. What type of assertions did the speaker mention DevTools helps with in relation to CSS properties?
    a) Database assertions
    b) Finding the right combination of CSS properties
    c) Server-side assertions
    d) Network security assertions
    **Correct Answer: b) Finding the right combination of CSS properties**

42. How many years into their career were the coding agents described as being, who learned web development without DevTools?
    a) One year
    b) Two years
    c) Over three years
    d) Less than a year
    **Correct Answer: c) Over three years**

43. What specific component of the signup form was mentioned that was *not* publicly documented?
    a) The email input field
    b) The password validation
    c) A company's internal auth provider called Showtime
    d) The submit button styling
    **Correct Answer: c) A company's internal auth provider called Showtime**

44. When an agent has access to source maps through DevTools for agents, what can it do regarding file paths?
    a) Delete unnecessary files
    b) Guide the agent to the right file
    c) Create new source map files
    d) Obscure file paths for security
    **Correct Answer: b) Guide the agent to the right file**

45. What does the CLI offer that can be more token-efficient compared to using the MCP server for scripting?
    a) Direct browser interaction
    b) Logging capabilities
    c) Scripting against DevTools for agents
    d) Advanced debugging UI
    **Correct Answer: c) Scripting against DevTools for agents**

46. What was the name of the talk mentioned that users could find on YouTube for more information on "modern web guidance"?
    a) "Deep Dive into Puppeteer"
    b) "Unlock modern web capabilities in your AI coding workflows" by Phil
    c) "Advanced DevTools Techniques"
    d) "Chrome for Testing Explained"
    **Correct Answer: b) "Unlock modern web capabilities in your AI coding workflows" by Phil**

47. When the agent validated navigation items on developer.chrome.com, what interaction was specifically mentioned for mobile viewports?
    a) Zooming in
    b) Interacting with the burger menu
    c) Swiping left and right
    d) Changing themes
    **Correct Answer: b) Interacting with the burger menu**

48. What did Matthias suggest as a way to return the agent's response after a bug validation, like the navigation item check?
    a) A generated screenshot
    b) A detailed log file
    c) A verbal report
    d) A text-based response in the screencast
    **Correct Answer: d) A text-based response in the screencast**

49. What is the advice given regarding protecting personal data when using agents?
    a) Always use `autoConnect`.
    b) Never give agents access to a browser.
    c) Carefully decide what you give agents access to.
    d) Trust agents implicitly with all data.
    **Correct Answer: c) Carefully decide what you give agents access to.**

50. What type of "flow" did the speaker mention DevTools for agents enables the agent to start for fixing issues?
    a) A waterfall flow
    b) A linear flow
    c) A full end-to-end fixing flow
    d) A manual verification flow
    **Correct Answer: c) A full end-to-end fixing flow**

## (F) FAQ

*   **Q: What is Chrome DevTools for agents?**
    A: Chrome DevTools for agents is a new UI surface and an NPM package that provides AI coding agents with access to the inspection and debugging capabilities of Chrome DevTools, enabling a closed feedback loop for agents in web development.

*   **Q: When was Chrome DevTools for agents initially announced?**
    A: It was announced in September of the year prior to the Google I/O talk.

*   **Q: What problem does DevTools for agents solve for coding agents?**
    A: It solves the problem of coding agents hitting dead ends when debugging issues that are only visible at runtime (e.g., in network responses or console logs) and not directly in the source code. It gives them access to runtime data and context.

*   **Q: What are the foundational technologies behind DevTools for agents?**
    A: It is built on Chrome for testing and Puppeteer.

*   **Q: How does a coding agent use DevTools for agents?**
    A: An agent can use it through an NPM package, either via an MCP server or a CLI, guided by a set of "skills" that teach it how and when to leverage the DevTools capabilities.

*   **Q: Does DevTools for agents have access to my passwords saved in Chrome's password manager?**
    A: No, the clear answer is no. DevTools for agents does not have access to passwords saved in Chrome's password manager. It uses a vetted and tested set of tools through Puppeteer, which doesn't expose that capability.

*   **Q: What kind of browser profile does DevTools for agents use by default?**
    A: It uses a separate, anonymous browser profile by default, which largely reduces common security risks.

*   **Q: Can DevTools for agents help improve web performance, accessibility, or SEO?**
    A: Yes, it includes specialized tools to run performance traces, analyze insights, and conduct Lighthouse audits for accessibility, best practices, and SEO, allowing agents to improve these areas by testing for known problems.

*   **Q: What is the `autoConnect` feature?**
    A: `autoConnect` allows your coding agent to connect to an already running Chrome instance, picking up where you left off. It essentially lets you share your screen with your coding agent.

*   **Q: How do I enable `autoConnect` for my running Chrome browser?**
    A: You need to go to Chrome, open DevTools (Inspect), select "Remote Debugging" in the sidebar, and then toggle the "Allow Remote Debugging for This Browser Instance" checkbox.

*   **Q: Are there any security risks when using `autoConnect`?**
    A: Yes. If `autoConnect` connects to your personal Chrome profile (rather than the anonymous default), it might use your personal data. This could lead to unintended consequences, such as an agent ordering items online from a logged-in shopping site. It's critical to carefully decide what you give agents access to.

*   **Q: Can I configure DevTools for agents?**
    A: Yes, you can configure it. For MCP server users, this is done by adding entries to the `args` array in config files like `.gemini/settings.json` or `.mcp.json`. For CLI users, options can be explicitly included in the prompt.

*   **Q: What are some examples of configuration options?**
    A: Examples include specifying the Chrome `channel` (e.g., "Stable"), enabling `experimentalScreencast` for screencast support, and for MCP server users, turning off certain tool categories to save tokens.

*   **Q: Is DevTools for agents a stable release?**
    A: Yes, it was announced as being in its first stable release, version 1.0 (or approximately 1.01), at the time of the presentation.

*   **Q: Where can I find more resources and documentation for DevTools for agents?**
    A: You can find install instructions, more use cases, and in-depth documentation on developer.chrome.com. There's also a video tutorial series starting at youtube.com/google/dtasetup.

*   **Q: Is DevTools for agents an open-source project?**
    A: Yes, it is described as a thriving open-source project, and users are encouraged to contribute or participate in feature discussions on GitHub.

> Tokens: 9.4k sent, 7.1k received. Cost: $0.02 message, $0.02 session.  
> .gitignore  
> Add file to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: n  
