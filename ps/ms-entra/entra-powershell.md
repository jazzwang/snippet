# Microsoft Entra PowerShell

- 2025-01-30: Microsoft Entra PowerShell module now generally available
  - https://techcommunity.microsoft.com/blog/microsoft-entra-blog/microsoft-entra-powershell-module-now-generally-available/4365718
- Microsoft Entra PowerShell documentation
  - https://learn.microsoft.com/en-us/powershell/entra-powershell/
  - [Overview] What is Microsoft Entra PowerShell?
    - https://learn.microsoft.com/en-us/powershell/entra-powershell/overview
  - [Concept] Microsoft Entra PowerShell best practices
    - https://learn.microsoft.com/en-us/powershell/entra-powershell/entra-powershell-best-practices
  - Install the Microsoft Entra PowerShell module
    - https://learn.microsoft.com/en-us/powershell/entra-powershell/installation

## 2025-02-28

- Install
```powershell
PS C:\Users\jazzw> Install-Module -Name Microsoft.Entra -Repository PSGallery -Scope CurrentUser -Force -AllowClobber
```
- Authentication
  - https://learn.microsoft.com/en-us/powershell/module/microsoft.entra/connect-entra?view=entra-powershell
```powershell
PS C:\Users\jazzw> Connect-Entra
```