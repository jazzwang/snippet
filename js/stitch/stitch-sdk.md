# @google/stitch-sdk 技術報告

**版本**: 1.x  
**日期**: 2026-11-08  
**語言**: 繁體中文（台灣技術用詞）

---

## 摘要

`@google/stitch-sdk` 是 Google 開發的程式庫，用於自動生成 UI 畫面並程式化提取 HTML 與螢幕截圖。本報告涵蓋安裝、測試與驗證的完整步驟，適用於台灣開發環境。

---

## 1. 環境準備

### 1.1 系統需求

| 項目 | 要求 |
|------|------|
| Node.js | 18.0+ |
| npm | 9.0+ |
| 作業系統 | Windows / macOS / Linux |

### 1.2 準備 API 金鑰

從 Google Cloud Console 取得 Stitch API 金鑰：

```bash
# 設定環境變數（Windows PowerShell）
$env:STITCH_API_KEY="your-api-key-here"

# 設定環境變數（Windows CMD）
set STITCH_API_KEY=your-api-key-here

# 設定環境變數（macOS / Linux）
export STITCH_API_KEY="your-api-key-here"
```

---

## 2. 安裝步驟

### 2.1 基礎安裝

```bash
npm install @google/stitch-sdk
```

### 2.2 使用 AI SDK 整合（可選）

如需與 Vercel AI SDK 整合，需額外安裝：

```bash
npm install @google/stitch-sdk ai
```

### 2.3 使用 ADK 整合（可選）

如需與 Google ADK 整合，需額外安裝：

```bash
npm install @google/stitch-sdk @google/adk
```

---

## 3. 測試步驟

### 3.1 基本功能測試

```typescript
import { stitch } from "@google/stitch-sdk";

// 取得所有專案
const projects = await stitch.projects();
console.log(`找到 ${projects.length} 個專案`);

// 參考專案並列出畫面
const project = stitch.project("your-project-id");
const screens = await project.screens();
console.log(`該專案共有 ${screens.length} 個畫面`);
```

### 3.2 產生畫面測試

```typescript
import { stitch } from "@google/stitch-sdk";

const project = stitch.project("your-project-id");

// 從文字提示產生畫面
const screen = await project.generate(
  "一個登入頁面，包含 Email 與密碼欄位",
);

// 取得 HTML 下載網址
const htmlUrl = await screen.getHtml();
console.log("HTML:", htmlUrl);

// 取得截圖下載網址
const imageUrl = await screen.getImage();
console.log("截圖:", imageUrl);
```

### 3.3 編輯畫面測試

```typescript
const screen = await project.generate("一個儀表板，包含圖表");

// 編輯現有畫面
const edited = await screen.edit("將背景改為深色並新增側邊欄");

// 取得編輯後的 HTML
const editedHtml = await edited.getHtml();
console.log("編輯後 HTML:", editedHtml);
```

### 3.4 產生變體測試

```typescript
const variants = await screen.variants(
  "嘗試不同的色彩方案",
  {
    variantCount: 3,
    creativeRange: "EXPLORE",
    aspects: ["COLOR_SCHEME", "LAYOUT"],
  }
);

for (const variant of variants) {
  const htmlUrl = await variant.getHtml();
  console.log(`變體 ${variant.id}:`, htmlUrl);
}
```

**變體選項說明**：

| 欄位 | 類型 | 預設值 | 說明 |
|------|------|--------|------|
| `variantCount` | `number` | 3 | 產生變體數量（1–5） |
| `creativeRange` | `string` | `"EXPLORE"` | `"REFINE"` / `"EXPLORE"` / `"REIMAGINE"` |
| `aspects` | `string[]` | 全部 | `"LAYOUT"` / `"COLOR_SCHEME"` / `"IMAGES"` / `"TEXT_FONT"` / `"TEXT_CONTENT"` |

### 3.5 使用工具客戶端測試

```typescript
import { stitch } from "@google/stitch-sdk";

// 列出可用工具
const { tools } = await stitch.listTools();
for (const tool of tools) {
  console.log(`工具 ${tool.name}: ${tool.description}`);
}

// 直接呼叫工具
const result = await stitch.callTool("create_project", {
  title: "我的應用程式",
});
console.log("專案建立:", result);
```

---

## 4. 驗證步驟

### 4.1 使用 StitchToolClient 驗證

```typescript
import { StitchToolClient } from "@google/stitch-sdk";

const client = new StitchToolClient({
  apiKey: "your-api-key-here",
});

try {
  const result = await client.callTool("create_project", {
    title: "驗證專案",
  });
  console.log("專案建立成功:", result);
  await client.close();
} catch (error) {
  console.error("失敗:", error);
  await client.close();
}
```

### 4.2 使用 AI SDK 整合驗證

