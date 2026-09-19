# fast-jev-compaction

- Git Repo
  - https://github.com/tamaratran/fast-jev-compaction

> [!NOTE]
> Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one fast request, stale ones are dropped or truncated, everything kept stays verbatim.

## 2026-09-19

- Learn from:
  - https://www.linkedin.com/feed/update/urn:li:activity:7506720858409873410
- Tool: Pi Agent + llama.cpp + Qwen3.5-9B

!!! QUESTION
> [!QUESTION]
> 請根據 https://github.com/tamaratran/fast-jev-compaction 撰寫一篇技術報告並包含 step-by-step 測試步驟，經 /skill:speak-human-tw 潤飾詞句後，儲存至 fast-jev-compaction.md

## fast-jev-compaction 技術報告

### 1. 專案概述

`fast-jev-compaction` 是一個用於 LLM 代理的持續性語境壓縮庫，使用 TypeSafe 的 Jev 模型進行智能決策。其核心理念是：傳統的語境壓縮會要求 LLM 對舊對話進行摘要，但這種摘要會造成資訊遺失——檔案路徑、精確錯誤、限制條件或指令都可能消失，而這些資訊在後續可能仍然重要。

這個庫從不重新寫入任何內容，只刪除 Jev 判斷不再需要的工具呼叫和工具結果，並保留所有需要保留的內容原汁原味。

### 2. 系統架構

#### 2.1 模組結構

```
src/
├── index.ts          # 主要匯出入口
├── client.ts         # API 客戶端實作
├── compact.ts        # 核心壓縮邏輯
├── messages.ts       # 訊息處理與格式化
├── request.ts        # HTTP 請求建構
├── state.ts          # 狀態管理與 fitState 演算法
└── types.ts          # TypeScript 類型定義

hooks/
└── fast-jev.ts       # Claude Code 擴充功能勾子

tests/
├── fast-jev-compaction.test.ts  # 核心單元測試
└── hook.test.ts                 # 勾子測試

examples/
└── demo.ts         # 示範程式碼

types/
└── claude-code.d.ts    # Claude Code 類型參考
```

#### 2.2 核心元件

| 元件 | 功能 |
|------|------|
| `compactMessages()` | 主要 API，執行完整的語境壓縮流程 |
| `JevClient` | API 客戶端，支援自定義 `fetch` 實現 |
| `fitState()` | 狀態壓縮演算法，將對話歷史壓縮到指定 token 上限 |
| `decideCall()` | 根據 Jev 的機率判斷是否保留工具呼叫/結果 |
| `applyDecisions()` | 應用決策結果，重建訊息列表 |

### 3. 工作流程

#### 3.1 壓縮流程圖

```
┌─────────────────────────────────────────────────────────┐
│                      輸入：對話歷史                        │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  1. 標記 Pinning：首條訊息與最新 N 條訊息永不處理         │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  2. 構建 State：完整對話歷史 + 工具結果簡短註記            │
│     - 工具輸入包含在內                                      │
│     - 文字內容包含在內                                      │
│     - 不進行任何摘要                                       │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  3. 狀態適配 (fitState)：根據 maxStateTokens 進行多階段壓縮 │
│     ├── 階段 1：工具輸入截斷 (1000 → 200 → 60 字元)       │
│     ├── 階段 2：長文字縮減 (頭尾顯示)                       │
│     ├── 階段 3：舊訊息摺疊 ( […N 字元略過…] )              │
│     ├── 階段 4：舊工具呼叫簡化 (單行顯示)                   │
│     └── 階段 5：無工具呼叫訊息排除                          │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  4. 問題分組：將工具呼叫分為多個批次                       │
│     - 每批次保持 state + 問題 < maxRequestTokens            │
│     - 同一完整狀態會重複發送給每個批次                      │
│     - 請求並行執行，答案合併                                │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  5. Jev 評分：對每個工具呼叫提出兩個問題                    │
│     ├── keepCall: 工具呼叫本身是否仍需保留                 │
│     └── keepResult: 完整結果內容是否仍需保留                │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  6. 決策應用：根據 keepThreshold 進行判斷                   │
│     ├── keepResult ≥ threshold → 保留呼叫和結果            │
│     ├── keepCall ≥ threshold → 保留呼叫，截斷結果          │
│     └── 否則 → 刪除呼叫及其結果                            │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  7. 重建訊息列表：移除內容完全丟失的訊息                   │
│     - 未受觸動的訊息保持原樣                               │
│     - 絕不會留下沒有對應呼叫的結果                         │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│                      輸出：壓縮後的對話                      │
│              附帶決策記錄與統計資訊                          │
└─────────────────────────────────────────────────────────┘
```

