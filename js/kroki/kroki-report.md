# Kroki 技術報告

**生成日期**: 2026-11-23  
**版本**: 1.0  
**作者**: AI 技術助手

## 目錄

1. [簡介](#1-簡介)
2. [系統需求](#2-系統需求)
3. [安裝步驟](#3-安裝步驟)
   - [3.1 使用 Docker 安裝（推薦）](#31-使用-docker-安裝推薦)
   - [3.2 使用 Podman 安裝](#32-使用-podman-安裝)
   - [3.3 手動安裝（Java）](#33-手動安裝java)
4. [配置說明](#4-配置說明)
5. [測試步驟](#5-測試步驟)
6. [驗證步驟](#6-驗證步驟)
7. [常見問題](#7-常見問題)
8. [參考資源](#8-參考資源)

## 1. 簡介

[Kroki](https://kroki.io/) 是一個「圖形即程式碼」（Diagram as Code）的工具套件，提供統一的 HTTP API 介面，可將多種圖形編輯器的文字描述轉換為圖片格式。Kroki 支援超過 100 種圖形語言，包括 PlantUML、GraphViz、Mermaid、BPMN、Excalidraw 等。

### 主要特性

- **統一的 API 介面**：單一 API 支援多種圖形語言
- **自託管解決方案**：可在地端運行，確保資料隱私
- **支援多格式輸出**：SVG、PNG、PDF 等
- **輕量級部署**：使用 Docker 容器即可快速開始

## 2. 系統需求

### 最低需求

| 項目 | 要求 |
|------|------|
| **作業系統** | Linux、macOS、Windows |
| **記憶體** | 至少 512MB |
| **Docker** | Docker Engine 20.10+ 或 Podman |
| **Java** | Java 21+（手動安裝時需要） |

### 建議配置

| 項目 | 建議 |
|------|------|
| **記憶體** | 2GB 或以上 |
| **磁碟空間** | 2GB（含圖形庫） |
| **網路** | 穩定的 Internet 連線（若使用外部圖形服務） |

## 3. 安裝步驟

### 3.1 使用 Docker 安裝（推薦）

這是推薦且最快速的安裝方式，特別是如果您不想手動安裝圖形庫。

#### 步驟 1：確認 Docker 已安裝

首先確認 Docker 已正確安裝並運行：

```bash
docker --version
docker ps
```

若未安裝，請執行以下命令（以 Debian/Ubuntu 為例）：

```bash
sudo apt-get update
sudo apt-get install docker.io
```

#### 步驟 2：拉取 Kroki 容器映像

```bash
docker pull yuzutech/kroki
```

#### 步驟 3：啟動 Kroki 服務

使用以下命令啟動 Kroki：

```bash
docker run -d -p 8000:8000 --name kroki yuzutech/kroki
```

**參數說明**：
- `-d`：後台運行
- `-p 8000:8000`：將主機 8000 端口映射到容器 8000 端口
- `--name kroki`：容器名稱

#### 步驟 4：（可選）使用額外的伴隨容器

Kroki 提供多個可選的伴隨容器，提供更專用的圖形庫：

```bash
# Mermaid
docker run -d -p 8001:8000 --name kroki-mermaid yuzutech/kroki-mermaid

# BPMN
docker run -d -p 8002:8000 --name kroki-bpmn yuzutech/kroki-bpmn

# Excalidraw
docker run -d -p 8003:8000 --name kroki-excalidraw yuzutech/kroki-excalidraw

# Diagrams.net
docker run -d -p 8004:8000 --name kroki-diagramsnet yuzutech/kroki-diagramsnet
```

#### 步驟 5：設定環境變數（可選）

若需要自訂配置，可以設定以下環境變數：

```bash
docker run -d \
  -p 8000:8000 \
  -e KROKI_LISTEN=:8000 \
  -e KROKI_DOT_BIN_PATH=/usr/bin/dot \
  --name kroki \
  yuzutech/kroki
```

### 3.2 使用 Podman 安裝

Podman 是一個不依賴系統服務管理器的容器解決方案，適合使用 rootless 模式。

#### 步驟 1：確認 Podman 已安裝

```bash
podman --version
```

#### 步驟 2：拉取並啟動 Kroki

```bash
podman run -d -p 8000:8000 --name kroki yuzutech/kroki
```

#### 步驟 3：使用 Podman 管理容器

查看容器狀態：

```bash
podman ps
```

停止容器：

```bash
podman stop kroki
```

刪除容器：

```bash
podman rm kroki
```

### 3.3 手動安裝（Java）

此方法適合需要高度自訂化的使用者，但需要自行安裝和配置圖形庫。

#### 步驟 1：安裝 Java 21+

確保系統已安裝 Java 21 或以上版本：

```bash
java -version
```

若未安裝，請參照 [Oracle JDK 或 OpenJDK 官方文件](https://openjdk.org/)。

#### 步驟 2：下載 Kroki 執行檔

從 [GitHub Releases](https://github.com/yuzutech/kroki/releases) 下載最新的 `kroki-server.jar`：

```bash
# 下載（以 curl 為例）
curl -L https://github.com/yuzutech/kroki/releases/download/<version>/kroki-server.jar -o kroki-server.jar

# 或使用 wget
wget https://github.com/yuzutech/kroki/releases/download/<version>/kroki-server.jar -O kroki-server.jar
```

#### 步驟 3：安裝必要的圖形庫

Kroki 手動安裝版本**不包含**圖形庫，需要自行安裝：

```bash
# 以 GraphViz 為例
sudo apt-get install graphviz
dot --version
```

其他常見圖形庫：

```bash
# PlantUML
sudo apt-get install plantuml

# Mermaid
npm install -g mermaid-cli

# BPMN
npm install -g bpmnlint
```

#### 步驟 4：配置並啟動 Kroki

設定 `dot` 二進位檔路徑並啟動：

```bash
java -DKROKI_DOT_BIN_PATH=/usr/bin/dot -jar kroki-server.jar
```

**環境變數說明**：
- `KROKI_DOT_BIN_PATH`：GraphViz 的 dot 二進位檔路徑
- `KROKI_MERMAID_HOST`：Mermaid 主機
- `KROKI_BPMN_HOST`：BPMN 主機
- `KROKI_EXCALIDRAW_HOST`：Excalidraw 主機
- `KROKI_DIAGRAMSNET_HOST`：Diagrams.net 主機
- `KROKI_PORT`：自訂端口（預設 8000）

#### 步驟 5：在背景運行

若要在背景運行，可以使用 nohup 或 screen：

```bash
# 使用 nohup
nohup java -DKROKI_DOT_BIN_PATH=/usr/bin/dot -jar kroki-server.jar > kroki.log 2>&1 &

# 使用 screen
screen -S kroki
java -DKROKI_DOT_BIN_PATH=/usr/bin/dot -jar kroki-server.jar
# 按 Ctrl+A, D 離開 screen
```

## 4. 配置說明

### 4.1 Docker 環境變數

| 環境變數 | 說明 | 預設值 |
|----------|------|--------|
| `KROKI_LISTEN` | Kroki 監聽的地址和端口 | :8000 |
| `KROKI_DOT_BIN_PATH` | GraphViz dot 二進位檔路徑 | - |
| `KROKI_MERMAID_HOST` | Mermaid 服務主機 | https://mermaid.kroki.io |
| `KROKI_BPMN_HOST` | BPMN 服務主機 | https://bpmn.kroki.io |
| `KROKI_EXCALIDRAW_HOST` | Excalidraw 服務主機 | https://excalidraw.kroki.io |
| `KROKI_DIAGRAMSNET_HOST` | Diagrams.net 服務主機 | https://www.diagrams.net |

### 4.2 啟動參數範例

```bash
# 基本啟動（使用預設配置）
docker run -d -p 8000:8000 yuzutech/kroki

# 自訂端口
docker run -d -p 3000:8000 -e KROKI_LISTEN=:3000 yuzutech/kroki

# 使用 HTTPS（需要自行配置 SSL）
docker run -d -p 8443:443 -e KROKI_LISTEN=:443 \
  -v /path/to/certs:/certs \
  --cap-add NET_ADMIN \
  yuzutech/kroki
```

## 5. 測試步驟

### 5.1 確認服務已啟動

#### Docker/Podman 方式

```bash
# 檢查容器運行狀態
docker ps  # 或 podman ps
# 應顯示 kroki 容器狀態為 "Up"

# 檢查端口綁定
docker port kroki
# 應顯示 8000/tcp -> 127.0.0.1:8000
```

#### Java 手動方式

```bash
# 檢查 Java 進程
ps aux | grep "kroki-server.jar"
# 或
ps aux | grep "kroki-server"
```

### 5.2 本地測試 API

#### 使用 curl 測試基本功能

測試 GraphViz 圖形生成：

```bash
# 使用 POST 請求（推薦，不需編碼）
curl -X POST http://localhost:8000/graphviz/svg \
  -H "Content-Type: text/plain" \
  -d "digraph G { Hello->World }" \
  -o /tmp/graphviz-test.svg

# 查看結果
ls -la /tmp/graphviz-test.svg
# 或
cat /tmp/graphviz-test.svg
```

#### 使用 GET 請求（需編碼）

```bash
# 使用 Python 編碼
cat < digraph.txt | python -c "import sys, base64, zlib; print(base64.urlsafe_b64encode(zlib.compress(sys.stdin.read().encode('utf-8'), 9)).decode('ascii'))"

# 將編碼後的結果貼到 URL
curl "http://localhost:8000/graphviz/svg/eNpLyUwvSizIUHBXqPZIzcnJ17ULzy_KSanlAgB1EAjQ"
```

### 5.3 測試不同圖形類型

#### PlantUML

```bash
curl -X POST http://localhost:8000/plantuml/svg \
  -H "Content-Type: text/plain" \
  -d "[Alice] --> [Bob] : Hello"
```

#### Mermaid

```bash
curl -X POST http://localhost:8000/mermaid/svg \
  -H "Content-Type: text/plain" \
  -d "graph TD; A-->B; B-->C;"
```

#### BPMN

```bash
curl -X POST http://localhost:8000/bpmn/svg \
  -H "Content-Type: text/plain" \
  -d "<bpmn:definitions xmlns:bpmn='...'>...</bpmn:definitions>"
```

#### Excalidraw

```bash
curl -X POST http://localhost:8000/excalidraw/svg \
  -H "Content-Type: text/plain" \
  -d "data:image/png;base64,..."
```

### 5.4 測試輸出格式

Kroki 支援多種輸出格式：

```bash
# SVG
curl -X POST http://localhost:8000/graphviz/svg \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B }"

# PNG
curl -X POST http://localhost:8000/graphviz/png \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B }"

# PDF
curl -X POST http://localhost:8000/graphviz/pdf \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B }"

# HTML
curl -X POST http://localhost:8000/graphviz/html \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B }"
```

### 5.5 測試 POST 與 GET 請求

#### POST 請求範例（推薦）

```bash
curl -X POST http://localhost:8000/plantuml/svg \
  -H "Content-Type: text/plain" \
  -d "sequenceDiagram
    participant Alice
    participant Bob
    Alice->>Bob: Hello"
```

#### GET 請求範例（需編碼）

```bash
# 編碼 PlantUML 圖形
echo "sequenceDiagram
  participant Alice
  participant Bob
  Alice->>Bob: Hello" | \
  python -c "import sys, base64, zlib; print(base64.urlsafe_b64encode(zlib.compress(sys.stdin.read().encode('utf-8'), 9)).decode('ascii'))"
```

將編碼結果貼到 URL：

```bash
curl "http://localhost:8000/plantuml/svg/<base64_encoded_string>"
```

## 6. 驗證步驟

### 6.1 驗證 Kroki 首頁

#### 使用瀏覽器

訪問 `http://localhost:8000`，應該看到 Kroki 的歡迎頁面：

```
Kroki: Diagrams as Code
```

#### 使用 curl

```bash
curl -I http://localhost:8000
# 應返回 HTTP/1.1 200 OK
```

### 6.2 驗證 OpenAPI 規格

訪問 OpenAPI 規格文件：

```bash
curl http://localhost:8000/openapi.json
```

應該返回 JSON 格式的 API 規格文件。若成功，可使用以下工具查看：

- [Swagger Editor](https://editor.swagger.io)
- [Scalar](https://scalar.com)
- [Redocly](https://redocly.com)

### 6.3 驗證錯誤處理

測試無效請求以確認錯誤處理正常運作：

```bash
# 測試無效的圖形
curl -X POST http://localhost:8000/plantuml/svg \
  -H "Content-Type: text/plain" \
  -d "invalid syntax here" \
  -H "Accept: application/json"

# 預期返回 JSON 錯誤訊息：
# {
#   "error": {
#     "code": 400,
#     "type": "diagram-error",
#     "message": "Syntax Error?",
#     "line": 1
#   }
# }
```

### 6.4 驗證多語言支援

測試支援的圖形語言清單：

```bash
# 查看支援的圖形類型
curl http://localhost:8000/openapi.json | \
  grep -o '"type": "[^"]*"' | \
  sort -u
```

### 6.5 驗證輸出格式支援

```bash
curl -X POST http://localhost:8000/graphviz/svg \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B }" > /tmp/test.svg

# 驗證 SVG 格式
file /tmp/test.svg
# 應顯示 "SVG document"

# 驗證內容
head /tmp/test.svg
# 應以 "<?xml version="1.0" encoding="UTF-8"?>" 開頭
```

### 6.6 驗證背景運行

確認 Kroki 在背景正常運行：

```bash
# Docker 方式
docker logs kroki
# 應顯示運行日誌，如 "Kroki started..."

# Java 手動方式
ps aux | grep "kroki-server.jar"
# 應顯示運行中的 Java 進程
```

### 6.7 驗證網路連線

若使用外部圖形服務，測試連線是否正常：

```bash
# 測試 Mermaid
curl -I https://mermaid.kroki.io

# 測試 PlantUML
curl -I https://plantuml.kroki.io

# 測試 BPMN
curl -I https://bpmn.kroki.io
```

## 7. 常見問題

### 7.1 Kroki 無法啟動

**問題**：`docker ps` 顯示 Kroki 容器狀態為 `Exited`

**解決方案**：

```bash
# 查看容器日誌
docker logs kroki

# 常見原因：
# 1. 端口已被佔用
# 2. 缺少圖形庫
# 3. Java 版本不支援

# 解決端口衝突
lsof -i :8000
# 停止佔用端口的進程
fuser -k 8000/tcp
```

### 7.2 圖形無法渲染

**問題**：POST 請求返回錯誤訊息

**解決方案**：

```bash
# 1. 確認圖形語法正確
# 2. 檢查環境變數
echo $KROKI_DOT_BIN_PATH

# 3. 確認圖形庫已安裝
dot -V
plantuml -version

# 4. 使用 POST 請求而非 GET
# GET 需要 deflate+base64 編碼，容易出錯
```

### 7.3 記憶體不足

**問題**：容器因記憶體不足而停止

**解決方案**：

```bash
# 增加記憶體限制
docker run -d \
  --memory="2g" \
  --memory-swap="2g" \
  -p 8000:8000 \
  yuzutech/kroki
```

### 7.4 CORS 錯誤

**問題**：前端應用呼叫 Kroki API 時出現 CORS 錯誤

**解決方案**：Kroki 預設支援 CORS，若仍有問題：

```bash
# 確認請求標頭
curl -I http://localhost:8000/openapi.json
# 應包含 Access-Control-Allow-Origin: *
```

## 8. 參考資源

### 官方文件

- [Kroki 官方網站](https://kroki.io/)
- [Kroki 官方文件](https://docs.kroki.io/)
- [GitHub 倉庫](https://github.com/yuzutech/kroki)
- [Docker Hub](https://hub.docker.com/r/yuzutech/kroki)
- [GitHub Releases](https://github.com/yuzutech/kroki/releases)

### 第三方託管服務

- [Wovalab](https://kroki.wovalab.com/) - 社群運行的託管 Kroki 實例
- [Hostinger](https://www.hostinger.com/) - 提供 Docker 託管服務
- [Easypanel](https://easypanel.io/templates/kroki) - 一鍵部署模板

### 支援的圖形語言

- PlantUML
- GraphViz (DOT)
- Mermaid
- BPMN
- Excalidraw
- Diagrams.net
- Structurizr
- 超過 100 種其他圖形語言

### 輸出格式

- SVG
- PNG
- PDF
- HTML
- 其他多種格式

## 附錄：快速開始範例

### 範例 1：基本 GraphViz 圖形

```bash
# 啟動 Kroki
docker run -d -p 8000:8000 yuzutech/kroki

# 生成圖形
curl -X POST http://localhost:8000/graphviz/svg \
  -H "Content-Type: text/plain" \
  -d "digraph G { A->B; B->C; }" > graph.svg

# 在瀏覽器中打開
xdg-open graph.svg  # Linux
open graph.svg      # macOS
start graph.svg     # Windows
```

### 範例 2：PlantUML 順序圖

```bash
curl -X POST http://localhost:8000/plantuml/svg \
  -H "Content-Type: text/plain" \
  -d "sequenceDiagram
    participant Alice
    participant Bob
    Alice->>Bob: Hello
    Bob-->>Alice: World" > sequence.svg
```

### 範例 3：整合到 CI/CD

```yaml
# GitHub Actions 範例
name: Generate Diagrams
on: [push]
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Kroki
        run: |
          docker run -d -p 8000:8000 yuzutech/kroki
          curl -X POST http://localhost:8000/graphviz/svg \
            -H "Content-Type: text/plain" \
            -d "digraph G { A->B }" > diagram.svg
```

**報告結束**
