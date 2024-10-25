# scoop

## 2024-10-25

- 紀錄一下修改 [`git-extra` scoop manifest file]() 的一些狀況。

- ( 2024-10-25 16:40:58 )
- enable Windows Developer Mode

> Notes
> -----
> If you encounter error to install, please enable developer mode.
run command within cmd.exe with Administrator permission:

```cmd
REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
```