# Google Stitch CLI 技術報告

> **版本**: 1.0  
> **最後更新**: 2026-10  
> **來源**: Google Labs 官方文件

## 一、執行緒說明

Google Stitch CLI（`@google/stitch`）是 Google Labs 於 2026 年 10 月 1 日正式推出的終端機工具，提供 Stitch 平台的第三種官方整合管道。與 MCP（協議）和 SDK（開發者套件）並行，CLI 專為習慣在終端機操作的開發者設計，讓設計產生、原型預覽和程式碼整合無需切換瀏覽器。

CLI 提供三大核心能力：

1. **連接在地程式碼代理**：將 Stitch 功能提供給已在終端機工作的代理
2. **產生介面與設計系統**：以指令方式呼叫核心產生引擎
3. **傳送在地開發伺服器快照**：將在地開發伺服器的介面狀態回傳給 Stitch

## 二、安裝步驟

### 2.1 環境需求

- Node.js 20 或更新版本
- npm 全球套件安裝權限（或 root/sudo）

### 2.2 安裝命令

```bash
npm install -g @google/stitch
```

### 2.3 登入帳號

```bash
stitch login
```

執行後會開啟瀏覽器完成登入，或按指示提供認證碼。

## 三、測試與驗證步驟

### 3.1 驗證安裝

```bash
# 檢查版本資訊
stitch --version

# 查看可用指令
stitch --help
```

### 3.2 建立專案

```bash
stitch create project --title "My App"
```

這會建立一個新的 Stitch 專案並初始化配置。

### 3.3 產生第一張畫面

```bash
stitch generate screen --device DESKTOP --prompt "Clean analytics dashboard with sidebar navigation"
```

參數說明：
- `--device`：指定目標裝置類型（`DESKTOP` 或 `MOBILE`）
- `--prompt`：描述性提示，說明要產生的介面內容

### 3.4 啟動在地預覽伺服器

```bash
stitch serve
```

此命令啟動在地預覽伺服器，可立即檢視產生結果，無需切回網頁應用程式。

## 四、核心指令速查表

| 指令 | 用途 |
|------|------|
| `stitch login` | 登入您的帳號 |
| `stitch create project` | 建立新專案 |
| `stitch generate screen` | 產生單張畫面；`--device` 指定 DESKTOP 或 MOBILE |
| `stitch generate variants` | 產生目前設計的變體；`--creative-range` 控制發散程度 |
| `stitch serve` | 在地預覽產生結果 |
| `stitch agent-skills add --user` | 為在地程式碼代理安裝 Stitch Skills |

### 4.1 產生設計變體

`--creative-range` 參數有三個等級，與 SDK 變體系統一致：

```bash
# 精修目前方向
stitch generate variants --creative-range REFINE

# 探索相鄰方向
stitch generate variants --creative-range EXPLORE

# 重新想像設計
stitch generate variants --creative-range REIMAGINE
```

### 4.2 安裝代理技能

```bash
stitch agent-skills add --user
```

單一指令即可為以下所有代理安裝 Stitch Skills：

- Claude Code
- Cursor
- Codex
- Gemini CLI
- Antigravity

安裝後，代理中會出現 `/stitch` 命令，涵蓋三項功能：
1. 產生畫面
2. 從 URL 擷取設計系統
3. 將 Stitch 原型轉為 React 元件

## 五、與 Skill 手動安裝的比較

| 項目 | 傳統手動安裝 | CLI 統一安裝 |
|------|-------------|-------------|
| 設定方式 | 每個代理需獨立設定 | 單一指令涵蓋所有代理 |
| 維護成本 | 新增代理需額外設定 | 重新執行即可更新 |
| 版本一致性 | 需手動校驗 | 自動保持同步 |

CLI 可為已使用舊方式的專案重新設定，確保各代理間的版本一致性。

## 六、工作流程整合

### 6.1 與 MCP 和 SDK 的分工

| 整合管道 | 目標受眾 | 典型用途 | 不適合情境 |
|----------|---------|---------|-----------|
| Stitch MCP | 透過協議呼叫的程式碼代理 | 讓 Claude Code 或 Cursor 讀取/寫入 Stitch 專案 | 需要手動控制每個步驟 |
| Stitch SDK | 撰寫程式的開發者 | 將產生功能嵌入自有工具鏈 | 只需快速生成單張畫面 |
| Stitch CLI | 終端機使用者與代理 | 在地生成、預覽與代理設定一站式 | 偏好留在瀏覽器操作 |

### 6.2 逆向通道（Reverse Channel）

CLI 新增的逆向通道允許 Stitch 查看「程式碼實際運行的介面」，而非靜態截圖。下一輪迭代從「程式碼實際渲染結果」開始，省去文字描述目前狀態的成本。

> 注意：此功能的公開細節仍有限，請參考官方文件確認具體命令與範圍。

