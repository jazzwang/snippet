# UnvibeCode 技術報告

> **UnvibeCode**：將複雜程式碼庫逆向工程為業務工作流、連通程式碼、邊界案例與證據支持的風險分析工具。

---

## 系統概述

UnvibeCode 是一款用於理解複雜程式碼庫的分析工具，它能自動逆向工程程式碼庫，提取出：

1. **業務工作流地圖**（Business Workflow Map）：理解系統實際執行的業務流程
2. **連通程式碼地圖**（Connected Code Map）：追蹤程式碼之間的關聯關係
3. **業務風險發現**（Business Risk Findings）：識別可能影響業務的潛在問題
4. **完整程式碼庫上下文**（Complete Repository Context）：歸一化的程式碼庫 ZIP 包供進一步分析

**核心價值**：不需要逐個閱讀檔案，即可理解大型程式碼庫的業務邏輯、組件關聯與潛在風險。

---

## 系統需求

| 項目 | 要求 |
|------|------|
| Python 版本 | 3.11 或更高版本 |
| 網路環境 | 需要網路連線（用於主機端業務分析服務） |
| 檔案權限 | 需要對待分析的程式碼庫擁有讀取權限 |
| 作業系統 | Windows / macOS / Linux |

---

## 安裝步驟

### 步驟 1：確認 Python 環境

首先確認您的環境已安裝 Python 3.11 或更高版本：

```powershell
# Windows
py --version
# 預期輸出範例：Python 3.11.9

# macOS 或 Linux
python3 --version
# 預期輸出範例：Python 3.11.9
```

### 步驟 2：安裝 UnvibeCode 套件

使用 pip 安裝或升級 UnvibeCode：

```bash
# Windows（PowerShell）
py -m pip install --upgrade unvibecode

# macOS 或 Linux
python3 -m pip install --upgrade unvibecode
```

**注意**：
- 如果您使用虛擬環境（virtual environment），請先啟動虛擬環境，並使用該環境的 Python 進行安裝
- 建議使用 `--upgrade` 參數確保安裝最新版本

### 步驟 3：驗證安裝

確認套件已成功安裝：

```powershell
# Windows
py -m pip show unvibecode

# macOS 或 Linux
python3 -m pip show unvibecode
```

預期會顯示套件資訊，包含版本號、安裝位置等。

### 步驟 4：確認命令可用

執行無參數命令確認工具可用：

```powershell
# Windows
py -m unvibecode --help

# macOS 或 Linux
python3 -m unvibecode --help
```

預期會顯示可用命令清單與使用說明。

---

## 測試步驟

### 測試 1：基本功能測試

#### 步驟 1.1：準備測試用程式碼庫

準備一個已知的程式碼庫目錄供測試。範例可使用官方提供的樣本：

```powershell
# Windows
py -m unvibecode review --repository "D:\Projects\customer-support-agent"

# macOS 或 Linux
python3 -m unvibecode review --repository "/Users/yourname/Projects/customer-support-agent"
```

#### 步驟 1.2：執行分析

執行分析命令，觀察以下事項：

- 分析進度是否正確顯示於終端機
- 是否有錯誤訊息
- 分析完成後是否自動開啟 HTML 報告檔案

### 測試 2：輸出結果驗證

#### 步驟 2.1：確認結果檔案結構

分析完成後，檢查結果儲存位置：

```text
./shipready_results/analysis_<timestamp>/customer_results/
```

預期應包含以下檔案：

| 檔案名稱 | 說明 |
|----------|------|
| `00_unvibecode_results.html` | 主入口頁面 |
| `01_connected_code_map_for_llm.html` | 連通程式碼地圖 |
| `02_business_workflow_map.html` | 業務工作流地圖 |
| `03_business_risk_findings.html` | 業務風險發現 |
| `complete_repository_context_for_llm.zip` | 完整程式碼庫上下文 ZIP |

#### 步驟 2.2：驗證 HTML 報告可開啟

在瀏覽器中開啟 `00_unvibecode_results.html`，確認：

- [x] 頁面正常加載，無 JavaScript 錯誤
- [x] 各報表分頁可正常切換
- [x] 連通程式碼地圖可互動
- [x] 業務工作流可閱讀且包含程式碼引用
- [x] 風險發現（如有）包含觸發條件、程式碼行為與業務後果說明

#### 步驟 2.3：驗證 ZIP 包內容

解壓 `complete_repository_context_for_llm.zip`，確認包含：

