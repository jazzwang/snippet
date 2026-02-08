# OpenCode Labs - Day 1

## 2026-02-08

- 測試環境  #1：Github Codespace (隨時可以清掉的環境)

``bash
@jazzwang ➜ /workspaces/snippet (master) $ curl -fsSL https://opencode.ai/install | bash

Installing opencode version: 1.1.53
■■■■･･････････････････････････････････････････････   8%
■■■■■･････････････････････････････････････････････  10%
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 100%
Successfully added opencode to $PATH in /home/codespace/.bashrc

                                 ▄     
█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
█░░█ █░░█ █▀▀▀ █░░█ █░░░ █░░█ █░░█ █▀▀▀
▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀  ▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀


OpenCode includes free models, to start:

cd <project>  # Open directory
opencode      # Run command

For more information visit https://opencode.ai/docs
```

- 驗證：

```bash
@jazzwang ➜ /workspaces/snippet (master) $ source ~/.bashrc
@jazzwang ➜ /workspaces/snippet (master) $ opencode --version
1.1.53
@jazzwang ➜ /workspaces/snippet (master) $ opencode -h

▄
█▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
█  █ █  █ █▀▀▀ █  █ █    █  █ █  █ █▀▀▀
▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀

Commands:
  opencode completion          generate shell completion script
  opencode acp                 start ACP (Agent Client Protocol) server
  opencode mcp                 manage MCP (Model Context Protocol) servers
  opencode [project]           start opencode tui                                          [default]
  opencode attach <url>        attach to a running opencode server
  opencode run [message..]     run opencode with a message
  opencode debug               debugging and troubleshooting tools
  opencode auth                manage credentials
  opencode agent               manage agents
  opencode upgrade [target]    upgrade opencode to the latest or a specific version
  opencode uninstall           uninstall opencode and remove all related files
  opencode serve               starts a headless opencode server
  opencode web                 start opencode server and open web interface
  opencode models [provider]   list all available models
  opencode stats               show token usage and cost statistics
  opencode export [sessionID]  export session data as JSON
  opencode import <file>       import session data from JSON file or URL
  opencode github              manage GitHub agent
  opencode pr <number>         fetch and checkout a GitHub PR branch, then run opencode
  opencode session             manage sessions

Positionals:
  project  path to start opencode in                                                        [string]

Options:
  -h, --help         show help                                                             [boolean]
  -v, --version      show version number                                                   [boolean]
      --print-logs   print logs to stderr                                                  [boolean]
      --log-level    log level                  [string] [choices: "DEBUG", "INFO", "WARN", "ERROR"]
      --port         port to listen on                                         [number] [default: 0]
      --hostname     hostname to listen on                           [string] [default: "127.0.0.1"]
      --mdns         enable mDNS service discovery (defaults hostname to 0.0.0.0)
                                                                          [boolean] [default: false]
      --mdns-domain  custom domain name for mDNS service (default: opencode.local)
                                                                [string] [default: "opencode.local"]
      --cors         additional domains to allow for CORS                      [array] [default: []]
  -m, --model        model to use in the format of provider/model                           [string]
  -c, --continue     continue the last session                                             [boolean]
  -s, --session      session id to continue                                                 [string]
      --prompt       prompt to use                                                          [string]
      --agent        agent to use                                                           [string]
@jazzwang ➜ /workspaces/snippet (master) $
```
- 設定： 原本 Gemini 生成的步驟要用 `opencode config` 設定要用哪個模型
```bash
@jazzwang ➜ /workspaces/snippet (master) $ cd /tmp/
@jazzwang ➜ /tmp $ mkdir opencode-labs
@jazzwang ➜ /tmp $ cd opencode-labs/
@jazzwang ➜ /tmp/opencode-labs $ git init .
Initialized empty Git repository in /tmp/opencode-labs/.git/
@jazzwang ➜ /tmp/opencode-labs (main) $ opencode config
Error: Failed to change directory to /tmp/opencode-labs/config
```
- 根據 `opencode -h` 顯示的參數，已經沒有看到 `config` 了，所以比較有可能是因為改版的關係，必須改用其他作法來設定。
- 根據 `opencode auth list` 顯示的結果，LLM API KEY 會放在 `~/.local/share/opencode/auth.json`
```bash
@jazzwang ➜ /tmp/opencode-labs (main) $ opencode auth
opencode auth

manage credentials

Commands:
  opencode auth login [url]  log in to a provider
  opencode auth logout       log out from a configured provider
  opencode auth list         list providers                                            [aliases: ls]

Options:
  -h, --help        show help                                                              [boolean]
  -v, --version     show version number                                                    [boolean]
      --print-logs  print logs to stderr                                                   [boolean]
      --log-level   log level                   [string] [choices: "DEBUG", "INFO", "WARN", "ERROR"]
@jazzwang ➜ /tmp/opencode-labs (main) $ opencode auth list

┌  Credentials ~/.local/share/opencode/auth.json
│
└  0 credentials

┌  Environment
│
●  GitHub Copilot GITHUB_TOKEN
│
●  GitHub Models GITHUB_TOKEN
│
└  2 environment variables

@jazzwang ➜ /tmp/opencode-labs (main) $
```
- 在 VS Code 搭配 Github Codespace 的狀態下，可以看到 OpenCode 的 Web UI
```bash
@jazzwang ➜ /tmp/opencode-labs (main) $ opencode web
!  OPENCODE_SERVER_PASSWORD is not set; server is unsecured.

                                   ▄
  █▀▀█ █▀▀█ █▀▀█ █▀▀▄ █▀▀▀ █▀▀█ █▀▀█ █▀▀█
  █  █ █  █ █▀▀▀ █  █ █    █  █ █  █ █▀▀▀
  ▀▀▀▀ █▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀ ▀▀▀▀

  Web interface:      http://127.0.0.1:4096/
```