#### 3.2 詳細步驟說明

##### 步驟 1：Pinning 機制

- **首條訊息 (index 0)**：永遠保留，包含初始指令或約束
- **最新 N 條訊息**：由 `preserveRecentMessages` 參數控制，預設為 6
- 這些訊息中的工具呼叫不會被處理

```typescript
const transcript: Message[] = [
  { role: 'user', text: 'Fix the failing test. Never edit src/generated.', toolUses: [] },
  {
    role: 'assistant',
    text: '',
    toolUses: [{ tool_use_id: 'toolu_1', tool: 'Read', input: { file_path: 'src/a.ts' } }],
  },
  { role: 'user', text: '', toolUses: [], toolResults: [{ tool_use_id: 'toolu_1', text: '…file…' }] },
  // …
];

const result = await compactMessages(transcript, { preserveRecentMessages: 4 });
```

##### 步驟 2：State 構建

State 是發送給 Jev 的完整對話歷史，特點包括：

- **工具結果替換**：每個工具結果被替換為短註記，例如 `ok, 4213 chars (omitted)`
- **工具輸入保留**：工具呼叫的輸入參數完整保留
- **文字內容保留**：使用者和助手文字完全保留，不進行摘要

```typescript
const state = {
  history: [
    { i: 0, text: 'Fix the failing test...' },
    {
      i: 1,
      tool_calls: [{
        id: 't1',
        tool: 'Read',
        input: { file_path: 'src/a.ts' },
        result: 'ok, 4213 chars (omitted)'
      }]
    },
    // ...
  ],
  goal: 'Fix the failing test',
  // ...
};
```

##### 步驟 3：Token 適配策略

Token 估算不使用tokenizer，而是使用以下公式：
- 每 6 個字母算作 1 個字
- 每個數字算作 0.5 個 token
- 其他符號算作約 1 個 token

這種估算會有意設計為略微高於 Jev 報告的 token 數。

**適配階段（依序執行）：**

| 階段 | 操作 | 觸發條件 |
|------|------|----------|
| `full` | 完整狀態 | 初始狀態 |
| `inputs<=1000` | 工具輸入截斷至 1000 字元 | token 超過上限 |
| `inputs<=200` | 工具輸入截斷至 200 字元 | 仍超過上限 |
| `inputs<=60` | 工具輸入截斷至 60 字元 | 仍超過上限 |
| `texts abridged` | 長文字縮減為頭尾顯示 | 仍超過上限 |
| `old messages collapsed` | 舊訊息摺疊為 `[…N 字元略過…]` | 仍超過上限 |
| `old calls compacted` | 舊工具呼叫簡化為單行顯示 | 仍超過上限 |
| `old calls merged` | 多個舊呼叫合併為一筆 | 仍超過上限 |
| `too large` | 即使摺疊後仍超過上限 | 拋出錯誤 |

##### 步驟 4：問題分組與並行請求

- 每個批次包含一組工具呼叫的問題
- 同一完整狀態會重複發送給每個批次
- 請求並行執行
- 答案合併後應用決策

```typescript
// 批次配置
const options = {
  maxRequestTokens: 30_000,  // 低於 Jev 的 32k 請求上限
  // ...
};

// 批次分組
const batches = batchCalls(calls, 29_600, options);
// 如果狀態佔用 29,600 字節，則每批次只能處理少量問題
```

##### 步驟 5：Jev 評分機制

Jev 對每個工具呼叫（排除已 pin 的）評估兩個問題：

