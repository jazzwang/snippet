# ARTEMIS

- Git Repo
  - https://github.com/google/artemis

> [!NOTE]
> ARTEMIS turns natural-language instructions into reliable Android automation. It automates end-to-end workflows, captures logs, and integrates seamlessly with AI coding assistants such as Antigravity, Codex, and Claude Code. It also achieves 99%+ success rate on AndroidWorld Benchmark.

## 2026-09-18

> [!QUESTION]
> 請根據 https://github.com/google/artemis 撰寫一篇技術簡介，包括 step-by-step 測試範例，經 /skill:speak-human-tw 潤飾詞句後，存到 artemis.md

## Google Artemis：AI 驅動的手機自動化測試平台

> **讓 AI 助手和測試套件像人類一樣操作真實手機**

### 專案概述

Google 開放原始碼專案 **Artemis** 是一個 AI 驅動的 Android 自動化測試平台，能夠將自然語言指令轉換為手機操作動作（點擊、滾動、輸入、驗證）。它支援實體 Android 裝置和模擬器，並提供原生 **Model Context Protocol (MCP)** 整合。

### 主要特色

#### 🎯 核心功能

- **跨應用自動化**：從自然語言指令執行測試工作流程和日常任務
- **多模態目標定位**：優先使用元素索引，搭配座標和視覺定位作為備援
- **IDE 診斷整合**：透過 MCP 讓 AI 程式碼編輯器直接控制測試裝置
- **快速執行**：反應式觀察與執行迴圈，通常每步驟 **3–5 秒**
- **專業探索**：執行動作前檢查目標，支援長時間的探索性和穩定性測試
- **AndroidWorld 結果**：在 Google Research 的 AndroidWorld 基準測試上達成 **99%+ 任務完成率**

#### 📊 AndroidWorld 基準測試

| 指標 | 結果 |
|------|------|
| 任務總數 | 116+ 多步驟任務 |
| 應用覆蓋 | 20+ 個應用 |
| 完成率 | **99%+** |
| 任務類型 | 動態、多步驟、跨應用工作流 |

### 快速開始

#### 系統需求

- Python 3.12+
- Android 裝置（USB 除錯已啟用）或模擬器
- 網路連線（用於自動安裝工具鏈）

#### 單一指令啟動

```bash
## macOS 和 Linux
git clone https://github.com/google/artemis.git && cd artemis
./start.sh

## Windows PowerShell
git clone https://github.com/google/artemis.git
cd artemis
.\\start.bat
```

執行後會自動：
- 偵測並自動安裝 ADB、scrcpy、FFmpeg 和 Python 相依套件
- 提示安裝全域 MCP 設定和測試規則
- 在預設瀏覽器開啟 `http://localhost:8000`

### MCP 設定指南

#### 自動安裝（推薦）

```bash
## 為 Antigravity 安裝 MCP 伺服器
uv run artemis mcp --install antigravity

## 或為所有支援的 AI IDE 安裝（包括 Codex）
uv run artemis mcp --install all
```

#### 手動 MCP 配置

##### Codex (`~/.codex/config.toml`)

```toml
[mcp_servers.artemis]
command = "/path/to/artemis/.venv/bin/python"
args = ["-m", "mcp_server"]
cwd = "/path/to/artemis"

[mcp_servers.artemis.env]
PYTHONUNBUFFERED = "1"
PYTHONPATH = "/path/to/artemis"
```

##### Claude Desktop (`claude_desktop_config.json`)

```json
{
  "mcpServers": {
    "artemis": {
      "command": "/path/to/artemis/.venv/bin/python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/artemis"
    }
  }
}
```

### Step-by-Step 測試範例

#### 範例 1：基本任務執行

**任務說明**：開啟裝置設定選單，找到電池項目並查詢當前剩餘電量

```bash
## 直接從 CLI 執行
uv run artemis run "Open Settings, find Battery and tell me current level" \
  --profile flash
```