## 七、常見問題（FAQ）

### Q1: Stitch CLI 是免費的嗎？

CLI 本身從 npm 免費安裝；產生功能遵循 Stitch 帳號配額系統。請參考官方文件確認目前限制。

### Q2: 我已經使用 MCP，還需要 CLI 嗎？

- 若工作流程圍繞程式碼代理，MCP 更自然
- 若偏好終端機，或需要腳本化與批次產生，CLI 更直接
- 兩者並存，無需二選一

### Q3: 安裝後找不到 `stitch` 命令怎麼辦？

1. 確認 Node.js 為 20 或更新版本
2. 檢查 npm 全球套件安裝目錄是否在 PATH 中
3. 重新執行 `npm install -g @google/stitch` 通常可解決

## 八、最佳實踐建議

### 8.1 五步驟循環流程

1. 使用 `stitch generate screen` 產生初始畫面
2. 以 `--creative-range` 迭代，直至方向合適
3. 將最終視覺規則記錄於 `DESIGN.md` 並鎖定
4. 讓程式碼代理依據 `DESIGN.md` 實現頁面
5. 在瀏覽器驗證並將偏差回傳至下一輪迭代

### 8.2 重要提醒

- **切勿跳過「鎖定 DESIGN.md」步驟**：社群實踐顯示，讓代理從記憶生成 UI，每張畫面會產生新風格
- **Alpha 階段特性與旗標快速變動**：建議在自動化流程中鎖定版本
- **配額限制**：產生指令依賴帳號配額；批次執行前請檢查使用限制
- **「虛假成功」問題**：社群報告過變更被標記為成功但未實際套用，關鍵步驟建議手動複核
- **代理整合非魔法**：技能安裝後，仍需提供清晰、具體的任務描述

## 九、延伸閱讀