```typescript
interface JevQuestions {
  call_<id>: { type: 'noul', noul: number }  // 呼叫本身
  result_<id>: { type: 'noul', noul: number } // 完整結果
}

// 範例評分
{
  call_t1: { noul: 0.95 },  // 呼叫保留機率 95%
  result_t1: { noul: 0.70 } // 結果保留機率 70%
}
```

##### 步驟 6：決策邏輯

| keepResult | keepCall | 動作 |
|------------|----------|------|
| ≥ threshold | ≥ threshold | `keep` - 保留呼叫和結果 |
| < threshold | ≥ threshold | `drop_result` - 保留呼叫，截斷結果 |
| < threshold | < threshold | `drop_call` - 刪除呼叫及其結果 |

**預設參數：**
- `keepThreshold: 0.5` - 最小保留機率
- `truncateHeadChars: 300` - 截斷結果保留的字元數

##### 步驟 7：結果重建

- 完全丟失內容的訊息會被移除
- 未受觸動的訊息保持原樣
- 絕不會留下沒有對應呼叫的結果

### 4. API 參數與選項

#### 4.1 核心選項

| 選項 | 預設值 | 說明 |
|------|--------|------|
| `apiKey` | `TYPESAFE_API_KEY` | TypeSafe API 金鑰 |
| `model` | `jev-latest` | Jev 模型名稱 |
| `baseUrl` | `https://api.typesafe.ai/v1/systemone` | System One 端點 |
| `fetch` | 原生 `fetch` | 可注射的 fetch 實現（用於測試）|
| `goal` | 最後 3 個使用者提示 | 持續任務描述，包含在 state 中 |
| `keepThreshold` | `0.5` | 呼叫或結果保留的最小機率 |
| `preserveRecentMessages` | `6` | 最新訊息永不處理 |
| `maxStateTokens` | `25000` | State 的 estimated token 上限 |
| `maxRequestTokens` | `30000` | State + 問題的 estimated token 上限 |
| `truncateHeadChars` | `300` | 捨棄結果保留的字元數 |

#### 4.2 統計資訊

`result.stats` 包含：
- `messagesBefore` / `messagesAfter` - 訊息數量變化
- `calls` - 工具呼叫數量
- `resultsDropped` - 捨棄的結果數量
- `kept` - 保留的結果數量
- `callsDropped` - 捨棄的呼叫數量
- `pinned` - 已 pin 的呼叫數量
- `stateStage` - 使用的適配階段
- `tokens` - State 的 estimated token 數
- `requests` - API 請求數量

### 5. 安裝與使用

#### 5.1 作為 npm 包

```bash
npm install fast-jev-compaction
export TYPESAFE_API_KEY="your_key_here"
```

```typescript
import {
  compactMessages,
  reductionRatio,
  type Message
} from 'fast-jev-compaction';

const transcript: Message[] = [
  { role: 'user', text: 'Fix the failing test.', toolUses: [] },
  {
    role: 'assistant',
    text: '',
    toolUses: [{ tool_use_id: 'toolu_1', tool: 'Read', input: { file_path: 'src/a.ts' } }],
  },
  { role: 'user', text: '', toolUses: [], toolResults: [{ tool_use_id: 'toolu_1', text: '…file…' }] },
];

const result = await compactMessages(transcript, { preserveRecentMessages: 4 });
console.log(result.messages, result.decisions, result.stats);

// 如果壓縮比例過低，可能不值得壓縮
if (reductionRatio(result) < 0.25) {
  // 保持原樣或改用摘要方式
}
```

#### 5.2 自定義 Transport

```typescript
// 實現 JevAsker 介面
interface JevAsker {
  ask(state: unknown, questions: JevQuestions): Promise<{
    answers: Record<string, { type: 'noul', noul: number }>
  }>;
}

// 使用自定義客戶端
await compact(messages, asker, options);

// 建構請求和解析回應的工具
import { buildJevRequest, parseJevResponse } from 'fast-jev-compaction';
```

#### 5.3 核心函數模組

