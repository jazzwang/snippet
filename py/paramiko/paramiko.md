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

# 2025-06-04

- https://g.co/gemini/share/b0682a75efcc
- Created with 2.5 Flash June 4, 2025 at 09:29 PM
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
can paramiko support listing SFTP file timestamp like `ls -al`?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Yes, Paramiko can support listing SFTP file timestamps in a way that gives you information similar to what `ls -al` provides.

While Paramiko doesn't directly execute the `ls -al` command on the remote server (because SFTP is a protocol, not a shell), it provides methods to retrieve file attributes, including timestamps.

Here's how you do it:

1.  **Use `sftp_client.listdir_attr()`:** This method returns a list of `SFTPAttributes` objects for each file and directory in the specified path.

2.  **Access `st_mtime` and `st_atime`:** Each `SFTPAttributes` object has attributes like `st_mtime` (last modified time) and `st_atime` (last access time). These are Unix timestamps (seconds since the epoch).

3.  **Convert to Human-Readable Format:** You can use Python's `datetime` module to convert these Unix timestamps into a human-readable date and time format.

Here's a code example:

```python
import paramiko
import datetime
import stat # For checking file/directory type

hostname = 'your_sftp_host'
port = 22
username = 'your_username'
password = 'your_password' # Or use key-based authentication

try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password)

    sftp_client = ssh_client.open_sftp()

    remote_path = '.'  # List files in the current directory on the SFTP server

    file_attrs_list = sftp_client.listdir_attr(remote_path)

    print(f"Listing files in {remote_path} on {hostname}:")
    print("-" * 50)
    print(f"{'Permissions':<12} {'Owner':<8} {'Group':<8} {'Size':<10} {'Last Modified':<20} {'Name':<25}")
    print("-" * 50)

    for attr in file_attrs_list:
        # Get file type (similar to 'd' for directory, '-' for file in ls -l)
        if stat.S_ISDIR(attr.st_mode):
            file_type = 'd'
        elif stat.S_ISREG(attr.st_mode):
            file_type = '-'
        else:
            file_type = '?' # Other types like symlinks, etc.

        # Get permissions
        permissions = oct(attr.st_mode)[-4:] # Get the last 4 digits of octal mode

        # Get owner and group (UID/GID are raw numbers, you might need to map them to names if available on the server)
        uid = attr.st_uid
        gid = attr.st_gid

        # Get file size
        size = attr.st_size

        # Get last modified time
        mtime_datetime = datetime.datetime.fromtimestamp(attr.st_mtime)
        modified_time_str = mtime_datetime.strftime('%b %d %H:%M %Y') # e.g., "Jan 01 12:30 2023"

        # Get file name
        file_name = attr.filename

        print(f"{file_type}{permissions:<11} {uid:<8} {gid:<8} {size:<10} {modified_time_str:<20} {file_name:<25}")

except paramiko.AuthenticationException:
    print("Authentication failed. Check your username and password/keys.")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'sftp_client' in locals() and sftp_client:
        sftp_client.close()
    if 'ssh_client' in locals() and ssh_client:
        ssh_client.close()
```

**Explanation:**

* **`paramiko.SSHClient()` and `connect()`:** Establishes the SSH connection.
* **`ssh_client.open_sftp()`:** Opens an SFTP client object over the established SSH connection.
* **`sftp_client.listdir_attr(remote_path)`:** This is the key method. It returns a list of `SFTPAttributes` objects.
* **`SFTPAttributes` Object:** This object is a Python representation of the file's metadata on the SFTP server. It attempts to mirror the `os.stat` object in Python. Key attributes for `ls -al` like information are:
    * `attr.filename`: The name of the file or directory.
    * `attr.st_size`: File size in bytes.
    * `attr.st_uid`: User ID of the owner.
    * `attr.st_gid`: Group ID of the owner.
    * `attr.st_mode`: File mode (permissions and file type). You can use `stat.S_ISDIR()`, `stat.S_ISREG()`, etc., with `st_mode` to determine if it's a directory, regular file, etc.
    * `attr.st_mtime`: Last modification time (Unix timestamp).
    * `attr.st_atime`: Last access time (Unix timestamp).
    * `attr.longname`: (Optional) Some SFTP servers might include a `longname` attribute which is a formatted string similar to `ls -l` output. However, it's not guaranteed to be present or consistent across all servers, so it's generally better to parse the individual `SFTPAttributes` members.