```typescript
import { generateText, stepCountIs } from "ai";
import { google } from "@ai-sdk/google";
import { stitchTools } from "@google/stitch-sdk/ai";

const { text, steps } = await generateText({
  model: google("gemini-2.5-flash"),
  tools: stitchTools(),
  prompt: "建立一個專案並產生現代化的儀表板，包含統計卡片",
  stopWhen: stepCountIs(5),
});

// 模型自動呼叫工具
const toolCalls = steps.flatMap((step) => step.toolCalls);
console.log(`模型呼叫 ${toolCalls.length} 個工具`);
```

### 4.3 使用 ADK 整合驗證

```typescript
import { stitchAdkTools } from "@google/stitch-sdk/adk";
import { LlmAgent } from "@google/adk";

// 取得所有 Stitch 工具並格式化為 ADK FunctionTools
const tools = stitchAdkTools();

// 將工具傳給 ADK Agent
const designerAgent = new LlmAgent({
  name: "設計師",
  model: "gemini-2.5-pro",
  instruction: "你是一名設計師。建立一個專案並產生畫面。",
  tools,
});

// 執行 Agent
const response = await designerAgent.run("建立一個登入頁面");
console.log(response);
```

### 4.4 使用 MCP Proxy Server 驗證

```typescript
import { StitchProxy } from "@google/stitch-sdk";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";

const proxy = new StitchProxy({
  apiKey: "your-api-key-here",
});

const transport = new StdioServerTransport();
await proxy.start(transport);
```

---

## 5. 錯誤處理

### 5.1 基本錯誤處理

```typescript
import { stitch, StitchError } from "@google/stitch-sdk";

try {
  const project = stitch.project("invalid-project-id");
  await project.screens();
} catch (error) {
  if (error instanceof StitchError) {
    console.error("錯誤代碼:", error.code); // 例如："UNKNOWN_ERROR"
    console.error("錯誤訊息:", error.message);
    console.error("是否可復原:", error.recoverable);
  } else {
    throw error;
  }
}
```

### 5.2 錯誤代碼清單

| 代碼 | 說明 |
|------|------|
| `AUTH_FAILED` | 認證失敗 |
| `NOT_FOUND` | 專案或畫面不存在 |
| `PERMISSION_DENIED` | 無權限 |
| `RATE_LIMITED` | 速率限制 |
| `NETWORK_ERROR` | 網路錯誤 |
| `VALIDATION_ERROR` | 輸入驗證失敗 |
| `CLARIFICATION_REQUIRED` | 需要澄清問題 |
| `UNKNOWN_ERROR` | 未知錯誤 |

### 5.3 處理需要澄清的問題

```typescript
import { stitch, StitchError } from "@google/stitch-sdk";

const project = stitch.project("4044680601076201931");

try {
  await project.generate("一個會幫你選早晨咖啡的應用程式");
} catch (error) {
  if (error instanceof StitchError && error.code === "CLARIFICATION_REQUIRED") {
    // 取得澄清問題與建議回覆
    console.log("問題:", error.clarification?.question);
    const reply = error.clarification?.suggestions[0] ?? "保持簡單";
    // 使用回覆重新呼叫
    const screen = await project.generate(reply);
    console.log("畫面 ID:", screen.id);
  } else {
    throw error;
  }
}
```

---

## 6. 配置選項

### 6.1 環境變數

| 變數 | 必要 | 說明 |
|------|------|------|
| `STITCH_API_KEY` | 是（或使用 OAuth） | 認證 API 金鑰 |
| `STITCH_ACCESS_TOKEN` | 否 | OAuth 存取令牌（API 金鑰替代） |
| `GOOGLE_CLOUD_PROJECT` | OAuth 時 | Google Cloud 專案 ID |
| `STITCH_HOST` | 否 | 覆寫 MCP 伺服器網址 |

### 6.2 程式配置

```typescript
import { Stitch, StitchToolClient } from "@google/stitch-sdk";

// 使用 StitchToolClient 建立自定義客戶端
const client = new StitchToolClient({
  apiKey: "your-api-key-here",
  baseUrl: "https://stitch.googleapis.com/mcp",
  timeout: 300_000,
});

const sdk = new Stitch(client);
const projects = await sdk.projects();
```

**配置選項**：

| 選項 | 類型 | 預設值 | 說明 |
|------|------|--------|------|
| `apiKey` | `string` | `STITCH_API_KEY` | API 金鑰 |
| `accessToken` | `string` | `STITCH_ACCESS_TOKEN` | OAuth 令牌 |
| `projectId` | `string` | `GOOGLE_CLOUD_PROJECT` | Cloud 專案 ID |
| `baseUrl` | `string` | `https://stitch.googleapis.com/mcp` | MCP 伺服器網址 |
| `timeout` | `number` | `300000` | 請求超時（毫秒） |

認證需要 `apiKey` 或 `accessToken` + `projectId`。

---

## 7. API 參考

### 7.1 Stitch（根類別）

管理專案。

| 方法 | 參數 | 返回 | 說明 |
|------|------|------|------|
| `projects()` | — | `Promise<Project[]>` | 列出所有可存取之專案 |
| `project(id)` | `id: string` | `Project` | 透過 ID 參考專案（無需 API 呼叫） |

