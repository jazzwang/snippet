# Microsoft Graph PowerShell SDK

[TOC]

- PowerShell Gallery
  - https://www.powershellgallery.com/packages/Microsoft.Graph
- Document
  - https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0
- Github Repo
  - https://github.com/microsoftgraph/msgraph-sdk-powershell
- Learning/Reference
  - https://m365corner.com/index.html

## 2024-10-04

### Install 安裝

- 測試環境：

```bash
jazzwang:~/git/snippet/ps/graph-powershell$ uname -a
Darwin ISTWLAPAPPLE1909.local 21.6.0 Darwin Kernel Version 21.6.0: Mon Jun 24 00:56:10 PDT 2024; root:xnu-8020.240.18.709.2~1/RELEASE_X86_64 x86_64
```

- 安裝 Powershell

```bash
jazzwang:~/git/snippet/ps/graph-powershell$ brew install powershell
```

- 在 macOS 使用 Powershell

```bash
jazzwang:~/git/snippet/ps/graph-powershell$ pwsh
PowerShell 7.4.5
PS /Users/jazzwang/git/snippet/ps/graph-powershell>
```

- 安裝 Microsoft Graph PowerShell SDK

```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
```

### Connect-MgGraph -- Authentication 身份認證

- https://learn.microsoft.com/en-us/powershell/microsoftgraph/authentication-commands?view=graph-powershell-1.0

- 最簡單就是下指令 `Connect-MgGraph` ，然後會跳到瀏覽器做 OAuth 認證。

```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Connect-MgGraph
Welcome to Microsoft Graph!

Connected via delegated access using 1xxxxxxx-204b-xxxx-xxxx-xxxxxxxxxxxx
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.
```

### Get-MgEnvironment -- 查有哪些環境

- 用 `Get-MgEnvironment` 可以查有哪些環境可以用（比較像是不同 Region 的 Endpoint）

```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgEnvironment
Name     AzureADEndpoint                   GraphEndpoint                           Type
----     ---------------                   -------------                           ----
China    https://login.chinacloudapi.cn    https://microsoftgraph.chinacloudapi.cn Built-in
Global   https://login.microsoftonline.com https://graph.microsoft.com             Built-in
USGov    https://login.microsoftonline.us  https://graph.microsoft.us              Built-in
Germany  https://login.microsoftonline.de  https://graph.microsoft.de              Built-in
USGovDoD https://login.microsoftonline.us  https://dod-graph.microsoft.us          Built-in
```

### Get-MgContext

- 在 `Get-MgContext` 結果裡可以看到 `Scope`

```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgContext

ClientId               : 1xxxxxxx-204b-xxxx-xxxx-xxxxxxxxxxxx
TenantId               : ffffffff-71b4-ffff-ffff-ffffffffffff
Scopes                 : {Device.ReadWrite.All, DeviceManagementConfiguration.Read.All, DeviceManagementManagedDevices.ReadWrite.All,
                         DeviceManagementServiceConfig.ReadWrite.All…}
AuthType               : Delegated
TokenCredentialType    : InteractiveBrowser
CertificateThumbprint  :
CertificateSubjectName :
SendCertificateChain   : False
Account                : Jazz.Wang@i***************s.com
AppName                : Microsoft Graph Command Line Tools
ContextScope           : CurrentUser
Certificate            :
PSHostVersion          : 7.4.5
ManagedIdentityId      :
ClientSecret           :
Environment            : Global

PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgContext | Select -ExpandProperty Scopes
Device.ReadWrite.All
DeviceManagementConfiguration.Read.All
DeviceManagementManagedDevices.ReadWrite.All
DeviceManagementServiceConfig.ReadWrite.All
Directory.AccessAsUser.All
Domain.ReadWrite.All
Group.ReadWrite.All
GroupMember.ReadWrite.All
OnPremDirectorySynchronization.ReadWrite.All
openid
profile
User.Read
email
```

### Get-MgUserCount

- 用 `Get-MgUserCount` 檢查有多少筆 User 帳號
- 備註：這裡看到有 16,798 筆記錄（當然我相信不完全是使用者的帳號，而是有群組的 Email 甚至有外部的帳號）
```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgUserCount -ConsistencyLevel eventual
16798
```

### Get-MgUser -- List User 列出使用者

- 最開始是參考這篇 https://stackoverflow.com/q/76630385

```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> $logDate = Get-Date -Format "dd-MMM-yyyy"
PS /Users/jazzwang/git/snippet/ps/graph-powershell> $csvFile = "AllAADUsers_$logDate.csv"
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgUser -All -ExpandProperty manager | Select DisplayName, UserPrincipalName, JobTitle, @{Name = 'Manager'; Expression = {$_.Manager.AdditionalProperties.displayName}} | Export-Csv -Path $csvFile
```

- 這個指令嘗試列出整個公司的所有 AAD 帳號，但遇到 Timeout 所以只匯出了 9003 筆

```
jazzwang:~/git/snippet/ps/graph-powershell$ wc AllAADUsers_04-Oct-2024.csv
    9004   38132  686757 AllAADUsers_04-Oct-2024.csv
```

- 那 User 到底有哪些欄位呢？
- 從 https://learn.microsoft.com/en-us/graph/api/resources/user?view=graph-rest-1.0#json-representation 可以查得到。
- 當然比較直覺的做法是用 https://developer.microsoft.com/en-us/graph/graph-explorer 去查看看自己的帳號有哪些資料。
- ( 2024-10-04 16:49:17 )
- 用 `-Filter` 來過濾結果，有些欄位只能用 `Select` 才拿得到
```powershell
PS /Users/jazzwang/git/snippet/ps/graph-powershell> Get-MgUser -ConsistencyLevel eventual -Count userCount -Filter "startsWith(OfficeLocation, 'I******a-Taipei')" | Select id, DisplayName, Mail, OfficeLocation, createdDateTime | Export-Csv -Path "TDC_MS365_ID.csv"
```

## 2025-02-22

### Connect-MgGraph

- https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.authentication/connect-mggraph

根據文件的說明，如果有多個不同的 Microsoft 365 訂閱，可以指定 `TenantId` 來切換。

```powershell
Connect-MgGraph
       [[-Scopes] <String[]>]
       [[-ClientId] <String>]
       [-TenantId <String>]
       [-ContextScope <ContextScope>]
       [-Environment <String>]
       [-UseDeviceCode]
       [-ClientTimeout <Double>]
       [-NoWelcome]
       [-ProgressAction <ActionPreference>]
       [<CommonParameters>]
```

那麼怎麼查詢 TenantId 呢？ <mark>連線到 https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView 就可以看到了。</mark>

- 參考：
  - https://learn.microsoft.com/en-us/sharepoint/find-your-office-365-tenant-id
  - https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant
    - 居然除了 [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) (在 TenMax 有用過) 之外，還有 [Microsoft 365 CLI](https://github.com/pnp/cli-microsoft365)

    ```powershell
    az login
    az account list
    az account tenant list
    ```

    ```powershell
    m365 tenant id get
    ```

- **Find tenant ID with PowerShell**

  To find the tenant ID with Azure PowerShell, use the cmdlet `Get-AzTenant`.

  ```powershell
  Connect-AzAccount
  Get-AzTenant
  ```

  For more information, see the [Get-AzTenant](https://learn.microsoft.com/en-us/powershell/module/az.accounts/get-aztenant) cmdlet reference.