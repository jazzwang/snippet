# pexpect

- PyPI
  - https://pypi.org/project/pexpect/
- Document
  - 
- Git Repo
  - https://github.com/pexpect/pexpect

## 2025-05-16

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
are there python library similar to expect which can be use to enter sftp password?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
While `pexpect` is a powerful Python library for automating interactive applications, including those that prompt for passwords like `sftp`, it might not be the most straightforward or recommended solution specifically for handling SFTP password entry in all scenarios. Here's why and what alternatives exist:

**Why `pexpect` might be less ideal for SFTP password entry:**

* **SFTP is often handled by dedicated libraries:** Libraries designed for SSH and SFTP often provide more direct and secure ways to handle authentication, including password-based authentication.
* **Complexity:** Using `pexpect` involves spawning an `sftp` subprocess and then interacting with its input and output streams to send the password when prompted. This can be more complex to manage and less robust to changes in the `sftp` client's behavior or prompts.
* **Security considerations:** Passing passwords as plain text within a script, even when using `pexpect`, can raise security concerns if not handled carefully.

**Recommended Python Libraries for SFTP with Password Authentication:**

The most recommended and widely used library for handling SFTP in Python, including password authentication, is **`paramiko`**.

* **`paramiko`:** This is a pure-Python implementation of the SSHv2 protocol, providing both client and server functionality. It supports various authentication methods, including username/password.

    ```python
    import paramiko

    hostname = 'your_sftp_host'
    port = 22  # Default SFTP port
    username = 'your_username'
    password = 'your_password'

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # For initial connection, might want to handle host keys more securely in production
        client.connect(hostname, port, username, password)

        sftp = client.open_sftp()

        # Perform SFTP operations here, e.g., uploading or downloading files
        # sftp.put('local_file.txt', 'remote_file.txt')
        # sftp.get('remote_file.txt', 'local_file.txt')

    except paramiko.AuthenticationException:
        print("Authentication failed.")
    except paramiko.SSHException as e:
        print(f"Could not establish SSH connection: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if sftp:
            sftp.close()
        if client:
            client.close()
    ```

* **`pysftp`:** This library builds on top of `paramiko` and provides a higher-level, more user-friendly interface for common SFTP tasks. It also supports password authentication.

    ```python
    import pysftp

    hostname = 'your_sftp_host'
    username = 'your_username'
    password = 'your_password'

    try:
        with pysftp.Connection(hostname, username=username, password=password) as sftp:
            # Perform SFTP operations
            # sftp.put('local_file.txt', 'remote_file.txt')
            # sftp.get('remote_file.txt', 'local_file.txt')
            print("SFTP operations successful.")
    except pysftp.ConnectionException as e:
        print(f"SFTP connection error: {e}")
    except pysftp.CredentialException:
        print("SFTP authentication failed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    ```

**Alternatives if you specifically want an Expect-like behavior:**

If you have a specific need for interacting with the `sftp` command-line client in an Expect-like way (e.g., for more complex scripting or handling unexpected prompts), you *could* still use `pexpect` or its Windows alternative, `wexpect`.

```python
import pexpect  # Or 'wexpect' on Windows

try:
    child = pexpect.spawn(f'sftp {username}@{hostname}')
    child.expect('password:')
    child.sendline(password)
    child.expect('sftp>')  # Wait for the sftp prompt

    # Now you can send sftp commands
    child.sendline('ls')
    child.expect('sftp>')
    print(child.before.decode())

    child.sendline('bye')
    child.expect(pexpect.EOF)

except pexpect.exceptions.TIMEOUT:
    print("Timeout occurred while connecting or authenticating.")
except pexpect.exceptions.EOF:
    print("Connection closed unexpectedly.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'child' in locals() and child.isalive():
        child.close()
```

**Important Security Note:**

When automating SFTP with passwords, it's generally more secure to avoid hardcoding passwords directly in your scripts. Consider using more secure methods like:

* **SSH Key-based authentication:** This is generally considered more secure than password authentication. `paramiko` and `pysftp` fully support SSH key authentication.
* **Environment variables:** Store the password in an environment variable and retrieve it in your script.
* **Secure credential management:** Use dedicated libraries or tools for securely storing and retrieving sensitive credentials.

