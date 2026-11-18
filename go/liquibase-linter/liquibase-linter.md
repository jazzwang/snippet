# Liquibase Linter

> [!NOTE]
> 請幫我查詢是否有 https://www.liquibase.com/resources/liquibase-schema-risk-scanner 的 CLI 實作

## Liquibase Linter - CLI 工具調查報告

### 背景

查詢是否有 Liquibase Schema Risk Scanner 的 CLI 實作。

原始網址：https://www.liquibase.com/resources/liquibase-schema-risk-scanner

### Liquibase Schema Risk Scanner 說明

Liquibase Schema Risk Scanner 是 Liquibase 提供的**線上工具**，用於掃描 Liquibase changelog 檔案，快速識別潛在風險。

#### 功能
- **Operational**: 檢查危險屬性 (runAlways, runOnChange) 和缺少 rollback
- **Security**: 掃描破壞性 SQL (DROP, DELETE, TRUNCATE)
- **Compliance**: 確保審計元資料 (author, label)

#### 使用方式
透過網頁上傳 changelog 檔案，**沒有 CLI 實作**。

### 替代方案

#### 1. Liquibase Linter (Go CLI 工具)

[https://github.com/n2jsoft-public-org/liquibase-linter](https://github.com/n2jsoft-public-org/liquibase-linter)

**特性**：
- 快速、安全導向的 command-line 工具
- 使用 Go 編寫
- 分析 Liquibase changelog 檔案
- 識別安全漏洞、效能問題和最佳實踐違反

**功能**：
- 防止安全事件：偵測 SQL injection、硬編碼憑證和危險操作
- 支援 JSON 和 YAML 格式的 Liquibase migrations

**安裝**：
```bash
go get -u github.com/n2jsoft-public-org/liquibase-linter
```

**使用範例**：
```bash
## 檢查單一 changelog 檔案
liquibase-linter check .../changelog-master.xml

## 檢查目錄中的所有 changelogs
liquibase-linter check db/changelog/.../yaml db/changelog/.../db

## 輸出 JSON 格式用於 CI/CD
liquibase-linter check ... --format json
```

#### 2. Apache Fineract DDL 安全檢查腳本

[https://github.com/apache/fineract/blob/develop/scripts/check-liquibase-ddl-safety.sh](https://github.com/apache/fineract/blob/develop/scripts/check-liquibase-ddl-safety.sh)

**特性**：
- Bash 腳本
- 使用 grep/sed (不需要 xmllint)
- 掃描危險的 DDL 操作和無效的 DATETIME precision

**使用方式**：
```bash
./scripts/check-liquibase-ddl-safety.sh \
  --base-ref origin/develop \
  --head-ref HEAD \
  --config config/liquibase \
  --output-dir ...
```

#### 3. migratesafe

[https://github.com/suhteevah/migratesafe](https://github.com/suhteevah/migratesafe)

**特性**：
- 支援多種 migration 工具：raw SQL、Rails、Django、Knex.js、Prisma、Flyway、Liquibase
- 完全在本地執行
- 不離機

**功能**：
- 偵測危險的 schema changes
- 無視生產環境風險

#### 4. Liquibase Secure (商業版)

**特性**：
- `checks run` 命令執行 policy checks
- 支援 XML、SQL、YAML、JSON changelog 格式
- 需要 Liquibase Secure 授權

**使用方式**：
```bash
## 執行 policy checks
liquibase checks run \
  --checks-scope changelog \
  --changelog-file changelog.xml
```

### 結論

| 工具 | 類型 | 語言 | 費用 | 主要功能 |
|------|------|------|------|----------|
| Schema Risk Scanner | Web 工具 | - | 免費 | 線上掃描 |
| liquibase-linter | CLI | Go | 開源 | 安全檢查、最佳實踐 |
| check-liquibase-ddl-safety.sh | 腳本 | Bash | 開源 | DDL 安全檢查 |
| migratesafe | CLI | - | - | 多工具支援 |
| Liquibase Secure | CLI | - | 商業 | 完整的 policy checks |

**推薦**：若需要 CLI 工具，建議使用 **liquibase-linter**，它功能齊全且支援 CI/CD 整合。

> [!NOTE]
> 根據 "https://github.com/n2jsoft-public-org/liquibase-linter" 內容，用繁體中文（台灣技術用詞）撰寫一篇技術報告，含 step-by-step 安裝、測試、驗證步驟，存成 "go/liquibase-linter.md" .

## Liquibase Linter 技術報告

### 摘要

Liquibase Linter 是一個用 Go 語言編寫的快速、注重安全性之命令列工具，可分析 Liquibase 變更日誌（changelog）檔案，識別安全漏洞、效能問題與最佳實踐違反。此工具能協助開發團隊在變更部署到生產環境前，預防安全事件、提升可靠性、優化效能，並維護程式碼品質。

### 一、功能特點

#### 1.1 安全性防護（Security First）
- **SQL 注入檢測**：識別潛在的 SQL 注入風險
- **硬編碼憑證**：發現硬編碼密碼與 API 金鑰
- **危險操作**：檢測缺少先決條件的 DROP/TRUNCATE 操作
- **權限提升**：識別過度寬鬆的權限授予

#### 1.2 程式碼品質（Code Quality）
- 強制 Liquibase 最佳實踐
- 命名規範一致性
- 適當的文件說明

#### 1.3 效能優化（Performance）
- 識別缺少索引的外來鍵
- 找出可能導致表鎖的操作
- 檢測無界資料操作

#### 1.4 其他特點
- **高速效能**：Go 語言編寫，典型變更日誌啟動時間 <100ms
- **多格式輸出**：支援 text、JSON、SARIF、JUnit 格式
- **靈活配置**：透過 YAML 檔案配置規則
- **內聯排除**：透過註解停用特定變更集（changeset）的規則
- **CI/CD 整合**：易於整合到 GitHub Actions、GitLab CI、Jenkins 等

### 二、安裝步驟

#### 2.1 macOS 與 Linux

使用 Homebrew 安裝：

```bash
brew install --cask n2jsoft-public-org/tap/liquibase-linter
```

#### 2.2 任何平台（需 Go）

若環境已安裝 Go 編譯器，使用 go install：

```bash
go install github.com/n2jsoft-public-org/liquibase-linter/cmd/liquibase-linter@latest
```

安裝後，執行 `liquibase-linter --version` 確認安裝成功。

#### 2.3 下載預編譯二進位檔

從 [releases 頁面](https://github.com/n2jsoft-public-org/liquibase-linter/releases) 下載對應作業系統的預編譯二進位檔：
- `liquibase-linter-linux-amd64`（Linux）
- `liquibase-linter-windows-amd64.exe`（Windows）
- `liquibase-linter-darwin-amd64`（macOS）

下載後請賦予執行權限：

```bash
## Linux / macOS
chmod +x liquibase-linter

## Windows
## 直接複製 .exe 檔案至目標目錄
```

### 三、快速開始

#### 3.1 檢查單一變更日誌檔案

```bash
liquibase-linter check db/changelog/db.changelog-master.xml
```

#### 3.2 檢查目錄中的所有變更日誌

```bash
liquibase-linter check db/changelog/
```

#### 3.3 使用配置檔案

```bash
liquibase-linter check --config=.liquibase-linter.yaml db/changelog/
```

#### 3.4 使用 JSON 格式輸出至 CI/CD

```bash
liquibase-linter check --format=json db/changelog/ > results.json
```

#### 3.5 列出所有可用規則

```bash
liquibase-linter rules
```

#### 3.6 查詢特定規則詳細資訊

```bash
liquibase-linter rules --info=sql-injection
```

#### 3.7 初始化配置檔案

```bash
liquibase-linter init
```

### 四、規則範例

#### 4.1 安全規則（Critical）

| 規則名稱 | 描述 |
|---------|------|
| `sql-injection` | 檢測潛在 SQL 注入漏洞 |
| `hardcoded-credentials` | 尋找硬編碼密碼與 API 金鑰 |
| `dangerous-operations` | 檢測缺少先決條件的 DROP/TRUNCATE 操作 |
| `privilege-escalation` | 識別過度寬鬆的權限授予 |

#### 4.2 可靠性規則（Warning）

| 規則名稱 | 描述 |
|---------|------|
| `missing-rollback` | 確保變更集有回滾腳本 |
| `non-idempotent` | 檢測非冪等（non-idempotent）變更 |
| `missing-preconditions` | 確保風險操作有安全檢查 |

#### 4.3 效能規則（Info/Warning）

| 規則名稱 | 描述 |
|---------|------|
| `missing-indexes` | 檢測缺少索引的外來鍵 |
| `table-locks` | 識別可能導致表鎖的操作 |
| `large-data-operations` | 檢測無界資料操作 |

#### 4.4 最佳實踐規則（Info）

| 規則名稱 | 描述 |
|---------|------|
| `naming-conventions` | 強制一致的命名標準 |
| `changelog-organization` | 確保適當的變更日誌結構 |
| `documentation` | 驗證變更集有文件說明 |

### 五、配置檔案範例

在變更日誌目錄或專案根目錄建立 `.liquibase-linter.yaml`：

```yaml
## 啟用/停用規則並設定嚴重程度
rules:
  sql-injection:
    enabled: true
    severity: critical
  hardcoded-credentials:
    enabled: true
    severity: critical
  dangerous-operations:
    enabled: true
    severity: critical
  missing-rollback:
    enabled: true
    severity: warning
  naming-conventions:
    enabled: true
    severity: info

## 忽略特定檔案或模式（相對於目標目錄）
ignore:
  - "test/fixtures/*.xml"
  - "init/**"
  - "db/changelog/legacy/**"

## 輸出配置
output:
  format: text        # text, json, sarif, junit
  colorize: true      # 啟用彩色輸出（僅限 text 格式）

## 解析器配置
parser:
  max_include_depth: 10    # include/includeAll 的最大巢狀深度
  follow_symlinks: true    # 檔案發現時跟隨符號連結

## 最低報告嚴重程度
severity_threshold: warning  # info, warning, critical
```

### 六、內聯排除規則

有時需要針對特定變更集（changeset）有意识地停用某條規則。在變更集註解中加入內聯排除：

```xml
<changeSet id="1" author="john">
    <comment>liquibase-linter:disable sql-injection</comment>
    <sql>
        -- 已知安全的參數，來自驗證過的配置
        INSERT INTO settings VALUES (${config_value});
    </sql>
</changeSet>
```

詳細格式與範例請參考 [排除規則文檔](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/suppression.md)。

### 七、測試與驗證

#### 7.1 測試環境準備

建立測試用的變更日誌目錄結構：

```bash
mkdir -p test-data/changelog
```

建立測試用的變更日誌檔案：

```xml
<!-- test-data/changelog/test-changelog.xml -->
<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
                   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                   xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
                   http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.20.xsd">

    <changeSet id="1" author="test-user">
        <comment>測試添加用戶表</comment>
        <createTable tableName="users">
            <column name="id" type="BIGINT" autoIncrement="true">
                <constraints primaryKey="true" nullable="false"/>
            </column>
            <column name="email" type="VARCHAR(255)" />
            <column name="password" type="VARCHAR(255)" />
        </createTable>
    </changeSet>

    <changeSet id="2" author="test-user">
        <comment>缺少回滾腳本的變更</comment>
        <createTable tableName="temp_table">
            <column name="id" type="INT" />
        </createTable>
    </changeSet>

</databaseChangeLog>
```

#### 7.2 執行測試

```bash
cd test-data
liquibase-linter check changelog/test-changelog.xml
```

預期輸出應包含：
- 命名規範警告（users 表未使用 snake_case）
- 缺少回滾腳本警告

#### 7.3 測試配置檔

建立測試配置：

```yaml
## test-data/.liquibase-linter.yaml
rules:
  naming-conventions:
    enabled: true
    severity: info
  missing-rollback:
    enabled: true
    severity: warning
severity_threshold: info
```

執行測試：

```bash
liquibase-linter check --config=.liquibase-linter.yaml changelog/
```

#### 7.4 測試 CI/CD 整合

建立測試用的 GitHub Actions 工作流程：

```yaml
## .github/workflows/test-lint.yml
name: Test Liquibase Linter

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Download Liquibase Linter
      run: |
        curl -L -o liquibase-linter \
          https://github.com/n2jsoft-public-org/liquibase-linter/releases/latest/download/liquibase-linter-linux-amd64
        chmod +x liquibase-linter
    
    - name: Run Liquibase Linter
      run: ./liquibase-linter check --format=json db/changelog/
```

### 八、輸出格式範例

#### 8.1 Text 格式（預設）

```
Checking: db/changelog/changelog-1.0.xml

[CRITICAL] sql-injection (line 15, changeset: create-user-1)
  Potential SQL injection: String concatenation detected in SQL statement
  Use parameterized queries or Liquibase's built-in change types instead.

[WARNING] missing-rollback (line 10, changeset: add-column-1)
  Changeset does not include a rollback script
  Add a <rollback> block to enable safe rollback of this change.

[INFO] naming-conventions (line 25, changeset: create-table-1)
  Table name 'UserData' does not follow naming convention
  Use lowercase snake_case for table names: user_data

Summary:
  Files checked: 1
  Violations: 3 (1 critical, 1 warning, 1 info)
```

#### 8.2 JSON 格式

```json
{
  "version": "1.0.0",
  "timestamp": "2024-02-04T10:30:00Z",
  "files": [
    {
      "path": "db/changelog/changelog-1.0.xml",
      "violations": [
        {
          "rule": "sql-injection",
          "severity": "critical",
          "message": "Potential SQL injection: String concatenation detected",
          "line": 15,
          "changeset_id": "create-user-1"
        }
      ]
    }
  ],
  "summary": {
    "files_checked": 1,
    "total_violations": 3,
    "critical": 1,
    "warning": 1,
    "info": 1
  }
}
```

### 九、CI/CD 整合範例

#### 9.1 GitHub Actions

```yaml
name: Liquibase Linting

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Download Liquibase Linter
      run: |
        curl -L -o liquibase-linter \
          https://github.com/n2jsoft-public-org/liquibase-linter/releases/latest/download/liquibase-linter-linux-amd64
        chmod +x liquibase-linter
    
    - name: Run Liquibase Linter
      run: ./liquibase-linter check --format=sarif db/changelog/ > results.sarif
    
    - name: Upload results
      uses: github/codeql-action/upload-sarif@v3
      with:
        sarif_file: results.sarif
```

#### 9.2 GitLab CI

```yaml
liquibase-lint:
  stage: test
  script:
    - curl -L -o liquibase-linter \
      https://github.com/n2jsoft-public-org/liquibase-linter/releases/latest/download/liquibase-linter-linux-amd64
    - chmod +x liquibase-linter
    - ./liquibase-linter check --format=json db/changelog/
```

#### 9.3 Jenkins

```groovy
pipeline {
    agent any
    
    stages {
        stage('Liquibase Lint') {
            steps {
                sh 'curl -L -o liquibase-linter \
                     https://github.com/n2jsoft-public-org/liquibase-linter/releases/latest/download/liquibase-linter-linux-amd64'
                sh 'chmod +x liquibase-linter'
                sh './liquibase-linter check --format=json db/changelog/'
            }
        }
    }
}
```

### 十、來源檔案支援

- ✅ XML changelogs
- ✅ SQL formatted changelogs
- ⏳ YAML changelogs（規劃中）
- ⏳ JSON changelogs（規劃中）

### 十一、效能

Liquibase Linter 設計為高速工具：
- 典型變更日誌啟動時間 <100ms
- 處理大型變更日誌目錄僅需數秒
- 使用 Go 的並行運算進行多檔案分析
- 極低的記憶體佔用

### 十二、Exit Codes

- `0`: 未發現違規項目
- `1`: 發現違規項目（基於 `fail_on` 嚴重程度閾值）
- `2`: 執行期間發生錯誤（找不到檔案、解析錯誤等）

### 十三、開發與貢獻

#### 13.1 從原始碼編譯

```bash
git clone https://github.com/n2jsoft-public-org/liquibase-linter.git
cd liquibase-linter

go build -o liquibase-linter ./cmd/liquibase-linter

go test ./...

go test -cover ./...

golangci-lint run
```

#### 13.2 貢獻指南
- [Development Guide](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/development.md) 包含設定與架構詳細資訊
- [Open Issues](https://github.com/n2jsoft-public-org/liquibase-linter/issues) 可發現需要處理的工作項目
- [Pull Request Guidelines](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/development.md#contributing) 說明工作流程

### 十四、測試資料範例

[testdata](https://github.com/n2jsoft-public-org/liquibase-linter/tree/main/testdata) 目錄包含範例變更日誌：

- [example-good-practices.xml](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/testdata/example-good-practices.xml)：符合最佳實踐的結構良好變更日誌
- [example-good-practices.sql](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/testdata/example-good-practices.sql)：SQL 格式且符合最佳實踐的變更日誌
- [problematic-changelog.xml](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/testdata/problematic-changelog.xml)：常見問題範例
- [problematic-changelog.sql](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/testdata/problematic-changelog.sql)：包含違規項目的 SQL 範例

### 十五、參考文檔

- [Usage Guide](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/usage.md)：使用指南
- [Rules Reference](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/rules.md)：完整規則列表與範例
- [Configuration Guide](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/configuration.md)：詳細配置選項
- [Suppression Guide](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/suppression.md)：如何針對特定變更集停用規則
- [CI/CD Integration](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/cicd.md)：各種 CI/CD 平台整合範例
- [Development Guide](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/development.md)：貢獻者與開發者指南

### 十六、支援管道

- 📝 [Documentation](https://github.com/n2jsoft-public-org/liquibase-linter/blob/main/docs/)
- 🐛 [Report Issues](https://github.com/n2jsoft-public-org/liquibase-linter/issues)
- 💬 [Discussions](https://github.com/n2jsoft-public-org/liquibase-linter/discussions)
- ⭐ 若發現此工具有用，請給個 Star！

### 十七、授權與專案資訊

- **授權**：MIT License
- **專案**：[n2jsoft-public-org/liquibase-linter](https://github.com/n2jsoft-public-org/liquibase-linter)
- **開發團隊**：[n2jsoft](https://github.com/n2jsoft)

*技術詞彙使用台灣地區常見譯名*
