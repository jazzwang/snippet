## example from Gemini - https://g.co/gemini/share/2c241a4d6736
import pexpect
import sys
import os

# --- Configuration ---
HOSTNAME = 'your_sftp_host'
USERNAME = 'your_username'
PASSWORD = 'your_password'  # !!! WARNING: Do NOT hardcode passwords in production. Use SSH keys or other secure methods.
REMOTE_PATH = '/path/to/remote/directory/'  # Path on the SFTP server
LOCAL_DOWNLOAD_PATH = './downloaded_files/'  # Local directory to save files
FILE_PATTERN = '*_20250519_*'  # The pattern to match files

# --- Ensure local download directory exists ---
os.makedirs(LOCAL_DOWNLOAD_PATH, exist_ok=True)


def sftp_automation(hostname, username, password, remote_path, local_download_path, file_pattern):
    """
    Automates SFTP file listing and download using pexpect.

    Args:
        hostname (str): The SFTP server hostname.
        username (str): The SFTP username.
        password (str): The SFTP password (use with caution).
        remote_path (str): The remote directory path.
        local_download_path (str): The local directory path to download files to.
        file_pattern (str): The file pattern to match.

    Returns:
        bool: True on success, False on failure.
    """
    sftp_command = f'sftp {username}@{hostname}'
    print(f"Executing: {sftp_command}")

    try:
        # 1. Spawn the sftp process
        child = pexpect.spawn(sftp_command, timeout=30)  # Increased timeout for connection establishment

        # Uncomment the line below to see the raw output from the sftp session for debugging.
        # This can be very helpful to understand what prompts and messages the server is sending.
        # child.logfile_read = sys.stdout.buffer

        # 2. Expect the password prompt
        i = child.expect(['password:', pexpect.TIMEOUT, pexpect.EOF])  # Expect multiple possible outcomes
        if i == 0:
            print("Password prompt found. Sending password.")
            child.sendline(password)
        elif i == 1:
            print("Timeout: Did not receive password prompt within the timeout period.")
            print(f"Output before timeout:\n{child.before.decode()}")  # show what we got before timeout
            return False  # Indicate failure
        elif i == 2:
            print("EOF: Connection closed unexpectedly before password prompt.")
            print(f"Output before EOF:\n{child.before.decode()}")
            return False  # Indicate failure

        # 3. Expect the sftp prompt after login
        j = child.expect(['sftp>', pexpect.TIMEOUT, pexpect.EOF])
        if j == 0:
            print("Successfully logged in to SFTP.")
        elif j == 1:
            print("Timeout: Did not receive sftp prompt after sending password.  Authentication likely failed.")
            print(f"Output before timeout:\n{child.before.decode()}")
            return False
        elif j == 2:
            print("EOF: SFTP session terminated unexpectedly after sending password.")
            print(f"Output before EOF:\n{child.before.decode()}")
            return False

        # 4. Change to the remote directory
        print(f"Changing to remote directory: {remote_path}")
        child.sendline(f'cd {remote_path}')
        cd_index = child.expect(['sftp>', "Couldn't stat remote file:", pexpect.TIMEOUT, pexpect.EOF])
        if cd_index == 0:
            print(f"Changed directory to {remote_path} successfully.")
        elif cd_index == 1:
            print(f"Error: Remote directory not found or inaccessible: {remote_path}")
            print(f"Server response:\n{child.before.decode()}")
            return False
        elif cd_index == 2:
            print("Timeout waiting for cd response")
            print(f"Server response:\n{child.before.decode()}")
            return False
        elif cd_index == 3:
            print("EOF received during cd command")
            print(f"Server response:\n{child.before.decode()}")
            return False

        # 5. List files matching the pattern
        print(f"Listing files matching pattern: {file_pattern}")
        child.sendline(f'ls {file_pattern}')
        ls_index = child.expect(['sftp>', pexpect.TIMEOUT, pexpect.EOF])
        if ls_index == 0:
            ls_output = child.before.decode().strip()  # Get the output and remove extra whitespace
            print("Files found (raw output from ls):")
            print(ls_output)
            #  Optional:  Parse the ls output.  The mget command will download the correct files
            #  even if we don't parse, but parsing lets you know what was found.
            # files_to_download = []
            # for line in ls_output.splitlines():
            #     if line and not line.startswith(" "):  # basic check for non-empty and not a directory listing
            #          parts = line.split()
            #          if len(parts) > 0:
            #             filename = parts[-1]
            #             files_to_download.append(filename)
            # print(f"Files to download: {files_to_download}")

        elif ls_index == 1:
            print("Timeout waiting for ls response")
            print(f"Server response:\n{child.before.decode()}")
            return False
        elif ls_index == 2:
            print("EOF during ls command")
            print(f"Server response:\n{child.before.decode()}")
            return False

        # 6. Set the local download directory
        print(f"Setting local download directory to: {local_download_path}")
        child.sendline(f'lcd {local_download_path}')
        lcd_index = child.expect(['sftp>', 'local: Cannot change directory:', pexpect.TIMEOUT, pexpect.EOF])
        if lcd_index == 0:
            print(f"Local download directory set to: {local_download_path}")
        elif lcd_index == 1:
            print(f"Error: Could not change to local directory: {local_download_path}")
            print(f"Server response:\n{child.before.decode()}")
            return False
        elif lcd_index == 2:
            print("Timeout waiting for lcd response")
            print(f"Server response:\n{child.before.decode()}")
            return False
        elif lcd_index == 3:
            print("EOF during lcd command")
            print(f"Server response:\n{child.before.decode()}")
            return False

        # 7. Download the files using mget
        print(f"Downloading files with mget: {file_pattern}")
        child.sendline(f'mget {file_pattern}')

        # 8. Handle potential prompts during mget (e.g., confirmation prompts)
        mget_index = child.expect(['sftp>', 'Are you sure you want to get', 'Error', pexpect.TIMEOUT, pexpect.EOF])
        while mget_index == 1:
            print("Received confirmation prompt. Sending 'y' to confirm.")
            child.sendline('y')  #  Answer yes to the confirmation prompt
            mget_index = child.expect(['sftp>', 'Are you sure you want to get', 'Error', pexpect.TIMEOUT, pexpect.EOF])

        if mget_index == 0:
            print("mget completed successfully.")
            print(f"Server Response:\n{child.before.decode()}")
        elif mget_index == 2:
            print("Error during mget")
            print(f"Server Response:\n{child.before.decode()}")
            return False
        elif mget_index == 3:
            print("Timeout during mget")
            print(f"Server Response:\n{child.before.decode()}")
            return False
        elif mget_index == 4:
            print("EOF during mget")
            print(f"Server Response:\n{child.before.decode()}")
            return False

        # 9. Exit the SFTP session
        print("Exiting SFTP session.")
        child.sendline('bye')
        child.expect(pexpect.EOF)  # Wait for the process to close
        print("SFTP session closed.")
        return True  # Indicate success

    except pexpect.exceptions.TIMEOUT as e:
        print(f"Pexpect Timeout Error: {e}")
        if 'child' in locals():  # Check if child process was started
            print(f"Output before timeout:\n{child.before.decode()}")
        return False  # Indicate failure
    except pexpect.exceptions.EOF as e:
        print(f"Pexpect EOF Error: {e}")
        if 'child' in locals():
           print(f"Output before EOF:\n{child.before.decode()}")
        return False  # Indicate failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False  # Indicate failure
    finally:
        # 10. Clean up: Close the connection if it's still open
        if 'child' in locals() and child.isalive():
            print("Child process is still alive. Closing it.")
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