In summary, while `pexpect` *can* be used to enter an SFTP password by interacting with the `sftp` command-line client, libraries like `paramiko` and `pysftp` are generally better suited for SFTP automation in Python due to their direct support for the SFTP protocol and more secure handling of authentication. If you specifically need Expect-like interaction, `pexpect` (or `wexpect` on Windows) is an option, but be mindful of security implications.
</td></tr></table>

## 2025-05-20

<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me an example python script using `pexpect` to list SFTP files based on pattern `*_20250519_*` and use 'mget *_20250519*` to download those files?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->
Got it. Here's a Python script using `pexpect` to interact with an `sftp` command-line client, list files matching a pattern, and then `mget` them.

**Important Considerations Before Running:**

1.  **Security:** Hardcoding passwords in scripts is a significant security risk. For production environments, **always prefer SSH key-based authentication** with `sftp` or use a more robust SFTP library like `paramiko` or `pysftp` that handles authentication more securely. This `pexpect` example is for demonstration purposes.
2.  **`sftp` Client Behavior:** The `pexpect` script relies heavily on the specific prompts and output of your `sftp` command-line client. If your `sftp` client behaves differently (e.g., different prompts, different output formats), you'll need to adjust the `child.expect()` patterns accordingly.
3.  **Error Handling:** The error handling in this script is basic. For robust applications, you'll want more comprehensive error checking (e.g., checking return codes of `sftp` commands).
4.  **Local Directory:** Ensure the local directory where files will be downloaded has appropriate write permissions.

<!-- end list -->

