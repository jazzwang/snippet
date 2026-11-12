# AI-Infra-Guard 技術報告

## 一、系統概述

### 1.1 專案介紹

**AI-Infra-Guard (A.I.G)** 是由騰訊朱雀實驗室開發的一站式 AI 紅隊測試平台，整合了以下五大安全掃描能力：

1. **AI 基礎設施掃描** (AI Infrastructure Scan) - 域名/IP/URL 指紋與漏洞掃描
2. **LLM 安全評估/越獄檢測** (Model Security Assessment) - OpenAI 相容 API 模型安全測試
3. **MCP 掃描** (MCP Security Scan) - MCP Server 源代碼安全掃描
4. **Skill 掃描** (Skill Security Audit) - AI Agent Skill 專案安全審計
5. **Agent 掃描** (Agent Security Testing) - 動態黑盒安全測試

### 1.2 核心功能

| 功能模組 | 描述 |
|---------|------|
| OpenClaw 安全檢查 | 整合 OpenClaw 安全掃描能力 |
| Agent 安全掃描 | 發送測試提示詞至運行中的 Agent 平台 |
| AI 工具與 Skill 掃描 | 審計 AI 工具與 Skill 的安全性 |
| AI 基礎設施漏洞掃描 | 掃描域名、IP、URL 的指紋與漏洞 |
| LLM 安全評估 | 越獄評估 (Jailbreak Evaluation) |

### 1.3 系統要求

| 組件 | 需求 |
|------|------|
| Docker | 20.10 或更高版本 |
| 記憶體 (RAM) | 4GB 以上 |
| 磁碟空間 | 10GB 以上 |
| Python | ≥ 3.9 (獨立模組使用) |

---

## 二、安裝步驟

### 2.1 完整平台部署（Docker）

#### 方法一：使用預構建映像檔（推薦）

此方法從 Docker Hub 拉取預先構建的映像檔，啟動速度最快。

```bash
# 克隆倉庫
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard

# 使用 docker compose v2+（推薦）
docker compose -f docker-compose.images.yml up -d

# 或使用 docker-compose v1
docker-compose -f docker-compose.images.yml up -d
```

#### 方法二：一鍵安裝腳本（最簡便）

此方法會自動安裝 Docker 並啟動 A.I.G。

```bash
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/main/docker.sh | bash
```

#### 方法三：從源代碼構建

此方法從本地源代碼構建 Docker 映像檔並啟動服務。

```bash
git clone https://github.com/Tencent/AI-Infra-Guard.git
cd AI-Infra-Guard
docker compose up -d
```

### 2.2 Docker Compose 配置說明

```yaml
version: '3.8'

services:
  webserver:
    image: zhuquelab/aig-server:latest
    container_name: ai-infra-guard-webserver
    ports:
      - "8088:8088"
    environment:
      - APP_ENV=production
      - UPLOAD_DIR=/app/uploads
      - DB_PATH=/app/db/tasks.db
      - TZ=Asia/Taipei  # 台灣時區
    volumes:
      - ./data:/app/data
      - ./db:/app/db
      - ./logs:/app/logs
      - ./uploads:/app/uploads
    networks:
      - ai-infra-guard-network
    restart: always
    healthcheck:
      test: [ "CMD", "curl", "http://localhost:8088/" ]
      interval: 30s
      timeout: 3s
      retries: 3

  agent:
    image: zhuquelab/aig-agent:latest
    container_name: ai-infra-guard-agent
    environment:
      - TZ=Asia/Taipei
      - AIG_SERVER=webserver:8088
    cap_add:
      - SYS_ADMIN
    security_opt:
      - seccomp:unconfined
    shm_size: '2gb'
    networks:
      - ai-infra-guard-network
    restart: always
    depends_on:
      webserver:
        condition: service_healthy
```

### 2.3 獨立模組安裝

#### A. AI 基礎設施掃描 (aig-infra-scan)

```bash
pip install aig-infra-scan
```

#### B. LLM 安全評估 (aig-model-scan)

```bash
pip install aig-model-scan
```

#### C. MCP 掃描 (aig-mcp-scan)

```bash
pip install aig-mcp-scan
```

#### D. Skill 掃描 (aig-skill-scan)

