# ttyd

> Share your terminal over the web

- Git Repo
  - https://github.com/tsl0922/ttyd
- Website
  - https://tsl0922.github.io/ttyd/

## 2026-02-15

- 緣起：想試試看能否用 ttyd 搭配 ngrok 把遠端的 Terminal 分享出來

<table><tr style="background-color:lightyellow;"><td>Q:</td><td>
is it possible to integrate ngrok and any SSH server or web shell server on Windows 11 which provides remote access?
</td></tr></table>

It is absolutely possible. While ngrok is famous for HTTP traffic, it is a versatile "tunneling" tool that can handle **TCP** traffic as well, which is exactly what SSH requires.

On Windows 11, you have two main paths: the robust, "pro" way using the built-in OpenSSH server, or the quick-and-dirty way using a Web Shell.

---

### Option 1: Remote Access via SSH (Recommended)

Windows 11 has a native OpenSSH server that you can activate, allowing you to access your full PowerShell or CMD environment remotely.

#### 1\. Enable OpenSSH Server

1. Open **Settings** > **System** > **Optional Features**.
2. Click **View features**, search for **OpenSSH Server**, and install it.
3. Open PowerShell as Administrator and start the service:
```powershell
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```

#### 2\. Tunnel SSH through ngrok

SSH usually runs on **Port 22**. To expose it, run:

```bash
ngrok tcp 22
```

#### 3\. Connect Remotely

ngrok will provide a URL like `tcp://0.tcp.ngrok.io:12345`. To connect from another machine, use:

```bash
ssh username@0.tcp.ngrok.io -p 12345
```

---

### Option 2: Remote Access via Web Shell

If you prefer using a browser instead of an SSH client, you can use a **Web Shell** (like `ttyd` or `gotty`). This converts your terminal into a web page, which you then forward via ngrok's HTTP tunnel.