* **`datetime.datetime.fromtimestamp()`:** Converts the Unix timestamp to a `datetime` object.
* **`.strftime()`:** Formats the `datetime` object into a desired string representation.

This approach gives you programmatic access to all the file attributes, allowing you to format the output exactly as you need, similar to `ls -al`.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
can paramiko support listing SFTP file timestamp like `ls -al *_20250603*`?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
You're hitting an important distinction between SFTP and a typical shell command like `ls`.

**SFTP (SSH File Transfer Protocol) does not natively support wildcards in its commands.** When you use `ls -al *_20250603*` in a shell, the shell itself (e.g., Bash) is expanding the wildcard (`*`) into a list of matching filenames *before* passing them to the `ls` command. SFTP clients like Paramiko don't have this built-in shell-like wildcard expansion for directory listings.

**How to achieve this with Paramiko:**

You need to perform the wildcard matching on the client-side (in your Python script) after getting a full listing of the directory. Here's how you can do it, using the `fnmatch` module which is ideal for shell-style wildcards:

```python
import paramiko
import datetime
import stat
import fnmatch # Import for wildcard matching

hostname = 'your_sftp_host'
port = 22
username = 'your_username'
password = 'your_password' # Or use key-based authentication

remote_path = '.'  # Directory to list files from
wildcard_pattern = '*_20250603*' # Your desired wildcard pattern

try:
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=hostname, port=port, username=username, password=password)

    sftp_client = ssh_client.open_sftp()

    print(f"Listing files in {remote_path} on {hostname} matching '{wildcard_pattern}':")
    print("-" * 50)
    print(f"{'Permissions':<12} {'Owner':<8} {'Group':<8} {'Size':<10} {'Last Modified':<20} {'Name':<25}")
    print("-" * 50)

    # Get all file attributes in the directory
    file_attrs_list = sftp_client.listdir_attr(remote_path)

    # Filter the list using fnmatch
    for attr in file_attrs_list:
        if fnmatch.fnmatch(attr.filename, wildcard_pattern):
            # Process and print the matching file's attributes
            if stat.S_ISDIR(attr.st_mode):
                file_type = 'd'
            elif stat.S_ISREG(attr.st_mode):
                file_type = '-'
            else:
                file_type = '?'

            permissions = oct(attr.st_mode)[-4:]
            uid = attr.st_uid
            gid = attr.st_gid
            size = attr.st_size

            mtime_datetime = datetime.datetime.fromtimestamp(attr.st_mtime)
            modified_time_str = mtime_datetime.strftime('%b %d %H:%M %Y')

            file_name = attr.filename

            print(f"{file_type}{permissions:<11} {uid:<8} {gid:<8} {size:<10} {modified_time_str:<20} {file_name:<25}")

except paramiko.AuthenticationException:
    print("Authentication failed. Check your username and password/keys.")
except paramiko.SSHException as e:
    print(f"SSH error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'sftp_client' in locals() and sftp_client:
        sftp_client.close()
    if 'ssh_client' in locals() and ssh_client:
        ssh_client.close()
```

**Key Change:**

1.  **`import fnmatch`**: This module provides functions for working with Unix shell-style wildcards.
2.  **`file_attrs_list = sftp_client.listdir_attr(remote_path)`**: You still retrieve *all* file attributes from the specified `remote_path`.
3.  **`if fnmatch.fnmatch(attr.filename, wildcard_pattern):`**: This is the crucial part. For each `SFTPAttributes` object (`attr`) in the list, we check if its `filename` matches your `wildcard_pattern` using `fnmatch.fnmatch()`. Only if it matches, do we then proceed to print its details.

This approach ensures you get the desired filtered listing with timestamps, even though SFTP itself doesn't handle the wildcard directly.
</td></tr>
<tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are paramiko similiar to winexpect or wexpect?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
While both Paramiko and `winexpect` (or `wexpect`, which is the Windows variant of `pexpect`) are Python libraries used for automation, they operate at very different levels and are designed for distinct purposes.

Here's a breakdown of their similarities and differences:

**Paramiko:**

* **What it is:** A pure-Python implementation of the SSHv2 protocol. This means it *understands* the SSH protocol itself.
* **Primary Use Case:** Directly interacting with remote SSH servers.
    * **SSH Client:** Establishing SSH connections, authenticating users (password, key-based), executing commands (blocking or non-blocking), opening interactive shell sessions, tunneling.
    * **SFTP Client:** Securely transferring files (uploading, downloading, listing directories, changing permissions) using the SFTP protocol (which runs over SSH).
    * **SSH Server:** (Less common for automation) You can even run an SSH server within your Python application.