```bash
pip install aig-skill-scan
```

#### E. Agent 掃描 (aig-agent-scan)

```bash
pip install aig-agent-scan
```

---

## 三、測試步驟

### 3.1 完整平台測試

#### 步驟一：確認服務啟動

```bash
# 檢查容器狀態
docker compose ps

# 預期輸出：
# ai-infra-guard-webserver   Up    zhuquelab/aig-server:latest
# ai-infra-guard-agent       Up    zhuquelab/aig-agent:latest
```

#### 步驟二：訪問 Web 介面

開啟瀏覽器訪問：`http://localhost:8088`

預期看到 A.I.G 主介面，包含以下功能區：
- 插件管理
- AI 基礎設施掃描
- LLM 安全評估
- MCP 掃描
- Skill 掃描
- Agent 掃描

#### 步驟三：手動啟動 Agent 節點（如需）

```bash
# 在另一終端啟動 Agent 節點
go build -o agent ./cmd/agent
AIG_SERVER=127.0.0.1:8088 ./agent
```

### 3.2 獨立模組測試

#### A. AI 基礎設施掃描測試

```bash
# 基本掃描
aig-infra-scan -t https://example.com

# JSON 輸出格式
aig-infra-scan -t 10.0.0.1 --json -o result.json

# 列出可用漏洞規則
aig-infra-scan --list-vul
```

**測試項目：**
- [ ] 掃描示例網站
- [ ] 驗證漏洞規則列表
- [ ] 確認 JSON 輸出格式

#### B. LLM 安全評估測試

```bash
# 基本評估命令
aig-model-scan \
  --model "gpt-4o-mini" \
  --base_url "https://api.openai.com/v1" \
  --api_key "your-api-key" \
  --max_concurrent 10 \
  --scenarios Bias \
  --techniques Raw
```

**測試項目：**
- [ ] 配置 OpenAI 相容 API
- [ ] 執行偏見測試 (Bias)
- [ ] 執行提示詞注入測試 (PromptInjection)
- [ ] 檢查速率限制處理 (HTTP 429)
- [ ] 驗證輸出報告

#### C. MCP 掃描測試

```bash
# 基本掃描
aig-mcp-scan --repo /path/to/mcp-server -o result.sarif.json

# 指定模型
aig-mcp-scan --repo ./myproject -m "anthropic/claude-3.5-sonnet"

# 使用環境變數 API Key
export LLM_API_KEY="sk-or-v1-xxxxx"
aig-mcp-scan --repo ./myproject
```

**測試項目：**
- [ ] 掃描本地 MCP Server 專案
- [ ] 驗證 SARIF 2.1.0 輸出格式
- [ ] 測試三階段掃描流程

#### D. Skill 掃描測試

```bash
# 基本掃描
export LLM_API_KEY="your-api-key"
aig-skill-scan --repo /path/to/your/skill \
           -m deepseek-v4-flash \
           --language en \
           -o result.sarif.json
```

**測試項目：**
- [ ] 掃描本地 Skill 專案
- [ ] 驗證 SARIF 輸出格式
- [ ] 檢查漏洞分類 (SkillTrustBench T01-T09)

#### E. Agent 掃描測試

```bash
# 基本掃描
aig-agent-scan --agent_provider providers.yaml -k "$LLM_API_KEY" -m deepseek-v3.2-exp

# 指定技能
aig-agent-scan --agent_provider providers.yaml \
  -k sk-xxx \
  -m deepseek-v3.2-exp \
  --skills "data-leakage-detection,tool-abuse-detection"

# 保存結果
python main.py --agent_provider providers.yaml \
  -k sk-xxx \
  -m deepseek-v3.2-exp \
  -o result.json
```

**測試項目：**
- [ ] 配置 Agent 提供者 YAML
- [ ] 執行數據洩漏檢測
- [ ] 執行工具濫用檢測
- [ ] 執行間接提示詞注入檢測

---

## 四、驗證步驟

### 4.1 平台功能驗證

#### 4.1.1 Web 介面驗證

1. **登入驗證**
   - 確認可以無密碼訪問 Web 介面（內部使用）
   - 確認所有功能區塊可正常顯示

