# Pi Agent 與 Claude Code Hooks 相容性說明

## 2026-11-11

```
Date:       11/11/2026, 11:47:45 AM
Models:     google/gemini-3.5-flash-lite, llama.cpp/unsloth/Qwen3.5-9B
Messages:   4 user, 25 assistant, 21 tool results, 1 compactions
Tool Calls: 22
Tokens:     ↑69k ↓14k R380k
Cost:       0.015
```

> [!NOTE]
> Pi Agent 有支援 claude code hook 的設計嗎？
> 請將結果存到 ~/git/snippet/js/pi-agent/pi-hooks.md

## 總結

Pi Agent 在設計上原生主要使用自己的一套強大 TypeScript 擴充與事件系統（Extension API 與 `pi.on(...)`），但透過生態系中的套件與模組，**完整支援並相容 Claude Code 的 Hook 與專案設定設計**。

## 1. 核心的事件驅動系統（Pi 自己的 Hook 機制）

Pi 內建了豐富的生命週期與事件監聽機制（透過 `ExtensionAPI`），你可以用 TypeScript 寫出類似 Hook 的行為：

- `pi.on("session_start")` / `pi.on("session_shutdown")`
- `pi.on("tool_call")`（可在工具執行前攔截、修改輸入或阻擋，類似 Claude Code 的 `PreToolUse`）
- `pi.on("before_agent_start")` / `pi.on("agent_end")`
- `pi.on("user_bash")` 等

官方與範例庫中也提供了許多現成的擴充套件（位於 `@earendil-works/pi-coding-agent/examples/extensions/`），例如：
- 權限閘道 (`permission-gate.ts`)
- 路徑保護 (`protected-paths.ts`)
- Git 檢查點 (`git-checkpoint.ts`)
- 專案規則 (`claude-rules.ts`)

## 2. 針對 Claude Code Hook（`.claude/settings.json`）的相容支援

如果你在專案中已經有用於 Claude Code 的 Hook 設定或 `.claude/settings.json`，Pi 生態系中有專門的套件可以無縫對應：

### 相容套件
- **`pi-code` / `pi-hooks` / `pi-match-rules` 等套件**：
  這些套件（例如透過 `pi install` 安裝）會自動讀取 `.claude/settings.json`（或專案根目錄的 `.claude/` 設定）中的 Hook 定義。

### 事件對應
這些套件會將 Claude Code 的生命週期事件轉譯並對應到 Pi 的事件系統中：
- `SessionStart` → `session_start`
- `PreToolUse` → `tool_call`（可攔截、修改輸入或阻擋）
- `PostToolUse` → `tool_call`（可處理結果並獲取 `additionalContext`）
- `UserPromptSubmit` → `input`
- `PreCompact` → `session_before_compact`
- `Stop` → `agent_settled`
- `SessionEnd` → `session_shutdown`

這讓原有的 shell 指令 Hook、stdin/json 傳輸與 `additionalContext` 捕捉機制在 Pi 底下也能直接運作。

### 3. Claude 專案規則（`.claude/rules/`）

Pi 也有對應的擴充套件，例如 `claude-rules.ts` 範例或 `pi-match-rules` 套件，能夠：
- 自動掃描專案中的 `.claude/rules/` 目錄
- 將裡面的 Markdown 規則檔案自動載入並注入 Pi 的系統提示詞中
- 維持與 Claude Code 相同的專案規範體驗

### 使用範例

#### 安裝相容套件
```bash
pi install npm:@hsingjui/pi-hooks
## 或
pi install npm:@fyeeme/pi-hooks
```

#### 使用 Pi 原生擴充
```typescript
// 在 ~/.pi/agent/extensions/my-hook.ts
pi.on("tool_call", async (event) => {
  // 攔截或修改工具調用
  if (event.tool.name === "dangerous_tool") {
    return {
      status: "error",
      message: "禁止執行此工具"
    };
  }
});
```

#### 使用 Claude Code Hook 設定
```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "echo 'Checking tool permission'",
        "stdin": "{\"tool_name\": \"{{tool.name}}\"}"
      }
    ]
  }
}
```

### 結論

- **如果要用 Pi 原生寫 Hook**：使用 Pi 的 TypeScript 擴充功能（Extension API）。
- **如果要直接沿用 Claude Code 的 Hook / 設定檔（`.claude/settings.json`）**：安裝生態系中的相容套件（如 `pi-code` / `pi-hooks`），即可直接讀取並運作。

