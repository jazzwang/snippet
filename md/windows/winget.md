# Windows Package Manager (winget)

## 升級與 Cache 管理

### 升級後舊版本處理

- **winget 預設不會自動清除舊版本**
- 升級行為取決於 manifest 設定：
  - `upgradeBehavior: uninstallPrevious` - 會先卸載舊版本
  - `upgradeBehavior: upgrade` - 舊版本會保留（側邊並存）
- 某些軟體（如 VC++ redistributables）為了相容性，會故意保留舊版本
- 若擔心舊版本佔空間，需要手動執行 `winget uninstall` 來清除

### Cache 管理

#### winget 的 cache 機制

- **已成功的安裝/升級**：installer 檔案在安裝成功後會被移除
- **失敗的安裝**：installer 會保留在 cache 中以便重試
- **主要 cache 位置**：`%LOCALAPPDATA%\Temp\WinGet\`
- **每個安裝器**：下載到 temp 目錄後，通常只會保留短期

#### 清除 cache 的方法

winget 沒有內建的 `clean` 指令，但可以手動清除：

```powershell
# 清除 WinGet 的 cache（僅針對失敗的安裝）
Remove-Item -Recurse "$env:LOCALAPPDATA\Temp\WinGet"

# 重置 WinGet 的 source-index cache（manifest list）
winget source reset --force
winget source update
```

### 相關命令

| 命令 | 說明 |
|------|------|
| `winget upgrade <package>` | 升級套件 |
| `winget uninstall <package>` | 卸載套件 |
| `winget source reset --force` | 重置 source cache |
| `winget source update` | 更新 source list |

---

*記錄時間：2026 年 11 月 03 日 17:47:41*
