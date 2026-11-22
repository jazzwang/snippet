# agent-desktop 技術報告

## 概述

**agent-desktop** 是由 Vercel Labs 開發的桌面自動化框架，讓 AI 代理（AI Agent）能夠透過操作系統的無障礙樹（Accessibility Tree）來「看見」和操控 macOS、Windows 和 Linux 上的桌面應用程式。它不像傳統自動化工具依賴螢幕截圖或像素匹配，而是透過系統提供的無障礙 API 直接讀取 UI 元件資訊，並返回每個可操作元件的唯一定位符（Ref）。

### 核心概念

- **Ref（引用）**：每個 UI 元件的唯一定位標識，用於精確定位和操作
- **Snapshot（快照）**：應用程式 UI 的完整狀態快照，包含所有元件及其 Ref
- **API Only**：不內嵌任何 LLM 模型，所有指令返回 JSON 封包
- **觀察 - 行動 - 驗證循環**：由調用方代理實現的自動化迴圈

## 系統需求與平台支援

| 平台 | 系統需求 | 無障礙 API |
|------|----------|-----------|
| **macOS** | macOS 13 或更高版本（Intel 或 Apple Silicon） | AX API |
| **Windows** | Windows 10 1809 或更高版本，或 Windows Server 2019 或更高版本（x64 或 ARM64） | UI Automation |
| **Linux** | Ubuntu 24.04 或更高版本（x86_64 或 aarch64），需要 AT-SPI 總線 | AT-SPI |

**注意**：所有平台都需要在互動式桌面環境中執行。

## 安裝步驟

### 方法一：使用 NPM（推薦）

```bash
# 使用 npm 全域安裝
npm install -g agent-desktop

# 或使用其他包管理工具
yarn global add agent-desktop
pnpm add -g agent-desktop
bun add -g agent-desktop
```

### 方法二：使用 Homebrew（macOS 和 Linux）

```bash
brew install agent-desktop
```

### 方法三：從 GitHub 下載原生程式碼（免 Node.js 環境）

