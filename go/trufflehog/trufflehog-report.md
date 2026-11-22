# TruffleHog 技術報告

## 簡介

**TruffleHog** 是由 Truffle Security 開發的強大秘鑰發現、分類、驗證與分析工具。此工具專門用於在程式碼庫、聊天平台、維基、系統日誌、物件儲存體等多元來源中尋找外洩的認證憑證（Credentials）。

### 核心功能

- **Discovery（發現）**：在 Git、聊天室、維基、系統日誌、API 測試平台、物件儲存體、檔案系統等多種來源中搜尋潛在的敏感資訊
- **Classification（分類）**：能辨識超過 800 種不同的秘鑰類型，包括 AWS 憑證、Stripe 金鑰、Cloudflare 金鑰、Postgres 密碼、SSL 私鑰等
- **Validation（驗證）**：對檢測到的每一個潛在憑證，都能透過 API 測試確認該憑證是否仍為活躍有效，降低誤報率
- **Analysis（分析）**：針對 20 種最常見的認證類型，不僅驗證其有效性，還能進一步分析其權限範圍、可訪問資源等詳細資訊

## 安裝步驟

TruffleHog 支援多種安裝方式，可依作業系統與環境需求選擇最適合的方式。

### 方式一：使用 Homebrew（macOS 使用者）

```bash
brew install trufflehog
```

安裝完成後，可透過 `trufflehog --version` 確認安裝是否成功。

### 方式二：使用 Docker

#### 一般 Linux 用戶

```bash
docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

#### Windows Command Prompt

```cmd
docker run --rm -it -v "%cd:/=\%:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

#### Windows PowerShell

```powershell
docker run --rm -it -v "${PWD}:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

#### Apple M1/M2 用戶

```bash
docker run --platform linux/arm64 --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/trufflesecurity/test_keys
```

### 方式三：下載預編譯二元檔（Binary Releases）

1. 前往 [TruffleHog Releases 頁面](https://github.com/trufflesecurity/trufflehog/releases)
2. 選擇對應作業系統的版本進行下載
3. 解壓檔案後，將 `trufflehog` 副檔名加入系統 PATH 即可使用

### 方式四：從原始碼編譯（Compile from Source）

```bash
git clone https://github.com/trufflesecurity/trufflehog.git
cd trufflehog
go install
```

### 方式五：使用安裝腳本（推薦）

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
```

此腳本會自動下載最新版本的 TruffleHog 並安裝到 `/usr/local/bin` 目錄。

### 方式六：安裝特定版本

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin v3.56.0
```

將 `v3.56.0` 替換為您需要的版本標籤（Release Tag）。

## 驗證步驟

TruffleHog 提供完整的金鑰簽名驗證機制，確保下載的二元檔未被篡改。驗證前需先安裝 [Cosign](https://docs.sigstore.dev/cosign/system_config/installation/) 工具。

### 驗證流程

1. **下載物件及簽名檔案**

   從 [Releases 頁面](https://github.com/trufflesecurity/trufflehog/releases) 下載以下檔案：

   - `trufflehog_{版本}_checksums.txt` - 金鑰校驗檔案
   - `trufflehog_{版本}_checksums.txt.pem` - 證書檔案
   - `trufflehog_{版本}_checksums.txt.sig` - 簽名檔案

2. **驗證簽名**

   ```bash
   cosign verify-blob <金鑰檔案路徑> \
     --certificate <證書檔案路徑> \
     --signature <簽名檔案路徑> \
     --certificate-identity-regexp 'https://github\.com/trufflesecurity/trufflehog/\.github/workflows/.+' \
     --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
   ```

3. **驗證 SHA256 校驗和**

   ```bash
   sha256sum --ignore-missing -c trufflehog_{版本}_checksums.txt
   ```

   若所有檢查均無錯誤訊息，表示檔案完整且未被篡改。

### 使用安裝腳本時自動驗證

若已安裝 Cosign，可使用 `-v` 參數讓安裝腳本自動執行驗證：

```bash
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -v -b /usr/local/bin
```

## 測試步驟

### 測試環境準備

1. **確認安裝成功**

   ```bash
   trufflehog --version
   ```

   若顯示版本號碼，表示安裝成功。

2. **查看命令列選項**

   ```bash
   trufflehog --help
   ```

   此命令將顯示所有可用的子命令與參數選項。

### 基本掃描測試

#### 測試 1：掃描公開 GitHub Repo（僅驗證有效憑證）

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --results=verified
```

預期輸出應包含：

