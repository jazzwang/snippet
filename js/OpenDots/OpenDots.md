# OpenDots 技術報告

**版本**: Alpha  
**最後更新**: 2024  
**授權**: MIT

---

## 摘要

OpenDots 是一個開源模板，用於構建持久化 AI 協作者（Dots），這些協作者可以在文字對話、通話和 Slack 之間切換。每個 Dot 都有獨立的電腦環境，可用於執行網頁瀏覽、檔案操作和系統命令。本報告提供詳細的技術架構說明和完整的測試步驟。

---

## 系統架構

### 核心技術棧

- **前端框架**: React + CopilotKit + AG-UI
- **後端**: TypeScript + Express
- **資料庫**: 本地工作區資料庫
- **AI 引擎**: CopilotKit Intelligence（可選自託管或本地 Docker 評估）
- **電腦模擬**: OpenBot 容器監督器和電腦服務

### 主要組件

| 組件 | 功能 | 位置 |
|------|------|------|
| Spaces | 工作文件的家 | `src/client/SpaceLibrary.tsx`, `src/client/SpaceWorkspace.tsx` |
| Specialist Dots | 具有特定角色和工具的 AI 代理 | `src/server/dot-agent.ts` |
| Dot Computers | 獨立電腦環境 | `src/server/computer-service.ts`, `deployment/computers/` |
| Review before saving | 保存前的人工審查 | `src/client/PageReviewCard.tsx` |
| Connections | MCP 服務工具連接 | `src/server/connection-tools.ts` |
| Composio | 第三方應用集成 | `src/server/composio.ts` |
| Voice Calls | 語音通話功能 | `src/client/CallView.tsx`, `src/server/voice.ts` |
| Slack 集成 | Slack 渠道連接 | `src/server/slack-channel.ts` |

---

## 安裝與設定步驟

### 步驟 1: 克隆專案

```bash
git clone https://github.com/CopilotKit/OpenDots.git
cd OpenDots
```

### 步驟 2: 環境變數設定

複製環境範例檔案並填入必要資訊：

```bash
cp .env.example .env
```

必要環境變數：

- `INTELLIGENCE_KEY`: CopilotKit Intelligence API 金鑰
- `COMPOSIO_API_KEY`（可選）: Composio API 金鑰
- `OWNER_ID`: 所有者的唯一識別碼

### 步驟 3: 安裝依賴

```bash
npm install
```

### 步驟 4: 啟動開發伺服器

```bash
npm run dev
```

預設訪問網址：http://localhost:3000

---

## 測試步驟（Step-by-Step）

### 測試 1: 基本功能測試

#### 步驟 1.1: 啟動應用程式

```bash
npm run dev
```

預期結果：應用程式在 `http://localhost:3000` 啟動，顯示主頁面。

#### 步驟 1.2: 檢查 Spaces 介面

1. 登入應用程式
2. 確認顯示 "Spaces Library"（空間書庫）
3. 確認可以切換 Grid 和 List 檢視模式

預期結果：可以正常瀏覽和切換空間檢視模式。

#### 步驟 1.3: 建立新空間

1. 點擊 "Create New Space" 按鈕
2. 輸入空間名稱（例如："Research Project"）
3. 選擇空間類型

預期結果：新空間成功建立並顯示在書庫中。

---

### 測試 2: Dot 配置與測試

#### 步驟 2.1: 建立第一個 Dot

1. 進入設定頁面
2. 點擊 "Add Dot"
3. 填入以下資訊：
   - **Name**: "Scout"
   - **Role**: "Research Assistant"
   - **Instructions**: "Help me research topics and summarize information"
   - **Permitted Tools**: 選擇允許的工具

預期結果：Dot 成功建立並顯示在清單中。

#### 步驟 2.2: 測試 Dot 文字對話

1. 選擇 "Scout" Dot
2. 在文字輸入框輸入："What are the latest developments in AI research?"
3. 發送訊息

