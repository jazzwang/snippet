# AgentShield 技術摘要（中文）

- Git Repo
  - https://github.com/affaan-m/agentshield

## 2026-09-07

- 緣起：
  - 研究 https://www.skills.sh/affaan-m/ecc/deep-research 作者 Affaan Mustafa 的 [Github Repo](https://github.com/affaan-m) 發現的 Agent 資安掃描工具

## 專案定位

[AgentShield](https://github.com/affaan-m/agentshield) 是一套針對 **AI Agent 組態安全** 的稽核工具，核心目標是掃描 Claude Code / 類似代理開發環境中的風險設定，提早發現可被攻擊者利用的弱點。

它提供多種交付型態：
- CLI（本機與 CI 掃描）
- GitHub Action（PR / pipeline 安全閘）
- GitHub App 生態整合
- 可攜式證據包（evidence pack）與 SARIF 匯出

## 核心能力
AgentShield 主要檢查五大面向：
1. **Secrets**：硬編碼 API key、Token、密碼、連線字串、私鑰片段
2. **Permissions**：過度寬鬆授權（如 `Bash(*)`、`Write(*)`）、缺乏 deny list
3. **Hooks**：命令注入、資料外洩、靜默失敗、危險啟動腳本
4. **MCP 伺服器**：高風險 MCP、未釘版套件、遠端傳輸、autoApprove 等
5. **Agent Prompt**：提示注入、越權指令、隱藏指令、輸出操控

README 中指出其規則集已擴展至多模組、多百條規則等級，並使用嚴重度分級（critical/high/medium/low/info）與總分（0–100）評估安全姿態。

## 風險評分模型
- 初始分數 100，依問題嚴重度扣分（critical/high/medium/low）
- 額外列出「Recognized Defenses」（例如 deny/ask、安全 sandbox、阻擋型 hook）
- 防禦設定 **不加分也不扣分**，避免以裝飾性規則灌分
- 報告包含 `runtimeConfidence`，區分：
  - `active-runtime`
  - `project-local-optional`
  - `template-example`
  - `docs-example`
  - `plugin-cache` / `plugin-manifest` / `hook-code`

這個設計的價值在於：可將「真正在跑的風險」與「樣板/文件中的風險訊號」分層處理，降低誤判干擾。

## 進階安全機制

### 1) Auto-fix（`--fix`）

可自動套用安全修補（例如秘密改為環境變數引用、收斂部分通配權限），並在修補後重掃：
- 若分數惡化或新增高風險，會回滾修改
- 輸出修補驗證資訊（attestation）

### 2) 對抗式深度分析（`--opus`）

採三代理流程：
- Attacker（紅隊）
- Defender（藍隊）
- Auditor（審計整合）

用來找多步驟攻擊鏈，而非只做靜態規則比對。

### 3) Supply chain 檢查

可對 MCP 與套件來源做離線/線上驗證，觀察：
- npm / git 來源與釘版狀態
- 維護者、下載量、postinstall 風險
- package manager 設定（registry 憑證、lifecycle scripts、release-age gate）

### 4) 組織政策治理

支援 policy init/export/promote，包含：
- 最低分數、最高容忍嚴重度
- 必要 deny 規則
- 有期限例外（exception）與 owner/ticket

## 輸出與整合

- 終端輸出：適合人工檢視
- JSON：適合自動化管線與機器消費
- Markdown/HTML：適合稽核與管理報告
- SARIF：可接 GitHub code scanning
- Evidence Pack：可驗證雜湊、可攜式審計證據

GitHub Action 可作為安全閘：

- 依嚴重度決定是否 fail
- 支援 baseline 漂移比較（新增/解除/未變更）
- 支援 policy 與 supply-chain gate

## 架構觀察（程式層）

程式碼結構模組化明確：
- `scanner/`：檔案探索與掃描協調
- `rules/`：風險規則庫（secrets/permissions/hooks/mcp/agents）
- `reporter/`：分數引擎與多格式輸出
- `fixer/`：自動修補
- `policy/`、`compliance/`：治理與合規映射
- `supply-chain/`、`runtime/`、`watch/`：供應鏈、運行監測與變更追蹤

此外，專案內建 **MiniClaw**（極簡沙箱化 agent runtime），用於縮小攻擊面：
- 單一 HTTP 入口
- Prompt sanitization
- 工具白名單分級
- 沙箱檔案系統與路徑保護

## 實務價值

AgentShield 的定位不是取代雲端 SAST，而是補上「**Agent 組態安全**」這塊傳統工具常忽略的區域：
- 把 prompt/hook/MCP/tool-permission 納入可量化治理
- 提供可落地的 CI gate 與基線比較
- 兼顧高靈敏度與可解釋性（runtimeConfidence、defense listing、evidence pack）

對於正在導入 AI coding agents 的團隊，這類工具可作為「上線前組態審查」與「持續治理」的基礎設施。

## 總結
AgentShield 是一個面向新型 AI 代理攻擊面的專用稽核器，技術路線結合：
- 規則式掃描
- 分層信心標記
- 自動修補與回滾
- 對抗式深度分析
- CI/CD 與合規證據輸出

若你的開發流程已大量依賴 Claude Code / MCP / Hook / 子代理配置，AgentShield 的最大價值在於把「容易被忽略的組態風險」變成可持續、可驗證、可治理的安全流程。

## 偏實作導向版（含導入步驟與 CI 範例）

以下提供一套可直接落地的最小導入流程，適合先從「可見性」再走向「強制閘門」。

### A. 本機導入（開發者工作站）

1. **先做一次基準掃描（不阻擋）**
   ```bash
   npx ecc-agentshield scan --format terminal
   ```
2. **輸出 JSON 供後續自動化使用**
   ```bash
   npx ecc-agentshield scan --format json > agentshield-report.json
   ```
3. **先修可自動修復項目**
   ```bash
   npx ecc-agentshield scan --fix
   ```
4. **建立 baseline（作為未來漂移比較基準）**
   ```bash
   npx ecc-agentshield baseline write --path . --output .github/agentshield-baseline.json
   ```

> 建議：第一次導入先不要求「零風險」，而是先凍結當前狀態，接著只擋「新增風險」。

### B. 優先修補順序（建議）

1. **Critical secrets**（硬編碼金鑰/Token）
2. **Wildcard 權限**（如 `Bash(*)`, `Write(*)`）
3. **可外連且可插值的 hooks**（例如含 `${file}` 且有 `curl/wget`）
4. **高風險 MCP server**（未釘版、自動安裝、remote transport）
5. **Agent prompt 的越權/隱藏指令**

這個順序通常能最快降低可被立即利用的攻擊面。

### C. GitHub Actions：最小可用版本

建立 `.github/workflows/agentshield.yml`：

```yaml
name: AgentShield Scan

on:
  pull_request:
  push:
    branches: [main]

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Run AgentShield
        uses: affaan-m/agentshield@v1
        with:
          path: "."
          min-severity: "medium"
          fail-on-findings: "true"
          format: "sarif"
          sarif-output: "agentshield-results.sarif"

      - name: Upload SARIF
        if: always()
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: agentshield-results.sarif
```

用途：在 PR 階段即時看到安全問題，並可於 Security 頁面集中追蹤。

### D. 進階 CI：Baseline 漂移閘（降低導入阻力）

當既有技術債較多時，建議先用 baseline gate：

```yaml
- name: AgentShield Drift Gate
  uses: affaan-m/agentshield@v1
  with:
    path: "."
    baseline: ".github/agentshield-baseline.json"
    fail-on-findings: "false"
    min-severity: "medium"
```

策略說明：
- 不因歷史問題直接卡住開發
- 僅在「新增/惡化」時阻擋
- 逐步償還舊風險

### E. 進階 CI：Policy + Supply Chain + Evidence Pack

```yaml
- name: AgentShield Policy & Supply Chain
  uses: affaan-m/agentshield@v1
  with:
    path: "."
    format: "json"
    min-severity: "medium"
    fail-on-findings: "true"
    policy: ".agentshield/policy.json"
    fail-on-policy: "true"
    supply-chain: "true"
    supply-chain-online: "false"
    evidence-pack: "agentshield-evidence"
    verify-evidence-pack: "true"
```

用途：
- **Policy**：把安全要求制度化（最低分數、最高嚴重度、必要 deny）
- **Supply chain**：補強 MCP/套件供應鏈可疑訊號
- **Evidence pack**：保留可驗證稽核證據，利於內控/客戶稽核

### F. 團隊落地建議（30 天）

- **第 1 週**：只掃描、不阻擋；盤點熱點檔案與 critical/high
- **第 2 週**：啟用 `--fix` + 人工審查權限收斂；建立 baseline
- **第 3 週**：PR 啟用 `min-severity=high` 阻擋新增高風險
- **第 4 週**：導入 policy/evidence pack，逐步收緊至 `medium`

這樣的漸進式導入可兼顧交付速度與安全治理成熟度。