> [!NOTE]
> 請幫我搜尋 pi-hooks 的 github repo 並根據 repo 內容撰寫一篇技術報告，包括 step-by-step 安裝、測試、驗證的步驟。並將這次的對話附加 append 到 ~/git/snippet/js/pi-agent/pi-hooks.md

## Pi-Hooks 技術報告：Claude Code Hooks 相容性擴充套件

### 摘要

`pi-hooks` 是一個專為 Pi Coding Agent 設計的擴充套件，它將 **Claude Code 的 Hook 配置格式**轉譯為 Pi 的事件系統，讓開發者可以無縫沿用已有的 Claude Code Hook 工作流程。本報告詳細介紹了該套件的安裝、配置、測試與驗證步驟。

### 1. 套件資訊

#### 1.1 基本資訊

| 項目 | 內容 |
|------|------|
| 套件名稱 | `@hsingjui/pi-hooks` |
| GitHub | [https://github.com/hsingjui/pi-hooks](https://github.com/hsingjui/pi-hooks) |
| 版本 | 0.0.2 (截至 2026-05) |
| 許可證 | MIT |
| 依賴 | 無需額外依賴（peer dependency: `@earendil-works/pi-coding-agent@^0.84.1`） |

#### 1.2 設計目標

- 將 Claude Code 的 Hook 配置格式轉譯為 Pi 的事件系統
- 支援現有的 command hook 工作流程
- 最小化改動需求，讓Claude Code 使用者快速過渡到Pi

### 2. 安裝步驟

#### 2.1 前提條件

1. 已安裝 Pi CLI（`pi --version`）
2. Pi 版本建議 >= 0.84.1（支援 `terminate: true` 功能）

#### 2.2 安裝命令

```bash
## 方式一：安裝到全域設定（使用者層級）
pi install npm:@hsingjui/pi-hooks

## 方式二：僅在當前專案安裝並寫入設定
pi install -l npm:@hsingjui/pi-hooks

## 方式三：測試版本（不寫入設定）
pi -e npm:@hsingjui/pi-hooks
```

#### 2.3 驗證安裝

```bash
## 列出已安裝套件
pi list

## 重新載入設定
pi /reload
```

### 3. 配置格式

#### 3.1 配置檔案位置

- 全域設定：`~/.pi/agent/settings.json`
- 專案設定：`.pi/settings.json`（需專案信任權限）

#### 3.2 基本配置範例

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'agent finished'"
          }
        ]
      }
    ]
  }
}
```

#### 3.3 支援的事件類型

| 事件名稱 | 對應 Pi 事件 | 說明 |
|----------|-------------|------|
| `SessionStart` | `session_start` | 會話啟動（含 startup/resume/compact） |
| `SessionEnd` | `session_shutdown` | 會話結束 |
| `PreCompact` | `session_before_compact` | 壓縮前 |
| `PostCompact` | `session_compact` | 壓縮後 |
| `PreToolUse` | `tool_call` | 工具執行前 |
| `PostToolUse` | `tool_result` | 工具執行成功後 |
| `PostToolUseFailure` | - | 工具執行失敗 |
| `UserPromptSubmit` | `input` | 使用者提交提示詞 |
| `Stop` | `agent_end` | 代理結束 |

#### 3.4 不支援的事件類型

- `http`
- `prompt`
- `agent`

#### 3.5 完整配置範例

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session started'"
          }
        ]
      },
      {
        "matcher": "resume",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session resumed'"
          }
        ]
      },
      {
        "matcher": "compact",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Context compacted'"
          }
        ]
      }
    ],
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Session ended on shutdown/exit'"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'bash only'"
          }
        ]
      },
      {
        "matcher": "write|edit",
        "hooks": [
          {
            "type": "command",
            "command": "echo 'write or edit'"
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'User submitted prompt'"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo 'Agent finished'"
          }
        ]
      }
    ]
  }
}
```

### 4. 配置要素詳解

#### 4.1 matcher（匹配規則）

**行為說明：**
- `matcher` 是單個正則表達式字串
- 省略 `matcher` 表示匹配所有
- `""` 或 `"*"` 表示匹配所有
- 其他值視為正則表達式
- 若正則無效，則退化为精確字串匹配

