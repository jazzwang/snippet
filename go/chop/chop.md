# chop

- Git Repo
  - https://github.com/AgusRdz/chop
- Website
  - https://getchop.run/

> [!NOTE]
> CLI output compressor for Claude Code. Reduces token consumption by 50–90% by compressing verbose command output before it enters the context window. Supports 52+ commands — git, docker, kubectl, npm, terraform, and more.

## 2026-09-04

- 緣起
  - 在研究 [headroom](../../py/headroom/headroom.md) 的時候，Gemini 提到這個專案
  - 進一步研究後，發現 `chop` 主要是用來整合 Claude Code 的 `pre-tool` Hook
    - 註：看到這裡才比較知道 Claude Code Hook 的功能有點類似 git 的 `pre-commit`, `post-commit` hook
- 繼續研究如何讓 Chop 可以整合 `Pi Coding Agent`

> [!QUESTION]
> https://pi.dev/ 支援 pre-tool 嗎?

感謝您提供更精確的官方網頁資訊，讓我能針對這款由 Earendil Inc. 開發的 Pi Coding Agent (@earendil-works/pi-coding-agent) 給您最正確的答案。

是的，Pi 支援指定 Pre-tool 的功能，它是透過「動態上下文（Dynamic Context）」與「延伸模組（Extensions）」架構來實現的。

雖然 Pi 為了保持核心極簡（Minimal Core），本身不硬編碼（Hardcode）複雜的工具攔截邏輯，但它把這項能力作為「原语（Primitives）」開放出來：

### Pi 實現 Pre-tool 指令的方式

   1. 動態上下文注入 (Dynamic Context)：
   Pi 允許延伸模組在每一次 Agent 執行工具或轉換回合（Before each turn）之前，動態注入自訂訊息、過濾歷史紀錄或修改即將執行的指令。這正是標準 Pre-tool 鉤子（Hook）的運作基石。
   2. 完全掌控工具與事件 (Extensions access to tools & events)：
   Pi 的延伸模組是標準的 TypeScript 模組，擁有對工具（Tools）、終端機指令（Commands）與事件系統的完整存取權限。開發者可以編寫模組來攔截即將執行的 Tool，先跑地端指令，再交給 Agent。
   3. 支援第三方工具生態 (例如 chop)：
   如同前述，像 chop 這種專為 AI Agent 設計的 CLI 壓縮器，也原生支援了 Pi Coding Agent（透過 chop init --global 或針對動態環境的調整），它就是利用 Pi 的延伸機制，在工具執行前先壓縮 verbose 的終端機輸出，來達到高達 50-90% 的 Token 節省效益。

### 如何在 Pi 中啟用或指定？

由於 Pi 的原則是 "Change the harness, not your workflow"（改變工具架構來適應你的工作流），如果您想加入自訂的 Pre-tool 指令（例如限制權限、特定路徑保護或前置檢查），您可以：

* 直接叫 Pi 幫你寫一個：在對話中直接對它說：「幫我寫一個 Pi extension，在每次執行 Bash 工具前先跑 [您的前置指令]」。它會動態修改自己，您輸入 /reload 後即可生效。
* 透過 `AGENTS.md` 載入技能：在專案根目錄的 `AGENTS.md` 中定義特定 Skills（包含自訂的指令說明與工具前置限制），Pi 在啟動時會自動載入該專案的 Context 規則。

如果您需要為 Pi 撰寫特定的 Pre-tool 延伸模組，可以告訴我：

* 您希望在工具執行前，自動幫您執行什麼地端指令（例如：預先備份、先執行 lint、或是進行安全檢查）？
* 您希望這個前置動作是全域生效，還是只針對特定專案（透過 `AGENTS.md`）呢？

> [!QUESTION]
> 可以做成全域生效嗎?

可以，完全可以做成全域生效！

在 Pi Coding Agent (`@earendil-works/pi-coding-agent`) 的極簡設計中，它提供了與專案級別對稱的全域配置路徑。您可以透過以下兩種最常見的全域方式，讓 Pre-tool 機制對你電腦上的所有專案生效： [1, 2]

### 方法一：將自訂的 Pre-tool 腳本（TypeScript）放進全域擴充目錄（推薦）

Pi 具備自動偵測（Auto-discovery）全域擴充模組的功能。您可以編寫一個 TypeScript 的 Extension 來攔截工具執行，並將其放置在全域目錄中： [3]

1.  全域擴充模組路徑：
    請將您的延伸模組腳本放在 `~/.pi/agent/extensions/` 底下。
    *例如建立一個：* `~/.pi/agent/extensions/my-pre-tool.ts`