1. **Download a Web Shell:** Use a tool like [ttyd](https://github.com/tsl0922/ttyd) for Windows.
2. **Run the Shell:**
```bash
./ttyd.exe -p 8080 cmd.exe
```


3. **Forward via ngrok:**
```bash
ngrok http 8080
```

*Now, hitting the ngrok URL in any browser will give you a live Windows command prompt.*

---

### Comparison: SSH vs. Web Shell

| Feature | SSH (Port 22) | Web Shell (HTTP) |
| --- | --- | --- |
| **Security** | High (Key-based auth / Encrypted) | Medium (Requires manual password setup) |
| **Interface** | Terminal Client (PuTTY, Termius) | Any Web Browser |
| **Ease of Use** | Best for file transfers & dev work | Best for quick access on public PCs |
| **ngrok Protocol** | `tcp` | `http` |

---

### ⚠️ A Note on Security

Exposing your Windows 11 machine to the internet is inherently risky.

* **For SSH:** Ensure your Windows user account has a **strong password**.
* **For Web Shells:** Never run a web shell without the `--credential user:password` flag (or similar), or anyone who finds your ngrok URL will have full control of your PC.

**Would you like me to help you configure the Windows Firewall rules to ensure these connections don't get blocked?**

### 實測

- 安裝 ttyd 跟 ngrok
```bash
~$ scoop install ttyd ngrok
```
- 設定 ngrok - 參考 https://dashboard.ngrok.com/get-started/setup/windows 使用 `ngrok config add-authtoken` 指令來設定金鑰
```powershell
PS C:\Users\wangjaz> scoop install ngrok
Installing 'ngrok' (3.36.1) [64bit] from 'main' bucket
ngrok-v3-3.36.1-windows-amd64.zip (11.2 MB) [====================================================================================================] 100%
Checking hash of ngrok-v3-3.36.1-windows-amd64.zip ... ok.
Extracting ngrok-v3-3.36.1-windows-amd64.zip ... done.
Linking ~\scoop\apps\ngrok\current => ~\scoop\apps\ngrok\3.36.1
Creating shim for 'ngrok'.
'ngrok' (3.36.1) was installed successfully!
Notes
-----
ngrok v2 is no longer supported.
PS C:\Users\wangjaz> ngrok config add-authtoken ${NGROK_AUTH_TOKEN}
Authtoken saved to configuration file: C:\Users\wangjaz\AppData\Local/ngrok/ngrok.yml
```
- 啟動 `ttyd`
```bash
~$ ttyd -p 8080 bash.exe
[2026/02/15 22:37:12:1016] N: ttyd 1.7.7-40e79c7 (libwebsockets 4.3.3-unknown)
[2026/02/15 22:37:12:1198] N: tty configuration:
[2026/02/15 22:37:12:1241] N:   start command: bash.exe
[2026/02/15 22:37:12:1273] N:   close signal: SIGHUP (1)
[2026/02/15 22:37:12:1316] N:   terminal type: xterm-256color
[2026/02/15 22:37:12:1407] N: The --writable option is not set, will start in readonly mode
[2026/02/15 22:37:12:1471] N: lws_create_context: LWS: 4.3.3-unknown, MbedTLS-2.28.5 NET SRV H1 H2 WS ConMon IPV6-off
[2026/02/15 22:37:12:1610] N: elops_init_pt_uv:  Using foreign event loop...
[2026/02/15 22:37:12:1700] N: __lws_lc_tag:  ++ [wsi|0|pipe] (1)
[2026/02/15 22:37:12:1945] N: __lws_lc_tag:  ++ [vh|0|default||8080] (1)
[2026/02/15 22:37:12:2169] N: [vh|0|default||8080]: lws_socket_bind: source ads 0.0.0.0
[2026/02/15 22:37:12:2345] N: __lws_lc_tag:  ++ [wsi|1|listen|default||8080] (2)
[2026/02/15 22:37:12:2489] N:  Listening on port: 8080
```
- 啟動 `ngrok`
```powershell
PS C:\Users\wangjaz> ngrok http 8080
```
- 可能因為有防火牆的關係，所以無法正常工作
```powershell
ngrok                                                                                                                                      (Ctrl+C to quit)

Session Status                reconnecting (failed to send authentication request: tls: failed to verify certificate: x509: certificate signed by unknown a
Version                       3.36.1
Web Interface                 http://127.0.0.1:4040

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
- 退而求其次，先在 Local Windows 11 環境實驗
```bash
~/git/snippet/c/ttyd$ ttyd -p 8080 cmd.exe
[2026/02/15 23:02:57:3174] N: ttyd 1.7.7-40e79c7 (libwebsockets 4.3.3-unknown)
[2026/02/15 23:02:57:3276] N: tty configuration:
[2026/02/15 23:02:57:3324] N:   start command: cmd.exe
[2026/02/15 23:02:57:3324] N:   close signal: SIGHUP (1)
[2026/02/15 23:02:57:3324] N:   terminal type: xterm-256color
[2026/02/15 23:02:57:3324] N: The --writable option is not set, will start in readonly mode
[2026/02/15 23:02:57:3465] N: lws_create_context: LWS: 4.3.3-unknown, MbedTLS-2.28.5 NET SRV H1 H2 WS ConMon IPV6-off
[2026/02/15 23:02:57:3465] N: elops_init_pt_uv:  Using foreign event loop...
[2026/02/15 23:02:57:3623] N: __lws_lc_tag:  ++ [wsi|0|pipe] (1)
[2026/02/15 23:02:57:3623] N: __lws_lc_tag:  ++ [vh|0|default||8080] (1)
[2026/02/15 23:02:57:4417] N: [vh|0|default||8080]: lws_socket_bind: source ads 0.0.0.0
[2026/02/15 23:02:57:4417] N: __lws_lc_tag:  ++ [wsi|1|listen|default||8080] (2)
[2026/02/15 23:02:57:4574] N:  Listening on port: 8080
[2026/02/15 23:03:21:0942] N: __lws_lc_tag:  ++ [wsisrv|0|adopted] (1)
[2026/02/15 23:03:21:1019] N: HTTP / - 127.0.0.1
[2026/02/15 23:03:21:1079] N: __lws_lc_tag:  ++ [wsisrv|1|adopted] (2)
[2026/02/15 23:03:21:5073] N: HTTP /token - 127.0.0.1
[2026/02/15 23:03:21:5567] N: __lws_lc_tag:  ++ [wsisrv|2|adopted] (3)
[2026/02/15 23:03:21:5690] N: WS   /ws - 127.0.0.1, clients: 1
== CreateProcessW failed with error 123: The filename, directory name, or volume label syntax is incorrect.
Segmentation fault
```
- 看樣子 Windows 版本不是很穩定，居然會 `Segmentation fault`