| 函數 | 說明 |
|------|------|
| `collectToolCalls` | 收集工具呼叫及其結果 |
| `fitState` | 將狀態壓縮到指定 token 上限 |
| `batchCalls` | 將工具呼叫分為多個批次 |
| `decideCall` | 判斷是否保留工具呼叫 |
| `applyDecisions` | 應用決策結果 |

### 6. Claude Code 擴充功能

#### 6.1 安裝步驟

1. **啟用 function hooks**（Claude Code 2.1.274+）

```json
// ~/.claude/settings.json
{
  "env": {
    "CLAUDE_CODE_ENABLE_FUNCTION_HOOKS": "1",
    "TYPESAFE_API_KEY": "<your key>"
  }
}
```

2. **添加至 Marketplace**

```bash
claude plugin marketplace add tamaratran/fast-jev-compaction
```

3. **安裝擴充功能**

```bash
claude plugin install fast-jev-compaction@fast-jev-compaction
```

安裝時會提示配置選項（API 金鑰、閾值、`truncateHeadChars` 等），可選擇使用預設值。

4. **重新啟動或重新載入**

```bash
claude /reload-plugins
```

#### 6.2 使用方式

- `/compact` - 手動執行壓縮
- 自動壓縮 - 根據 `compactAtPercent` 設定自動觸發

**Toast 顯示：**
- `fast-jev-compaction: kept N/M messages, no summary (…)` - 成功壓縮
- `fallback to built-in summary (…)` - 回退至內建摘要

#### 6.3 本地開發

```bash
CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1 claude --plugin-dir .
```

無需發布步驟，只需從倉庫根目錄執行。

### 7. 測試步驟

#### 7.1 基礎測試環境準備

```bash
cd /path/to/fast-jev-compaction

## 安裝依賴
npm install

## 檢查類型
npm run typecheck

## 執行測試
npm test
```

#### 7.2 詳細測試步驟

##### 步驟 1：執行核心功能測試

```bash
npm test
```

**測試覆蓋範圍：**
- `options` - 選項預設值與驗證
- `token estimate` - Token 估算準確性
- `tool call collection` - 工具呼叫收集
- `state fitting` - 狀態適配各階段
- `question batching` - 問題分組
- `decisions` - 決策邏輯
- `compact` - 完整壓縮流程
- `HTTP client` - API 客戶端

##### 步驟 2：檢查測試輸出

測試會輸出：
- 每個決策的詳細資訊
- 保留/捨棄的統計數據
- State 適配階段
- API 請求數量

##### 步驟 3：執行範例程式碼

```bash
npm run demo
```

**預期輸出：**
```bash
id | tool | action | keep call | keep result
t1 | Read | drop_result (keepCall ≥ threshold) | 0.95 | 0.70
...

stats: {...}
chars saved: XX.X%
messages: M → N
```

#### 7.3 類型檢查測試

```bash
npm run typecheck
```

檢查：
- 核心庫類型定義
- 勾子類型定義

#### 7.4 構建測試

```bash
npm run build
```

確認 TypeScript 編譯成功，產生 `dist/` 目錄。

#### 7.5 插件驗證

```bash
npm run validate:plugin
```

驗證 Claude Code 插件配置。

### 8. 範例程式碼分析

#### 8.1 範例轉錄結構

```typescript
const messages: Message[] = [
  user('Fix the failing parser test in the checkout service. ...'),
  assistant('I will inspect the test and the parser implementation first.'),
  ...call('Glob', { pattern: 'src/**/*.ts' }, 'src/parser.ts
  src/parser.test.ts
  src/legacy/parser.ts'),
  ...call('Read', { file_path: 'src/legacy/parser.ts' }, legacyTs),
  // ...
];

const result = await compactMessages(messages, { preserveRecentMessages: 2 });

console.log('id | tool | action | keep call | keep result');
for (const d of result.decisions) {
  console.log(
    `${d.id} | ${d.tool} | ${d.action} (${d.reason}) | ${d.keepCall.toFixed(2)} | ${d.keepResult.toFixed(2)}`
  );
}
console.log('');
console.log('stats:', JSON.stringify(result.stats));
console.log(`chars saved: ${(reductionRatio(result) * 100).toFixed(1)}%`);
console.log(`messages: ${result.stats.messagesBefore} → ${result.stats.messagesAfter}`);
```