1. 前往 [GitHub Releases](https://github.com/vercel-labs/agent-desktop/releases)
2. 下載對應平台的原生壓縮檔
3. 將 helper 程式碼放置於執行檔旁邊

### 方法四：從原始碼編譯

```bash
# macOS
cargo build --release

# Windows
cargo build --release -p agent-desktop-windows

# Linux
cargo build --release -p agent-desktop-linux
```

## 測試與驗證

### 步驟一：確認系統狀態

```bash
# 檢查平台狀態、權限和支援的表面
agent-desktop status
```

**預期輸出範例**：
```json
{
  "version": "2.6",
  "ok": true,
  "command": "status",
  "data": {
    "platform": "macos",
    "permissions": {
      "accessibility": "granted",
      "screen_reader": "granted"
    },
    "supported_surfaces": ["finder", "slack", "safari", "chrome", "terminal", "settings"],
    "headless_supported": ["finder", "terminal"],
    "headed_required": ["safari", "chrome"]
  }
}
```

### 步驟二：檢查權限（macOS）

```bash
# 啟動權限設定輔助工具
agent-desktop permissions --guide

# 或使用系統設定手動授權
open x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility
```

**macOS 權限設定步驟**：
1. 開啟「系統設定」→「隱私權與安全性」→「無障礙」
2. 新增 `agent-desktop` 至已信任應用程式清單
3. 重新執行 `agent-desktop status` 確認權限授予成功

### 步驟三：取得版本資訊

```bash
agent-desktop version
```

**預期輸出**：
```
agent-desktop v2.6.0
```

## 快速開始測試

### 範例一：Finder 應用程式測試

```bash
# 步驟 1：取得 Finder 的互動元件快照
agent-desktop snapshot --app Finder -i

# 步驟 2：對特定元件執行點擊動作
agent-desktop click @s8f3k2p9:e8

# 步驟 3：再次取得快照以驗證結果
agent-desktop snapshot --app Finder -i
```

**JSON 輸出範例（Snapshot）**：
```json
{
  "version": "2.6",
  "ok": true,
  "command": "snapshot",
  "data": {
    "app": "Finder",
    "snapshot_id": "s8f3k2p9",
    "ref_count": 59,
    "complete": true,
    "tree": {
      "role": "window",
      "name": "Downloads",
      "children": [
        {
          "role": "treeitem",
          "name": "Documents",
          "ref_id": "@s8f3k2p9:e8",
          "available_actions": ["Click"]
        }
      ]
    }
  }
}
```

### 範例二：程式計算機（gnome-calculator）完整流程

```bash
# 步驟 1：取得淺層骨架（快速導覽）
agent-desktop snapshot --app gnome-calculator --skeleton -i --compact

# 步驟 2：深入特定區域（展開按鈕區域）
agent-desktop snapshot --root @s2txcl95uvubmn:e1 -i --compact

# 步驟 3：執行操作（按 7 按鈕）
agent-desktop click @s2txcl95uvubmn:e11

# 步驟 4：驗證結果（確認顯示為 7）
agent-desktop wait --element @s2txcl95uvubmn:e6 --predicate value --value 7
```

## 錯誤處理與常見問題

### 錯誤類型

| 錯誤代碼 | 說明 | 解決方案 |
|----------|------|----------|
| `INVALID_ARGS` | Ref 格式錯誤或不存在 | 重新取得 snapshot，確認 Ref 格式為 `@snapshot_id:element_id` |
| `STALE_REF` | 元件已失效（UI 已變更） | 重新取得 snapshot 以更新 Ref |
| `AMBIGUOUS_TARGET` | 多個視窗匹配相同 Ref | 使用 `--window-id` 指定目標視窗 |

### PowerShell 使用者注意事項

在 PowerShell 中執行時，所有 Ref 必須使用單引號包裹：

```powershell
# ❌ 錯誤 - PowerShell 會將 @ 視為 splatting 操作符
agent-desktop click @s8f3k2p9:e8

# ✅ 正確
agent-desktop click '@s8f3k2p9:e8'
```

## 進階功能

### MCP（Model Context Protocol）支援

```json
{
  "mcpServers": {
    "agent-desktop": {
      "command": "agent-desktop",
      "args": ["mcp"]
    }
  }
}
```

Global flags（如 `--session`、`--headed`、`--trace`）會套用至所有呼叫，除了 `sandbox exec` 指令（其客體指令可擁有自己的 flags）。

### C 庫（FFI）整合

```python
import ctypes

lib = ctypes.CDLL("./lib/libagent_desktop_ffi.dylib")
lib.ad_adapter_create.restype = ctypes.c_void_p
lib.ad_adapter_destroy.argtypes = [ctypes.c_void_p]

# 初始化（AD_ABI_VERSION_MAJOR 必須與 header 一致）
assert lib.ad_init(7) == 0  # AD_RESULT_OK

adapter = lib.ad_adapter_create()
lib.ad_adapter_destroy(adapter)
```

### 指令清單摘要

| 類別 | 主要指令 |
|------|----------|
| **觀察** | `snapshot`, `find`, `get`, `is`, `screenshot`, `list-surfaces` |
| **Ref 操作** | `click`, `double-click`, `right-click`, `type`, `set-value`, `focus`, `select`, `toggle`, `check` |
| **鍵盤與滑鼠** | `press`, `hover`, `drag`, `mouse-move`, `mouse-click`, `key-down`, `key-up` |
| **視窗管理** | `launch`, `close-app`, `list-apps`, `list-windows`, `focus-window`, `resize-window` |
| **剪貼簿** | `clipboard-get`, `clipboard-set`, `clipboard-clear` |
| **等待** | `wait` |
| **沙箱** | `sandbox` |
| **系統** | `status`, `permissions`, `version`, `batch`, `skills` |

## 安全性與隱私

⚠️ **重要警告**：

- **Snapshot**、剪貼簿讀取、截圖、指令輸出和除錯副產品可能包含私人桌面內容
- 請勿將這些檔案放入公開日誌或上傳至公共儲存庫
- 敏感操作（如輸入密碼）建議使用獨立命令執行，避免 batch JSON 文字出現在程式參數中

## 參考文件

- [官方文件](https://agent-browser.dev/desktop)
- [快速開始指南](https://agent-browser.dev/desktop/quick-start)
- [錯誤處理與回復](https://agent-browser.dev/desktop/errors-and-recovery)
- [技能指南](https://agent-browser.dev/desktop/skills)
- [指令完整說明](https://agent-browser.dev/desktop/commands)

## 授權

Apache-2.0 授權

*技術報告生成日期：2026-11-17 21:17:34*
