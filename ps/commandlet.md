# Powershell Cmdlet

# Get-ComputerInfo

- 從 https://rocm.docs.amd.com/projects/install-on-windows/en/latest/how-to/install.html 看到這個 Cmdlet

```powershell
Get-ComputerInfo | Format-Table CsSystemType,OSName,OSDisplayVersion
```

- 範例結果：
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
                                                                                                                                                            Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows                                                                                                                                                                                                                               PS C:\Users\jazzw> Get-ComputerInfo | Format-Table CsSystemType,OSName,OSDisplayVersion
CsSystemType OsName                    OSDisplayVersion
------------ ------                    ----------------
x64-based PC Microsoft Windows 11 Home 24H2

PS C:\Users\jazzw>
```
