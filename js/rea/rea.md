# REA 技術報告：逆向工程 Agents 工具

## 一、專案概述

### 1.1 專案簡介

**REA (Reverse Engineering for Your Coding Agent)** 是由 morluto 開發的一項創新工具，旨在讓編碼 Agents 具備逆向工程能力。透過 REA，Agents 可以深入理解軟體如何運作，從應用程式行為分析到原生二進製檔案解碼，提供全方位的逆向工程能力。

### 1.2 核心價值

- **跨平台支援**：支援原生執行檔、JavaScript 應用程式、網頁、二進製檔案等多種目標
- **MCP 整合**：透過 Model Context Protocol (MCP) 與 Coding Agents 無縫整合
- **自動化工具**：提供六種導向式工作流程，自動化複雜的逆向工程任務
- **透明化分析**：所有分析結果皆提供證據來源（檔案、函式、位址、請求）

## 二、系統需求

### 2.1 環境需求

| 項目 | 版本要求 |
|------|----------|
| Node.js | v22.23.4+、v24.22.1+ 或 v26.12.1+ |
| npm | 隨附於 Node.js |
| Coding Agent | Claude Code、Codex、Cursor 等 |

### 2.2 檢查方式

```bash
node -v
npm -v
```

## 三、安裝步驟

### 3.1 基本安裝

1. **執行安裝命令**

```bash
npx rea-agents@latest setup
```

2. **審批安裝計劃**

- Setup 會預覽配置變更
- 要求使用者明確批准後才執行
- 自動備份現有配置

3. **重啟 Coding Agent**

安裝完成後必須重啟 Agent 才能使 REA 功能生效

### 3.2 自訂選項

| 選項 | 說明 |
|------|------|
| `--skill=false` | 省略調查技能，僅使用 CLI |
| `--clie` | 指定特定 Agent 客戶端 |

### 3.3 安裝 Hopper（可選）

```bash
# Hopper 需獨立批准
npx rea-agents@latest setup --hopper
```

Hopper 可分析二進製檔案，需額外配置 Ghidra 或 IDA。

## 四、功能特性

### 4.1 支援分析目標

| 目標類型 | 可分析內容 |
|----------|------------|
| 原生執行檔與函式庫 | 函式、組裝語言、擬代碼、參考關聯 |
| JavaScript 與 Electron 應用程式 | 模組、匯入、IPC 通訊、原始碼位置 |
| 瀏覽器網頁 | 腳本、請求、網頁內容 |
| 二進製格式 | GPU 程式碼物件、BEAM、Python 位元組碼、Unity IL2CPP、Godot PCK、PyInstaller、Node.js SEA、PE/ELF 表 |

### 4.2 MCP 導向式工作流程

REA 提供六種 Provider 中性（Provider-neutral）的調查工作流程：

1. **Understand a feature and build your own**
   - 理解功能原理並建構類似功能
   - 需要明確授權確認
   - 提供所有結論的證據

2. **Find out how software works**
   - 了解軟體運作機制
   - 從使用者視角解釋功能

3. **Inspect the code**
   - 程式碼檢查與分析
   - 追蹤程式碼路徑

4. **Export notes**
   - 導出分析筆記
   - 記錄調查過程

5. **Guided workflows**
   - 導向式調查流程
   - 適合初學者使用

6. **Target-free guided_workflows**
   - 無需特定目標的工具
   - `action: "list"` 列出所有工具
   - `action: "render"` 渲染工具清單

### 4.3 CLI 命令

```bash
# 列出所有工作流程
rea guided-workflows

# 渲染特定工作流程
rea guided-workflows --action render --workflow-id ID --arguments-json '{"key": "value"}'
```

## 五、測試步驟（Step-by-Step）

### 5.1 環境準備測試

#### 步驟 1：檢查 Node.js 版本

```bash
# 確認 Node.js 版本符合需求
node -v
# 預期輸出：v22.x.x、v24.x.x 或 v26.x.x

# 確認 npm 版本
npm -v
```

#### 步驟 2：檢查網路連線

```bash
# 測試能否連接到 GitHub
curl -I https://github.com/morluto/rea

# 測試能否連接到官方網站
curl -I https://morluto.github.io/rea/
```

#### 步驟 3：驗證 npm 可用

```bash
# 測試 npm 執行
npm --version
```

### 5.2 REA 安裝測試

#### 步驟 4：執行安裝命令

```bash
# 執行安裝
npx rea-agents@latest setup
```

#### 步驟 5：審批安裝計劃

1. 系統會顯示安裝計劃預覽
2. 確認所有變更符合預期
3. 輸入確認（通常為 `y` 或 `yes`）

#### 步驟 6：驗證安裝成功