```python
import pexpect
import sys
import os

# --- Configuration ---
HOSTNAME = 'your_sftp_host'
USERNAME = 'your_username'
PASSWORD = 'your_password' # !!! WARNING: Do NOT hardcode passwords in production. Use SSH keys.
REMOTE_PATH = '/path/to/remote/directory/' # Path on the SFTP server
LOCAL_DOWNLOAD_PATH = './downloaded_files/' # Local directory to save files
FILE_PATTERN = '*_20250519_*' # The pattern to match files

# --- Ensure local download directory exists ---
os.makedirs(LOCAL_DOWNLOAD_PATH, exist_ok=True)

def sftp_automation(hostname, username, password, remote_path, local_download_path, file_pattern):
    sftp_command = f'sftp {username}@{hostname}'
    print(f"Executing: {sftp_command}")

    try:
        # Spawn the sftp process
        child = pexpect.spawn(sftp_command, timeout=30) # Increased timeout for connection

        # Uncomment to see the raw output for debugging
        # child.logfile_read = sys.stdout.buffer

        # Expect the password prompt
        i = child.expect(['password:', pexpect.TIMEOUT, pexpect.EOF])
        if i == 0:
            print("Password prompt found.")
            child.sendline(password)
        elif i == 1:
            print("Timeout: Did not receive password prompt.")
            print(child.before.decode())
            return False
        elif i == 2:
            print("EOF: Connection closed unexpectedly before password prompt.")
            print(child.before.decode())
            return False

        # Expect the sftp prompt after login
        j = child.expect(['sftp>', pexpect.TIMEOUT, pexpect.EOF])
        if j == 0:
            print("Successfully logged in to SFTP.")
        elif j == 1:
            print("Timeout: Did not get sftp prompt after sending password. Authentication failed?")
            print(child.before.decode())
            return False
        elif j == 2:
            print("EOF: SFTP session terminated unexpectedly after password.")
            print(child.before.decode())
            return False

        # Change to the remote directory
        print(f"Changing to remote directory: {remote_path}")
        child.sendline(f'cd {remote_path}')
        cd_idx = child.expect(['sftp>', 'Couldn\'t stat remote file:', pexpect.TIMEOUT, pexpect.EOF])
        if cd_idx == 0:
            print("Changed directory successfully.")
        elif cd_idx == 1:
            print(f"Error: Remote directory '{remote_path}' not found or accessible.")
            print(child.before.decode())
            return False
        elif cd_idx == 2:
            print("Timeout waiting for 'cd' command response.")
            print(child.before.decode())
            return False
        elif cd_idx == 3:
            print("EOF: SFTP session ended during 'cd' command.")
            print(child.before.decode())
            return False

        # List files matching the pattern
        print(f"Listing files with pattern: {file_pattern}")
        child.sendline(f'ls {file_pattern}')
        ls_idx = child.expect(['sftp>', pexpect.TIMEOUT, pexpect.EOF])
        if ls_idx == 0:
            ls_output = child.before.decode().strip()
            print("LS Output:")
            print(ls_output)
            # Parse the ls output to find actual files (optional, as mget will handle it)
            # files_to_download = [line.split()[-1] for line in ls_output.splitlines() if line.strip() and line.split()[-1] != file_pattern]
            # print(f"Files identified for download: {files_to_download}")
        elif ls_idx == 1:
            print("Timeout waiting for 'ls' command response.")
            print(child.before.decode())
            return False
        elif ls_idx == 2:
            print("EOF: SFTP session ended during 'ls' command.")
            print(child.before.decode())
            return False

        # Set local download path
        print(f"Setting local download path to: {local_download_path}")
        child.sendline(f'lcd {local_download_path}')
        lcd_idx = child.expect(['sftp>', 'local: Cannot change directory:', pexpect.TIMEOUT, pexpect.EOF])
        if lcd_idx == 0:
            print("Local directory set successfully.")
        elif lcd_idx == 1:
            print(f"Error: Local directory '{local_download_path}' not found or accessible.")
            print(child.before.decode())
            return False
        elif lcd_idx == 2:
            print("Timeout waiting for 'lcd' command response.")
            print(child.before.decode())
            return False
        elif lcd_idx == 3:
            print("EOF: SFTP session ended during 'lcd' command.")
            print(child.before.decode())
            return False

        # Use mget to download files
        print(f"Downloading files with 'mget {file_pattern}'")
        child.sendline(f'mget {file_pattern}')

        # Expect specific prompts based on mget behavior
        # 'mget' often asks for confirmation for each file or just shows progress.
        # We'll look for the sftp prompt again to signify completion.
        mget_idx = child.expect(['sftp>', 'Are you sure you want to get', 'Error', pexpect.TIMEOUT, pexpect.EOF])
        while mget_idx == 1: # If it asks for confirmation for each file
            print("Confirming 'y' for file download.")
            child.sendline('y')
            mget_idx = child.expect(['sftp>', 'Are you sure you want to get', 'Error', pexpect.TIMEOUT, pexpect.EOF])

        if mget_idx == 0:
            print("Mget command completed.")
            mget_output = child.before.decode().strip()
            print("MGET Output:")
            print(mget_output)
        elif mget_idx == 2:
            print("Error during mget command.")
            print(child.before.decode())
            return False
        elif mget_idx == 3:
            print("Timeout waiting for 'mget' command completion.")
            print(child.before.decode())
            return False
        elif mget_idx == 4:
            print("EOF: SFTP session ended during 'mget' command.")
            print(child.before.decode())
            return False

        # Exit sftp
        print("Exiting SFTP session.")
        child.sendline('bye')
        child.expect(pexpect.EOF) # Wait for the sftp process to terminate
        print("SFTP session ended.")
        return True

    except pexpect.exceptions.TIMEOUT as e:
        print(f"Pexpect Timeout Error: {e}")
        if 'child' in locals():
            print(child.before.decode())
        return False
    except pexpect.exceptions.EOF as e:
        print(f"Pexpect EOF Error: {e}")
        if 'child' in locals():
            print(child.before.decode())
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False
    finally:
        if 'child' in locals() and child.isalive():
            print("Child process still alive, closing.")
            child.close()
            print(f"Child exit status: {child.exitstatus}")
            print(f"Child signal status: {child.signalstatus}")

# --- Run the automation ---
if __name__ == '__main__':
    print(f"Attempting to download files matching '{FILE_PATTERN}' from {USERNAME}@{HOSTNAME}:{REMOTE_PATH}")
    print(f"To local directory: {LOCAL_DOWNLOAD_PATH}")
    success = sftp_automation(HOSTNAME, USERNAME, PASSWORD, REMOTE_PATH, LOCAL_DOWNLOAD_PATH, FILE_PATTERN)
    if success:
        print("\nSFTP automation completed successfully.")
    else:
        print("\nSFTP automation failed.")
```

**How to Use:**

1.  **Install `pexpect`:**
    ```bash
    pip install pexpect
    ```
2.  **Fill in Configuration:**
      * `HOSTNAME`: The hostname or IP address of your SFTP server.
      * `USERNAME`: Your SFTP username.
      * `PASSWORD`: Your SFTP password. **Seriously, consider SSH keys\!**
      * `REMOTE_PATH`: The directory on the SFTP server where the files are located. Make sure to include the trailing slash.
      * `LOCAL_DOWNLOAD_PATH`: The local directory where you want to save the downloaded files. Make sure to include the trailing slash.
      * `FILE_PATTERN`: The pattern for the files you want to download (e.g., `*_20250519_*`).