- [Stitch Skills + Claude Code 教學](https://stitchprompt.com/blog/stitch-skills-claude-code-tutorial/)
- [Stitch 提示詞教學](https://stitchprompt.com/blog/tutorials/)
- [Google Stitch 2026 功能更新](https://stitchprompt.com/blog/google-stitch-2026-feature-update/)

## 十、參考資源

- 官方文件：https://stitch.google.com/docs
- 套件資訊：https://www.npmjs.com/package/@google/stitch
- CLI 教學：https://stitchprompt.com/blog/google-stitch-cli-tutorial/

*註：CLI 功能迭代快速，命令可能會變更。建議隨時檢查 `stitch --help` 獲取最新行為。*

## 2026-11-06

---
title: "Google Stitch CLI Just Changed AI Coding!"
source: https://www.youtube.com/watch?v=HyWwnNLfxWg
created: 2026-11-06
notebooklm: Stitch
source-id: 1e530186-287a-4187-b187-4401ed36325d
report-id: e42f5cb0-3414-43f9-a119-6d6ef30c2d9b
---
# 告別手動截圖！Google Stitch CLI 如何徹底改變 AI 網頁開發流程

## 1. 引言：設計與編碼的最後一哩路終於打通

在過去的網頁開發流程中，「畫面設計工具」與「程式碼撰寫工具」始終像是兩條平行線。設計師或開發者在設計工具中繪製出優美的畫面後，往往必須手動下載圖檔、複製資產，再交由 AI 或工程師重新撰寫成真正的網頁程式碼。這中間繁瑣的檔案傳送、手動截圖與反覆溝通，正是拉長開發週期的主要痛點。

如今，Google 正式推出了最新的 **Stitch CLI**（套件名稱為 `@google/stitch`），將旗下 AI 設計工具 Stitch 的強大能力直接注入到你的終端機（Terminal）中。這意味著你的 AI 編碼代理（AI Coding Agent）在構建網站的同時，能夠直接與設計工具無縫對話。

**簡單來說，「畫頁面的工具」與「造頁面的工具」終於能直接溝通對話了！**

這項突破性的更新將徹底重塑我們建立與驗證真實網站的速度，讓個人開發者或小型團隊無需雇用整支隊伍來回傳遞檔案，就能以驚人的效率打造出高品質網頁。

## 2. 什麼是 Google Stitch CLI？三大核心功能拆解

回顧 Stitch 的發展歷程，它最早只是一個「輸入文字構想、產生畫面設計」的工具。你說出想要的介面，它幫你畫出來，但體驗僅停留在產生一張靜態圖片，後續仍需自行想辦法將圖片轉化為可運行的網頁。

為了打通這個瓶頸，Google 逐步推動 Stitch 的升級。在 Google /2026 的展演中，Google 展示了實時設計體驗（Realtime design experience），使用者可以透過文字或語音互動，導入既有的程式碼或設計檔案，讓設計即時串流顯示於畫布（Canvas）上，並能直接傳送至 Google 的 AI 編碼代理工具 **Google Anti-gravity**。

在此過程中，Google 也開放了全站設計規範檔案 `design.md` 供大家使用。這是一份讓開發者定義全站視覺與佈局規範的 Markdown 文件，其核心價值在於**讓 AI 編碼代理在建立每一個新頁面時，都能自動遵循統一的設計語言與視覺風格**。而 Stitch CLI 的登場，正是 Google 今年精心佈局的最後一塊關鍵拼圖。

Stitch CLI 主要提供以下三大核心功能：

* **連結在地 AI 編碼代理 (Connect local AI coding agents)**：讓運行於本機開發環境的 AI 編碼代理能夠直接與 Stitch 設計平台建立連線與指令調用。
* **生成介面與設計系統 (Generate screens and design systems)**：支援透過終端機指令快速生成網頁畫面，並建立一致性的設計系統。
* **回傳區域開發伺服器快照 (Send local development server snapshot back to Stitch)**：**這是全套更新中最關鍵、最具價值的亮點**。它能將你在本機開發伺服器（Localhost）上實際運行的網頁快照回傳給 Stitch，讓 AI 針對「真正運作中的網頁」而非「預想的設計草圖」進行即時比對與修正。

## 3. 技術生態系三劍客：MCP、SDK 與 CLI 有何不同？

隨著 Stitch CLI 的推出，目前圍繞 Stitch 的技術生態系共有三個核心元件。需要特別強調的是：**Stitch CLI 並非用來取代 MCP 或 SDK，而是與它們並存的新管道**，讓開發者與 AI 代理可以在最習慣的工作環境中直接呼叫 Stitch。

為了讓大家一目瞭然，我們將這三者整理如下：

| 工具元件 | 概念比喻 | 主要功能與定位 |
| :--- | :--- | :--- |
| **Stitch MCP** | 溝通電話線 (Phone Line) | 作為 AI 編碼代理與 Stitch 設計工具之間的橋樑，讓兩者機能順暢對話。 |
| **Stitch SDK** | 開發者工具箱 (Toolkit) | 供開發者撰寫程式碼來調用 Stitch，執行建立畫面、擷取 HTML、抓取截圖、編輯畫面及產生不同設計版本等功能。 |
| **Stitch CLI** | 終端機指令視窗 (Text Window) | 提供直接在終端機輸入文字指令的介面，讓開發者或 AI 代理無需開啟瀏覽器點擊，即可直接執行操作。 |

在官方 Stitch CLI 正式發布之前，市場上其實已經存在針對 Gemini CLI 的 Stitch 延伸功能（利用 MCP 運作）。當時使用者已經可以透過文字指令執行「查詢專案清單（List projects）」、「取得畫面（Get screen）」、「下載資產（Download assets）」或「建立新畫面（Make new screen）」等任務。而這次官方 Stitch CLI 的發布，則讓這條從編碼工具通往設計工具的管道變得更加直接、穩固且自動化。

## 4. 顛覆性的「快照循環」（Snapshot Loop）：新舊工作流程大對決

要理解 Stitch CLI 的威力，必須對比傳統的開發流程與導入 CLI 後的「快照循環」（Snapshot Loop）。

> **舊工作流程的比喻**：就像兩個人身處不同的建築物中，只能透過牆上的郵件投遞口（Mail slot）傳遞紙條。溝通充滿時間差與隔閡，每次修改都必須重新傳遞一張紙。
> 
> **「快照循環」新工作流程的比喻**：兩個人坐在同一個房間裡，看著同一頁網頁，直接指著畫面的同一個位置說：「這裡需要修改！」

在傳統開發中，你在 A 工具做設計，下載資產後開啟編碼工具，AI 代理寫出網頁並在瀏覽器的 `localhost`（本機伺服器）呈現。當你發現間距歪了或按鈕太小時，你必須手動截圖、切換回設計工具、上傳截圖，並試圖用文字解釋哪裡錯了——這過程充滿無謂的來回奔波。

### 實例示範：打造「AI Profit Boardroom 著陸頁」

藉由 Stitch CLI 的「快照循環」，你可以體驗到「一頁、一循環、無需手動截圖」的流暢開發：

1. **下達初始指令**：告訴 AI 代理：「設計一個 AI Profit Boardroom 的著陸頁 (Landing Page)，展示 AI 自動化如何幫商家節省時間並介紹社群內容。」
2. **Stitch 生成設計與 AI 寫碼**：Stitch 產出設計，AI 編碼代理自動將其轉化為程式碼並於本機伺服器運行。
3. **回傳本機快照 (Localhost Snapshot)**：將本機伺服器上真實運行的網頁快照回傳給 Stitch。
4. **比對與修復疊代**：開發者或 AI 代理直接詢問 Stitch：「**有哪些地方看起來歪了或不對勁？ (what looks off)**」，Stitch 直接比對真實網頁並給出修復建議，AI 代理隨即自動修正程式碼。整個過程無需手動截圖或切換視窗。

## 5. 新手入門：簡單幾步開啟你的第一個 Stitch Loop

由於 Stitch CLI 是一項全新的工具，官方的軟體套件細節與指令可能會隨後續更新調整，建議實作時務必參考嘗試當天的官方最新說明。

以下為開啟第一個 Stitch Loop 的標準步驟：

### 步驟一：安裝與登入
開啟終端機，透過 npm（Node.js 的套件管理工具）安裝官方推出的 `@google/stitch` 套件，執行 `npm install @google/stitch` 指令，並依提示完成帳號登入驗證，確保 CLI 能成功連線至你的 Stitch 帳戶。

### 步驟二：啟動 AI 編碼代理
開啟支援此工作流的 AI 編碼代理工具，例如 Google 官方推薦的 **Google Anti-gravity**。

### 步驟三：輸入自然語言提示詞 (Prompt)
無需使用複雜的專有名詞，使用自然的指令引導 AI 代理調用 Stitch。

```text
Use Stitch to create a landing page for the AI profit boardroom, build it in this project, and follow the Stitch design system.
```

### 步驟四：觀察自動化循環
送出指令後，觀察你的 AI 代理如何在一趟運作中自動完成「調用 Stitch 設計 -> 自動編寫程式碼 -> 將本機瀏覽器快照回傳比對」的完整自動化流程。

## 6. 結論與關鍵帶走點 (Key Takeaways)

目前，市場上仍存在著顯著的資訊落差紅利（Window of opportunity）。大多數企業主與開發者依然習慣手動將檔案在設計軟體與程式碼工具之間搬來搬去，甚至還未聽說過 Stitch CLI 的存在。隨著工具的演進，率先掌握自動化快照循環的人，將能以極高效率拉開生產力差距。

本篇文章的 **3 大核心帶走點**：

1. **打通設計與編碼介面**：Stitch CLI (`@google/stitch`) 讓 AI 編碼代理能在終端機直接呼叫 Stitch 設計工具，徹底打破設計與程式碼之間的壁壘。
2. **本機快照循環（Snapshot Loop）取代手動截圖**：直接將 `localhost` 開發伺服器的真實網頁快照傳回 Stitch 比對，並透過詢問「what looks off」實現精準的自動化校正疊代。
3. **把握先機紅利期**：結合 Stitch、`design.md`、Google Anti-gravity 與 AI 編碼代理的新一代工作流已然成型，及早導入即可享有巨大的開發速度優勢。

準備好提升你的開發效率了嗎？今天就安裝 `@google/stitch`，親自體驗第一個無需截圖的 Stitch Loop 吧！

## 2026-11-06 實測

- Google Labs Stitch Skills
  - https://www.skills.sh/google-labs-code/stitch-skills
```bash
[11/05 16:32:03] npx skills search google-labs-code/stitch-skills
```
- 安裝
```bash
[11/06 21:58:12] npm install -g @google/stitch
```
- 登入
```bash
[11/06 21:58:28] stitch login
~/git/snippet$ stitch login
🔐 Starting Stitch CLI Google OAuth 2.0 login...
Note: Google sign-in requests the 'cloud-platform' scope because Stitch Canvas and Loop APIs authenticate through Google Cloud.

Opening your browser to Google sign-in...
If your browser does not open automatically, copy and paste this URL:

   (略)

✅ Logged in successfully!
   User: jazz************@gmail.com
   Expires: 11/8/2026, 3:06:43 PM
   Saved to: C:\Users\jazzw\.stitch\credentials.json

Next step:

  Open your project in your AI coding agent and ask:
    "I just installed the stitch CLI. Run stitch agent-skills add to install the Stitch skill, read stitch --help, and help me design or capture screens for my project."
```
- 確認狀態
```bash
[11/06 21:58:59] stitch status
```
```bash
~$ stitch status
🔑 Stitch CLI Authentication Status
   Status:       Valid
   User:         jazz*******@gmail.com
   Expires At:   11/8/2026, 3:06:43 PM
   Auto-Refresh: Yes
   Storage:      C:\Users\jazzw\.stitch\credentials.json
   Experiments:  loop=off
~$
```
- 新增 Stitch Agent Skill
```bash
[11/06 21:59:44] stitch agent-skills add --user
```
```bash
~$ npx skills list -g
Global Skills

speak-human-tw ~\.agents\skills\speak-human-tw
  Agents: Gemini CLI, GitHub Copilot, OpenCode, Pi  Source: raymondhou0917/speak-human-tw
stitch         ~\.agents\skills\stitch
  Agents: Gemini CLI, GitHub Copilot, OpenCode, Pi  Source: untracked
```
