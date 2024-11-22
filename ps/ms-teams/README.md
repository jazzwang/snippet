# README

## 2022-05-23

- Q: How can I get the `Teams` list of a user?
- A:
  - https://docs.microsoft.com/en-us/answers/questions/283171/how-can-i-get-the-list-of-teams-a-user-belongs-to.html
    - using Microsoft Graph PowerShell - https://docs.microsoft.com/en-us/graph/powershell/installation
    ```
    $user = get-MgUser -Filter "DisplayName eq '<User Name>'"
    get-MgUserJoinedTeam -UserId $user.Id
    ```
    - using  https://docs.microsoft.com/en-us/powershell/module/teams/
    ```
    Get-Team -User user@domain.com
    ```

## 2022-05-25

- Install Microsoft Teams cmdlet
- https://www.powershellgallery.com/packages/MicrosoftTeams/

## 2024-11-22

- ( 2024-11-22 16:10:24 )
- 根據 https://learn.microsoft.com/en-us/powershell/microsoftgraph/installation?view=graph-powershell-1.0
- 在 PowerShell 中執行以下指令：
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\jazzw> Install-Module Microsoft.Graph -Scope CurrentUser -Repository PSGallery -Force
```
- 驗證安裝：
```powershell
PS C:\Users\jazzw> Get-InstalledModule

Version    Name                                Repository           Description
-------    ----                                ----------           -----------
2.25.0     Microsoft.Graph.Applications        PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Authentication      PSGallery            Microsoft Graph PowerShell Authentication Module.
2.25.0     Microsoft.Graph.BackupRestore       PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Bookings            PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Calendar            PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.ChangeNotifications PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.CloudCommunications PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Compliance          PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.CrossDeviceExper... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DeviceManagement    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DeviceManagement... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DeviceManagement... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DeviceManagement... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DeviceManagement... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Devices.CloudPrint  PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Devices.Corporat... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Devices.ServiceA... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.DirectoryObjects    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Education           PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Files               PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Groups              PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Identity.Directo... PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Identity.Governance PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Identity.Partner    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Identity.SignIns    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Mail                PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Notes               PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.People              PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.PersonalContacts    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Planner             PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Reports             PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.SchemaExtensions    PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Search              PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Security            PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Sites               PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Teams               PSGallery            Microsoft Graph PowerShell Cmdlets
2.25.0     Microsoft.Graph.Users               PSGallery            Microsoft Graph PowerShell Cmdlets
```
- 身份認證：
```powershell
PS C:\Users\jazzw> Connect-MgGraph
Welcome to Microsoft Graph!

Connected via delegated access using 1xxxxxxx-204b-xxxx-xxxx-xxxxxxxxxxxx
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.
```
- 用 Administrator 身份安裝 Microsoft Teams cmdlet
  - https://www.powershellgallery.com/packages/MicrosoftTeams/
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Windows\system32> Install-Module MicrosoftTeams

Untrusted repository
You are installing the modules from an untrusted repository. If you trust this repository, change its
InstallationPolicy value by running the Set-PSRepository cmdlet. Are you sure you want to install the modules from
'PSGallery'?
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "N"): Y
```
- 登入
```powershell
PS C:\Windows\system32> Connect-MicrosoftTeams

Account                       Environment Tenant                               TenantId
-------                       ----------- ------                               --------
Jazz.Wang@xxxxxxxxxxxxx.com AzureCloud  7xxxxxxa-7xx4-4xx3-9xx4-exxxxxxxxxxf 7xxxxxxa-7xx4-4xx3-9xx4-exxxxxxxxxxf
```
- https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.teams/get-mgteam?view=graph-powershell-1.0
```powershell
PS C:\Users\jazzw> Connect-MgGraph
Welcome to Microsoft Graph!

Connected via delegated access using 14d82eec-204b-4c2f-b7e8-296a70dab67e
Readme: https://aka.ms/graph/sdk/powershell
SDK Docs: https://aka.ms/graph/sdk/powershell/docs
API Docs: https://aka.ms/graph/docs

NOTE: You can use the -NoWelcome parameter to suppress this message.

PS C:\Users\jazzw> Get-MgTeam -All
Get-MgTeam : Missing scope permissions on the request. API requires one of 'Team.ReadBasic.All, TeamSettings.Read.All, TeamSettings.ReadWrite.All'. Scopes
on the request 'Application.ReadWrite.All, Device.ReadWrite.All, DeviceManagementConfiguration.Read.All, DeviceManagementManagedDevices.ReadWrite.All,
DeviceManagementServiceConfig.ReadWrite.All, Directory.AccessAsUser.All, Domain.Read.All, Domain.ReadWrite.All, Group.ReadWrite.All,
GroupMember.ReadWrite.All, OnPremDirectorySynchronization.ReadWrite.All, openid, profile, User.Read, User.Read.All, UserAuthenticationMethod.Read.All,
email'
Status: 403 (Forbidden)
ErrorCode: Forbidden
Date: 2024-11-22T12:18:53
Headers:
Transfer-Encoding             : chunked
Vary                          : Accept-Encoding
Strict-Transport-Security     : max-age=31536000
request-id                    : 4ea46c9c-8999-4360-b6d4-30eb1e57aaff
client-request-id             : 6260cc28-e202-4529-9e48-16dcf8097994
x-ms-ags-diagnostic           : {"ServerInfo":{"DataCenter":"Korea Central","Slice":"E","Ring":"4","ScaleUnit":"001","RoleInstance":"SE1PEPF000098CE"}}
Date                          : Fri, 22 Nov 2024 12:18:52 GMT
At line:1 char:1
+ Get-MgTeam -All
+ ~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: ({ Top = , Skip ... , Headers =  }:<>f__AnonymousType30`9) [Get-MgTeam_List], Exception
    + FullyQualifiedErrorId : Forbidden,Microsoft.Graph.PowerShell.Cmdlets.GetMgTeam_List