2.  撰寫攔截邏輯（範例）：
    利用 Pi 提供的 `Event Interception` 機制，在 `beforeToolCall` 事件中注入您的前置地端指令：
    ```js
    // ~/.pi/agent/extensions/my-pre-tool.tsimport { execSync } from'child_process';

    exportdefaultfunction (ctx: any) {
      // 訂閱工具執行前的事件 (Pre-tool Hook)
      ctx.events.on('beforeToolCall', async (event: any) => {
        // 如果 AI 準備調用 bash 指令工具if (event.toolName === 'bash') {
          constoriginalCommand = event.args.command;

          // 範例：在每次執行前自動跑 Lint 或安全性檢查
          console.log(`[Pre-tool] 正在全域檢查指令: ${originalCommand}`);
          try {
            // 執行您的前置指令
            execSync('your-pre-command-here', { stdio: 'inherit' });
          } catch (err) {
            // 如果前置指令失敗，可以選擇阻止（Abort）AI 的後續動作
            event.abort('Pre-tool 檢查失敗，已安全攔截。');
          }
        }
      });
    }

    ```

3.  啟用全域配置：
    打開您的全域設定檔 `~/.pi/config.json`，將該 Extension 的名稱或路徑加進去，即可全域載入：
    ```json
    {
      "extensions": [
        "my-pre-tool"
      ]
    }

    ```

    [2, 3]

### 方法二：透過全域 ``AGENTS.md`` 注入規則（免寫程式碼）

如果您不想寫 TypeScript，只想透過「文字型規則」來約束、引導模型在全域調用工具前必須先跑某些指令，Pi 提供了全域的 Context 注入路徑： [4]

1.  編輯全域文件：
    打開或建立 `~/.pi/agent/AGENTS.md`。
2.  寫入 Pre-tool 規則指引：
    ```md
    # Global Pre-tool Instructions
    Whenever you are about to use the `bash` tool to execute a command, you MUST always prefix it with `your-pre-command && ...`.
    For example, instead of running `npm test`, you must run `your-pre-command && npm test`.
    ```

    Pi 在任何資料夾啟動時，都會自動將這個全域 `AGENTS.md` 與專案當地的檔案進行串接（Concatenate），確保全域規則不漏接。 [4]

### 方法三：如果是整合已有的第三方 Pre-tool（如 `chop`）

如果您是用像是 `chop`（Token 壓縮器）這種已經包裝好的工具，通常它有更直覺的一鍵全域註冊指令：
```bash
chop init --global
```

執行後，它會自動將攔截 Hook 配置寫入 Pi 能夠讀取到的全域環境中，之後不管你在哪個專案目錄輸入 `pi` 啟動 Agent，它都會自動在背後幫你包裹執行前置壓縮。 [5, 6]

您目前是打算自己寫一段 TypeScript 腳本來客製化工具（方法一），還是傾向用 文字規則來引導模型（方法二） 呢？我可以為您提供更具體的程式碼範本！

[1] [https://pi.dev](https://pi.dev/docs/latest)
[2] [https://pi.dev](https://pi.dev/packages/pi-context-optimizer)
[3] [https://pi.dev](https://pi.dev/docs/latest/extensions)
[4] [https://deepakness.com](https://deepakness.com/blog/pi-agent-setup/)
[5] [https://github.com](https://github.com/realchendahuang/pi-config)
[6] [https://www.facebook.com](https://www.facebook.com/jackshenadvisor/photos/-ai-%E4%B8%8D%E5%8F%AA%E6%9C%83%E8%81%8A%E5%A4%A9%E9%82%84%E8%83%BD%E5%8B%95%E6%89%8B%E5%81%9A%E4%BA%8Bpi-coding-agent-%E5%B0%8F%E7%99%BD%E4%B9%9F%E8%83%BD%E7%9C%8B%E6%87%82%E4%BD%A0%E6%9C%89%E6%B2%92%E6%9C%89%E6%83%B3%E9%81%8E%E5%A6%82%E6%9E%9C-ai-%E4%B8%8D%E5%8F%AA%E6%98%AF%E5%9B%9E%E7%AD%94%E6%80%8E%E9%BA%BC%E5%81%9A%E8%80%8C%E6%98%AF%E7%9C%9F%E7%9A%84%E5%8F%AF%E4%BB%A5%E5%B9%AB%E4%BD%A0%E5%9F%B7%E8%A1%8C%E5%B7%A5%E4%BD%9C%E6%9C%83%E7%99%BC%E7%94%9F%E4%BB%80%E9%BA%BC%E4%BA%8B%E4%BE%8B%E5%A6%82%E4%BD%A0%E8%AA%AA-/28643476051911448/)