3.  **Run the script:**
    ```bash
    python your_script_name.py
    ```

**Explanation of `pexpect` Usage:**

  * `pexpect.spawn(command)`: Starts the `sftp` command as a child process.
  * `child.expect(pattern)`: Waits until the child process's output matches one of the provided patterns. It returns the index of the matched pattern.
      * `'password:'`: Looks for the password prompt.
      * `'sftp>'`: Looks for the SFTP command prompt, indicating a successful login or command completion.
      * `pexpect.TIMEOUT`: A special pattern that matches if the `expect` call times out.
      * `pexpect.EOF`: A special pattern that matches if the child process closes its output stream (i.e., terminates).
  * `child.sendline(string)`: Sends a string followed by a newline character to the child process (simulating typing and pressing Enter).
  * `child.before.decode()`: Returns the output received *before* the matched pattern. `.decode()` converts bytes to string.
  * `child.close()`: Closes the child process.
  * `child.isalive()`: Checks if the child process is still running.
  * `child.exitstatus` / `child.signalstatus`: Provide information about how the child process terminated.

This script provides a functional example for your request, but remember the strong recommendation to use libraries like `paramiko` for more robust and secure SFTP interactions in Python.
</td></tr></table>

## 2025-06-01

- 測試 Qwen 2.5 Coder 從 Bash Script 轉成 pexpect Python code 的時候，錯誤訊息居然說 `module 'pexpect' has no attribute 'spawn'`
```
jazzw@JazzBook:/tmp$ ./check-sftp-files.py --date 20250530 test
Traceback (most recent call last):
  File "C:\Users\jazzw\AppData\Local\Temp\check-sftp-files.py", line 44, in <module>
    main()
  File "C:\Users\jazzw\AppData\Local\Temp\check-sftp-files.py", line 35, in main
    child = pexpect.spawn(f"sftp {SFTP_USER}@{SFTP_HOST}")
            ^^^^^^^^^^^^^
AttributeError: module 'pexpect' has no attribute 'spawn'
```
- 看樣子得回過頭查一下最新的實作文件或範例。

## 2025-06-02

