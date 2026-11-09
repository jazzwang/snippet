# Gemini API CLI 技術報告

## 概述

Gemini API CLI 是由 Google 開發的命令行工具，讓程式碼代理（coding agents）、助手工具或腳本能夠直接調用 Gemini 模型能力。該工具提供統一的接口，可存取文字與推理模型、多模態檔案分析、影像/音訊/音樂/影片生成，以及受管代理（managed agents）功能。

此 CLI 設計為無狀態執行，每個呼叫獨立運作，適合用於編碼代理、助手工具和 CI/CD 工作流。單一 Go 二進制檔可在 macOS、Linux 和 Windows 上運行。

---

## 一、安裝步驟

### 1.1 使用預設安裝腳本（推薦）

根據作業系統選擇對應的安裝方式：

#### macOS 和 Linux

```bash
curl -fsSL https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.sh | bash
```

**說明：**
- 該腳本會自動下載最新版本的二進制檔
- 安裝後 `gemini-api` 會自動加入系統 PATH
- 執行 `gemini-api --version` 確認安裝成功

#### Windows（PowerShell）

```powershell
iwr -useb https://raw.githubusercontent.com/google-gemini/gemini-api-cli/main/scripts/install.ps1 | iex
```

**說明：**
- `iwr` 為 Windows PowerShell 的 "Invoke-WebRequest" 簡寫
- `-useb` 參數表示使用 HTTP/HTTPS 協議
- `| iex` 將輸出結果執行（execute expression）

#### 使用 Go 安裝（開發者推薦）

```bash
go install github.com/google-gemini/gemini-api-cli/cmd/gemini-api@latest
```

**說明：**
- 安裝最新發布版本
- 如需開發版本，使用 `@main` 取代 `@latest`
- 目前 `main` 分支需要 **Go 1.26.10** 或更高版本
- Go 的自動工具鏈選擇會自動下載所需版本（如需要）

#### 預編譯二進制檔