2. **插件管理驗證**
   - 點擊「插件管理」
   - 確認可新增、編輯、刪除插件
   - 確認插件配置可保存

3. **掃描任務驗證**
   - 選擇任一掃描功能
   - 配置測試參數
   - 執行掃描任務
   - 驗證結果頁面顯示

#### 4.1.2 掃描結果驗證

**AI 基礎設施掃描驗證項目：**
- [ ] 正確識別目標域名/IP
- [ ] 顯示匹配的指紋資訊
- [ ] 列出檢測到的漏洞
- [ ] 提供修復建議

**LLM 安全評估驗證項目：**
- [ ] 正確連接目標模型
- [ ] 執行指定的測試場景
- [ ] 輸出評估報告
- [ ] 處理速率限制 (HTTP 429)

**MCP 掃描驗證項目：**
- [ ] 三階段流程正常執行
  - 資訊收集 (Info Collection)
  - 代碼審計 (Code Audit)
  - 漏洞覆核 (Vulnerability Review)
- [ ] 輸出 SARIF 2.1.0 格式
- [ ] 計算安全分數

**Skill 掃描驗證項目：**
- [ ] 執行代碼審計
- [ ] 可疑結果觸發漏洞覆核
- [ ] 正常/惡意結果快速通過
- [ ] 輸出 SARIF 格式報告

**Agent 掃描驗證項目：**
- [ ] 成功連接目標 Agent
- [ ] 執行動態黑盒測試
- [ ] 輸出 JSON 安全報告
- [ ] 提供 OWASP ASI 映射

### 4.2 獨立模組驗證

#### 4.2.1 AI 基礎設施掃描驗證

```bash
# 驗證基本功能
aig-infra-scan -t https://example.com

# 驗證輸出格式
aig-infra-scan -t https://example.com --json

# 驗證漏洞規則
aig-infra-scan --list-vul
```

**驗證項目：**
- [ ] 命令正常執行
- [ ] 輸出正確的 JSON 格式
- [ ] 漏洞規則列表可讀取
- [ ] 支持中文提示詞

#### 4.2.2 LLM 安全評估驗證

```bash
# 驗證基本功能
aig-model-scan \
  --model "gpt-4o-mini" \
  --base_url "https://api.openai.com/v1" \
  --api_key "test-api-key" \
  --scenarios Bias \
  --techniques Raw

# 驗證多場景測試
aig-model-scan \
  --model "gpt-4o-mini" \
  --base_url "https://api.openai.com/v1" \
  --api_key "test-api-key" \
  --scenarios "Bias,PromptInjection,Toxic" \
  --techniques Raw
```

**驗證項目：**
- [ ] 正確連接目標 API
- [ ] 多場景測試正常執行
- [ ] 輸出評估報告
- [ ] 速率限制處理正常（等待 8s/16s/32s）
- [ ] 連續 3 次速率限制後跳過剩餘測試

#### 4.2.3 MCP 掃描驗證

```bash
# 驗證基本功能
aig-mcp-scan --repo ./test-mcp-server -o result.sarif.json

# 驗證三階段模式
export LLM_API_KEY="test-key"
aig-mcp-scan --repo ./test-mcp-server --aig-mode
```

**驗證項目：**
- [ ] 單階段模式正常執行（約快 3 倍）
- [ ] 三階段模式正常執行
- [ ] SARIF 2.1.0 格式正確
- [ ] 支持 GitHub Code Scanning 格式

#### 4.2.4 Skill 掃描驗證

```bash
# 驗證基本功能
aig-skill-scan --repo /path/to/skill -m deepseek-v4-flash

# 驗證三階段模式
aig-skill-scan --repo /path/to/skill --aig-mode
```

**驗證項目：**
- [ ] 單階段模式正常執行
- [ ] 三階段模式正常執行
- [ ] 漏洞分類正確 (T01-T09)
- [ ] 判定結果正確 (malicious/suspicious/normal)

#### 4.2.5 Agent 掃描驗證

```bash
# 驗證基本功能
aig-agent-scan --agent_provider providers.yaml -k test-key -m deepseek-v3.2-exp

# 驗證特定技能
aig-agent-scan --agent_provider providers.yaml \
  -k test-key \
  --skills "data-leakage-detection,tool-abuse-detection"
```

