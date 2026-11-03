# Open Source Grok Bot Alternatives

搜尋日期：2026 年 11 月 03 日

## 簡介

Grok Bot 是由 xAI 推出的 AI 團隊聊天應用，允許用戶創建多個 AI 代理人並進行對話。以下是幾個開源替代方案，可以在本地運行並使用自己的 AI 模型。

---

## 1. Rakazo ⭐ 最推薦

**GitHub**: https://github.com/elie222/rakazo  
**狀態**: Beta 版

### 特點
- 完全開源，Apache-2.0 許可
- 最接近 Grok Bot 的功能
- 每個 AI 機器人擁有獨立的記憶體、瀏覽器/終端機存取權限
- 支援自定義模型和計算提供者
- 可完整本地部署

### 功能
- 每個 bot 擁有獨立的 thread、computer、memory、routines 和 history
- bot 可以產生更多 bots，每個都是獨立的 peer
- 支援短時 subagents 執行
- Web、桌面 (Electron)、iOS、Android 平台支援

### 部署
- 可自託管完整堆疊
- 支援 Bring Your Own Model 和 Computer Provider

---

## 2. OpenMausBot (OpenGrokBot)

**GitHub**: https://github.com/milind-soni/OpenMausBot  
**網站**: https://openmausbot.com

### 特點
- 開源 Grok Bot 替代品
- 獨立專案，受 Grok Bot 啟發
- 非 xAI、Meta、OpenAI 或 Manus 相關
- 本地優先 (local-first)
- 使用已有模型的 AI 代理

### 功能
- 多 AI 代理團隊聊天應用
- 支援自定義代理 (bring-your-own-agent)
- 可在已有訂閱的模型上運行 (Claude, Codex, Grok 等)

### 技術架構
- FastAPI API
- Next.js UI
- Docker/remote runtimes
- 審批系統
- 連接器支援
- 本地化狀態管理

---

## 3. Open Grok Bot

**GitHub**: https://github.com/Anil-matcha/open-grok-bot

### 特點
- 本地優先 AI 工作空間
- 可創建 AI bot personas
- 在機器上保持對話歷史

### 技術
- 介面：Next.js + React
- API：FastAPI + Python
- 獨立開源專案，非 xAI 相關

### 功能
- 聊天機器人人設創建
- 透過 MUAPI 與模型對話
- 本地化對話歷史
- 支援多種 AI API

---

## 4. SuperKagi

**GitHub**: https://github.com/0xGingi/SuperKagi

### 特點
- Grok 風格的聊天 UI
- 本地 LLM 支援
- 簡單易用的 Docker 部署

### 支援
- 本地 OpenAI 相容 LLM 服務 (Ollama / LM Studio)
- OpenRouter
- Nano-gpt.com
- Kagi 網頁搜尋 (透過 KagiMCP)

### 部署
```bash
# 使用 Docker Compose
cp .example.env .env
docker compose up -d --build
```
運行於 port 3545

---

## 5. Open GrokBot

**GitHub**: https://github.com/ishandutta2007/open-grokbot

### 特點
- 24/7 運行的 AI 代理團隊
- 自我託管、開源、免費
- 多代理協作環境

### 功能
- 24/7 AI 代理準備執行任務
- 代理可相互協作
- 從用戶演示中學習
- 在隔離沙盒環境中完成端到端任務

---

## 6. 其他相關專案

### Private AI Chatspace
**GitHub**: https://github.com/magnusfroste/private-ai-chatspace  
- 自我託管、隱私優先的 LLM 聊天應用
- Grok 風格介面
- 支援 RAG (檢索增強生成)
- 文件上傳 (PDF/DOCX/TXT/MD)

### Tetsuo Code
**GitHub**: https://github.com/tetsuo-ai/tetsuo-code  
- 基於 Grok 模型的開源 Claude Code
- 瀏覽器基礎 LLM 聊天工具
- 三欄式 UI，vim 快捷鍵

### Grok Web
**GitHub**: https://github.com/cwmaguire/grok-web  
- 瀏覽器基礎 LLM 聊天工具
- 使用 xAI Grok 模型
- "Claude Code 克隆"
- 三欄式瀏覽器 UI，vim 快捷鍵
- 給 LLM 提供完整本地機器存取權

---

## 快速比較

| 專案 | Grok Bot 相似度 | 易於部署 | 模型支援 | 主要優勢 |
|------|---------------|----------|----------|----------|
| Rakazo | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 自定義 | 功能最完整，最接近 |
| OpenMausBot | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 多模型 | 多代理協作，功能齊全 |
| Open Grok Bot | ⭐⭐⭐⭐ | ⭐⭐⭐ | 多模型 | 本地化對話，快速設定 |
| SuperKagi | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 本地/第三方 | 簡單易用，Docker 部署 |
| Open GrokBot | ⭐⭐⭐ | ⭐⭐⭐ | 多模型 | 24/7 代理，沙盒執行 |

---

## 選擇建議

### 想要最接近 Grok Bot 體驗
- **選擇**: Rakazo
- **理由**: 功能最完整，每個 bot 獨立運行，支援瀏覽器/終端機存取

### 想要多代理協作
- **選擇**: OpenMausBot
- **理由**: 專門為多 AI 代理設計，支援複雜協作場景

### 想要快速簡單部署
- **選擇**: SuperKagi
- **理由**: Docker 部署，簡單的 Grok UI，快速上手

### 想要本地化隱私保護
- **選擇**: Private AI Chatspace
- **理由**: 隱私優先，RAG 支援，完全本地化

---

## 部署注意事項

所有這些專案都支援：
1. **自定義模型**：使用自己訂閱的 AI 服務 (Claude, ChatGPT, Grok, Gemini 等)
2. **本地化運行**：數據不會上傳到第三方
3. **開源許可**：大多使用 MIT 或 Apache-2.0 許可
4. **Docker 部署**：大部分支援容器化部署

請注意：這些專案**非官方**，與 xAI、Meta、OpenAI 等公司無關。
