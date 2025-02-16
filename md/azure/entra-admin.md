# Microsoft Azure Entra (Active Directory, AD)

## Microsoft Entra admin center

- Microsoft Entra admin center
  - https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView
- 註冊應用程式 
  - https://aad.portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade
- Reference: 
  - Client ID and client secret inputs
    - https://docs.microfocus.com/doc/CS_MicrosoftOffice365_Content/1.2.0/GetClientInputs
- 緣起：
  - 原本想要用 Thunderbird 備份 Microsoft 365 的信件，但是被擋掉了。先前找一些 command line 工具時，知道只要有 Entra Application client_id 跟 client_secret 就可以做 OAuth 身份認證。當時查到 Thunderbird 的固定 client_id 跟 client_secret。想知道是否 Outlook 也有 client_id 跟 client_secret。