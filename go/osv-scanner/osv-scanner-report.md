- 緣起：
  - 在查 Docker Image 以前是用哪一套軟體時，再次看到 Google osv-scanner 的 github
- 備註：
  - 先前是用 Twistlock / Prisma Cloud
  - https://www.paloaltonetworks.com/blog/2019/11/cloud-prisma-cloud-compute-edition/
- OSV Scanner 支援掃描 Docker Image
  - https://google.github.io/osv-scanner/usage/scan-image

> [!NOTE]
> 根據 "https://github.com/google/osv-scanner https://google.github.io/osv-scanner/usage/scan-image https://osv.dev/" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "go/osv-scanner/osv-scanner-report.md" .

## OSV-Scanner 技術報告

### 概述

OSV-Scanner 是 Google 開發的安全掃描工具，用於偵測專案相依套件中已知漏洞。該工具提供對 [OSV 資料庫](https://osv.dev/) 的官方支援介面和 CLI 介面，可將專案的相依套件清單與影響它們的漏洞進行比對。

#### 主要功能

- **支援語言**: C/C++, Dart, Elixir, Go, Java, Javascript, PHP, Python, R, Ruby, Rust
- **套件管理器**: npm, pip, yarn, maven, go modules, cargo, gem, composer, nuget
- **作業系統**: 偵測 Linux 系統上 OS 套件漏洞
- **容器掃描**: 掃描容器映像的基礎映像和包含套件
- **指導修復**: 提供基於相依關係深度、最小嚴重程度、修復策略和投資回報率的套件版本升級建議

### 第一部分：安裝步驟

#### 方法一：使用 Go 安裝（推薦）

```bash
## 安裝最新版本
go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest

## 或指定特定版本（如 v2.x.x）
go install github.com/google/osv-scanner/v2/cmd/osv-scanner@v2.x.x
```

安裝後，可透過 `which` 命令驗證：

```bash
which osv-scanner
```

#### 方法二：使用預編譯二進製檔

1. 前往 [GitHub Releases 頁面](https://github.com/google/osv-scanner/releases)
2. 選擇適合平台的版本
3. 下載對應的壓縮檔並解壓縮
4. 將二進製檔移動至系統 PATH 目錄（如 `/usr/local/bin`）

```bash
## 範例：macOS
curl -L https://github.com/google/osv-scanner/releases/download/v2.0.0/osv-scanner-v2.0.0-darwin-arm64.tar.gz | tar xz
sudo mv osv-scanner-v2.0.0-darwin-arm64/osv-scanner /usr/local/bin/
```

#### 方法三：從原始碼編譯

```bash
## 克隆專案
git clone https://github.com/google/osv-scanner.git
cd osv-scanner

## 編譯
make

## 或使用 go build
go build -o osv-scanner ./cmd/osv-scanner

## 移動至系統 PATH
sudo mv osv-scanner /usr/local/bin/
```

### 第二部分：測試步驟

#### 步驟 1：驗證安裝

```bash
## 確認版本資訊
osv-scanner --version

## 顯示程式說明
osv-scanner --help
```

預期輸出應顯示版本資訊與可用選項。

#### 步驟 2：掃描目錄測試

```bash
## 建立測試目錄結構
mkdir -p test-project
cd test-project

## 建立簡單的 package.json
cat > package.json << 'EOF'
{
  "name": "test-project",
  "version": "1.0.0",
  "dependencies": {
    "lodash": "^4.17.0"
  }
}
EOF

## 執行掃描
osv-scanner -r .
```

#### 步驟 3：掃描鎖定檔測試

```bash
## 建立 package-lock.json
npm install

## 掃描鎖定檔
osv-scanner --lockfile=package-lock.json
```

#### 步驟 4：容器映像掃描測試

```bash
## 測試掃描 Alpine 基礎映像
osv-scanner scan image alpine:3.18

## 或掃描自定義映像（需要先下載）
docker pull alpine:3.18
osv-scanner scan image alpine:3.18
```

#### 步驟 5：離線模式測試

```bash
## 下載離線資料庫
osv-scanner --offline --download-offline-databases ./

## 使用離線資料庫掃描
osv-scanner --offline -r . --offline-db-dir ./
```

### 第三部分：驗證步驟

#### 驗證一：檢查漏洞資訊來源

```bash
## 掃描並查看漏洞詳細資訊
osv-scanner -r . --format=json

## 解析 JSON 輸出，驗證漏洞 ID 格式
cat output.json | jq '.[] | select(.vulnerability_id != null)'
```

驗證內容應包含：
- `vulnerability_id`：符合 OSV 格式的漏洞識別碼
- `package.ecosystem`：相依套件生態系統（如 npm, PyPI, Go, Maven）
- `package.name`：套件名稱
- `package.installed_version`：已安裝版本

#### 驗證二：比對 OSV 資料庫

```bash
## 取得掃描結果中的漏洞 ID
osv-scanner -r . --json | jq -r '.[] | .vulnerability_id'

## 個別查詢 OSV API 驗證
curl -d '{
  "id": "GHSA-xxxx-xxxx-xxxx"
}' https://api.osv.dev/v1/query
```

#### 驗證三：容器掃描輸出驗證

```bash
## 執行容器掃描並查看詳細資訊
osv-scanner scan image alpine:3.18

## 預期輸出應包含：
## 1. Debian/Ubuntu 作業系統套件
## 2. 語言相關相依套件（如 Go, Node, Python）
## 3. 每個套件的安裝版本、可用修復版本、漏洞數量
```

範例輸出解讀：

```
Container Scanning Result (Debian GNU/Linux 12 (bookworm)):
Total 20 packages affected by 105 vulnerabilities (7 Critical, 14 High, 19 Medium, 1 Low, 64 Unknown) from 2 ecosystems.
54 vulnerabilities have fixes available.

Debian:12
╭─────────────┬───────────────────┬─────────────────────────┬────────────┬──────────────────┬───────────────╮
│ PACKAGE     │ INSTALLED VERSION │ FIX AVAILABLE           │ VULN COUNT │ INTRODUCED LAYER │ IN BASE IMAGE │
╞═════════════╪═══════════════════╪═════════════════════════╪════════════╪══════════════════╪═══════════════╡
│ aom         │ 3.6.0-1+deb12u1   │ No fix available        │          2 │ # 1 Layer        │ --            │
╰─────────────┴───────────────────┴───────────────┴────────────┴──────────────────┴───────┴───────────────╯
```

#### 驗證四：輸出格式驗證

```bash
## 測試 HTML 輸出
osv-scanner -r . --format=html --serve

## 測試 JSON 輸出
osv-scanner -r . --format=json > results.json

## 驗證 JSON 結構
cat results.json | jq 'keys'
```

#### 驗證五：離線模式完整性測試

```bash
## 1. 下載離線資料庫
osv-scanner --offline --download-offline-databases ./offline-dbs

## 2. 斷網環境測試
## 斷開網路連線
## osv-scanner --offline -r . --offline-db-dir ./offline-dbs

## 3. 驗證掃描結果與線上模式一致
osv-scanner -r . --format=json > online-results.json
osv-scanner --offline -r . --offline-db-dir ./offline-dbs --format=json > offline-results.json

## 比對結果
diff -u online-results.json offline-results.json
```

### 第四部分：故障排除

#### 問題一：找不到命令

```bash
## 解決方案：將 Go bin 目錄加入 PATH
export PATH=$PATH:$HOME/go/bin

## 永久設定（Linux/macOS）
echo 'export PATH=$PATH:$HOME/go/bin' >> ~/.bashrc
source ~/.bashrc
```

#### 問題二：掃描失敗

```bash
## 檢查 Go 模組代理
go env GOPROXY

## 設定 Go 模組代理（如需要）
go env -w GOPROXY=https://goproxy.cn,direct
```

#### 問題三：容器掃描無結果

```bash
## 確保 Docker 已正確安裝並可執行
docker --version

## 確認映像存在
docker images | grep alpine

## 檢查權限問題
sudo chown -R $USER /var/run/docker.sock
```

### 第五部分：最佳實踐

#### 1. CI/CD 整合

```yaml
## .github/workflows/security-scan.yml
name: Security Scan
on: [push, pull_request]
jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Go
        uses: actions/setup-go@v5
        with:
          go-version: 'stable'
      
      - name: Run OSV-Scanner
        run: |
          go install github.com/google/osv-scanner/v2/cmd/osv-scanner@latest
          osv-scanner -r . --json > scan-results.json
      
      - name: Upload Results
        uses: actions/upload-artifact@v4
        with:
          name: security-results
          path: scan-results.json
```

#### 2. 定期掃描設定

```bash
## 設定 cron 任務進行定期掃描
0 2 * * 0 /usr/local/bin/osv-scanner -r /path/to/project --json > /var/log/osv-scanner-$(date +\%Y\-%m\-%d).json

## 或搭配 Docker Compose
docker run --rm --volume /path/to/project:/project \
  google/osv-scanner:v2.0.0 \
  -r /project --json > /results/output.json
```

#### 3. 監控與告警

```bash
## 解析 JSON 結果並產生摘要報告
cat scan-results.json | jq '
  {
    "total_vulnerabilities": (.[] | .vulnerability_count // 0 | add // 0),
    "high_severity": [.[] | select(.severity == "High")] | length,
    "critical_severity": [.[] | select(.severity == "Critical")] | length
  }
' | tee summary.json
```

### 參考資源

- [官方網站](https://google.github.io/osv-scanner/)
- [GitHub 專案](https://github.com/google/osv-scanner)
- [OSV 資料庫](https://osv.dev/)
- [OSV Schema 格式](https://ossf.github.io/osv-schema/)
- [OSV-Scanner 使用文件](https://google.github.io/osv-scanner/usage/)

### 版本資訊

- **OSV-Scanner**: v2.x.x (最新版本請參閱 [GitHub Releases](https://github.com/google/osv-scanner/releases))
- **OSV 資料庫**: [osv.dev](https://osv.dev/)
- **報告生成日期**: `$(date '+%Y-%m-%d')`

*報告由 OSV-Scanner 技術驗證生成*