**預期工作流程**：

1. **裝置連接驗證** → 確認 USB 除錯已啟用
2. **螢幕解析度偵測** → 獲取元素索引資訊
3. **開啟設定選單** → 使用點擊和滑動動作
4. **搜尋電池項目** → 執行文字輸入和選擇動作
5. **擷取電量資訊** → 分析畫面內容提取數據
6. **回報結果** → 提供電量數值和原始截圖

#### 範例 2：跨應用工作流

**任務說明**：開啟 YouTube，搜尋並播放 Coldplay 的歌曲

```bash
uv run artemis run "Open YouTube, search for and play a Coldplay song"
```

**工作流程展示**：

```
┌─────────────────────────────────────────────────────────────┐
│ 1. 開啟 YouTube 應用程式                                      │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 2. 點擊搜尋框並輸入 "Coldplay"                               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 3. 選擇搜尋結果                                               │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 4. 點擊播放按鈕並驗證音訊輸出                                │
└─────────────────────────────────────────────────────────────┘
```

#### 範例 3：使用 MCP 在 IDE 中執行

**在 Antigravity 中使用 MCP**：

1. **提示輸入（任務分派）**：描述測試情境和目標指標
2. **測試計畫產生**：建立步驟式測試計畫和架構供審閱
3. **自主測試執行**：驅動真實裝置、導覽 UI 並分析效能
4. **最終報告**：提供結構化的稽核發現、指標表格和原始數據集

#### 範例 4：效能測試工作流

使用 **Antigravity × ARTEMIS** 的完整測試流程：

**階段 1：提示輸入**
- 描述測試情境
- 設定目標效能指標

**階段 2：測試計畫產生**
- 建立步驟式測試計畫
- 生成測試架構設計

**階段 3：自主測試執行**
- 驅動真實裝置
- 導覽 UI 元素
- 分析效能數據

**階段 4：最終報告**
- 提供結構化稽核發現
- 包含指標表格
- 附帶原始數據集

### 工作流展示

#### Antigravity × ARTEMIS：自主測試工作流

```
┌─────────────────────────────────────────────────────────────┐
│                    階段 1：提示輸入                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 描述你的測試情境和目標指標在 Antigravity              │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    階段 2：測試計畫產生                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 建立步驟式測試計畫和架構供審閱                        │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    階段 3：自主測試執行                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 驅動真實裝置、導覽 UI、分析效能                       │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│                    階段 4：最終報告                           │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 提供結構化稽核發現、指標表格和原始數據集              │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 技術架構

#### 核心模組

- **Agents**：包含 explorer、operator、checker、diagnoser 等智能代理
- **MCP Server**：原生 Model Context Protocol 伺服器
- **Flash Execution**：反應式觀察與執行迴圈
- **Pro Exploration**：進階探索與穩定性測試

#### 相容的 AI IDE

- Antigravity
- Claude Code
- Windsurf
- Codex
- Cursor
- VS Code
- Cline/Roo
- OpenClaw

### 效能比較

| 平台 | AndroidWorld 完成率 |
|------|---------------------|
| **Artemis** | **99%+** |
| 其他自動化工具 | <90% |

### 貢獻與社群

- **Discord 社群**：[加入討論](https://discord.gg/wF2FN4WHGY)
- **貢獻指南**：查看 [CONTRIBUTING.md](./CONTRIBUTING.md)
- **许可证**：Apache 2.0

### 相關資源

- [AndroidWorld 基準測試](https://google-research.github.io/android_world/)
- [Artemis GitHub](https://github.com/google/artemis)
- [MCP 官方文件](https://modelcontextprotocol.io/)

---

*最後更新：2025 年*

> 提示：在 Windows PowerShell 中執行 `start.bat` 時請使用 `.\\start.bat`（無尾端反斜線）。在 Command Prompt 中則直接使用 `start.bat`。