預期結果：
- Dot 回應並進行研究
- 顯示工作更新和來源連結
- 可以展開側邊欄查看詳細結果

#### 步驟 2.3: 測試 Page Chat 功能

1. 在空間中開啟一個頁面
2. 點擊頁面的 Dot 按鈕
3. 在頁面聊天中輸入："Summarize this document"

預期結果：
- 開啟獨立的頁面對話
- Dot 讀取並摘要頁面內容
- 對話歷史與頁面連結

---

### 測試 3: 電腦功能測試（Computer Tools）

> **注意**: 此測試需要先設定 OpenBot 服務

#### 步驟 3.1: 設定 OpenBot 服務

1. 進入 `deployment/computers/` 目錄
2. 啟動 Docker 服務：
   ```bash
   docker-compose -f compose.computers.yml up -d
   ```
3. 確認服務運行：
   ```bash
   docker ps | grep openbot
   ```

#### 步驟 3.2: 測試網頁瀏覽

1. 在 Dot 聊天中輸入："Please open https://www.wikipedia.org"
2. 查看側邊欄的 Computer Panel

預期結果：
- Dot 成功開啟網頁
- 顯示即時瀏覽器視圖
- 可以控制瀏覽器（點擊、輸入、導航）

#### 步驟 3.3: 測試網頁操作

1. 在 Computer Panel 中：
   - 使用工具列點擊網頁元素
   - 在地址欄輸入新 URL
   - 執行搜尋查詢

預期結果：
- 瀏覽器操作正常執行
- 側邊欄顯示當前網頁狀態
- 操作歷史記錄可查

#### 步驟 3.4: 測試檔案存取

1. 在聊天中輸入："List files in my documents folder"
2. 查看 Computer Panel 的檔案視圖

預期結果：
- 顯示檔案清單
- 可以上傳和下載檔案
- 檔案操作有明確的權限控制

#### 步驟 3.5: 測試終端機訪問

1. 在聊天中輸入："Run ls -la command"
2. 查看 Computer Panel 的終端機輸出

預期結果：
- 終端機執行命令
- 輸出結果顯示在側邊欄
- 命令執行有明確的權限限制

---

### 測試 4: 保存前審查功能測試

#### 步驟 4.1: 測試 Human-in-the-loop 審查

1. 選擇一個 Dot（例如："Writer"）
2. 在聊天中輸入："Create a draft about machine learning"
3. 讓 Dot 生成草稿

預期結果：
- Dot 生成草稿內容
- 出現 "Review before saving" 卡片
- 顯示 "Approve & Save" 和 "Decline" 選項

#### 步驟 4.2: 批准草稿

1. 點擊 "Approve & Save"
2. 選擇保存的空間

預期結果：
- 草稿轉換為可編輯的 Space 頁面
- 返回編輯器介面
- 頁面連結回對話歷史

#### 步驟 4.3: 拒絕草稿

1. 選擇另一個 Dot（例如："Researcher"）
2. 讓其生成報告草稿
3. 點擊 "Decline"

預期結果：
- 草稿不被保存
- Dot 繼續對話，可以要求重新生成
- 對話歷史保留

---

### 測試 5: Connection 工具測試

#### 步驟 5.1: 設定 MCP 工具

1. 進入設定頁面
2. 選擇 "Connections"
3. 啟用所需的 MCP 工具（例如：GitHub、Email）

預期結果：工具成功啟用並顯示在清單中。

#### 步驟 5.2: 測試只讀工具

1. 在聊天中輸入："List my open GitHub issues"
2. 觀察工具執行行為

預期結果：
- 只讀工具自動執行
- 不需要人工確認
- 結果顯示在對話中

#### 步驟 5.3: 測試需要確認的工具

1. 在聊天中輸入："Create a new GitHub repository"
2. 觀察出現的確認卡片

預期結果：
- 出現 "Approve & Run" 卡片
- 需要用戶明確點擊確認
- 只有確認後才執行工具

---

### 測試 6: Composio 集成測試

#### 步驟 6.1: 設定 Composio