* **How it works:** Paramiko communicates directly with the SSH daemon on the remote server using the SSH protocol. It doesn't launch an external `ssh` client process. It handles encryption, authentication, and channel management internally.
* **"Expect" functionality:** Paramiko itself doesn't have a built-in "expect" mechanism. If you need to automate interactive shell sessions (where you send a command and then wait for a specific prompt or output before sending the next command), you'd typically implement that logic yourself by reading from the channel's output and looking for patterns. There are also libraries like `paramiko-expect` that build "expect"-like functionality on top of Paramiko.
* **Platform:** Cross-platform (Linux, Windows, macOS).

**`winexpect` / `wexpect` (and `pexpect` for Linux):**

* **What it is:** A Python module for spawning child applications and controlling them automatically by "expecting" patterns in their output. It's in the spirit of Don Libes's "Expect" tool (originally for Tcl).
* **Primary Use Case:** Automating interactive command-line programs, *especially those that prompt for input*. This includes:
    * Automating `ssh` (the command-line client).
    * Automating `ftp` (the command-line client).
    * Automating `telnet`, `passwd`, and other interactive console applications.
    * Automating setup scripts or tests for console applications.
* **How it works:** `pexpect` (and its Windows variants) works by spawning a child process (e.g., `ssh.exe`, `cmd.exe`). It then reads the output of that child process and allows you to define patterns to "expect" (like a "Password:" prompt). When a pattern is matched, you can then "send" input to the child process (like the password). It essentially simulates a human interacting with a command-line interface.
* **"Expect" functionality:** This is its core feature. It's designed specifically for pattern matching and sending responses.
* **Platform:**
    * `pexpect`: Primarily Unix-like systems (Linux, macOS). It relies on pseudo-terminals (PTYs).
    * `winexpect`/`wexpect`: Designed to bring `pexpect`-like functionality to Windows, where PTYs behave differently or aren't available in the same way. They often use pipes or other Windows-specific mechanisms to interact with child processes.

**Key Differences and Similarities:**

| Feature             | Paramiko                                  | `winexpect`/`wexpect` (and `pexpect`)           |
| :------------------ | :---------------------------------------- | :--------------------------------------------- |
| **Level of Abstraction** | Protocol-level (implements SSH/SFTP)      | Process-level (controls external commands)    |
| **Core Function** | Secure SSH/SFTP communication             | Automating interactive console applications   |
| **SSH/SFTP Handling** | Direct, native implementation             | Can automate the *command-line* `ssh` or `ftp` clients |
| **"Expect" Pattern** | Not built-in, but can be added (e.g., `paramiko-expect`) | **Core functionality** |
| **Wildcard Support**| Not native (client-side processing needed) | Inherits from the shell or command it spawns; `fnmatch` needed for path filtering |
| **Error Handling** | Protocol-specific errors, connection issues | Process exit codes, timeouts, unexpected output |
| **Windows Support** | Excellent, pure Python                    | Specifically designed or adapted for Windows   |

**When to use which:**

* **Use Paramiko when:**
    * You need to directly connect to an SSH server and perform actions like executing commands, transferring files, or running an interactive shell *without* relying on the external `ssh` or `sftp` executables.
    * You want fine-grained control over the SSH protocol.
    * You are building a client that interacts with a server using SSH/SFTP.
    * You need to build an SSH *server* in Python.

* **Use `winexpect`/`wexpect` (or `pexpect` on Linux) when:**
    * You need to automate any command-line program that prompts for input (not just SSH).
    * You want to interact with a program as if a human were typing commands and reading output.
    * The program you're automating is not specifically an SSH/SFTP client, or you prefer to use the system's native `ssh` client for some reason (though this is less common for robust automation).

In essence, Paramiko is like a sophisticated SSH *library*, while `pexpect`/`wexpect` is more of a generic *process automation* tool for command-line interfaces. For modern SSH automation, Paramiko is generally preferred because it's more robust, direct, and doesn't rely on spawning external shell processes, which can be less reliable. However, for automating other interactive console applications, `pexpect`/`wexpect` is invaluable.
</td></tr></table>