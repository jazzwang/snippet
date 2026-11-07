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
