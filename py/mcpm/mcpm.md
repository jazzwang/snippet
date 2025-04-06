# mcpm

> MCP Manager CLI

> Open source, community-driven, forever free.

- Homepage
  - https://mcpm.sh/
- Git Repo
  - https://github.com/pathintegral-institute/mcpm.sh
- PyPI
  - https://pypi.org/project/mcpm/

## 2025-04-06

- 緣起：
  - 本來想說 node.js 有實作 `mcpm` 來管理 MCP Server
    - https://www.npmjs.com/package/@mcpm/cli
    - https://www.npmjs.com/package/@mcpkit/mcpm
  - 那只要 MCP 也有 Python SDK 應該也可以把 `mcpm` 與 `mcpm-aider` 也改用 Python 實作（最好是能類似 `git-extras` 那樣把額外的指令加到 `mcpm` 的 `command` 中）
- 簡單搜尋了一下，發現有很多不一樣的 `mcpm` 實作，當然很多不是跟 `MCP Server` 有關。而這個 `mcpm.sh` 跟 node.js 版的 `mcpm` 指令類似。

### Install 安裝

```bash
jazzw@JazzBook:~/git/snippet/py/mcpm$ uv tool install mcpm
Resolved 35 packages in 2.46s
Prepared 30 packages in 5.01s
Installed 35 packages in 106ms
 + annotated-types==0.7.0                                                                                                                                                                                
 + anyio==4.9.0                                                                                                                                                                                          
 + attrs==25.3.0                                                                                                                                                                                         
 + certifi==2025.1.31                                                                                                                                                                                    
 + charset-normalizer==3.4.1                                                                                                                                                                             
 + click==8.1.8                                                                                                                                                                                          
 + colorama==0.4.6                                                                                                                                                                                       
 + h11==0.14.0                                                                                                                                                                                           
 + httpcore==1.0.7                                                                                                                                                                                       
 + httpx==0.28.1                                                                                                                                                                                         
 + httpx-sse==0.4.0                                                                                                                                                                                      
 + idna==3.10                                                                                                                                                                                            
 + jsonschema==4.23.0                                                                                                                                                                                    
 + jsonschema-specifications==2024.10.1                                                                                                                                                                  
 + markdown-it-py==3.0.0                                                                                                                                                                                 
 + mcp==1.6.0
 + mcpm==1.0.3
 + mdurl==0.1.2
 + pydantic==2.11.2
 + pydantic-core==2.33.1
 + pydantic-settings==2.8.1
 + pygments==2.19.1
 + python-dotenv==1.1.0
 + referencing==0.36.2
 + requests==2.32.3
 + rich==14.0.0
 + rpds-py==0.24.0
 + ruamel-yaml==0.18.10
 + sniffio==1.3.1
 + sse-starlette==2.2.1
 + starlette==0.46.1
 + typing-extensions==4.13.1
 + typing-inspection==0.4.0
 + urllib3==2.3.0
 + uvicorn==0.34.0
Installed 1 executable: mcpm.exe
```
- 因為跟 `@mcpm/cli` 名稱相衝，所以把 js 版的移除。
```bash
jazzw@JazzBook:~/git/snippet/py/mcpm$ which mcpm
/c/Users/jazzw/AppData/Local/pnpm/mcpm
jazzw@JazzBook:~/git/snippet/py/mcpm$ pnpm -g uninstall @mcpm/cli
Packages: -1
-
Progress: resolved 404, reused 404, downloaded 0, added 0, done

C:\Users\jazzw\AppData\Local\pnpm\global\5:
- @mcpm/cli 1.6.2

Done in 1.2s using pnpm v10.6.1
```
- ( 2025-04-06 15:59:20 )
- 登出所有 bash 環境，重新登入後，再檢查一次：
```bash
jazzw@JazzBook:~/git/snippet$ which mcpm
/c/Users/jazzw/.local/bin/mcpm
jazzw@JazzBook:~/git/snippet$ mcpm
╭────────────────────────────────────────────────────────╮
│   ███╗   ███╗ ██████╗██████╗ ███╗   ███╗               │
│   ████╗ ████║██╔════╝██╔══██╗████╗ ████║               │
│   ██╔████╔██║██║     ██████╔╝██╔████╔██║               │
│   ██║╚██╔╝██║██║     ██╔═══╝ ██║╚██╔╝██║               │
│   ██║ ╚═╝ ██║╚██████╗██║     ██║ ╚═╝ ██║               │
│   ╚═╝     ╚═╝ ╚═════╝╚═╝     ╚═╝     ╚═╝               │
│                                                        │
│  v1.0.3                                                │
│  Model Context Protocol Manager                        │
│  Supports Claude Desktop, Windsurf, Cursor, and more   │
╰────────────────────────────────────────────────────────╯
No active client set! Please run 'mcpm client <client-name>' to set one.

Usage: mcpm [OPTIONS] COMMAND [ARGS]...

Description: A tool for managing MCP servers across various clients.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  add        Add an MCP server directly to a client.
  client     Manage the active MCPM client.
  config     Manage MCPM configuration.
  edit       View or edit the active MCPM client's configuration file.
  inspector  Launch the MCPM Inspector UI to examine servers.
  list       List all installed MCP servers.
  remove     Remove an installed MCP server.
  search     Search available MCP servers.
  stash      Temporarily store a server configuration aside.
  pop        Restore a previously stashed server configuration.

Run mcpm CLIENT -h for more information on a command.
jazzw@JazzBook:~/git/snippet$ 
```
- 啟用 Cline 的 MCP Client
```bash
jazzw@JazzBook:~/git/snippet$ mcpm client 
Current active client: None

To change the active client, run:
  mcpm client 5ire
  mcpm client claude-desktop
  mcpm client cline
  mcpm client continue
  mcpm client cursor
  mcpm client goose
  mcpm client roo-code
  mcpm client windsurf

To see all supported clients:
  mcpm client --list
jazzw@JazzBook:~/git/snippet$ mcpm client cline
Success: Active client set to cline
╭──────────────────────────────────────────────────────────────────────────────────────── Active Client Changed ────────────────────────────────────────────────────────────────────────────────────────╮
│ The active client (cline) will be used for all MCP operations.                                                                                                                                        │
│ Commands like 'mcpm list', 'mcpm status', and 'mcpm install' will now operate on cline.                                                                                                               │
╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```
- 列舉支援的 MCP Client
```bash
jazzw@JazzBook:~/git/snippet$ mcpm client --list
                   Supported MCP Clients                    
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ Client Name                     ┃ Installation  ┃ Status ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ 5ire (5ire)                     │ Not installed │        │
│ Claude Desktop (claude-desktop) │ Installed     │        │
│ Cline (cline)                   │ Not installed │ ACTIVE │
│ Continue (continue)             │ Not installed │        │
│ Cursor (cursor)                 │ Not installed │        │
│ Goose (goose)                   │ Not installed │        │
│ Roo Code (roo-code)             │ Not installed │        │
│ Windsurf (windsurf)             │ Not installed │        │
└─────────────────────────────────┴───────────────┴────────┘

To use a non-installed client, you need to install it first.
Windsurf: https://codeium.com/windsurf/download
Cursor: https://cursor.sh/download
Cline: https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev
Continue: https://marketplace.visualstudio.com/items?itemName=Continue.continue
Goose: https://github.com/block/goose/releases/download/stable/download_cli.sh
5ire: https://5ire.app/
Roo Code: https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline
```
- 目前看起來 MCP Server 生態圈還很雜亂，可能還要再觀望一陣子，看哪一個工具會成為公認的標準，公認的 registry (類似 npm, pypi, docker hub 等的 MCP Server 集散地)
```bash
jazzw@JazzBook:~/git/snippet$ mcpm add playwright
Using active client: cline
Client config file not found at: C:\Users\jazzw\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json

Playwright (playwright)
This MCP Server will help you run browser automation and webscraping using Playwright
Author: executeautomation 
Add this server to Cline? [y/n]: y

Using npm installation method
⠋ Saving server metadata...                                                                                                                                                                              
⠋ Configuring playwright...
Client config file not found at: C:\Users\jazzw\AppData\Roaming\Code\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
Successfully added Playwright to Cline!
jazzw@JazzBook:~/git/snippet$ mcpm list
MCP servers installed in Cline:
Configured servers: 1

playwright
  Command: npx
  Arguments:
    0: -y
    1: @executeautomation/playwright-mcp-server
  Environment Variables: None
  --------------------------------------------------
```
- 就像 `@mcpm/cli` 也找不到微軟的 `@playwright/mcp`。
- 看樣子未來應該是會有類似 `mvn`, `pip` 或 `npm` 對應的 publish 機制，來發佈 MCP Server 到不同的 `registry` / `artifactory` (?)