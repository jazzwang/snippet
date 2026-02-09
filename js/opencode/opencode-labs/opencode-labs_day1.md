# OpenCode Labs - Day 1

## 2026-02-08

- 測試環境  #1：Github Codespace (隨時可以清掉的環境)

```bash
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

## 2026-02-09

- 測試環境  #2： `Git for Windows` on Windows 11
```bash
~/git/snippet/js/opencode$ cd
~$ neofetch
jazzw@JazzBook
OS: Windows 11 Home x86_64
CPU: AMD Ryzen 7 7735HS with Radeon
GPU: AMD Radeon(TM) Graphics
GPU: NVIDIA GeForce RTX 4060 Laptop GPU
Memory: 16802MiB / 31994MiB

~$ curl -fsSL https://opencode.ai/install | bash
```
- 驗證：
```bash
~$ uname -a
MINGW64_NT-10.0-26200 JazzBook 3.6.5-22c95533.x86_64 2025-10-10 12:02 UTC x86_64 Msys
~$ source ~/.bashrc
~$ which opencode
/c/Users/jazzw/.opencode/bin/opencode
```
- 設定 API 金鑰
```bash
~$ opencode auth login

┌  Add credential
│
◆  Select provider

│  Search:
│  ○ OpenCode Zen
│  ○ Anthropic
│  ○ GitHub Copilot
│  ○ OpenAI
│  ● Google
│  ○ OpenRouter
│  ○ Vercel AI Gateway
│  ...
│  ↑/↓ to select • Enter: confirm • Type: to search
```
- 選 Google，然後填入通常設定 `GEMINI_API_KEY` 環境變數的金鑰
```bash
~$ opencode auth login

┌  Add credential
│
◇  Select provider
│  Google
│
◆  Enter your API key
│  _
└
```
- 這樣用 `opencode auth list` 列出所有認證金鑰時，就會顯示不同的 provider
```bash
~$ opencode auth list

┌  Credentials ~\.local\share\opencode\auth.json
│
●  Google api
│
└  1 credentials
```
- 試跑範例 Prompt 並另存 session
- 首先設定使用 Gemini 2.5 Flash Preview 模型 `gemini-2.5-flash-preview-09-2025`
- 貼入：
```
Create a simple Python script named `sys_info.py` that prints the current OS version and the number of CPU cores. Then, execute it to prove it works.
```
- 結果會生成 `sys_info.py`
```python
import platform
import os

def print_sys_info():
    print(f"OS Version: {platform.platform()}")
    print(f"CPU Cores: {os.cpu_count()}")

if __name__ == "__main__":
    print_sys_info()
```
- 使用以下命令來儲存 session 過程到 markdown file
```
/export
```
- 推論過程(session)：
<div style="background-color:lightyellow; padding-space:20px;">

# Python script for OS and CPU info

**Session ID:** ses_3bd0a5281ffeeCdp1D8UC68oQ8
**Created:** 2/9/2026, 11:12:02 PM
**Updated:** 2/9/2026, 11:12:22 PM

---

## User

Create a simple Python script named sys_info.py that prints the current OS version and the number of CPU cores. Then, execute it to prove it works.

---

## Assistant (Build ┬╖ gemini-2.5-flash-preview-09-2025 ┬╖ 16.2s)

_Thinking:_

**Developing the Script**

I'm currently focused on coding the Python script, `sys_info.py`. I plan to use the `platform` module for operating system information and the `os` module to determine the number of CPU cores. The script's core functionality is under active construction.


**Outlining the Execution**

I've sketched out the initial steps for my Python script, `sys_info.py`. First, I'll write and save the script. Then, I plan to execute it using `bash` and the Python interpreter. The script's content will use the `platform` module for OS version and the `os` module for CPU cores.

**Tool: write**

**Input:**
```json
{
  "content": "import platform\nimport os\n\ndef print_sys_info():\n    print(f\"OS Version: {platform.platform()}\")\n    print(f\"CPU Cores: {os.cpu_count()}\")\n\nif __name__ == \"__main__\":\n    print_sys_info()\n",
  "filePath": "C:\\Users\\jazzw\\sys_info.py"
}
```

**Output:**
```
Wrote file successfully.
```

---

## Assistant (Build ┬╖ gemini-2.5-flash-preview-09-2025 ┬╖ 1.9s)

**Tool: bash**

**Input:**
```json
{
  "description": "Execute the Python script to print system info.",
  "command": "python sys_info.py"
}
```

**Output:**
```
OS Version: Windows-11-10.0.26200-SP0
CPU Cores: 16
```

---

## Assistant (Build ┬╖ gemini-2.5-flash-preview-09-2025 ┬╖ 1.5s)

The script `sys_info.py` was created and executed successfully, printing the current OS version and the number of CPU cores.

---

</div>