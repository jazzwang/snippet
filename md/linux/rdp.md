# Remote Desktop Protocol (RDP)

- 備註：這是在評估 Windows Virtual Display Driver 時，看到的 Linux RDP 多螢幕支援的討論。
- Source: https://serverfault.com/a/738390

    > Remmina and Chrome RDP only support Full screen mode and don't support multi monitor at the moment. You can install FreeRDP:

    ```
    sudo apt-get install freerdp-x11
    ```

    > and use the following command from the terminal:

    ```
    xfreerdp /multimon /u:username /v:server_address:server_port
    ```
    > where `username` is your username on server, `server_address` is server location (IP address or hostname) and `server_port` is port (leave empty without ":" for default port)

    answered **Nov 23, 2015 at 16:56**