**驗證項目：**
- [ ] 成功連接目標 Agent
- [ ] 動態測試正常執行
- [ ] JSON 報告格式正確
- [ ] 支持 10 種檢測技能

### 4.3 整合驗證

#### 4.3.1 多模組併行測試

```bash
# 同時執行多個獨立掃描
aig-infra-scan -t https://example.com --json -o infra_result.json &
aig-model-scan --model "gpt-4o-mini" --base_url "https://api.openai.com/v1" --api_key "test-key" --scenarios Bias --techniques Raw &
wait

# 確認所有任務完成
echo "All scans completed"
```

#### 4.3.2 平台整合驗證

1. **啟動平台**
   ```bash
   docker compose up -d
   ```

2. **執行 Web 介面掃描**
   - 訪問 `http://localhost:8088`
   - 選擇任一掃描功能
   - 執行測試任務

3. **驗證整合輸出**
   - 確認 Web 前端可接收結果
   - 確認結果可視化正常顯示
   - 確認 SARIF/JSON 格式正確

---

## 五、常見問題排錯

### 5.1 Docker 相關問題

#### 問題 1：容器啟動失敗

**症狀：** `docker compose ps` 顯示容器狀態為 `Exited`

**解決方案：**
```bash
# 查看容器日誌
docker compose logs webserver

# 查看容器日誌
docker compose logs agent

# 重新啟動容器
docker compose restart
```

#### 問題 2：端口衝突

**症狀：** `ERROR: port 8088:8088 is already allocated`

**解決方案：**
```bash
# 查找佔用端口的容器
docker ps

# 停止衝突的容器
docker stop <container_id>

# 或使用其他端口
docker compose -f docker-compose.images.yml up -d
```

#### 問題 3：權限問題

**症狀：** 容器內寫入日誌或數據時失敗

**解決方案：**
```bash
# 修改目錄權限
chmod -R 777 ./data ./db ./logs ./uploads

# 或使用 root 用戶啟動
docker compose up -d
```

### 5.2 Python 模組相關問題

#### 問題 1：pip 安裝失敗

**症狀：** `ERROR: Could not find a version that satisfies the requirement...`

**解決方案：**
```bash
# 更新 pip
python -m pip install --upgrade pip

# 安裝指定版本
pip install aig-infra-scan==0.1.0

# 使用國產鏡像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple aig-infra-scan
```

#### 問題 2：API Key 配置問題

**症狀：** `Authentication failed` 或 `Rate limit exceeded`

**解決方案：**
```bash
# 確認 API Key 格式正確
echo $LLM_API_KEY

# 使用環境變數
export LLM_API_KEY="sk-or-v1-xxxxx"

# 確認 API Key 有效
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer your-api-key"
```

#### 問題 3：速率限制處理

**症狀：** 測試過程中出現大量 HTTP 429 錯誤

**解決方案：**
```bash
# 降低並發數
aig-model-scan --model "gpt-4o-mini" --max_concurrent 1 --api_key "your-key"

# 或增加間隔時間
```

### 5.3 Agent 掃描相關問題

#### 問題 1：無法連接目標 Agent

**症狀：** `Connection refused` 或 `Timeout`

**解決方案：**
```bash
# 確認目標 Agent 正在運行
curl http://127.0.0.1:18081/chat

# 確認提供者配置正確
cat providers.yaml

# 確認 API Key 有效
```

#### 問題 2：響應解析失敗

**症狀：** `Failed to parse response`

**解決方案：**
```bash
# 確認 transform_response 配置正確
# 在 providers.yaml 中檢查響應解析邏輯

# 確認目標 Agent 返回的格式
curl -X POST http://127.0.0.1:18081/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "test"}'
```

### 5.4 驗證相關問題

#### 問題 1：SARIF 格式驗證失敗

**症狀：** GitHub Code Scanning 無法解析結果

**解決方案：**
```bash
# 確認 SARIF 版本
head -20 result.sarif.json | grep -i version

# 確認格式正確
python -c "import json; json.load(open('result.sarif.json'))"

# 使用 sarif-visualizer 驗證
pip install sarif-visualizer
sarif-visualizer result.sarif.json
```

#### 問題 2：日誌文件過大