**範例：**
```json
{
  "PreToolUse": [
    {
      "matcher": "bash",
      "hooks": [...]
    },
    {
      "matcher": "write|edit",
      "hooks": [...]
    }
  ]
}
```

#### 4.2 事件專屬匹配字段

| 事件類型 | 匹配字段 | 可選值 |
|----------|----------|--------|
| `SessionStart` | `source` | `startup`, `resume`, `compact` |
| `SessionEnd` | `reason` | `other` |
| `PreToolUse` / `PostToolUse` / `PostToolUseFailure` | `tool_name` | `bash`, `read`, `write`, `edit`, `grep`, `find`, `ls`, `mcp__.*` |

#### 4.3 if 條件（工具事件專屬）

**語法：** `ToolName(pattern)`

- `ToolName` 大小寫不敏感
- `pattern` 使用簡單通配符（`*` 表示任意字串）
- 僅支援以下工具事件：
  - `PreToolUse`
  - `PostToolUse`
  - `PostToolUseFailure`

**範例：**
```json
{
  "PreToolUse": [
    {
      "if": "Bash(git push*)",
      "hooks": [
        {
          "type": "command",
          "command": "printf '%s\n' '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"git push is blocked\"}}'"
        }
      ]
    }
  ]
}
```

#### 4.4 輸入字段（Input）

##### SessionStart
```json
{
  "session_id": "session-file-path",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/working/directory",
  "hook_event_name": "SessionStart",
  "source": "startup"
}
```

##### SessionEnd
```json
{
  "session_id": "session-file-path",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/working/directory",
  "hook_event_name": "SessionEnd",
  "reason": "other"
}
```

##### PreToolUse
```json
{
  "session_id": "session-file-path",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/working/directory",
  "hook_event_name": "PreToolUse",
  "tool_name": "bash",
  "tool_input": { "command": "ls -la" },
  "tool_use_id": "toolu_123"
}
```

##### PostToolUse
```json
{
  "session_id": "session-file-path",
  "transcript_path": "/path/to/session.jsonl",
  "cwd": "/current/working/directory",
  "hook_event_name": "PostToolUse",
  "tool_name": "bash",
  "tool_input": { "command": "pwd" },
  "tool_response": {
    "content": [{ "type": "text", "text": "/tmp/project" }],
    "details": {},
    "is_error": false,
    "output": "/tmp/project"
  },
  "tool_use_id": "toolu_123"
}
```

#### 4.5 輸出字段（Output）

##### PreToolUse

| 字段 | 說明 |
|------|------|
| `permissionDecision` | `"allow" \| "deny" \| "ask"` |
| `permissionDecisionReason` | 顯示給使用者/呼叫方的原因 |
| `updatedInput` | 重寫工具輸入 |
| `additionalContext` | 附加上下文 |

**範例：拒絕執行**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Dangerous command blocked"
  }
}
```

**範例：允許並重寫輸入**
```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Reason here",
    "updatedInput": { "field_to_modify": "new value" },
    "additionalContext": "Context message"
  }
}
```

##### Stop

| 字段 | 說明 |
|------|------|
| `decision` | `"block"`（阻止停止並多轉一次） |
| `reason` | 注入為隱藏上下文 |
| `additionalContext` | 附加上下文 |

**範例：**
```json
{
  "decision": "block",
  "reason": "Run a final self-check before stopping",
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Verify there are no missing tests."
  }
}
```

##### PostToolUse

```json
{
  "decision": "block",
  "reason": "Explanation for decision",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "Additional information for Claude"
  }
}
```

### 5. 測試步驟

#### 5.1 基本功能測試

##### 步驟一：安裝並重新載入
```bash
pi install npm:@hsingjui/pi-hooks
pi /reload
```

##### 步驟二：創建測試配置
```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '✓ SessionStart hook triggered'"
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "echo '✓ Stop hook triggered'"
          }
        ]
      }
    ]
  }
}
```

##### 步驟三：測試 SessionStart
1. 開啟新的 Pi 會話
2. 輸入任何訊息
3. 驗證終端機輸出是否包含 `✓ SessionStart hook triggered`

##### 步驟四：測試 Stop
1. 讓代理完成一個任務
2. 驗證終端機輸出是否包含 `✓ Stop hook triggered`

#### 5.2 PreToolUse 測試

##### 配置範例：阻擋 git push
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "if": "Bash(git push*)",
        "hooks": [
          {
            "type": "command",
            "command": "printf '%s\\n' '{\"hookSpecificOutput\":{\"hookEventName\":\"PreToolUse\",\"permissionDecision\":\"deny\",\"permissionDecisionReason\":\"git push is blocked by hook\"}}'"
          }
        ]
      }
    ]
  }
}
```