```
🐷🔑🐷  TruffleHog. Unearth your secrets. 🐷🔑🐷

Found verified result 🐷🔑
Detector Type: AWS
Decoder Type: PLAIN
Raw result: AKIAYVP4CIPPERUVIFXG
Line: 4
Commit: fbc14303ffbf8fb1c2c1914e8dda7d0121633aca
File: keys
Email: counter <counter@counters-MacBook-Air.local>
Repository: https://github.com/trufflesecurity/test_keys
Timestamp: 2022-06-16 10:17:40 -0700 PDT
```

#### 測試 2：掃描 GitHub 組織（僅驗證有效憑證）

```bash
trufflehog github --org=trufflesecurity --results=verified
```

此命令會掃描整個 `trufflesecurity` 組織下所有公開程式碼庫。

#### 測試 3：掃描 GitHub Repo 並排除封存（Archived）倉庫

```bash
trufflehog github --org=trufflesecurity --exclude-archived
```

#### 測試 4：輸出 JSON 格式

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --results=verified --json
```

此選項可將輸出格式化為 JSON，方便與 CI/CD 或其他工具整合。

#### 測試 5：掃描 GitHub Repo 的 Issue 與 PR 評論

```bash
trufflehog github --repo=https://github.com/trufflesecurity/test_keys --issue-comments --pr-comments
```

#### 測試 6：掃描本地檔案系統

```bash
trufflehog filesystem path/to/file1.txt path/to/file2.txt path/to/dir
```

#### 測試 7：掃描 Docker 影像

```bash
# 從遠端登記掃描
trufflehog docker --image trufflesecurity/secrets --results=verified

# 從本地 Docker 守護進程掃描
trufflehog docker --image docker://new_image:tag --results=verified

# 從 tarball 檔案掃描
trufflehog docker --image file://path_to_image.tar --results=verified
```

#### 測試 8：使用 SSH 認證掃描 GitHub

```bash
docker run --rm -v "$HOME/.ssh:/root/.ssh:ro" trufflesecurity/trufflehog:latest git ssh://github.com/trufflesecurity/test_keys
```

#### 測試 9：掃描 S3 Bucket

```bash
# 使用本機設定的憑證或 EC2 實例金鑰
trufflehog s3 --bucket=<bucket-name>

# 使用假設角色（IAM Role）
trufflehog s3 --bucket=<bucket-name> --role-arn=<iam-role-arn>
```

#### 測試 10：掃描 GCS Bucket（Google Cloud Storage）

```bash
trufflehog gcs --project-id=<project-ID> --cloud-environment --results=verified
```

#### 測試 11：掃描本地 Git 倉庫

```bash
# 複製測試倉庫
git clone git@github.com:trufflesecurity/test_keys.git

# 從父目錄執行掃描
trufflehog git file://test_keys --results=verified,unknown
```

> **注意**：為防止惡意 Git 配置（如 CVE-2025-41390），TruffleHog 會自動將本地 Git 倉庫複製到暫存目錄後再進行掃描。若信任該倉庫，可使用 `--trust-local-git-config` 參數跳過此步驟。

#### 測試 12：掃描 Jenkins 伺服器

```bash
trufflehog jenkins --url https://jenkins.example.com --username admin --password admin
```

#### 測試 13：掃描 Elasticsearch 伺服器

##### 連線至本機集群

```bash
# 使用使用者名稱與密碼
trufflehog elasticsearch --nodes 192.168.14.3 192.168.14.4 --username truffle --password hog

# 使用服務金鑰
trufflehog elasticsearch --nodes 192.168.14.3 192.168.14.4 --service-token 'AAEWVaWM...Rva2VuaSDZ'
```

##### 掃描 Elastic Cloud 集群

```bash
trufflehog elasticsearch \
  --cloud-id 'search-prod:dXMtY2Vx...YjM1ODNlOWFiZGRlNjI0NA==' \
  --api-key 'MlVtVjBZ...ZSYlduYnF1djh3NG5FQQ=='
