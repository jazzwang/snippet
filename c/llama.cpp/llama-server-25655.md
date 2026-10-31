# llama-server #25655：CORS 控制跟 Router Mode 設定手冊

## PR #25655 一次看

**狀態**: 已合併 ✅
**作者**: ngxson
**合併時間**: 2026-07-14
**影響**: +177 −21, 6 個檔案

### 為什麼要做這支 PR？

以前 `llama-server` 的 CORS 一直設為 `*` 且關不掉，這對只開無狀態、唯讀端點沒問題。但現在加上 `--agent` 模式（內建工具）後，伺服器可以透過 API 讀寫任意檔案。如果 CORS 還是這麼鬆，惡意網頁就能借著伺服器 API 存取你的本地檔案了，這可是個大問題。

### 新增什麼功能？

這支 PR 參考 vllm 的設計，加入了 4 個 CORS 參數：

| 參數 | 做什麼 |
|------|--------|
| `--cors-origins` | 允許哪些 Origin，預設還是 `*` |
| `--cors-methods` | 允許哪些 HTTP 方法 |
| `--cors-headers` | 允許哪些 HTTP 請求標頭 |
| `--cors-credentials` / `--no-cors-credentials` | 要不要允許 CORS 憑證（預設是允許） |

### 預設會怎樣？

- 用較寬鬆的設定：允許憑證、回傳 Origin 標頭（不破壞現有行為），但伺服器啟動時會提醒你一下
- 如果開了伺服器工具，CORS origin 預設只會允許 `localhost`（可以用 `--cors-origins` 改）

---

## Router Mode 怎麼開？

Router Mode 讓你能透過單一入口點動態載入/卸載不同模型，不用重開伺服器。

### 快速開始

```bash
# 不指定模型，自動從 cache 或預設路徑載
llama-server
```

伺服器會自動掃描這三處：
1. **Cache** - 之前用 `-hf` 下載的模型
2. **Models 目錄** - `--models-dir ./models_directory`
3. **Preset 檔案** - `--models-preset ./my-models.ini`

### 完整設定範例

```bash
llama-server \
  --no-models-autoload \
  --host 127.0.0.1 \
  --port 8080 \
  --port-child 8081 \
  -ngl all \
  -c 32768
```

### 啟動多個模型（Router）

```bash
# 用 preset 檔案定義多個模型
llama-server --models-preset models.ini

# 或直接指定 models 目錄
llama-server --models-dir ./models
```

### Router 怎麼運作的？

Router 透過 `subprocess` 啟動子進程，根據請求的模型自動路由到對應的後端實例：

```
客戶端 → Router (llama-server) → Child Instance (特定模型)
```

- **Router 模式**: 不指定 `--model`, `-m`, `-hf`
- **Single-model 模式**: 指定具體模型

---

## Pi Agent 的 CORS 設定建議

### 不同環境，不同設定

| 部署類型 | 建議設定 |
|----------|----------|
| **Public 部署** | 設 API Key + Reverse Proxy，`--cors-origins` 可選 |
| **Local 網路部署** | 明確設 `--cors-origins` 為前端 origin |
| **Same machine** | `--cors-origins localhost`（`--agent` 自動設） |

### 實際配置範例

#### 1. 本地開發（Pi Agent + Frontend 同一台電腦）

```bash
# 啟動 Router Mode
llama-server --agent --cors-origins localhost \
  --port 8080 --port-child 8081 \
  --models-dir ./models
```

**Pi Agent 設定**:
```json
{
  "model": "llama-server",
  "host": "localhost",
  "port": 8080,
  "corsOrigin": "null",
  "maxConcurrentRequests": 4
}
```

#### 2. 本地網路部署（Frontend 跟 Server 不同機）

```bash
# 設 Frontend 的 origin（例如 http://192.168.1.100:3000）
llama-server --agent --cors-origins "http://192.168.1.100:3000" \
  --api-key-file ./llama-server.key \
  --port 8080 --port-child 8081 \
  --models-dir ./models
```

**Pi Agent 設定**:
```json
{
  "model": "llama-server",
  "host": "192.168.1.100",
  "port": 8080,
  "corsOrigin": "http://192.168.1.100:3000",
  "apiKeys": ["your-api-key"],
  "maxConcurrentRequests": 4
}
```

#### 3. 公共部署（Production）

```bash
# 放 Reverse Proxy 後面（Nginx/Traefik）
llama-server --agent --api-key-file ./llama-server.key \
  --no-cors-credentials \
  --cors-origins "https://yoursite.com" \
  --port 8080 --port-child 8081 \
  --models-dir ./models
```

**Pi Agent 設定**:
```json
{
  "model": "llama-server",
  "host": "your-server-host",
  "port": 8080,
  "corsOrigin": "https://yoursite.com",
  "apiKeys": ["production-api-key"],
  "maxConcurrentRequests": 2
}
```

---

## 安全性要注意什麼？

### 風險在哪？

1. **DoS 攻擊**: CORS 太鬆會讓任意網站發起請求，可能耗光伺服器資源
2. **檔案存取風險**: 開了 `--agent` 後，惡意網站就能透過 API 讀寫本地檔案

### 防護措施

| 措施 | 做什麼 |
|------|--------|
| **API Key** | 公共部署一定要設 `--api-key-file` |
| **Reverse Proxy** | 放 Nginx/Traefik 後面，統一處理 CORS |
| **CORS 限制** | 本地環境設 `--cors-origins localhost` |
| **Port 分離** | Router 用 `--port`，Child 用 `--port-child`，避免直接連 Child |

### 測試建議

用這些命令測試 CORS 設定：

```bash
# 測試不同 Origin
curl -H "Origin: http://localhost:3000" \
     -H "Authorization: Bearer YOUR_API_KEY" \
     http://localhost:8080/v1/chat/completions

# 測試無憑證（應該會被拒絕）
curl -H "Origin: http://localhost:3000" \
     http://localhost:8080/v1/chat/completions
```

---

## 環境變數

所有參數也能用環境變數：

| 參數 | 環境變數 |
|------|----------|
| `--cors-origins` | `LLAMA_ARG_CORS_ORIGINS` |
| `--cors-methods` | `LLAMA_ARG_CORS_METHODS` |
| `--cors-headers` | `LLAMA_ARG_CORS_HEADERS` |
| `--cors-credentials` | `LLAMA_ARG_CORS_CREDENTIALS` |

---

## 參考連結

- PR: https://github.com/ggml-org/llama.cpp/pull/25655
- Server README: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md
- Router Mode 文檔: https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README-dev.md
- Pi Agent 設定: https://pi.dev/docs/llama-cpp
