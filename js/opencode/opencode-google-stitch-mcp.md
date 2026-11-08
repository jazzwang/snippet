# OpenCode Google Stitch MCP 設定指南

## 一、Opencode MCP 設定檔位置

OpenCode 的 MCP 設定主要位於以下檔案（依優先順序）：

1. **專案設定**：`./opencode.json` 或 `./opencode.jsonc`（專案根目錄）
2. **全域設定**：`~/.config/opencode/opencode.json`（使用者設定）
3. **自訂設定**：透過 `OPENCODE_CONFIG` 環境變數指定

## 二、Opencode MCP 基本設定格式

所有 MCP 伺服器都在 `"mcp"` 區塊中設定：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "my-mcp-server": {
      "type": "local",  // 或 "remote"
      "command": ["npx", "-y", "@modelcontextprotocol/server-tool"],
      "enabled": true,
      "environment": {
        "API_KEY": "your-api-key"
      }
    }
  }
}
```

## 三、Google Stitch MCP 設定

### 1. 取得 Stitch API Key

```bash
# 開啟設定頁面
https://stitch.withgoogle.com/settings

# 找到 API Keys 區塊，新增一個 API Key
# 複製這個 Key，後續要用到
```

### 2. 設定 opencode.json

在 `~/.config/opencode/opencode.json` 中加入：

```jsonc
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "google-stitch": {
      "type": "remote",
      "url": "https://stitch.googleapis.com/mcp",
      "enabled": true,
      "headers": {
        "X-Goog-Api-Key": "{env:STITCH_API_KEY}"
      }
    }
  }
}
```

### 3. 設定環境變數

在您的終端機環境變數中設定：

```bash
export STITCH_API_KEY="your-api-key-here"
```

### 4. 安裝 Stitch MCP 工具

#### 方式 A：使用初始化腳本（推薦）

```bash
npx @_davideast/stitch-mcp init --client opencode
```

此命令會處理：
- 身份驗證
- 專案選擇
- MCP 客戶端設定

可跳過提示使用參數：

```bash
npx @_davideast/stitch-mcp init --client opencode --transport stdio
```

#### 方式 B：手動安裝 stitch-skills

```bash
# 複製 skills 到 OpenCode 的發現路徑
mkdir -p .opencode/skills
git clone https://github.com/google-labs-code/stitch-skills.git .opencode/skills/stitch-skills
```

### 5. 驗證設定

```bash
# 列出已設定的 MCP 伺服器
opencode mcp list

# 或開啟 OpenCode，在 Agent Manager 中檢查 MCP 伺服器狀態
```

## 四、Opencode MCP 管理指令

```bash
# 互動式新增 MCP
opencode mcp add

# 直接新增遠端 MCP
opencode mcp add context7 --url https://mcp.context7.com/mcp

# 列出已設定的 MCP
opencode mcp list

# OAuth 身份驗證
opencode mcp auth my-server
opencode mcp logout my-server

# 除錯 MCP 連線問題
opencode mcp debug my-server
```

## 五、重要注意事項

- Google Stitch MCP 是 **遠端伺服器 (Remote)**，不位在您的機器上
- 需要 API Key 來進行身份驗證
- 建議使用 `{env:STITCH_API_KEY}` 的方式，不要將 API Key 直接寫入設定檔
- 如果需要使用 stitch-skills，請將技能複製到 `.opencode/skills/` 目錄
- 每個活躍的 MCP 工具 schema 都會注入到 LLM 的系統提示中，添加太多 MCP 伺服器會消耗大量 context window

## 六、相關資源

- [Opencode MCP Servers 官方文件](https://opencode.ai/docs/mcp-servers/)
- [Stitch MCP 官方文件](https://stitchprompt.com/docs/mcp/setup/)
- [stitch-skills GitHub](http://www.github.com/google-labs-code/stitch-skills)
- [stitch-mcp 設定指南](https://davideast.github.io/stitch-mcp/setup/)
