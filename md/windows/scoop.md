# scoop

## 2024-10-25

- 紀錄一下修改 [`git-extra` scoop manifest file]() 的一些狀況。

- ( 2024-10-25 16:40:58 )
- enable Windows Developer Mode
  - [官方文件] https://learn.microsoft.com/en-us/windows/apps/get-started/enable-your-device-for-development 只有寫到 GUI 操作。
  - 指令參考：https://stackoverflow.com/a/44160849
  > In the cmd.exe that is running as admin, run the following command:
  >
  >    REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
- 查詢 Developer Mode 狀態
  - https://learn.microsoft.com/en-us/powershell/module/windowsdeveloperlicense/get-windowsdeveloperlicense?view=windowsserver2022-ps
