# FreeLLMAPI 技術摘要

> **Repository:** <https://github.com/tashfeenahmed/freellmapi>
> **License:** MIT
> **撰寫日期：** 2025-07

---

## 一、專案概述

FreeLLMAPI 是一個開源的 LLM 代理路由器（proxy router），將 **34 家免費 LLM 提供商** 的免費額度彙整為單一的 OpenAI 相容 API 端點。透過智慧路由與自動故障轉移，使用者每月可獲得約 **74 億 tokens** 的免費推論能力，涵蓋 **474 個模型系列 / 635 個免費端點**。

核心理念：每家 AI 實驗室的免費額度單獨使用只是玩具，但疊加在一起便構成可用的推論容量。FreeLLMAPI 將「手動管理 34 個 SDK、34 組速率限制」的痛苦，收斂為一個統一端點。

---

## 二、系統架構

```
┌──────────────────┐   Bearer freellmapi-…   ┌─────────────────────────┐
│  OpenAI SDK /    │ ──────────────────────▶ │  Express proxy (:3001)  │
│  curl / 任何     │ ◀────────────────────── │  /v1/chat/completions   │
│  OpenAI 客戶端   │      streamed tokens    └────────────┬────────────┘
└──────────────────┘                                      │
                                                          ▼
                             ┌────────────────────────────────────────────────┐
                             │  Router                                        │
                             │   1. 挑選優先順序最高、有健康 key 且             │
                             │      未超出速率限制的模型                        │
                             │   2. 解密 key，呼叫上游 Provider SDK            │
                             │   3. 遇到 429/5xx → cooldown + 轉移至下一模型   │
                             └────────────────────────────────────────────────┘
                                          │
   ┌──────────────┬────────────┬──────────┴─────────┬─────────────┬──────────┐
   ▼              ▼            ▼                    ▼             ▼          ▼
 Google         Groq        Cerebras           OpenRouter        HF       …29 more
```

### 核心元件

| 元件 | 路徑 | 說明 |
|------|------|------|
| **Router** | `server/src/services/router.ts` | 每次請求挑選最佳模型 |
| **Rate-limit Ledger** | `server/src/services/ratelimit.ts` | 記憶體內 RPM/RPD/TPM/TPD 計數器，以 SQLite 持久化，搭配 429 cooldown |
| **Provider Adapters** | `server/src/providers/*.ts` | 每家 provider 一個檔案，實作 `chatCompletion()` 與 `streamChatCompletion()` |
| **Health Service** | `server/src/services/health.ts` | 定期探測維持 key 健康狀態 |
| **Dashboard** | `client/` | React + Vite + shadcn/ui 管理介面 |
| **Storage** | SQLite (`better-sqlite3`) | AES-256-GCM 信封加密儲存 API keys |
| **CLI** | `cli/` | 命令列工具，用於設定與管理 |

---

## 三、路由機制

### 3.1 自動故障轉移（Automatic Fallover）

當選定的 provider 回傳 429、5xx 或逾時，路由器會：
1. 跳過該 provider
2. 將對應 key 加入短暫 cooldown
3. 嘗試 fallback chain 中的下一個模型（最多 20 次嘗試）

### 3.2 六種路由策略

| 策略 | 模型名稱 | 說明 |
|------|----------|------|
| Priority | `auto` | 依使用者手動排序 |
| Balanced | `auto:balanced` | 預設混合策略 |
| Smartest | `auto:smart` | 偏好最高智慧的模型 |
| Fastest | `auto:fast` | 偏好低延遲模型 |
| Reliable | `auto:reliable` | 偏好高成功率模型 |
| Custom | 自訂權重 | 使用者自定義的混合權重 |

路由評分基於即時的每模型量測值（速度、能力、速率限制餘裕、近期錯誤率），底層採用 **Thompson Sampling Bandit** 演算法。

### 3.3 Sticky Sessions

多輪對話會在 30 分鐘內維持與同一模型的連線，避免中途切換模型造成的幻覺問題。

### 3.4 統一模型（Unified Models）

同一邏輯模型由多家 provider 提供時（如 GLM-4.7 同時在 Cloudflare 與 Z.ai 上），會合併為單一條目，在 `/v1/models` 中只出現一次，並在同群組內嚴格 failover。

---

## 四、API 相容性

### 4.1 OpenAI 相容端點

- `POST /v1/chat/completions` — 聊天完成（含串流）
- `POST /v1/embeddings` — 嵌入向量
- `POST /v1/images/generations` — 圖片生成
- `POST /v1/videos/generations` — 影片生成
- `POST /v1/audio/speech` — 語音合成
- `GET /v1/models` — 模型列表
- `GET /v1/docs` — 互動式 OpenAPI 文件

### 4.2 Anthropic 相容端點

- `POST /v1/messages` — Claude Messages API
- `POST /v1/messages/count_tokens` — Token 計數

### 4.3 Gemini 原生端點

