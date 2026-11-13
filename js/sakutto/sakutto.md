# Sakutto

> A browser extension for easy on-device translation with a local LLM (PLaMo). Private, free, no server needed.

- Git Repo
  - https://github.com/jammaru/sakutto
- Chrome Extension
  - https://chrome.google.com/webstore/detail/mhlbjjijfkoghmcjndgdimhdlfkhadfl

## 2026-11-10

```
Date:       11/10/2026, 5:17:23 PM
Models:     llama.cpp/unsloth/Qwen3.5-9B
Messages:   2 user, 9 assistant, 7 tool results
Tool Calls: 7
Tokens:     ↑20k ↓4.5k R107k
```

> [!NOTE]
> 根據 "https://github.com/jammaru/sakutto" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "js/sakutto/sakutto.md" .

## Sakutto 技術報告

> 在地化網頁翻譯 Chrome/Firefox 擴充功能技術文書
> 版本：2026-11-09 | 授權：MIT

---

### 1. 概述

Sakutto 是一個非官方的 Chrome 與 Firefox 瀏覽器擴充功能，可在裝置上直接翻譯網頁內容。它透過固定的 [wllama](https://github.com/ngxson/wllama) 建置執行 [PLaMo 3 Translate](https://huggingface.co/pfnet/plamo-3-translate-0.8b-GGUF) 模型。

**關鍵特性：**
- 在地化翻譯（不上傳任何資料到伺服器）
- 支援 53 種語言雙向翻譯
- Chrome 使用 PLaMo 作為主要翻譯引擎，Firefox 僅使用 PLaMo
- 無廣告、無付費功能、無追蹤
- 採用 MIT 授權

---

### 2. 系統需求

#### 最低需求

| 項目 | 版本 |
|------|------|
| Chrome | 任意版本（MV3 擴充功能） |
| Firefox | 153 或更新（MV3 擴充功能） |
| 作業系統 | Windows / macOS / Linux |
| 硬體 | 建議具備 WebGPU 支援的 GPU（可選，但大幅提升效能） |

#### 自編譯需求

| 項目 | 版本 |
|------|------|
| Node.js | 24.x |
| pnpm | 12.x |
| Docker Desktop / Docker Engine | Compose v2 支援 |
| 網路 | 可存取 Hugging Face、GitHub、npm 等 |
| 硬碟空間 | 數 GB（模型權重、wasm 編譯檔案） |
| 編譯時間 | 冷啟動約數十分鐘 |

---

### 3. 安裝步驟

#### 3.1 從 Chrome Web Store 安裝（推薦）

1. 前往 Chrome Web Store 頁面：
   - https://chrome.google.com/webstore/detail/mhlbjjijfkoghmcjndgdimhdlfkhadfl
2. 點擊「新增至 Chrome」
3. 確認授權後，擴充功能即完成安裝

#### 3.2 從 Firefox 安裝

1. 目前需使用「暫時性擴充功能」方式安裝（等待 AMO 上架）
2. 前往 `about:debugging`
3. 選擇「此 Firefox」→「載入暫時性附加元件」
4. 選取 `.output/firefox-mv3/manifest.json`（需先建置，見第 4 節）

#### 3.3 自行編譯與安裝（進階）

##### 步驟 1：安裝開發環境

```bash
## 安裝 Node.js 24.x
## Windows: 從 https://nodejs.org 下載安裝器
## macOS: brew install node@24
## Linux: curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash - && sudo apt-get install node

## 安裝 pnpm 12.x
npm install -g pnpm@12

## 驗證版本
node --version  # 應為 v24.x
pnpm --version  # 應為 12.x
```

##### 步驟 2：複製倉庫並安裝相依套件

```bash
git clone https://github.com/jammaru/sakutto.git
cd sakutto

## 安裝 npm 相依套件
pnpm install
```

##### 步驟 3：建置 PLaMo 運算環境（必須）

```bash
## 建置 wllama 運算庫
pnpm build:wllama

## 驗證建置
pnpm verify:wllama
```

**注意事項：**
- `pnpm build:wllama` 需要 Docker，會在容器中編譯 WebAssembly
- 首次建置需要數十分鐘（冷啟動）
- 編譯的 wasm 檔案不會納入 Git 倉庫
- 驗證步驟確保檔案完整性

##### 步驟 4：建置擴充功能

```bash
## Chrome 擴充功能（MV3）
pnpm build

## Firefox 擴充功能（MV3）
pnpm build:firefox
```

##### 步驟 5：安裝擴充功能

**Chrome：**
1. 開啟 `chrome://extensions`
2. 開啟「開發人員模式」
3. 選擇「載入未封裝」
4. 選取 `.output/chrome-mv3` 目錄

**Firefox：**
1. 開啟 `about:debugging`
2. 選擇「此 Firefox」
3. 選擇「載入暫時性附加元件」
4. 選取 `.output/firefox-mv3/manifest.json`

---

### 4. 測試步驟

#### 4.1 基本功能測試

##### 測試 1：頁面翻譯

1. 開啟任意英文網頁（建議使用 Wikipedia 或長篇文章）
2. 按 `Alt+A`（Firefox：`Alt+Shift+A`）
3. 觀察頁面是否開始翻譯
4. 等待翻譯完成（首次需要下載 0.8B 模型）

**預期結果：**
- 翻譯按鈕出現
- 模型開始下載（僅一次）
- 頁面內容逐步顯示翻譯
- 右上角可切換「僅原文」/「雙語並列」模式

##### 測試 2：選擇翻譯

1. 選取一段文字
2. 按 `Alt+S`（Firefox：`Alt+Shift+S`）
3. 確認彈出翻譯結果

**預期結果：**
- 選擇的文字被翻譯並顯示
- 不影響原始頁面

##### 測試 3：輸入框即時翻譯

1. 聚焦到文字輸入框（如搜尋框、留言框）
2. 按 `Alt+T`（Firefox：`Alt+Shift+T`）
3. 開始輸入文字
4. 觀察「あA」按鈕旁的翻譯預覽

**預期結果：**
- 輸入時即時顯示翻譯預覽
- 再次按 `Alt+T` 可替換原文
- 可隱藏「あA」按鈕（設定中）

##### 測試 4：文字輸入頁面翻譯

1. 開啟「已輸入文字」頁面（https://sakutto.jammaru.com）
2. 按 `Ctrl+Enter`（macOS：`⌘+Enter`）
3. 輸入或貼上文字
4. 點擊「翻譯」

**預期結果：**
- 支援長文本（最多 100,000 字元）
- 顯示翻譯結果並可複製

#### 4.2 語言支援測試

##### 測試步驟

1. 開啟擴充功能選單
2. 確認「語言設定」中顯示以下語言：
   - 來源語言：自動偵測（53 種支援）
   - 目標語言：預設為瀏覽器 UI 語言

**支援語言清單（53 種）：**
- 英語、日語、中文（簡體/繁體）、韓語、越南語、泰語、印尼語
- 西班牙語、葡萄牙語、法語、德語、意大利語、俄語
- 以及其他多達 53 種語言（詳細清單請查閱 PLaMo 官方文件）

**Chrome 特殊：**
- 11 種語言（cs, da, el, fi, kn, no, pt, ro, sv, tr, uk）僅在 Chrome 中使用瀏覽器內建翻譯
- Firefox 隱藏這些目標語言選項

---

### 5. 驗證步驟

#### 5.1 功能驗證

##### 驗證 1：翻譯正確性

1. 選擇已知翻譯的段落（如官方例句）
2. 使用 Sakutto 翻譯
3. 與瀏覽器內建翻譯或其他參考來源比對

**驗證指標：**
- 語意正確
- 語法通順
- 專有名詞正確

##### 驗證 2：隱私設定

1. 開啟擴充功能選單 → 設定
2. 確認「隱私」頁面顯示：
   - 不傳送任何資料到外部伺服器
   - 不追蹤使用情況
   - 不儲存帳號資訊

3. 使用網路監控工具（如 Wireshark、Fiddler）監控擴充功能網路請求

**預期結果：**
- 唯一網路請求：從 Hugging Face 下載模型（僅初次）
- 無其他對外連線

##### 驗證 3：效能測試

**Chrome 測試（RTX 4090 為例）：**

| 測試項目 | 預期表現 |
|----------|----------|
| 首次翻譯（含模型下載） | 約 2-5 秒（依網路速度） |
| 翻譯完成時間（長文章） | CPU：約 3-5 秒 / WebGPU：約 1-2 秒 |
| 即時翻譯輸入框 | 即時預覽，無明顯延遲 |

**Firefox 測試（RTX 4070 Ti SUPER 為例）：**

| 測試項目 | 預期表現 |
|----------|----------|
| WebGPU 模式（kick on） | 全頁約 1.6-1.9 秒 |
| CPU 模式 | 全頁約 15-16 秒 |
| 首次句子顯示 | WebGPU：約 0.5-0.8 秒 |

#### 5.2 硬體適配驗證

##### WebGPU 測試

1. 開啟擴充功能設定 → 診斷
2. 確認顯示 GPU 資訊：
   - GPU 名稱
   - 是否支援 `shader-f16`
   - WebGPU 狀態

3. 觀察翻譯時的效能層級顯示

**預期結果：**
- NVIDIA GPU：自動使用 WebGPU 模式
- AMD/Intel GPU：可能使用 CPU 模式或 WebGPU（依硬體支援）
- 無 WebGPU 硬體：自動切換至 CPU 模式

##### 錯誤處理測試

**情境 1：WebGPU 失敗**
1. 在系統設定中停用 WebGPU
2. 重新整理頁面
3. 確認自動切換至 CPU 模式

**預期結果：**
- 不拋出錯誤
- 使用 CPU 繼續翻譯（單執行緒）

**情境 2：記憶體不足**
1. 開啟多個分頁並翻譯
2. 觀察擴充功能設定 → 診斷

**預期結果：**
- 顯示記憶體使用量
- 可設定模型大小（預設 0.8B）

#### 5.3 快捷鍵驗證

| 功能 | Windows/Linux | macOS | Firefox |
|------|---------------|-------|---------|
| 翻譯頁面 | `Alt+A` | `Option+A` | `Alt+Shift+A` |
| 切換雙語/原文 | `Alt+B` | `Option+B` | `Alt+Shift+B` |
| 翻譯選取 | `Alt+S` | `Option+S` | `Alt+Shift+S` |
| 翻譯輸入 | `Alt+T` | `Option+T` | `Alt+Shift+T` |

**驗證步驟：**
1. 按各快捷鍵
2. 確認對應功能啟動
3. 確認不會與瀏覽器預設功能衝突

---

### 6. 常見問題（FAQ）

#### Q1：首次使用很慢，是否正常？
**A：** 是。首次需要下載 PLaMo 模型（約數百 MB）。之後會快很多。

#### Q2：為什麼有些語言翻譯品質較差？
**A：** PLaMo 支援 53 種語言，但模型對不同語言的訓練程度不同。建議優先使用主要語言。

#### Q3：擴充功能佔用太多記憶體？
**A：** 預設模型為 0.8B，記憶體占用約數十 MB。可在設定中調整。

#### Q4：如何在設定中修改翻譯目標語言？
**A：** 開啟擴充功能選單 → 設定 → 選擇目標語言。也可針對特定網站設定。

#### Q5：擴充功能是否支援離線使用？
**A：** 模型下載後即可離線使用（需網路下載模型）。翻譯本身不依賴網路。

#### Q6：如何移除擴充功能？
**A：** Chrome/Firefox 擴充功能管理頁 → 移除即可。模型會自動刪除。

---

### 7. 進階設定

#### 7.1 設定檔案位置

| 瀏覽器 | 設定位置 |
|--------|----------|
| Chrome | `%APPDATA%\Google\Chrome\User Data\Default\Extensions\<extension-id>/` |
| Firefox | `%APPDATA%\Mozilla\Firefox\Profiles\<profile>.default\extensions\<extension-id>/` |

#### 7.2 開發者模式

若要修改擴充功能代碼：

```bash
## 開發建置（不最小化）
pnpm dev

## 監聽檔案變更
## 自動重新載入擴充功能
```

#### 7.3 效能調校

**Chrome 效能層級：**
- 0 (g)：WebGPU，16 並行（最佳效能）
- 1-4：WebGPU，減少並行
- 5：CPU，多執行緒
- 6：CPU，單執行緒（最省資源）

**Firefox 效能層級：**
- GPU mode (kick on/off)
- CPU mode (單執行緒)

設定位置：擴充功能選單 → 設定 → 效能

---

### 8. 參考資源

#### 官方資源
- GitHub: https://github.com/jammaru/sakutto
- Chrome Web Store: https://chrome.google.com/webstore/detail/mhlbjjijfkoghmcjndgdimhdlfkhadfl
- 隱私權政策：https://jammaru.com/sakutto/privacy/
- Discord 社群：https://discord.gg/pdSRBaSr38

#### 技術文件
- BUILDING.md: 建置流程說明
- TRANSLATING.md: 多語言支援說明
- FIREFOX.md: Firefox 相容性說明

#### 依賴專案
- PLaMo 3 Translate: https://huggingface.co/pfnet/plamo-3-translate-0.8b-GGUF
- wllama: https://github.com/ngxson/wllama
- llama.cpp: https://github.com/ggml-org/llama.cpp

---

### 9. 授權與開源

| 組件 | 授權 |
|------|------|
| 專案代碼 | MIT |
| PLaMo 3 Translate | PLaMo Community License |
| llama.cpp / wllama / Emscripten / Dawn / Svelte | 各自授權（見 NOTICE 文件） |

**重要：**
- 專案代碼採用 MIT 授權
- 模型權重採用 PLaMo Community License
- 商業使用需符合 PLaMo 條款（年收入未超過 10 億日圓者可申請商業授權）

---

### 10. 貢獻者資訊

**開發者：** jammaru
**版本記錄：** 見 CHANGELOG.md
**贊助計畫：** https://github.com/sponsors/jammaru

**注意：** 此擴充功能為獨立開發，與 Preferred Networks Inc. 無關。

---

*最後更新：2026-11-09*