```
- 看起來需要一些權限。查了一下，可以透過 Connect-MgGraph 指令來新增 scope
```powershell
PS C:\Users\jazzw> Connect-MgGraph -scope "Team.ReadBasic.All"
Connect-MgGraph : InteractiveBrowserCredential authentication failed: User canceled authentication.
At line:1 char:1
+ Connect-MgGraph -scope "Team.ReadBasic.All"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: (:) [Connect-MgGraph], AuthenticationFailedException
    + FullyQualifiedErrorId : Microsoft.Graph.PowerShell.Authentication.Cmdlets.ConnectMgGraph
```
- 因為還要管理者審核，所以失敗。
- https://learn.microsoft.com/en-us/powershell/module/microsoft.graph.teams/?view=graph-powershell-1.0
- 本來想拿來備份 Teams Chat 的，沒法子～只好找其他方法了。
- ( 2024-11-22 20:59:03 )
- 再仔細看一次文件，重試了一次 Microsoft Teams PowerShell Module
  - `Get-Team` 指令說明：https://github.com/MicrosoftDocs/office-docs-powershell/blob/main/teams/teams-ps/teams/Get-Team.md
  - 指令一覽：https://learn.microsoft.com/en-us/powershell/module/teams/?view=teams-ps
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\jazzw> Connect-MicrosoftTeams

Account                       Environment Tenant                               TenantId                                                                     -------                       ----------- ------                               --------
Jazz.Wang@xxxxxxxxxxxxxxx.com AzureCloud  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

PS C:\Users\jazzw> Get-Team -User jazz.wang@xxxxxxxxxxxxxxx.com

GroupId                              DisplayName        Visibility  Archived  MailNickName       Description
-------                              -----------        ----------  --------  ------------       -----------
d6ce4d32-a436-4052-a98f-9454f15e1213 ...........        Private     False     ............       ...........
cce87c5f-8f84-4203-80cb-6b751c45dbbc ...........        Private     False     ............       ...........
bacf4aa0-6905-48a6-b626-0bc1eebc83e5 ...........        Public      False     ............       ...........
ddba3a61-4ea7-43b0-b80c-b5d5f2dce579 ...........        Public      False     ............       ...........
7942214c-8d35-4239-96f2-9d280c30e08d ...........        Private     False     ............       ...........
71897618-eb98-4fd7-93a6-c7f94af53f09 ...........        Private     False     ............       ...........
88146e33-446e-47aa-a635-d637502190cc ...........        Private     False     ............       ...........
c5471c21-9d93-4e64-a2f6-ff4ea8b46633 ...........        Private     False     ............       ...........
7542be0d-66e2-49a7-a4ca-80578c8f98e1 ...........        Private     False     ............       ...........
08521800-4f73-40f5-a4f8-9e7480538e6c ...........        Private     False     ............       ...........
ab55429d-f565-4583-adc0-cea79eb06226 ...........        Private     False     ............       ...........
40bac83b-36b2-43ff-bd64-d4870b2b7b52 ...........        Public      False     ............       ...........
fa83da2b-585f-4dc5-8277-ef426091e4e4 ...........        Private     False     ............       ...........
442873f6-39e3-4993-9150-4db9d387eee7 ...........        Private     False     ............       ...........
a457bd45-0ee2-4ceb-bdec-fb80ce394bc8 ...........        Private     False     ............       ...........
87125498-17bb-443b-b7cd-a0e0b2b07454 ...........        Public      False     ............       ...........
bffd771f-2b0f-4d6f-891b-44175a21b2aa ...........        Private     False     ............       ...........
10d06eb5-0182-43a1-b941-5386335d3662 ...........        Private     False     ............       ...........
0696b95c-c4b7-429d-a2f4-153160613bb5 ...........        Public      False     ............       ...........
5d94dd88-d27c-4ea3-808c-5543a7c7e27c ...........        Public      False     ............       ...........
1e35f467-a123-4e2e-9434-2853ab770129 ...........        Public      False     ............       ...........
d6166102-5e9f-4a59-9cf9-1be3977ce73d ...........        Public      False     ............       ...........
680f9951-3f75-41e0-b9d0-5b0d048bcb6c ...........        Private     False     ............       ...........
792f8e31-c2b3-44c2-86bf-1e32d6e47e57 ...........        Private     False     ............       ...........
```
- 取得特定 Group 的成員
- `Get-TeamUser` 指令說明：https://learn.microsoft.com/en-us/powershell/module/teams/get-teamuser?view=teams-ps
```powershell
PS C:\Users\jazzw> Get-TeamUser -GroupId 10d06eb5-0182-43a1-b941-5386335d3662

UserId                               User                                           Name                         Role
------                               ----                                           ----                         ----
b059b2db-0011-xxxx-2233-3dfb3d54f538                                                                             owner
85937712-0011-xxxx-2233-af24a7323564                                                                             owner
3caade21-0011-xxxx-2233-c699ee813f01                                                                             owner
e9548442-0011-xxxx-2233-ae39ab54b0d6                                                                             member
e79accc9-0011-xxxx-2233-db4b5e9ff2d9                                                                             member
38f09e39-0011-xxxx-2233-5aa9bb30c12c                                                                             member
27a05529-0011-xxxx-2233-551ca1c24be1                                                                             member
```