| 檔案 | 說明 |
|------|------|
| `manifest.json` | 程式碼庫身份、計數與套件元資料 |
| `chunks.jsonl` | 程式碼區塊，含檔案與行號資訊 |
| `connections.jsonl` | 程式碼區塊間的連結關係 |
| `selections.jsonl` | 按檔案與範圍預先計算的上下文選擇 |
| `README.md` | 使用說明檔 |

---

## 驗證步驟

### 驗證 1：功能完整性驗證

#### 步驟 1.1：驗證業務工作流分析

1. 開啟 `02_business_workflow_map.html`
2. 選擇一個業務工作流區域
3. 確認以下資訊完整：
   - ✓ 工作流的目的與存在意義
   - ✓ 工作流的產出與依賴者
   - ✓ 工作流的重要性說明
   - ✓ 支援的程式碼引用

**驗證範例**（以 smolagents 為例）：
- 應能探索 Agent 記憶體與重播功能
- 多步驟 Agent 執行流程
- UI 串流功能實現

#### 步驟 1.2：驗證連通程式碼地圖

1. 開啟 `01_connected_code_map_for_llm.html`
2. 滑鼠懸停在檔案上預覽連通程式碼
3. 點擊檔案選擇下載的上下文大小：

| 上下文大小 | 約莫 Token 預算 | 適用時機 |
|------------|----------------|----------|
| Narrow | 30K | 針對檔案及其鄰近上下文的聚焦問題 |
| Optimal | 45K | 理解連通實現的推薦起點 |
| Wider | 75K | 需要更多 surrounding code 的問題 |

4. 確認下載的上下文檔可正常開啟，包含正確的程式碼與連結

#### 步驟 1.3：驗證風險發現分析

1. 開啟 `03_business_risk_findings.html`
2. 如有風險發現，確認每個發現包含：
   - ✓ 觸發條件與程式碼行為
   - ✓ 業務規則、後果與影響
   - ✓ 導致結果的程式碼路徑
   - ✓ 建議修改與接受檢查
   - ✓ 支援的檔案、符號與程式碼引用

**注意**：無風險發現（no-findings）僅表示已完成的分析範圍內無發現，不代表程式碼庫完全無瑕疵。

### 驗證 2：安全性與隱私驗證

#### 步驟 2.1：驗證憑證防護機制

UnvibeCode 在發送程式碼供 AI 分析前，會自動偵測並替換以下敏感憑證：

- API 金鑰（API keys）
- 密碼（passwords）
- 存取權杖（access tokens）
- 私鑰（private keys）

**驗證方法**：
1. 在測試程式碼庫中故意放入包含 API 金鑰的檔案
2. 執行 UnvibeCode 分析
3. 檢查結果報告中敏感憑證應已被替換為 placeholder

**注意**：深度編碼或自訂格式的密鑰檔案可能無法被防護機制偵測。

#### 步驟 2.2：驗證無需 API 金鑰

確認以下條件成立：

- [x] 無需輸入 UnvibeCode 啟動金鑰（activation key）
- [x] 無需提供客戶端 OpenAI API 金鑰
- [x] 無需設定 `.env` 檔案

### 驗證 3：效能驗證

#### 步驟 3.1：大程式碼庫處理測試

對於大型程式碼庫（約 200 萬 estimated source tokens 以上），驗證以下行為：

1. 執行分析命令
2. 確認輸出：
   - [x] 仍會產生連通程式碼地圖（Connected Code Map）
   - [x] 仍會產生完整程式碼庫上下文（Complete Repository Context）
   - [x] 但**不會**啟動深度的業務工作流與風險審查（Business Workflow and Risk Review）

**原因說明**：此設計避免過大的程式碼庫進入冗長的 hosted review，同時仍能提供有用的程式碼圖與 LLM 上下文輸出。

#### 步驟 3.2：分析時間監控

監控分析時間，確認：

- 分析進度在終端機正常顯示
- 分析完成後自動開啟 HTML 報告
- 無異常的記憶體耗用或 CPU 使用率

---

## 支援的程式語言

UnvibeCode 的連通程式碼映射與上下文準備支援以下語言：

| 語言 | 檔案類型 |
|------|----------|
| Python | `.py` |
| JavaScript | `.js`, `.jsx`, `.mjs`, `.cjs` |
| TypeScript | `.ts`, `.tsx` |
| Rust | `.rs` |
| PHP | `.php` |
| Ruby | `.rb` |
| HTML 和 CSS | `.html`, `.htm`, `.css` |
| Go | `.go` |

