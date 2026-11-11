# Pi Agent: 啟動時檢查系統時間

## 官方建議方案

使用 `@falling-ts/pi-start-command` 擴展，透過 `PI_START_COMMAND` 環境變數在每次對話啟動時自動執行檢查系統時間的命令。

## 工作原理

- **掛鉤位置**：`before_agent_start`
- **執行時機**：Pi 會 `await` 全部 handler 之後才組裝並派發模型請求，因此在此處執行命令即滿足「先跑命令、再發請求」
- **觸發條件**：
  1. 配置了命令（`PI_START_COMMAND` 未設或空白時插件完全靜默，零副作用）
  2. `event.messageType === "user"`——只對用戶提交的 prompt 生效

## 安裝

```bash
pi install npm:@falling-ts/pi-start-command
```

## 配置

在 `~/.pi/agent/settings.json` 中添加：

```json
{
  "PI_START_COMMAND": "date '+\"%Y-%m-%d %H:%M:%S\"'",
  "packages": [
    "npm:pi-web-access",
    "npm:@falling-ts/pi-start-command"
  ]
}
```

或者設置環境變數：

```bash
export PI_START_COMMAND="date '+\"%Y-%m-%d %H:%M:%S\"'"
```

## 效果

現在每次當你與 Pi Agent 進行對話時，Pi 會在處理你的請求前先執行：

```bash
date "+%Y-%m-%d %H:%M:%S"
```

並輸出格式化的時間戳（例如：`"2026-03-15 14:30:45"`），這樣 Pi 就能在系統上下文中獲取當前時間。

## 其他可選方案（非官方建議）

- **`@vahor/pi-hooks`**：可以執行 shell 命令，但用於更通用的 life cycle events
- **`pi-tick`**：用於定時任務，不是啟動時檢查

## 參考文檔

- [pi-start-command 官方文檔](https://pi.dev/packages/@falling-ts/pi-start-command?name=hook)
- [GitHub Issue #2013](https://github.com/earendil-works/pi/issues/2013)