#### 8.2 決策輸出格式

| ID | Tool | Action | Keep Call | Keep Result |
|----|------|--------|-----------|-------------|
| t1 | Read | drop_result (keepCall ≥ threshold) | 0.95 | 0.70 |
| t2 | Read | keep | 0.98 | 0.96 |
| t3 | Bash | drop_result (keepCall ≥ threshold) | 0.92 | 0.65 |
| t4 | Bash | drop_call (keepCall < threshold) | 0.35 | 0.28 |

### 9. 限制與注意事項

#### 9.1 已知限制

1. **僅處理工具呼叫和結果**：文字訊息不會被移除或縮短（僅在 state 中被摘要）

2. **Token 大小為估算值**：基於字元計數，而非實際 tokenizer

3. **校准在請求層級**：機率並非證明結果安全的保證，助手可以隨時重新執行工具

4. **完整狀態重複發送**：靠近 state 上限的歷史會導致每個批次的手數問題需要一次請求

#### 9.2 最佳實踐

1. **設定合理上限**：根據實際使用情況調整 `maxStateTokens` 和 `maxRequestTokens`

2. **監控壓縮比例**：當 `reductionRatio` 低於 0.25 時，可能不值得壓縮

3. **保留重要訊息**：適當設定 `preserveRecentMessages` 以保護關鍵對話

4. **處理錯誤**：Jev 失敗、回應格式錯誤或狀態無法適配時需要回退機制

### 10. 開發指南

#### 10.1 開發命令

```bash
npm install              # 安裝依賴
npm run typecheck        # 檢查類型
npm test                 # 執行測試
npm run build            # 構建
npm run validate:plugin  # 驗證插件
TYPESAFE_API_KEY="$(cat ~/.typesafe_key)" npm run demo
```

#### 10.2 動畫演示

**macOS 專用演示程式：**

```bash
demo/JevDemo/build.sh  # 建立並啟動演示程式
```

**功能說明：**
- SwiftUI 應用程式
- 在 Claude Code 風格終端中重現壓縮流程
- 工具呼叫會被評分
- Jev 捨棄的結果和呼叫會變紅並摺疊
- 其他內容保持原樣
- 不使用實際 API，適合螢幕錄影

### 11. 參考資源

- [TypeSafe 官方文件](https://www.typesafe.ai/)
- [Claude Code 插件文檔](https://code.claude.com/docs/en/plugins)
- [Claude Code 插件參考](https://code.claude.com/docs/en/plugins-reference)
- [Claude Code 勾子文檔](https://code.claude.com/docs/en/hooks)

### 12. 總結

`fast-jev-compaction` 提供了一種創新且保守的語境壓縮方法：

- **保守性**：從不重新寫入或摘要內容，只刪除確定不需要的部分
- **透明性**：所有保留的內容都是原始訊息，可追溯
- **效率**：透過智能評分和並行請求實現快速壓縮
- **可靠性**：完善的錯誤處理和回退機制

這個庫不僅可以用作 npm 包，還可以作為 Claude Code 的擴充功能，為開發者提供了一套完整的語境管理解決方案。透過精確的 token 適配策略、智能的決策機制和並行的 API 請求，它能夠在保持對話上下文完整性的同時，有效減少 token 使用量。

### 13. 附錄：完整測試腳本

```bash
##!/bin/bash
## fast-jev-compaction 完整測試腳本

set -e

echo "=== 測試環境檢查 ==="
node --version
npm --version

echo ""
echo "=== 安裝依賴 ==="
npm install

echo ""
echo "=== 類型檢查 ==="
npm run typecheck

echo ""
echo "=== 執行測試 ==="
npm test

echo ""
echo "=== 構建 ==="
npm run build

echo ""
echo "=== 驗證插件 ==="
npm run validate:plugin

echo ""
echo "=== 執行範例 ==="
npm run demo

echo ""
echo "=== 測試完成 ==="
```