```

#### 測試 14：掃描 Postman Workspace

```bash
trufflehog postman --token=<postman-api-token> --workspace-id=<workspace-id>
```

#### 測試 15：從標準輸入（stdin）掃描

```bash
aws s3 cp s3://example/gzipped/data.gz - | gunzip -c | trufflehog stdin
```

#### 測試 16：CI/CD 環境下的掃描

```bash
trufflehog git file://. --since-commit main --branch feature-1 --results=verified,unknown --fail
```

- `--since-commit main`：設定主要分支（如 `main`）
- `--branch feature-1`：設定 PR 分支名稱
- `--fail`：若發現有效憑證，退出碼為 183

## 進階選項與參數

### 常用參數說明

| 參數 | 說明 |
|------|------|
| `--debug, -v` | 啟用除錯模式，增加日誌詳細度 |
| `--json` | 輸出格式化為 JSON |
| `--sarif` | 輸出 SARIF 格式（可上傳至 GitHub Code Scanning） |
| `--results=RESULTS` | 指定輸出結果類型：`verified`（已驗證有效）、`unknown`（驗證失敗）、`unverified`（檢測但未驗證） |
| `--fail` | 若發現結果，以 183 錯誤碼退出 |
| `--concurrency=N` | 設定併發工作數量（預設 12） |
| `--no-verification` | 不執行驗證步驟，僅輸出檢測結果 |
| `--filter-entropy=N` | 使用 Shannon 熵值過濾未驗證結果（預設 3.0） |
| `--config=CONFIG` | 指定配置檔案路徑 |
| `--clone-path=PATH` | 指定本地 Git 倉庫的複製路徑 |
| `--trust-local-git-config` | 跳過本地 Git 配置複製，直接掃描 |
| `--no-ignore-tag` | 即使檔案有 `trufflehog:ignore` 註記也輸出結果 |

### SARIF 格式輸出

SARIF 格式可與 GitHub Code Scanning 整合，上傳後會將結果顯示在 Pull Request 的 diff 中：

```bash
trufflehog git https://github.com/trufflesecurity/test_keys --results=verified --sarif > results.sarif

# 上傳至 GitHub
gh api /repos/OWNER/REPO/actions/runs/upload-sarif \
  --upload-filename results.sarif
```

### 排除特定偵測器

```bash
# 排除所有 AWS 相關偵測器
trufflehog git https://example.com/repo --exclude-detectors=aws

# 排除特定編號的偵測器
trufflehog git https://example.com/repo --exclude-detectors=49
```

### 包含特定偵測器

```bash
trufflehog git https://example.com/repo --include-detectors=githubtoken,githubpat
```

## 配置檔案

TruffleHog 支援使用配置檔案定義自訂 regex 偵測器與多來源掃描。

### 基本配置範例

```yaml
concurrency: "8"

detectors:
  - name: "Custom Detector 1"
    keywords:
      - "keyword1"
      - "keyword2"
    regex:
      pattern1: "regex_pattern_1"
      pattern2: "regex_pattern_2"
    verify:
      - endpoint: "https://verify.example.com/api"
        headers:
          - "Authorization: Bearer token"
        unsafe: false
        successRanges:
          - "200-299"
    description: "Description of the custom detector"
    numWorkers: 16
```

### 多來源配置範例

```yaml
sources:
  - connection:
      '@type': type.googleapis.com/sources.GitHub
      repositories:
        - https://github.com/trufflesecurity/test_keys.git
      unauthenticated: {}
    name: "example config scan"
    type: SOURCE_TYPE_GITHUB
    verify: true

  - connection:
      '@type': type.googleapis.com/sources.S3
      bucket: example-bucket
    name: "S3 scan"
    type: SOURCE_TYPE_S3
    verify: true
```

執行時使用：

```bash
./trufflehog multi-scan --config=config.yaml
```

## 常見問題（FAQ）

### Q1: 只看到 `🐷🔑🐷 TruffleHog. Unearth your secrets. 🐷🔑🐷` 就結束，為什麼？

**A**: 這表示未檢測到任何憑證。

### Q2: 為什麼掃描 GitHub 組織時速度很慢？

**A**: 未經認證的 GitHub 掃描有速率限制。可使用 `--token` 參數加上 Personal Access Token 來提升速率限制。

### Q3: 顯示私鑰已被驗證（Verified），代表什麼意思？

**A**: 表示 TruffleHog 已成功透過 API 測試確認該憑證有效且活躍。對於私鑰，我們已確認其可用於 SSH 或 SSL 認證。

### Q4: 有簡單的方法忽略特定秘鑰嗎？

**A**: 可在包含秘鑰的列上使用 `trufflehog:ignore` 註記：

```bash
# .env 檔案範例
DB_PASSWORD=supersecret
# trufflehog:ignore
```

### Q5: 要包含帶有 `trufflehog:ignore` 註記的秘鑰結果嗎？

**A**: 使用 `--no-ignore-tag` 參數即可：

```bash
trufflehog git https://example.com/repo --no-ignore-tag
```

## 結論

TruffleHog 是一個功能完善的秘鑰掃描工具，支援多平台安裝、提供完整的驗證流程，並具備豐富的使用案例與進階選項。透過本報告所介紹的安裝、測試與驗證步驟，您應該能順利掌握 TruffleHog 的基本與進階使用方式，有效提升組織的安全防護能力。

*報告撰寫日期：$(date -I)*  
*資料來源：TruffleHog Official Documentation*  
- https://github.com/trufflesecurity/trufflehog  
- https://trufflesecurity.com/