- `POST /v1beta/models/{model}:generateContent`
- `POST /v1beta/models/{model}:streamGenerateContent`

### 4.4 Ollama 模擬端點

- `/api/*` — 可選啟用的 Ollama 相容 NDJSON 串流介面

### 4.5 特色功能

- **Tool Calling** — 支援 OpenAI 風格的 function calling，跨 provider 翻譯
- **Tool-call Rescue** — 模型以純文字輸出 tool call 時，自動搶救為結構化 JSON
- **Vision** — 自動將含圖片的請求路由至支援視覺的模型
- **Fusion** — 多模型平行推論，由 judge model 綜合產出最終答案
- **Structured Outputs** — 支援 `json_object` / `json_schema`，含 Gemini 原生 `responseSchema` 翻譯
- **Prompt Compression** — 可選的提示壓縮功能，降低 token 消耗
- **Response Cache** — 可選的精確匹配 LRU 快取，命中時零 provider 配額消耗

---

## 五、支援的 Provider（34 家）

主要包含：

| 類別 | Provider |
|------|----------|
| **雲端大廠** | Google (Gemini)、NVIDIA NIM、Cloudflare Workers AI |
| **推論加速** | Groq、Cerebras |
| **模型平台** | OpenRouter、HuggingFace、GitHub Models、ModelScope |
| **獨立廠商** | Mistral、Cohere、Zhipu (Z.ai)、Pollinations |
| **社群平台** | AI Horde、OVH AI Endpoints、Ollama Cloud |
| **自訂** | 任何 OpenAI 相容端點（llama.cpp、LM Studio、vLLM、Ollama 本地等） |

---

## 六、相容的 CLI 與程式碼代理

FreeLLMAPI 已驗證可與以下工具搭配使用：

- **Claude Code** / **Codex CLI** / **Gemini CLI**
- **Aider** / **Cline** / **Roo Code** / **Continue**
- **OpenCode** / **Goose** 及其他 OpenAI 相容客戶端

---

## 七、安全與儲存

- **AES-256-GCM 信封加密**：API key 加密後存入 SQLite，僅在請求時於記憶體中解密
- **統一 API Key**：客戶端僅需一組 `freellmapi-…` bearer token，不暴露上游 provider key
- **Dashboard 登入**：email + password 帳號（scrypt 雜湊），session-token 認證
- **可撤銷 URL Token**：為無 header 客戶端提供 `/v1/t/{token}/…` 路徑，以 hash 儲存、可即時撤銷
- **加密資料庫備份**：可選的定期加密 SQLite 快照

---

## 八、技術棧

| 層級 | 技術 |
|------|------|
| **後端** | Node.js + Express + TypeScript |
| **前端** | React + Vite + shadcn/ui + Tailwind CSS |
| **資料庫** | SQLite (`better-sqlite3`) |
| **加密** | AES-256-GCM |
| **部署** | Docker / Docker Compose / 桌面應用 (macOS, Windows) / Android (Google Play) |
| **CI/CD** | GitHub Actions |
| **國際化** | 支援 50+ 語言 |

---

## 九、部署方式

1. **Docker Compose**（推薦用於自架伺服器）
2. **桌面應用**（macOS / Windows 安裝檔）
3. **Android 應用**（Google Play）
4. **CLI 安裝**（npm / 安裝腳本）

---

## 十、限制與注意事項

| 限制 | 說明 |
|------|------|
| **額度即天花板** | 前沿模型（GPT-5.x、Grok 4.x 等）的每日配額最小，最容易被限制或下架 |
| **智慧度隨時間下降** | 頂級模型配額用完後，路由器會降級到較弱模型 |
| **延遲高度變異** | Cerebras/Groq 極快，其他 provider 不一定 |
| **免費額度隨時可能變更** | Provider 可能無預警收緊或取消免費額度 |
| **無 SLA** | 免費額度本質上無服務保證 |
| **單用戶設計** | 無多租戶認證，不應直接暴露於網際網路 |
| **不支援** | `/v1/moderations`、`n > 1` 多重完成 |

---

## 十一、Premium 方案

- **免費版**：每月快照更新模型目錄（延遲 30 天）
- **Premium**（$19/年）：即時同步模型目錄簽名更新，新免費模型、配額變更當天生效

---

## 十二、總結

FreeLLMAPI 解決了一個實際痛點：將碎片化的免費 LLM 額度統一為單一可靠端點。其核心價值在於：

1. **統一介面**：一個 OpenAI 相容端點取代 34 個 SDK
2. **智慧路由**：Thompson Sampling + 多策略的自適應路由
3. **自動容錯**：無縫故障轉移，最多 20 層 fallback
4. **安全儲存**：AES-256-GCM 加密所有上游 API key
5. **自動更新**：模型目錄自動同步，無需手動維護
6. **廣泛相容**：支援 OpenAI / Anthropic / Gemini / Ollama 四種 API 協定

適合個人開發者、實驗性專案、以及希望在不花錢的前提下獲得多模型推論能力的使用場景。