```bash
# 確認 rea-agents 已安裝
npx rea-agents --version

# 測試 CLI 功能
rea guided-workflows
```

#### 步驟 7：重啟 Coding Agent

- 根據使用的 Agent 類型執行重啟
- 例如：Claude Code、Cursor 等

### 5.3 功能測試

#### 步驟 8：測試基本功能

```bash
# 列出可用工作流程
rea guided-workflows --action list

# 測試特定工作流程
rea guided-workflows --action render --workflow-id 0
```

#### 步驟 9：實際分析測試（以網頁為例）

1. **選擇測試目標**
   - 選擇一個簡單的網站或應用程式

2. **開啟 Coding Agent**
   - 使用已安裝 REA 的 Agent

3. **提出分析問題**
   ```
   "請幫我分析這個網站的登入功能是如何運作的，並解釋其原理"
   ```

4. **確認授權**
   - REA 會要求確認是否擁有分析目標的授權
   - 確認後繼續

5. **檢視證據**
   - 檢查所有結論的證據來源
   - 確認檔案、函式、位址、請求等資訊

#### 步驟 10：測試二進製檔案分析（如適用）

```bash
# 如果有 Hopper 安裝，可測試二進製分析
# 需要提供合法的二進製檔案並獲得授權
```

### 5.4 錯誤處理測試

#### 步驟 11：測試無網路環境

```bash
# 斷網後執行
# 預期結果：安裝命令顯示錯誤訊息
# 斷網後使用已安裝版本應可正常工作
```

#### 步驟 12：測試舊版 Node.js

```bash
# 使用舊版 Node.js（如 v20.x）
# 預期結果：安裝命令提示版本不符
```

#### 步驟 13：測試無權限環境

```bash
# 使用 sudo 執行
sudo npx rea-agents@latest setup
# 預期結果：顯示無權限警告
```

## 六、使用範例

### 6.1 分析網頁功能

```
用戶：請幫我分析這個網站的購物車功能
REA Agent: 好的，我將使用 REA 工具分析購物車功能
         1. 首先會檢查網頁的 JavaScript 程式碼
         2. 追蹤商品加入流程
         3. 分析後端 API 請求
         4. 提供完整的證據鏈
```

### 6.2 理解應用程式功能

```
用戶：這個 App 的加密功能是如何實現的？
REA Agent: 我將分析加密功能的實現細節
         1. 定位加密函式庫
         2. 分析加密演算法
         3. 追蹤資料處理流程
         4. 提供可驗證的證據
```

### 6.3 建立類似功能

```
用戶：我想在專案中實現類似的功能，請幫我解釋原理
REA Agent: 好的，我將：
         1. 分析原功能的實現方式
         2. 解釋核心概念
         3. 提供實作建議
         4. 確認授權後繼續
```

## 七、最佳實踐

### 7.1 授權確認

- **永遠先確認授權**：REA 會自動要求確認分析權限
- **合法使用**：僅分析自己擁有或授權的軟體
- **尊重版權**：分析結果僅供學習與理解，不得用於非法用途

### 7.2 證據驗證

- **檢查所有結論的證據**：包括檔案路徑、函式名稱、記憶體位址等
- **交叉驗證**：使用不同方法驗證相同結論
- **記錄完整過程**：保存分析筆記供後續參考

### 7.3 安全性考量

- **小心分析惡意軟體**：逆向工程可能觸發防護機制
- **沙箱環境**：在隔離環境中進行分析
- **資料保護**：勿將敏感資料傳入分析流程

## 八、故障排除

### 8.1 常見問題

| 問題 | 解決方案 |
|------|----------|
| 安裝失敗 | 檢查 Node.js 版本，確保符合需求 |
| 找不到命令 | 確認已重啟 Coding Agent |
| 無法分析特定目標 | 確認目標類型在支援列表中 |
| 證據不足 | 提供更多上下文或調整分析問題 |

### 8.2 更新 REA

```bash
# 更新到最新版本
npx rea-agents@latest setup
```

### 8.3 移除 REA

```bash
# 按照官方文件移除
# 通常需在 Coding Agent 設定中取消勾選
```

## 九、參考資源

- **官方網站**：https://morluto.github.io/rea/
- **GitHub 倉庫**：https://github.com/morluto/rea
- **官方文件**：https://github.com/morluto/rea/blob/main/docs/
- **FAQ 頁面**：https://rea.tools/faq/
- **開始使用指南**：https://morluto.github.io/rea/get-started/

## 十一、聯絡與支援

- **GitHub Issues**：https://github.com/morluto/rea/issues
- **官方文件**：https://github.com/morluto/rea/docs/
- **安裝支援**：https://morluto.github.io/rea/get-started/

*基於 morluto/rea 官方文件與網站內容整理而成*