##### 測試步驟
1. 配置上述設定
2. 輸入指令：`git push origin main`
3. 驗證：
   - 指令被阻擋
   - 顯示 `git push is blocked by hook` 錯誤訊息

#### 5.3 PostToolUse 測試

##### 配置範例：添加上下文
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "printf '%s\\n' '{\"hookSpecificOutput\":{\"hookEventName\":\"PostToolUse\",\"additionalContext\":\"Post-processing note\"}}'"
          }
        ]
      }
    ]
  }
}
```

##### 測試步驟
1. 配置上述設定
2. 讓代理執行任何工具（如 `ls`）
3. 驗證代理回應中是否包含附加上下文訊息

#### 5.4 驗證工具清單

```bash
pi list | grep pi-hooks
```

預期輸出：
```
pi-hooks 0.0.2
```

### 6. 驗證檢查清單

#### 6.1 安裝驗證

- [ ] `pi list` 顯示 `pi-hooks`
- [ ] 無安裝錯誤訊息
- [ ] 可正常執行 `pi /reload`

#### 6.2 基本 Hook 測試

- [ ] `SessionStart` hook 在新會話啟動時觸發
- [ ] `Stop` hook 在代理結束時觸發
- [ ] Hook 輸出正確顯示在終端機

#### 6.3 PreToolUse 測試

- [ ] `matcher` 正確匹配工具名稱
- [ ] `if` 條件正確過濾工具
- [ ] `permissionDecision: "deny"` 成功阻擋工具
- [ ] `permissionDecision: "allow"` 允許工具執行

#### 6.4 輸入輸出測試

- [ ] 輸入字段正確傳遞到 hook
- [ ] 輸出字段正確返回
- [ ] `additionalContext` 正確注入上下文

#### 6.5 整合測試

- [ ] 多條 hook 規則正確執行
- [ ] 全域與專案設定正確合併
- [ ] 無衝突或錯誤訊息

### 7. 故障排除

#### 7.1 Hook 未觸發

**可能原因：**
- 配置語法錯誤
- Pi 版本過舊
- 未執行 `pi /reload`

**解決方案：**
1. 檢查 JSON 語法
2. 確認 Pi 版本 >= 0.84.1
3. 執行 `pi /reload`

#### 7.2 指令執行失敗

**可能原因：**
- Shell 路徑問題（Windows vs WSL）
- 權限問題

**解決方案：**
```json
{
  "type": "command",
  "command": "sh -c 'echo test'"
}
```

#### 7.3 matcher 匹配失敗

**可能原因：**
- 正則表達式無效
- 工具名稱大小寫不一致

**解決方案：**
- 測試正則表達式
- 確認工具名稱（可用 Pi 日誌查看）

### 8. 最佳實踐

#### 8.1 配置組織

```json
{
  "hooks": {
    "SessionStart": [...],
    "PreToolUse": [...],
    "PostToolUse": [...],
    "Stop": [...]
  }
}
```

#### 8.2 安全性

- 在 `PreToolUse` 中阻擋危險指令
- 使用 `if` 條件精確匹配工具
- 避免在 hook 中執行未經授權的指令

#### 8.3 日誌記錄

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          {
            "type": "command",
            "command": "echo \"[$(date)] Tool: $tool_name\" >> ~/.pi/hooks.log"
          }
        ]
      }
    ]
  }
}
```

### 9. 參考資源

- [官方 GitHub 倉庫](https://github.com/hsingjui/pi-hooks)
- [Pi 官方文件](https://pi.dev/docs)
- [Claude Code Hooks 文件](https://code.claude.com/docs/hooks)
- [CHANGELOG](https://github.com/hsingjui/pi-hooks/blob/main/CHANGELOG.md)

### 10. 更新日誌

#### 0.0.2 (2026-05-08)
- 初始版本發布
- 支援基本事件類型
- 完整的 `matcher` 和 `if` 條件系統

*報告生成日期：2026-XX-XX*  
*技術支持：[Pi Agent Community](https://pi.dev/community)*