從 [GitHub Releases](https://github.com/google-gemini/gemini-api-cli/releases) 下載：

```bash
# 下載 macOS 版本
curl -L https://github.com/google-gemini/gemini-api-cli/releases/latest/download/gemini-api-darwin-amd64.tar.gz | tar xz

# 下載 Linux 版本
curl -L https://github.com/google-gemini/gemini-api-cli/releases/latest/download/gemini-api-linux-amd64.tar.gz | tar xz

# 下載 Windows 版本
curl -L https://github.com/google-gemini/gemini-api-cli/releases/latest/download/gemini-api-windows-amd64.zip | unzip -o -
```

將 `gemini-api` 二進制檔放入系統 PATH 目錄（如 `/usr/local/bin`、`C:\Windows\System32`）。

---

### 1.2 驗證安裝

執行以下命令確認安裝成功：

```bash
gemini-api --version
```

預期輸出類似：
```
gemini-api version X.X.X
```

---

## 二、測試步驟

### 2.1 配置 API Key

#### 步驟 1：取得 Gemini API Key

1. 開啟 [Google AI Studio](https://aistudio.google.com)
2. 登入 Google 帳號
3. 前往 API Keys 頁面
4. 建立新的 API Key
5. 複製生成的 API Key

#### 步驟 2：設定環境變數

```bash
export GEMINI_API_KEY="your_api_key_here"
```

**Windows PowerShell：**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**Windows CMD：**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

#### 步驟 3：使用 CLI 配置工具（推薦）

```bash
gemini-api configure --api-key "your_api_key_here"
```

或使用互動式設定：

```bash
gemini-api configure --interactive
```

配置會儲存至：
- macOS: `~/.config/gemini-api/config.yaml`
- Linux: `~/.config/gemini-api/config.yaml`
- Windows: `%APPDATA%\gemini-api\config.yaml`

#### 步驟 4：確認配置

```bash
gemini-api whoami
```

預期輸出：
```
API Key: your_api_key_here (configured)
```

---

### 2.2 基礎功能測試

#### 測試文字生成

```bash
gemini-api generate "Hello from my agent"
```

預期：CLI 會呼叫 Gemini 模型並返回文字回應。

#### 測試影像生成

```bash
gemini-api image "A friendly robot mascot for a developer tool" --out ./assets/
```

預期：
- CLI 會生成影像檔案
- stdout 輸出影像檔案的路徑
- `./assets/` 目錄下會建立生成的影像檔案

#### 測試語音合成

```bash
gemini-api tts "Hello, welcome to the demo." --out ./assets/welcome.wav
```

預期：
- 生成 `.wav` 格式的語音檔案
- stdout 輸出檔案路徑

#### 測試音樂生成

```bash
gemini-api music "Warm ambient music for a product walkthrough" --out ./assets/
```

#### 測試影片生成

```bash
gemini-api video "A slow camera move through a sunlit workshop" --out ./assets/
```

---

### 2.3 多模態分析測試

#### 分析檔案

```bash
gemini-api analyze --input document.pdf "Summarize the key points"
```

#### 影像分析

```bash
gemini-api analyze --input before.png --input after.png "Describe the visual changes"
```

#### 轉錄音訊/影片

```bash
gemini-api transcribe --input interview.mp4 --format srt --out interview.srt
```

---

## 三、驗證步驟

### 3.1 使用 --dry-run 驗證（無網路呼叫）

**重要：** 在執行真正 API 呼叫前，先用 `--dry-run` 驗證參數和請求結構。

```bash
# 驗證文字生成請求
gemini-api generate "Hello world" --dry-run

# 驗證影像生成請求
gemini-api image "A robot mascot" --out ./assets/ --dry-run

# 驗證影像生成請求（JSON 格式）
gemini-api image "A robot mascot" --out ./assets/ --dry-run --output-format json
```

**預期：**
- CLI 會輸出解析後的 HTTP 請求
- **不會**實際呼叫 API 或讀取 OS keychain
- 可安全測試請求結構和參數

### 3.2 檢查模型可用性

```bash
# 檢視離線模型目錄（預設模型）
gemini-api models

# 查詢所有可用模型
gemini-api models list --all

# 取得特定模型資訊
gemini-api models get gemini-3.8-flash
```

### 3.3 測試自描述介面

CLI 提供機可讀的使用說明，適合代理工具使用：

```bash
# 檢視所有命令
gemini-api --help

# 檢視特定命令說明
gemini-api image --help

# 取得請求 Body 的 JSON Schema
gemini-api image --schema > image-schema.json

# 取得機可讀的使用說明（KDL 格式）
gemini-api --usage
```

### 3.4 測試多輪對話

```bash
# 第一輪：生成互動 ID
TURN1_ID=$(gemini-api generate "Propose 3 database indexing strategies." \
  --stream=false --jq '.id')

# 第二輪：使用 previous_interaction_id 延續對話
gemini-api agent run "Compare strategy #2 and #3 for write-heavy workloads." \
  --body "{\"previous_interaction_id\": \"$TURN1_ID\"}" \
  --stream=false
```

### 3.5 測試檔案上傳與重用

對於大檔案（>14MB），使用 Files API 上傳一次後可重複使用：

```bash
# 上傳檔案並等待完成
FILE_URI=$(gemini-api files upload interview.mp4 --wait --output-format json --jq '.name')

# 使用上傳的 URI 進行分析
gemini-api analyze --input "$FILE_URI" "List key action items with timestamps"
```

### 3.6 測試受管代理（Managed Agent）

```bash
# 啟動背景受管代理並取得互動 ID
INTERACTION_ID=$(gemini-api agent run "Research battery recycling approaches and cite sources" \
  --agent deep-research-preview-04-2026 \
  --background \
  --jq '.id')

echo "Started interaction: $INTERACTION_ID"

# 檢查進度
gemini-api agent status "$INTERACTION_ID" --stream=false --output-format json

# 或串流即時進度
gemini-api agent status "$INTERACTION_ID" --stream

# 取消進行中的任務
# gemini-api agent cancel "$INTERACTION_ID"
```

### 3.7 測試自訂請求體

```bash
# 檢視 image 命令的 Schema
gemini-api image --schema > image-schema.json

# 建立自訂請求 Body
cat > hero-image.json <<'JSON'
{
  "model": "gemini-nano-banana-2.1",
  "input": "A friendly robot mascot in a sunlit workshop, composed on the right with uncluttered space on the left.",
  "response_format": {
    "type": "image",
    "aspect_ratio": "16:9",
    "image_size": "2K"
  },
  "store": false,
  "stream": false
}
JSON

# 使用自訂 Body 執行
gemini-api image --body @hero-image.json --out ./assets/hero.jpg --dry-run --output-format json
gemini-api image --body @hero-image.json --out ./assets/hero.jpg --output-format json
```

### 3.8 測試不同輸出格式

```bash
# 預設格式（TOON）
gemini-api generate "Hello world" --stream=false

# JSON 格式
gemini-api generate "Hello world" --stream=false --output-format json

# 使用 jq 過濾
gemini-api generate "Hello world" --stream=false --output-format json --jq '.output'
```

### 3.9 測試代理模式（Agent Mode）

```bash
# 啟動代理模式（結構化 JSON 錯誤封裝）
export GEMINI_CLI_AGENT_MODE=1

# 或直接在命令中設定
gemini-api agent run "Test task" --agent-default-model --agent-mode

# 檢視錯誤（結構化 JSON）
gemini-api generate "invalid model name" --agent-mode 2>&1 | jq
```

---

## 四、常見命令速查

### 4.1 生成命令

| 命令 | 說明 | 預設模型 |
|------|------|----------|
| `gemini-api generate` | 文字和多模態生成 | gemini-3.8-flash |
| `gemini-api image` | 影像生成/編輯 | gemini-nano-banana-2.1 |
| `gemini-api tts` | 文字轉語音 | gemini-3.8-flash-tts |
| `gemini-api music` | 音樂生成 | lyria-3.5 |
| `gemini-api video` | 對話式影片生成 | gemini-omni-1.1-flash |

### 4.2 分析命令

| 命令 | 說明 | 預設模型 |
|------|------|----------|
| `gemini-api analyze` | 分析 PDF、影像、音訊、影片、CSV | gemini-3.8-flash |
| `gemini-api transcribe` | 轉錄音訊/影片為字幕 | gemini-3.5-transcribe |

### 4.3 管理命令

| 命令 | 說明 |
|------|------|
| `gemini-api agent` | 管理受管代理互動 |
| `gemini-api files` | 檔案上傳與管理（48 小時保留期） |
| `gemini-api models` | 檢視模型目錄 |
| `gemini-api configure` | 配置認證和全域參數 |
| `gemini-api auth` | 管理儲存的認證 |

---

## 五、輸出格式與 Exit Codes

### 5.1 輸出格式

| 格式 | 說明 |
|------|------|
| `toon`（預設） | 結構化但人類可讀的格式 |
| `json` | JSON 格式（適合機器解析） |
| `--jq` | 直接過濾 JSON 輸出 |

### 5.2 Exit Codes

| 代碼 | 說明 |
|------|------|
| 0 | 成功 |
| 1 | 運行時/API 失敗 |
| 2 | 無效使用/驗證錯誤 |
| 3 | 認證/權限失敗 |

---

## 六、給代理工具的建議配置

```text
You have access to gemini-api through the shell.
Use it to call Gemini models, generate or edit media, analyze files, or launch managed agents.

1. Inspect --help or --usage to choose a command, and --schema when building a --body JSON payload.
2. Preview API calls with --dry-run (or --dry-run --output-format json).
3. For discrete JSON output or --jq filtering on streaming commands, pass --stream=false --output-format json.
4. Capture returned file paths (from media commands) and interaction IDs (from agent/model runs) to continue multi-step tasks.
```

---

## 七、注意事項

1. **Beta 版本：** `gemini-api` 目前處於 Beta 階段，可能會隨 Gemini Interactions API 的演進而發生變更
2. **CI/CD 建議：** 在 CI 和自動化工作流中，建議鎖定特定 [release version](https://github.com/google-gemini/gemini-api-cli/releases)
3. **API Key 安全：** 建議使用 OS keychain 儲存 API Key，而非明文環境變數
4. **檔案保留：** 上傳的檔案在 Files API 中保留 48 小時

---

## 八、參考資源

- [GitHub Repository](https://github.com/google-gemini/gemini-api-cli)
- [GitHub Releases](https://github.com/google-gemini/gemini-api-cli/releases)
- [Gemini API 文件](https://aistudio.google.com/docs)
- [Gemini Interactions API 概觀](https://aistudio.google.com/docs/interactions-overview)
- [GitHub Issues](https://github.com/google-gemini/gemini-api-cli/issues)