**注意**：分析深度會因語言與程式碼庫結構而異。詳細限制請參閱 [Limitations](https://github.com/FinanceFlash/unvibecode/blob/main/docs/LIMITATIONS.md)。

---

## 使用時機

### 適合使用 UnvibeCode 的場景

1. **理解陌生程式碼庫**
   - 快速了解業務工作流、連通組件與實現路徑
   - 無需手動開啟每個檔案

2. **審查 AI 生成應用**
   - 了解實際實現了什麼
   - 調查潛在的業務邏輯缺陷

3. **跨檔案除錯**
   - 在變更函數前先追蹤依賴與周圍程式碼
   - 理解函數間的關聯

4. **調查應用風險**
   - 審查有源碼支援的發現
   - 了解潛在的營運後果

5. **為 AI 編碼助手準備上下文**
   - 下載完整程式碼庫上下文
   - 下載聚焦的連通程式碼

### 不適合的場景

UnvibeCode **不取代**以下工作：

- 單元測試、整合測試、端對端測試、負載測試或滲透測試
- 熟悉系統的工程師進行的手動程式碼審查
- 安全、隱私、法律或法規評估
- 生產環境監控與事件調查
- 與負責的產品負責人驗證業務需求

---

## 故障排除

### 常見問題 1：無法找到模組 unvibecode

**症狀**：執行 `python -m unvibecode` 時出現錯誤訊息

**解決方案**：
1. 確認套件安裝在正確的 Python 環境中
2. 檢查套件是否安裝：`py -m pip show unvibecode`
3. 如果使用虛擬環境，請使用該環境的 Python 進行安裝與執行

### 常見問題 2：python / python3 未識別

**症狀**：執行命令時顯示 `'python' 不是內部或外部命令`

**解決方案**：
1. 安裝 Python 3.11 或更高版本
2. 重新開啟終端機
3. 確認使用的命令（`py`、`python` 或 `python3`）可用
4. Windows 上如 `py` 不可用但 `python --version` 可用，請一致使用 `python` 代替 `py`

### 常見問題 3：程式碼庫路徑找不到

**症狀**：分析時提示路徑不存在

**解決方案**：
1. 確認 `--repository` 指向的是**已存在的本地程式碼庫資料夾**
2. 不要使用 GitHub URL 或 ZIP 檔案
3. 先 clone 或解壓縮程式碼庫
4. 引號包裹完整路徑，特別是含空格的路徑
5. 確認您的帳戶有權讀取該路徑

### 常見問題 4：主機端分析無法連線

**症狀**：工作流與風險分析階段失敗

**解決方案**：
1. 確認網路連線正常
2. 確認網路允許 HTTPS 存取 UnvibeCode 主機端服務
3. 遵循終端機錯誤訊息提示
4. 如涉及組織網路限制，請聯絡網路管理員

### 常見問題 5：僅有連通程式碼與 LLM 上下文可用

**症狀**：缺少業務工作流與風險發現輸出

**解決方案**：
1. 確認程式碼庫大小是否超過約 200 萬 estimated source tokens
2. 超過此閾值時，UnvibeCode 會跳过深度的業務工作流與風險審查
3. 這不是錯誤，而是設計上的大小限制行為
4. 詳細限制請參閱 [Limitations](https://github.com/FinanceFlash/unvibecode/blob/main/docs/LIMITATIONS.md)

### 常見問題 6：報告未自動開啟

**症狀**：分析完成後未開啟 HTML 報告

**解決方案**：
1. 手動開啟結果資料夾：`./shipready_results/analysis_<timestamp>/customer_results/`
2. 雙擊 `00_unvibecode_results.html`
3. 使用最新完成分析的資料夾
4. 保持入口檔案與其伴隨報告在同一資料夾

### 常見問題 7：報告分頁空白或顯示「檔案找不到」

**症狀**：開啟入口頁面後，點擊某些分頁無反應

**解決方案**：
1. 確認所有必要的 HTML 檔案都在同一資料夾：
   - `01_connected_code_map_for_llm.html`
   - `02_business_workflow_map.html`
   - `03_business_risk_findings.html`
   - `complete_repository_context_for_llm.zip`
2. 確認任何伴隨資料夾（如 `_support/`）也在一起
3. 移動或複製時請保持完整結果資料夾一起移動

---

## 資料處理與隱私

### 本地處理的作業

UnvibeCode Python 套件在客戶端電腦上執行以下作業：

- 程式碼庫掃描
- 檔案與語言偵測
- 相依性與符號映射
- 連通圖建構
- 程式碼區塊準備
- 上下文套件組裝
- HTML 與 ZIP 渲染

### 主機端服務處理

需要業務工作流與風險分析的結構化程式碼上下文，會安全地傳送至主機端 UnvibeCode 服務。

**客戶端不提供 OpenAI API 金鑰**。模型提供者憑證保留於主機端服務。

### 客戶端責任

- 僅審查您有權處理的程式碼庫
- 不要包含不需要審查的密鑰、憑證、私鑰或受管制的資料
- 在分析前移除包含敏感值的生成檔案或本地設定
- 遵循您組織的原始碼與第三方處理政策

### 營運元資料

對於高度敏感或受管制的程式碼庫，在使用 UnvibeCode 進行主機端程式碼分析前，請獲得任何必要的組織批准。

---

## 輸出結果維護

### 保持報告檔案一起

轉移或分享分析結果時，請保持以下檔案一起：

| 檔案 | 說明 |
|------|------|
| `00_unvibecode_results.html` | 主入口頁面 |
| `01_connected_code_map_for_llm.html` | 連通程式碼地圖 |
| `02_business_workflow_map.html` | 業務工作流地圖 |
| `03_business_risk_findings.html` | 業務風險發現 |
| `complete_repository_context_for_llm.zip` | 完整程式碼庫上下文 ZIP |
| `_support/` | 任何伴隨資料夾（如存在） |

**重要提醒**：僅下載入口頁面不會下載它所顯示的報告。請下載完整結果資料夾。

---

## 參考文檔

- [快速開始指南](https://github.com/FinanceFlash/unvibecode/blob/main/docs/QUICKSTART.md)
- [理解四種輸出](https://github.com/FinanceFlash/unvibecode/blob/main/docs/OUTPUTS.md)
- [UnvibeCode 運作原理](https://github.com/FinanceFlash/unvibecode/blob/main/docs/HOW_IT_WORKS.md)
- [限制與負責任使用](https://github.com/FinanceFlash/unvibecode/blob/main/docs/LIMITATIONS.md)
- [資料處理與隱私](https://github.com/FinanceFlash/unvibecode/blob/main/docs/DATA_PROCESSING.md)
- [故障排除](https://github.com/FinanceFlash/unvibecode/blob/main/docs/TROUBLESHOOTING.md)
- [公開程式碼庫審查](https://github.com/FinanceFlash/unvibecode/blob/main/docs/PUBLIC_PREVIEW.md)

---

## 範例資源

探索官方提供的範例分析：

- [smolagents](https://financeflash.github.io/unvibecode/gitdocs/smolagents/2026-10-18/)
- [PocketFlow](https://financeflash.github.io/unvibecode/gitdocs/pocketflow/2026-10-18/)
- [mini-swe-agent](https://financeflash.github.io/unvibecode/gitdocs/mini-swe-agent/2026-10-18/)
- [django-payments](https://financeflash.github.io/unvibecode/gitdocs/django-payments/2026-10-18/)

---

## 授權

UnvibeCode 使用混合授權模式：
- 公開材料採用 [Apache License 2.0](https://github.com/FinanceFlash/unvibecode/blob/main/LICENSE)
- 官方 Python 套件可能包含獨立的商業領域定義、工作流原型與分析資產

詳細授權範圍、許可、限制與套件元資料說明請參閱 [Licensing Clarification](https://github.com/FinanceFlash/unvibecode/blob/main/docs/LICENSE_CLARIFICATION.md)。

---

## 貢獻與支援

**貢獻**：歡迎參與文件、測試、範例與支援工具開發。
- [貢獻指南](https://github.com/FinanceFlash/unvibecode/blob/main/.github/CONTRIBUTING.md)
- [初學者友善問題](https://github.com/FinanceFlash/unvibecode/labels/good%20first%20issue)

**問題回報**：發現問題或有功能請求？[開啟 GitHub issue](https://github.com/FinanceFlash/unvibecode/issues)

**產品諮詢**：[divya.singaravelu@iiml.org](mailto:divya.singaravelu@iiml.org)

---

**版本**：v1.0  
**最後更新**：2026 年 11 月 17 日  
**來源**：[FinanceFlash/unvibecode](https://github.com/FinanceFlash/unvibecode)
