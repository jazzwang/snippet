# paramiko

## 2025-06-03

- 工作上有需求要批次從 SFTP 下載檔案。原本是寫 Shell Script，但有點煩的地方是要手動輸入密碼（因為該 SFTP Server 不支援 SSH 金鑰交換）。
- 曾經花了一些時間，跟 Gemini 聊可以用 Python 怎麼做到類似 Perl Expect 模組，用來自動輸入密碼。
  - 試過 pexpect - 詳 [pexpect](../pexpect/pexpect.md) 的紀錄。卡在 Windows 支援的問題，也因此看到 `winexpect` 跟 `wexpect` 的關鍵字。
- 用 aider 搭配 ollama Qwen 2.5 Coder 7B 模型，嘗試把 Shell Script 轉成 Python Code，並且邀請改從環境變數讀取 SFTP_HOST, SFTP_USER, SFTP_PASSWD 三個重要的參數。aider 選擇用 `paramiko` 來實作。初步，經過一些手動調整，可以正常列出 SFTP Server 上符合日期字串的檔案（因為同一個目錄下有多個不同日期的檔案）。
- 紀錄一下 `.aider.chat.history.md` 的內容。註：部份敏感字眼已使用其他字串取代。

### aider chat started at 2025-06-03 22:55:28

> C:\Users\jazzw\.local\bin\aider --model ollama/qwen25-7b-it-1m:q4_k_m --no-auto-commits --auto-lint  
> Aider v0.76.1.dev0+gc838f9bf.d20250509  
> Model: ollama/qwen25-7b-it-1m:q4_k_m with whole edit format  
> Git repo: .git with 2 files  
> Repo-map: using 4096 tokens, auto refresh  

#### /add `check-sftp-files.sh`  
> Added `check-sftp-files.sh` to the chat  

#### /read-only  
> Converted `check-sftp-files.sh` to read-only  

#### convert `check-sftp-files.sh` into python code using `wexpect` and `argparse`. store the result in `check-sftp-files.py`  
> check-sftp-files.py  
> Add file to the chat? (Y)es/(N)o/(D)on't ask again [Yes]: n  

To convert `check-sftp-files.sh` into Python using `paramiko` for SFTP operations and `argparse` for command-line argument parsing, we will create a new file named `check-sftp-files.py`. Here is the suggested content:

`check-sftp-files.py`

```python
#!/usr/bin/env python3

import argparse
import paramiko
from datetime import date

def parse_arguments():
    parser = argparse.ArgumentParser(description="Check files on SFTP server.")
    parser.add_argument('partner', help='Partner name for subfolder')
    parser.add_argument('--date', default=date.today().strftime('%Y%m%d'), type=str, help='Specify a specific date in YYYYMMDD format')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()

    SFTP_HOST = "sftp.example.com"
    SFTP_USER = "demo"
    REMOTE_DIR = f"/output/{args.partner}"
    DATE = args.date
    FILE_PATTERN = f"*_{DATE}*"

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(SFTP_HOST, username=SFTP_USER)
        sftp = ssh.open_sftp()
        files = sftp.listdir(f"{REMOTE_DIR}")
        matching_files = [f for f in files if FILE_PATTERN in f]
        print("Matching files:")
        for file in matching_files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()

if __name__ == '__main__':
    main()
```

Please add this file to the chat so I can review and confirm if any changes are needed.

> Tokens: 1.1k sent, 368 received.  
> `check-sftp-files.py`
> Allow edits to file that has not been added to the chat? (Y)es/(N)o [Yes]: y  
> Applied edit to `check-sftp-files.py`  

#### convert `check-sftp-files.sh` into python code using `wexpect` and `argparse`. make sure to use password instead of exchanging ssh key. store the result in `check-sftp-files.py`  

To convert `check-sftp-files.sh` into Python using `paramiko` for SFTP operations and `argparse` for command-line argument parsing, while also using a password instead of exchanging SSH keys, we will create a new file named `check-sftp-files.py`. Here is the suggested content:

`check-sftp-files.py`

```python
#!/usr/bin/env python3

import argparse
import paramiko
from getpass import getpass

def parse_arguments():
    parser = argparse.ArgumentParser(description="Check files on SFTP server.")
    parser.add_argument('partner', help='Partner name for subfolder')
    parser.add_argument('--date', default=date.today().strftime('%Y%m%d'), type=str, help='Specify a specific date in YYYYMMDD format')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()

    SFTP_HOST = "sftp.example.com"
    SFTP_USER = "demo"
    REMOTE_DIR = f"/output/{args.partner}"
    DATE = args.date
    FILE_PATTERN = f"*_{DATE}*"

    password = getpass("Enter your SSH password: ")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(SFTP_HOST, username=SFTP_USER, password=password)
        sftp = ssh.open_sftp()
        files = sftp.listdir(f"{REMOTE_DIR}")
        matching_files = [f for f in files if FILE_PATTERN in f]
        print("Matching files:")
        for file in matching_files:
            print(file)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ssh.close()

if __name__ == '__main__':
    main()
```

Please add this file to the chat so I can review and confirm if any changes are needed.

> Tokens: 1.7k sent, 396 received.  
> Applied edit to `check-sftp-files.py`  
>  
> **Fix any errors below, if possible.**  
>  
> **Running:** `C:\Users\jazzw\AppData\Roaming\uv\tools\aider-chat\Scripts\python.exe -m flake8 --select=E9,F821,F823,F831,F406,F407,F701,F702,F704,F706 --show-source --isolated check-sftp-files.py`  
>  
> check-sftp-files.py:10:43: F821 undefined name 'date'  
> parser.add_argument('--date', default=date.today().strftime('%Y%m%d'), type=str, help='Specify a specific date in YYYYMMDD format')  
> ^  
>  
> **See relevant line below marked with █.**  

- 經過一些迭代測試，確實可以成功地完成 check 跟 scp 的動作。