**症狀：** 日誌文件佔用大量磁碟空間

**解決方案：**
```bash
# 限制日誌大小
docker compose down
# 編輯 docker-compose.images.yml
# 添加 log_config 設定

# 或使用 logrotate
logrotate -f /var/log/syslog
```

---

## 六、最佳實踐建議

### 6.1 生產環境部署

1. **使用 Docker Compose 封裝**
   - 避免手動配置多個容器
   - 使用環境變數管理配置

2. **配置時區**
   ```yaml
   environment:
     - TZ=Asia/Taipei
   ```

3. **定期更新映像檔**
   ```bash
   docker compose pull
   docker compose up -d
   ```

4. **配置數據持久化**
   - 使用卷映射保存掃描結果
   - 定期清理舊的日誌文件

### 6.2 安全評估流程

1. **建立基準線**
   - 在正式評估前，先對已知安全的目標進行測試
   - 記錄正常行為作為基準

2. **分階段執行**
   - 先用低風險場景測試
   - 再逐步增加測試強度

3. **記錄與追蹤**
   - 保存所有掃描結果
   - 記錄測試配置與參數
   - 追蹤漏洞修復進度

### 6.3 API 使用建議

1. **合理配置並發數**
   ```bash
   # 開發環境
   --max_concurrent 10

   # 生產環境
   --max_concurrent 5
   ```

2. **使用專用 API Key**
   - 不要使用生產環境的主 API Key
   - 為安全評估設置獨立的限額

3. **監控 API 使用量**
   - 定期檢查 API 使用情況
   - 設置使用量告警

---

## 七、資源連結

### 7.1 官方資源

- **GitHub 倉庫**: https://github.com/Tencent/AI-Infra-Guard
- **官方文檔**: https://tencent.github.io/AI-Infra-Guard/
- **中文文檔**: https://tencent.github.io/AI-Infra-Guard/?menu=getting-started

### 7.2 相關專案

- **OpenClaw**: https://github.com/openclaw/clawscan
- **SkillTrustBench**: https://github.com/Tencent/AI-Infra-Guard
- **Zhuque AI Detection**: https://github.com/Tencent/Zhuque-AI-Detection

### 7.3 社群與支援

- **GitHub Issues**: https://github.com/Tencent/AI-Infra-Guard/issues
- **GitHub Discussions**: https://github.com/Tencent/AI-Infra-Guard/discussions

---

## 八、版本資訊

| 組件 | 當前版本 | 最新發布 |
|------|---------|---------|
| A.I.G Platform | 見 Docker Hub | https://hub.docker.com/r/zhuquelab/aig-server |
| aig-infra-scan | v0.x | https://pypi.org/project/aig-infra-scan/ |
| aig-model-scan | v0.x | https://pypi.org/project/aig-model-scan/ |
| aig-mcp-scan | v0.x | https://pypi.org/project/aig-mcp-scan/ |
| aig-skill-scan | v0.x | https://pypi.org/project/aig-skill-scan/ |
| aig-agent-scan | v0.x | https://pypi.org/project/aig-agent-scan/ |

---

## 九、附錄

### 9.1 快速參考命令

```bash
# 一鍵安裝
curl https://raw.githubusercontent.com/Tencent/AI-Infra-Guard/main/docker.sh | bash

# 啟動 Docker 平台
docker compose -f docker-compose.images.yml up -d

# AI 基礎設施掃描
aig-infra-scan -t https://example.com

# LLM 安全評估
aig-model-scan --model "gpt-4o-mini" --scenarios Bias --techniques Raw

# MCP 掃描
aig-mcp-scan --repo ./mcp-server -o result.sarif.json

# Skill 掃描
aig-skill-scan --repo ./skill -o result.sarif.json

# Agent 掃描
aig-agent-scan --agent_provider providers.yaml -k "$LLM_API_KEY"
```

### 9.2 參考文獻

1. OWASP ASI (AI Security)
2. SkillTrustBench 漏洞分類
3. SARIF 2.1.0 規範
4. OpenAI API 規格

---

**報告版本**: 1.0  
**最後更新**: $(date +"%Y-%m-%d %H:%M:%S %Z")  
**作者**: AI-Infra-Guard 技術團隊  
**許可**: Apache License 2.0
