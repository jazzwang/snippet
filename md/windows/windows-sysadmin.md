# Windows System Administrator

## 2026-09-05 - `ps aux` alternatives

> [!QUESTION]
> windows 可以用什麼指令列出類似 linux `ps aux` 的結果?

在 Windows 環境下，如果想要列出類似 Linux ps aux 的所有處理程序與詳細資訊，主要有以下三種最常用的指令（依據您使用的終端機環境而定）： [1]

### 1. PowerShell 環境（推薦）

如果您使用的是 PowerShell，最強大且資訊最完整的指令是 Get-Process。 [1]

* 基本列出所有程序：
```powershell
Get-Process
```
* 取得類似 ps aux 的超詳細資訊（包含 CPU、記憶體、啟動時間、路徑、使用者等）：
```powershell
Get-Process -IncludeUserName | Select-Object Id, ProcessName, CPU, WorkingSet, StartTime, Path, UserName
```
(注意：-IncludeUserName 參數需要以「系統管理員身分」執行 PowerShell 才能完整顯示所有使用者的程序。)

### 2. 命令提示字元 (CMD) 或 PowerShell 皆通用

如果您使用的是傳統的 CMD，最經典的指令是 tasklist。 [1, 2]

* 基本列出所有程序：
```cmd
tasklist
```
* 顯示詳細資訊（包含使用者名稱、CPU 時間、視窗標題，最接近 ps aux）：
```cmd
tasklist /V
```
* 列出服務對應的程序（類似尋找背景守護行程）：
```cmd
tasklist /SVC
```

### 3. 想查看「完整的執行指令與參數」時（最像 ps aux 結尾的 COMMAND）

在 Linux 中，ps aux 可以看到程式啟動時後面帶了什麼參數。在 Windows 中，上述兩個指令預設看不到完整的參數，這時您可以使用 wmic 或新的 Get-CimInstance： [3]

* 在 CMD 執行：
```cmd
wmic process get caption, commandline, processid
```
* 在 PowerShell 執行（更現代的作法）：
```powershell
Get-CimInstance Win32_Process | Select-Object ProcessId, Name, CommandLine
```

### 💡 快速對照表

| 需求 | Linux 指令 | Windows CMD 指令 | Windows PowerShell 指令 |
|---|---|---|---|
| 列出所有程序 | ps aux | tasklist /V | Get-Process -IncludeUserName |
| 過濾特定程序 | ps aux | grep nginx | tasklist | findstr nginx | Get-Process *nginx* |
| 刪除/結束程序 | kill -9 <PID> | taskkill /F /PID <PID> | Stop-Process -Id <PID> |

您目前是需要在 CMD 還是 PowerShell 環境下操作呢？如果您有特定的過濾需求（例如想找出某個連接埠 (Port) 被哪個程序佔用），我可以為您提供更精準的複合指令！

[1] [https://hackmd.io](https://hackmd.io/@Ernie1999/BJyihk1uxe)
[2] [https://superuser.com](https://superuser.com/questions/18830/is-there-a-command-in-windows-like-ps-aux-in-unix)
[3] [https://blog.csdn.net](https://blog.csdn.net/promaster/article/details/125093806)