1. 在 `.env` 檔案中添加：
   ```
   COMPOSIO_API_KEY=your_composio_api_key
   ```
2. 重新啟動應用程式
3. 進入設定頁面
4. 啟用 "Connected apps"
5. 選擇要連接的工具（例如：`gmail`, `google_calendar`）

預期結果：
- 工具列表顯示已連接的應用
- 可以為每個 Dot 設定特定的工具清單

#### 步驟 6.2: 測試 Gmail 工具

1. 選擇已設定 Gmail 的 Dot
2. 在聊天中輸入："Check my emails"
3. 觀察回應

預期結果：
- Dot 列出電子郵件
- 可以閱讀內容
- 需要確認才能執行寫入操作

#### 步驟 6.3: 測試日曆工具

1. 選擇已設定 Google Calendar 的 Dot
2. 在聊天中輸入："Create a meeting next Friday"
3. 觀察確認卡片

預期結果：
- 出現 "Approve & Run" 卡片
- 確認後建立日曆事件
- 返回對話確認結果

---

### 測試 7: Voice Call 功能測試

#### 步驟 7.1: 設定語音提供者

1. 進入設定頁面
2. 配置語音提供者（需要額外設定）
3. 確認設定正確

預期結果：語音功能正常運作。

#### 步驟 7.2: 測試語音通話

1. 選擇支援語音的 Dot
2. 點擊 "Start Call" 按鈕
3. 確認通話介面顯示：
   - Live 計時器
   - 用戶和 Dot 的獨立的字幕
   - Microphone 和 Speaker 的靜音控制
   - Minimize 按鈕

預期結果：
- 通話介面正常顯示
- 可以開始和結束語音對話
- 可以切換回文字聊天

#### 步驟 7.3: 測試語音與計算結合

1. 在語音通話中說話
2. 觀察 Dot 同時進行文字處理
3. 確認兩者可以並行運作

預期結果：
- 語音和文字對話共用同一對話背景
- 工具權限保持一致
- 可以切換視圖而不丟失上下文

---

### 測試 8: Slack 集成測試

#### 步驟 8.1: 設定 Slack 連接

1. 進入設定頁面
2. 選擇 "Slack"
3. 使用 Channels SDK 連接
4. 配置 Workspace/User 白名單
5. 選擇專用的 Specialist Dot

預期結果：
- 成功建立 Slack 連接
- 顯示連接狀態

#### 步驟 8.2: 測試 Slack 對話

1. 在 Slack 中提及 Dot（例如：@Scout）
2. 觀察對話線
3. 繼續在 Slack 線中對話

預期結果：
- 成功開啟 Slack 對話線
- 對話歷史可查
- 可以切換回 Web 介面

---

### 測試 9: 多空間訪問測試

#### 步驟 9.1: 設定 Dot 訪問多個空間

1. 進入 Dot 設定
2. 在 "Spaces" 選項中選擇：
   - Space A（例如："Research"）
   - Space B（例如："Personal"）

預期結果：
- Dot 可以訪問所有指定空間
- 每個空間有獨預設保存位置

#### 步驟 9.2: 測試跨空間工作

1. 在 Space A 中開啟頁面
2. 在聊天中要求 Dot 參考 Space B 的內容
3. 觀察 Dot 的回應

預期結果：
- Dot 可以訪問多個空間
- 跨空間資訊整合正常運作

---

### 測試 10: Autosave 功能測試

#### 步驟 10.1: 測試自動保存

1. 開啟編輯器
2. 輸入內容但不手動保存
3. 關閉編輯器

預期結果：
- 自動保存報告其進度
- 失敗的保存保留草稿
- 版本檢查防止覆蓋新版本

#### 步驟 10.2: 測試版本恢復

1. 編輯已保存的頁面
2. 進行大幅修改
3. 意外關閉頁面

預期結果：
- 可以恢復未完成的編輯
- 版本歷史可查
- 可以比較不同版本的內容

---

## 故障排除

### 常見問題

