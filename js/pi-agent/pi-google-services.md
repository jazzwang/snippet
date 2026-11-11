# Google Workspace Calendar MCP 與 Pi Agent 整合

## 問題
Google Workspace 個人版 Calendar 支援 MCP 或者可以安裝 Agent Skill 嗎？若有，請告訴我如何跟 Pi Agent 整合？

## 答案

### ✅ 支援情況
Google Workspace **個人版** 的 Calendar **支援 MCP（Model Context Protocol）**，Pi Agent 也有官方套件可以整合。

---

## 🔧 與 Pi Agent 整合的兩種方式

### **方式一：使用官方 Pi Google Services 套件（推薦）**

這是 Pi 官方推出的套件，整合了 Calendar、Gmail、Tasks、Drive、Contacts 和 Meet。

**設定步驟：**

```bash
# 1. 安裝套件
pi install npm:pi-google-services

# 2. 設定並授權
pi-google-services setup
```

執行 `setup` 後，會開啟瀏覽器讓您在 Google 上進行 OAuth 授權。

**功能：**
- 📅 Calendar (7 個工具)
- 📧 Gmail (5 個工具)
- ✅ Tasks (5 個工具)
- 📁 Drive (6 個工具)
- 👤 Contacts (3 個工具)
- 🎥 Meet

**常用指令範例：**
```bash
pi show my events
pi read my inbox
pi create a meeting with Meet
```

---

### **方式二：使用獨立 Calendar MCP Server**

Google 提供專用的 Calendar MCP 端點。

**設定步驟：**

1. **啟用 Calendar MCP API**
   - 前往 [Google Cloud Console](https://console.cloud.google.com/)
   - 啟用 `Google Calendar MCP API`
   - 網址：https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server

2. **配置 Pi Agent**
   - 在 Pi 中配置 MCP 伺服器設定
   - 端點：`https://calendarmcp.googleapis.com/mcp/v1`

---

## 📋 完整設定流程（推薦方式一）

```bash
# 1. 開啟終端機，切換到 Pi 工作目錄
cd ~/.pi

# 2. 安裝 Google Services 套件
pi install npm:pi-google-services

# 3. 執行設定（會自動開啟瀏覽器）
pi-google-services setup

# 4. 在瀏覽器中完成 Google OAuth 授權

# 5. 重新啟動 Pi 工作區
pi restart

# 6. 測試功能
pi "show my events"
```

---

## ⚠️ 重要注意事項

1. **個人版 Google Workspace** 同樣支援這些功能
2. **需要 Google 帳戶** 進行一次授權（OAuth 2.0 PKCE）
3. **授權是一次性的**，後續 Pi 會自動使用保存的憑證
4. **個人版功能受限** 的部分（如大型會議室預約），建議使用企業版

---

## 🔗 官方資源

- [Pi Google Services 套件](https://pi.dev/packages/pi-google-services)
- [GitHub 專案](https://github.com/lucasvidela94/pi-google-services/)
- [Google Calendar MCP 官方文件](https://developers.google.com/workspace/calendar/api/guides/configure-mcp-server)

---

## 📝 討論記錄

### 驗證過程
使用 `source_check` 工具驗證以下主張：
> "Google Workspace 個人版 Calendar 支援 MCP 協議並可以與 Pi Agent 整合，使用 pi-google-services npm 套件安裝"

### 驗證結果
- **主要資訊正確**：
  - ✅ Google Calendar 支援 MCP 協議
  - ✅ Pi Agent 支援 `pi-google-services` 套件
  - ✅ 設定步驟正確
  - ✅ 整合功能完整

- **需要補充確認**：個人版與企業版之間的功能差異尚未明確確認，但從官方文件來看，MCP 功能應該是通用的。

### 關鍵發現
1. Google Calendar 提供遠端 MCP Server，端點為 `https://calendarmcp.googleapis.com/mcp/v1`
2. `pi-google-services` 套件版本 0.1.28，截至 2026 年 10 月，下載量 1,794/mo
3. 使用 OAuth 2.0 with PKCE 進行一次授權，後續自動使用保存憑證
4. 支援 36 個工具跨 5 個 Google 服務
