# Atlassian CLI

- Atlassian Command Line Interface (CLI)
  - https://developer.atlassian.com/cloud/acli/guides/introduction/

## 2025-07-02

- 緣起：
  - 因為先前看到 [Atlassian Rovo Dev agent](https://www.atlassian.com/blog/announcements/rovo-dev-command-line-interface) 但是需要裝 Atlassian CLI。所以實驗一下可以怎麼跟 Jira 或 Confluence 整合。
- 安裝：
  - 文件：
    - Windows - https://developer.atlassian.com/cloud/acli/guides/install-windows/
    - Linux - https://developer.atlassian.com/cloud/acli/guides/install-linux/
    - macOS - https://developer.atlassian.com/cloud/acli/guides/install-macos/
  - 實測：
    - Windows 11 - 習慣裝在家目錄的 `bin` 底下
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.
Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows
PS C:\Users\jazzw> cd .\bin\
PS C:\Users\jazzw\bin> Invoke-WebRequest -Uri  https://acli.atlassian.com/windows/latest/acli_windows_amd64/acli.exe -OutFile acli.exe
PS C:\Users\jazzw\bin>
```
- 設定：
  - 文件：https://developer.atlassian.com/cloud/acli/guides/how-to-get-started/
  - 身份認證： Here are all the ways to authenticate with Atlassian CLI:
    | Authentication type | Command type |
    | --- |  --- |
    | API token | [Jira auth](https://developer.atlassian.com/cloud/acli/reference/commands/jira-auth/), [Rovo Dev](https://rovodevagents-beta.atlassian.net/wiki/external/Yzc2NzI4MTk3YTBhNDdiYjkzZDhhZTc3MjE0ZmE4Y2Q) |
    | API key | [Admin auth](https://developer.atlassian.com/cloud/acli/reference/commands/admin-auth/) |
    | OAuth | [Jira auth](https://developer.atlassian.com/cloud/acli/reference/commands/jira-auth/) |
- 功能：
  - 簡單看了一下可以用的指令，還蠻偏 Jira 管理工具。
    - https://developer.atlassian.com/cloud/acli/reference/commands/
```
Options

    -h, --help   Show help for command

SEE ALSO

    acli admin - Admin commands.
    acli feedback - Submit a request or report a problem.
    acli jira - Jira Cloud commands.
    acli rovodev - Atlassian’s AI coding agent: Rovo Dev (Beta).
```