#### 問題 1: 電腦功能無法執行

**症狀**: Dot 無法執行網頁瀏覽或系統命令

**解決方案**:
1. 確認 OpenBot 服務正在運行：`docker ps`
2. 檢查 `.env` 檔案中的 `COMPUTER_CREDENTIAL` 設定
3. 確認 Dot 有電腦權限設定
4. 查看伺服器日誌：`npm run server`

#### 問題 2: Composio 工具無法連接

**症狀**: 選擇 Composio 工具時顯示錯誤

**解決方案**:
1. 確認 `COMPOSIO_API_KEY` 已正確設定
2. 重新啟動應用程式
3. 在設定中重新啟用 Connected apps
4. 確認 `OWNER_ID` 設定穩定

#### 問題 3: CopilotKit Intelligence 錯誤

**症狀**: 對話無法進行，顯示 Intelligence 錯誤

**解決方案**:
1. 確認 `INTELLIGENCE_KEY` 已正確設定
2. 檢查 CopilotKit 服務狀態
3. 使用本地 Docker 評估：參見 `docs/SETUP.md#local-intelligence-evaluation`
4. 或配置自託管 CopilotKit Intelligence

#### 問題 4: 語音功能無效

**症狀**: 語音通話無法啟動

**解決方案**:
1. 確認語音提供者已正確設定
2. 檢查瀏覽器麥克風權限
3. 確認網路連線正常
4. 查看 Console 中的錯誤訊息

---

## 性能最佳化建議

### 前端最佳化

1. **延遲加載**: 使用 React.lazy() 延遲加載大型組件
2. **虛擬化列表**: 對大量項目使用 virtualization
3. **優化圖片**: 使用 WebP 格式和 lazy loading

### 後端最佳化

1. **資料庫索引**: 為常用查詢欄位建立索引
2. **快取層級**: 使用 Redis 快取頻繁訪問的資料
3. **API 分頁**: 對列表查詢實施分頁限制

### 資源管理

1. **瀏覽器限制**: 每個 Dot 最多開 10 個標籤頁
2. **記憶體監控**: 設定記憶體警報閾值
3. **自動清理**: 定期清理未使用的瀏覽器視圖

---

## 安全性考量

### 權限控制

1. **電腦權限**: 每個 Dot 有獨立的權限設定
2. **工具權限**: 可為每個 Dot 啟用/停用工具
3. **空間權限**: Dot 只能訪問授權的空間

### 資料保護

1. **API 金鑰**: 所有金鑰儲存在伺服器端
2. **傳輸加密**: 使用 HTTPS 加密所有通訊
3. **存取控制**: 實施適當的存取控制清單 (ACL)

### 審計日誌

1. **操作記錄**: 記錄所有工具執行和檔案存取
2. **使用者動作**: 記錄人工審查決策
3. **安全事件**: 記錄可疑活動和錯誤

---

## 未來發展方向

### 短期目標

1. **更多預設工具**: 增加更多 MCP 和 Composio 工具
2. **改進 UI**: 優化使用者介面和體驗
3. **多語言支援**: 支援更多語言的對話

### 長期目標

1. **Edge 計算**: 將部分功能移至邊緣計算
2. **跨平台**: 擴展到更多平台（iOS、Android）
3. **企業功能**: 增加企業級特性和支援

---

## 參考資源

- [OpenDots GitHub](https://github.com/CopilotKit/OpenDots)
- [CopilotKit 官方文件](https://docs.copilotkit.ai/)
- [OpenBot 電腦模擬](https://github.com/CopilotKit/OpenBot)
- [Composio 集成](https://composio.dev)
- [AG-UI 框架](https://docs.ag-ui.com/introduction)

---

## 貢獻

OpenDots 是開源專案，歡迎貢獻。請參見 [CONTRIBUTING.md](CONTRIBUTING.md) 獲取指導。

---

## 授權

本專案採用 MIT 授權。詳細資訊請參見 [LICENSE](LICENSE) 檔案。
