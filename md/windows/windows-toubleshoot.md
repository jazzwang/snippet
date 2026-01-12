# Windows Troubleshoot 各種疑難雜症/狀況排除

## 2026-01-11

- 狀況：突然 Windows 的 Start Menu 沒辦法按，要開 Terminal 也顯示 explore.exe 無法開啟
- 參考：
  - https://learn.microsoft.com/en-us/answers/questions/5657217/after-windows-11-update-start-menu-does-not-work-r
- 解法：
  - 按 CTRL+R 然後輸入 powershell
  - 在 PowerShell 底下輸入
    ```powershell
    Windows PowerShell
    Copyright (C) Microsoft Corporation. All rights reserved.

    Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

    PS C:\Users\jazzw> reg delete HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\IrisService /f
    PS C:\Users\jazzw> shutdown -r -t 0
    ```
  - 重新開機以後，就恢復正常了。
- 追查：
  - Explore.exe 在 2025-12-11 有被更動過，看起來是 Security Patch/Update 造成的