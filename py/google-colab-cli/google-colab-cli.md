# Google Colab CLI

- Git Repo
  - https://github.com/googlecolab/google-colab-cli

## 2026-06-11

- Read from: https://www.linkedin.com/feed/update/urn:li:activity:7470771669742063616
> 一行指令，就能即時取得免費 GPU？！
> Google 推出 Colab CLI，包含四大功能:
> 1. 即時配置GPU
> 2. 遠端執行
> 3. 取回資料
> 4. 互動存取
- 2026-06-05
  - Introducing the Google Colab CLI
  - https://developers.googleblog.com/introducing-the-google-colab-cli/

## 2026-06-12

- Windows 11 實測
```bash
~$ uv tool install google-colab-cli
~$ colab
Traceback (most recent call last):
  File "<frozen runpy>", line 203, in _run_module_as_main
  File "<frozen runpy>", line 88, in _run_code
  File "C:\Users\jazzw\scoop\persist\uv\tools\shims\colab.exe\__main__.py", line 5, in <module>
    from colab_cli.cli import main
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\cli.py", line 26, in <module>
    from colab_cli.commands import session, execution, files, automation, run, utility
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\commands\execution.py", line 28, in <module>
    from colab_cli.console import connect_console
  File "C:\Users\jazzw\scoop\persist\uv\tools\versions\google-colab-cli\Lib\site-packages\colab_cli\console.py", line 20, in <module>
    import termios
ModuleNotFoundError: No module named 'termios'
~$ uv tool install google-colab-cli --with termios
  × No solution found when resolving dependencies:
  ╰─▶ Because termios was not found in the package registry and you require termios, we can conclude that your requirements are unsatisfiable.
~$ uv tool uninstall google-colab-cli
Uninstalled 1 executable: colab.exe
```
- 改用 WSL 測試看看
```bash
~$ wsl
/mnt/c/Users/jazzw$ which uv
/home/jazz/.local/bin/uv
/mnt/c/Users/jazzw$ uv tool install google-colab-cli
/mnt/c/Users/jazzw$ colab

 Usage: colab [OPTIONS] COMMAND [ARGS]...

 Colab CLI

╭─ Options ──────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --client-oauth-config  -c      TEXT          Path to client OAuth config JSON file                                 │
│                                              [default: /home/jazz/.colab-cli-oauth-config.json]                    │
│ --config                       TEXT          Path to session state file (~/.config/colab-cli/sessions.json)        │
│ --logtostderr                                Log all output to stderr                                              │
│ --auth                         [oauth2|adc]  Authentication strategy to use: 'oauth2' (public InstalledAppFlow),   │
│                                              or 'adc' (Application Default Credentials).                           │
│                                              [default: oauth2]                                                     │
│ --install-completion                         Install completion for the current shell.                             │
│ --show-completion                            Show completion for the current shell, to copy it or                  │
│                                              customize the installation.                                           │
│ --help                 -h                    Show this message and exit.                                           │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ console         Connect to raw TTY console                                                                         │
│ download        Download a file from a session                                                                     │
│ drivemount      Mount Google Drive at path                                                                         │
│ edit            Edit a file on a running Colab session                                                             │
│ exec            Execute code in a session                                                                          │
│ help            Show help for a command.                                                                           │
│ install         Install python packages on the VM                                                                  │
│ log             Manage and view session history logs                                                               │
│ ls              List files in a session                                                                            │
│ new             Create a new session                                                                               │
│ pay             Open the Colab signup page to manage compute units                                                 │
│ readme          Print the bundled README.md file                                                                   │
│ repl            Start an interactive REPL                                                                          │
│ restart-kernel  Restart a session's kernel                                                                         │
│ rm              Remove a remote file                                                                               │
│ run             Run a Python script on a fresh Colab VM, then release the VM                                       │
│ sessions        List all active sessions                                                                           │
│ skill           Print the bundled COLAB_SKILL.md file                                                              │
│ status          Show session status                                                                                │
│ stop            Stop a session                                                                                     │
│ update          Check for latest version and print if an update is available                                       │
│ upload          Upload a file to a session                                                                         │
│ url             Print a browser URL that connects to an existing session.                                          │
│ version         Show the version of the Colab CLI                                                                  │
╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
/mnt/c/Users/jazzw$
```