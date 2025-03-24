# SSH Server on Windows 11

- [Reference Microsoft 365 Copilot Link](https://www.microsoft365.com/chat/entity1-d870f6cd-4aa5-4d42-9626-ab690c041429/eyJpZCI6IlZYTmxjbFl4ZkdoMGRIQnpPaTh2YzNWaWMzUnlZWFJsTFdsdWRDNXZabVpwWTJVdVkyOXRMM3hQU1VRNlpXSTFOamM0T0RrdE1XSTBPUzAwWkdaaUxUZ3hOak10TURabVpqbGhOamczTnpkamZHRmxNRFExWTJJeExXTXdOV1l0TkRSak1DMDVNemN6TFRsak9EWmxaakkzTXpObU4zd3lNREkxTFRBekxUSTBWREE0T2pReU9qSXdMamMxTWpjNE5ETmEiLCJzY2VuYXJpbyI6InNoYXJlTGlua1ZpYVJpY2hDb3B5IiwicHJvcGVydGllcyI6eyJwcm9tcHRTb3VyY2UiOiJ1c2VyIiwiY2xpY2tUaW1lc3RhbXAiOiIyMDI1LTAzLTI0VDA4OjQyOjIwLjMxMVoifSwiY2hhdFR5cGUiOiJ3ZWIiLCJ2ZXJzaW9uIjoxLjF9)
<table><tr><td>Q:</td><td>
<!-- add your Prompt bellow-->
could you give me more details on setting up SSH server on Windows 11 if I don't have admin permission?
</td></tr><tr><td>A:</td><td>
<!-- add Chatbot Response bellow-->

Setting up an SSH server on Windows 11 without admin permissions is challenging because installing and configuring the OpenSSH server typically requires administrative rights. However, there are a few workarounds you can try:

1. **Portable SSH Server Applications**:
   - Look for portable versions of SSH server applications that don't require installation. These can be run directly from a USB drive or any folder on your computer. One example is **Bitvise SSH Server**, which offers a portable mode.

2. **Using Windows Subsystem for Linux (WSL)**:
   - If WSL is already installed on your machine, you can use it to run an SSH server. Here's how:
     1. Open your WSL terminal.
     2. Install OpenSSH server in your WSL distribution:
        ```bash
        sudo apt update
        sudo apt install openssh-server
        ```
     3. Start the SSH server:
        ```bash
        sudo service ssh start
        ```
     4. You can now connect to your WSL instance using SSH.

3. **Using PowerShell with Posh-SSH**:
   - While this method is more about creating SSH sessions rather than running an SSH server, it can be useful for remote command execution:
     1. Open PowerShell (no admin rights needed).
     2. Install the `Posh-SSH` module for the current user:
        ```powershell
        Install-Module -Name Posh-SSH -Scope CurrentUser
        ```
     3. Create a new SSH session:
        ```powershell
        $session = New-SSHSession -ComputerName <hostname> -Credential (Get-Credential)
        ```
     4. Run commands on the remote machine:
        ```powershell
        Invoke-SSHCommand -SessionId $session.SessionId -Command "your-command"
        ```

These methods should help you set up and use SSH on Windows 11 without needing admin permissions. Let me know if you need more details on any of these steps!

</td></tr></table>