### 7.2 Project（專案類別）

包含畫面的 Stitch 專案。

| 屬性 | 類型 | 說明 |
|------|------|------|
| `id` | `string` | `projectId` 的別名 |
| `projectId` | `string` | 裸專案 ID（無 `projects/` 前綴） |

| 方法 | 參數 | 返回 | 說明 |
|------|------|------|------|
| `generate(prompt, deviceType?)` | `prompt: string`, `deviceType?: DeviceType` | `Promise<Screen>` | 從文字提示產生畫面 |
| `screens()` | — | `Promise<Screen[]>` | 列出專案中的所有畫面 |
| `getScreen(screenId)` | `screenId: string` | `Promise<Screen>` | 透過 ID 檢索特定畫面 |
| `createDesignSystem(designSystem)` | `designSystem: object` | `Promise<DesignSystem>` | 為專案建立設計系統 |
| `listDesignSystems()` | — | `Promise<DesignSystem[]>` | 列出專案中的所有設計系統 |
| `designSystem(id)` | `id: string` | `DesignSystem` | 透過 ID 參考設計系統（無需 API 呼叫） |

**DeviceType**：`"MOBILE"` \| `"DESKTOP"` \| `"TABLET"` \| `"AGNOSTIC"`

### 7.3 Screen（畫面類別）

已產生的 UI 畫面。提供 HTML 與截圖存取。

| 屬性 | 類型 | 說明 |
|------|------|------|
| `id` | `string` | `screenId` 的別名 |
| `screenId` | `string` | 裸畫面 ID |
| `projectId` | `string` | 父專案 ID |

| 方法 | 參數 | 返回 | 說明 |
|------|------|------|------|
| `edit(prompt, deviceType?, modelId?)` | `prompt: string` | `Promise<Screen>` | 使用文字提示編輯畫面 |
| `variants(prompt, variantOptions, deviceType?, modelId?)` | `prompt: string`, `variantOptions: object` | `Promise<Screen[]>` | 產生設計變體 |
| `getHtml()` | — | `Promise<string>` | 取得畫面 HTML 下載網址 |
| `getImage()` | — | `Promise<string>` | 取得畫面截圖下載網址 |

**modelId**：`"GEMINI_3_8_FLASH"` \| `"GEMINI_3_5_FLASH_LITE"`（可選，預設為後端預設值）

`getHtml()` 與 `getImage()` 會使用產生回應中的快取資料（若有）。若畫面是從 `screens()` 或 `getScreen()` 載入，它們會自動呼叫 `get_screen` API。

### 7.4 DesignSystem（設計系統類別）

應用於專案與畫面的視覺主題或品牌。

| 屬性 | 類型 | 說明 |
|------|------|------|
| `id` | `string` | `assetId` 的別名 |
| `assetId` | `string` | 裸資產 ID（無 `assets/` 前綴） |
| `projectId` | `string` | 父專案 ID |

| 方法 | 參數 | 返回 | 說明 |
|------|------|------|------|
| `update(designSystem)` | `designSystem: object` | `Promise<DesignSystem>` | 更新設計系統主題 |
| `apply(selectedScreenInstances)` | `selectedScreenInstances: object[]` | `Promise<Screen[]>` | 將設計系統應用至畫面 |

**selectedScreenInstances** 是 `{ id: string, sourceScreen: string }` 物件的陣列。從 `project.data.screenInstances` 取得。

### 7.5 StitchToolClient（工具客戶端）

低階認證管道，用於直接存取 Stitch MCP 伺服器。在 AI Agent 等情境下使用。

| 方法 | 參數 | 返回 | 說明 |
|------|------|------|------|
| `callTool<T>(name, args)` | `name: string`, `args: Record<string, any>` | `Promise<T>` | 呼叫 MCP 工具 |
| `listTools()` | — | `Promise<{ tools }>` | 列出可用工具 |
| `connect()` | — | `Promise<void>` | 明確連線（`callTool` 會自動呼叫） |
| `close()` | — | `Promise<void>` | 關閉連線 |

---

## 8. 最佳實踐

1. **錯誤處理**：所有方法失敗時會拋出 `StitchError`，務必進行錯誤處理。
2. **快取利用**：`getHtml()` 與 `getImage()` 會自動使用快取資料，減少 API 呼叫。
3. **資源清理**：使用 `StitchToolClient` 時，記得在完成後呼叫 `close()`。
4. **明確配置**：在生產環境，建議使用明確的配置而非依賴環境變數。
5. **工具過濾**：使用 `stitchTools({ include: [...] })` 限制暴露的工具，提升安全性。

---

## 9. 免責聲明

此專案並非官方支援的 Google 產品，不適用於 [Google Open Source Software Vulnerability Rewards Program](https://bughunters.google.com/open-source-security)。

---

## 10. 授權

Apache 2.0 — 詳細資訊請參閱 [LICENSE](LICENSE)

---

*本報告根據 @google/stitch-sdk 官方文件撰寫（https://github.com/google-labs-code/stitch-sdk）*