- 查了一下文件，看到這一段：
  - https://pexpect.readthedocs.io/en/stable/install.html#requirements
  > As of version 4.0, Pexpect can be used on Windows and POSIX systems. However, [`pexpect.spawn`](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#pexpect.spawn "pexpect.spawn") and [`pexpect.run()`](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#pexpect.run "pexpect.run") are only available on POSIX, where the [`pty`](https://docs.python.org/3/library/pty.html#module-pty "(in Python v3.8)") module is present in the standard library. See [Pexpect on Windows](https://pexpect.readthedocs.io/en/stable/overview.html#windows) for more information.
- 把程式碼改成用 `popen_spawn` 還是會錯
```python
- child = pexpect.spawn(f"sftp {SFTP_USER}@{SFTP_HOST}")
+ child = pexpect.popen_spawn.PopenSpawn(f"sftp {SFTP_USER}@{SFTP_HOST}")
```
- 錯誤訊息：
```bash
/tmp$ ./check-sftp-files.py --date 20250530 test
Traceback (most recent call last):
  File "C:\Users\jazzw\AppData\Local\Temp\check-sftp-files.py", line 46, in <module>
    main()
  File "C:\Users\jazzw\AppData\Local\Temp\check-sftp-files.py", line 38, in main
    child.expect('Password:')
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pexpect\spawnbase.py", line 354, in expect
    return self.expect_list(compiled_pattern_list,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pexpect\spawnbase.py", line 383, in expect_list
    return exp.expect_loop(timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pexpect\expect.py", line 179, in expect_loop
    return self.eof(e)
           ^^^^^^^^^^^
  File "C:\Users\jazzw\scoop\apps\python\current\Lib\site-packages\pexpect\expect.py", line 122, in eof
    raise exc
pexpect.exceptions.EOF: End Of File (EOF).
<pexpect.popen_spawn.PopenSpawn object at 0x0000016E76AE6ED0>
searcher: searcher_re:
    0: re.compile(b'Password:')
```

- 根據  [Pexpect on Windows](https://pexpect.readthedocs.io/en/stable/overview.html#windows) 的解釋，`PopenSpawn` 不是拿來取代 `spawn`，在 Windows 平台上的行為可能會不同。

> **Pexpect on Windows**
> 
> New in version 4.0: Windows support
> 
> Pexpect can be used on Windows to wait for a pattern to be produced by a child process, using [`pexpect.popen_spawn.PopenSpawn`](https://pexpect.readthedocs.io/en/stable/api/popen_spawn.html#pexpect.popen_spawn.PopenSpawn "pexpect.popen_spawn.PopenSpawn"), or a file descriptor, using [`pexpect.fdpexpect.fdspawn`](https://pexpect.readthedocs.io/en/stable/api/fdpexpect.html#pexpect.fdpexpect.fdspawn "pexpect.fdpexpect.fdspawn").
> 
> <mark>[`pexpect.spawn`](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#pexpect.spawn "pexpect.spawn") and [`pexpect.run()`](https://pexpect.readthedocs.io/en/stable/api/pexpect.html#pexpect.run "pexpect.run") ***are *not* available*** on Windows</mark>, as they rely on Unix pseudoterminals (ptys). Cross platform code must not use these.
> 
> <mark>`PopenSpawn` is not a direct replacement for `spawn`.</mark> Many programs only offer interactive behaviour if they detect that they are running in a terminal. When run by `PopenSpawn`, they may behave differently.
>
> **See also**
>
> [winpexpect](https://pypi.python.org/pypi/winpexpect) and [wexpect](https://gist.github.com/anthonyeden/8488763)
> 
> Two unmaintained pexpect-like modules for Windows, which work with a hidden console.
- ( 2025-06-02 12:55:48 )
- 在 WSL 裡面測試，遇到另一個狀況
```
/tmp$ ./check-sftp-files.py --date 20250530 test
Traceback (most recent call last):
  File "/tmp/check-sftp-files.py", line 44, in <module>
    main()
  File "/tmp/check-sftp-files.py", line 36, in main
    child.expect('Password:')
  File "/home/jazz/.local/lib/python3.12/site-packages/pexpect/spawnbase.py", line 354, in expect
    return self.expect_list(compiled_pattern_list,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazz/.local/lib/python3.12/site-packages/pexpect/spawnbase.py", line 383, in expect_list
    return exp.expect_loop(timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/jazz/.local/lib/python3.12/site-packages/pexpect/expect.py", line 181, in expect_loop
    return self.timeout(e)
           ^^^^^^^^^^^^^^^
  File "/home/jazz/.local/lib/python3.12/site-packages/pexpect/expect.py", line 144, in timeout
    raise exc
pexpect.exceptions.TIMEOUT: Timeout exceeded.
<pexpect.pty_spawn.spawn object at 0x7bc11c3fa360>
command: /usr/bin/sftp
args: ['/usr/bin/sftp', 'guest@sftp.example.com']
buffer (last 100 chars): b'not known by any other names.\r\nAre you sure you want to continue connecting (yes/no/[fingerprint])? '
before (last 100 chars): b'not known by any other names.\r\nAre you sure you want to continue connecting (yes/no/[fingerprint])? '
after: <class 'pexpect.exceptions.TIMEOUT'>
match: None
match_index: None
exitstatus: None
flag_eof: False
pid: 905
child_fd: 5
closed: False
timeout: 30
delimiter: <class 'pexpect.exceptions.EOF'>
logfile: None
logfile_read: None
logfile_send: None
maxread: 2000
ignorecase: False
searchwindowsize: None
delaybeforesend: 0.05
delayafterclose: 0.1
delayafterterminate: 0.1
searcher: searcher_re:
    0: re.compile(b'Password:')
```

- 手動用 sftp 連線一次，讓 SFTP Server 被加進 known_host 以後，還是遇到一樣的錯誤! :(

```bash
/cdk/edp$ sftp guest@sftp.example.com
The authenticity of host 'sftp.example.com' can't be established.
ECDSA key fingerprint is SHA256:7Rpp024zhMBpYNAnw5GGhnEEeGGH4gsDeZzcKVdMyZI.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Failed to add the host to the list of known hosts (/home/jazz/.ssh/known_hosts).
guest@sftp.example.com's password:
Connected to sftp.example.com.
sftp> quit
```

- 看樣子 `pexpect.spawn` 的行為不是那麼直觀！！