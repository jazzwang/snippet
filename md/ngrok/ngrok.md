# ngrok

- https://ngrok.com/

## 2026-02-15

- 安裝
```bash
~$ scoop info ngrok


Name        : ngrok
Description : ngrok is your app's front door. ngrok is a globally distributed reverse proxy that secures, protects and accelerates your applications and
              network services, no matter where you run them. ngrok supports delivering HTTP, TLS or TCP-based applications.
Version     : 3.36.1
Source      : main
Website     : https://ngrok.com
License     : Freeware
Updated at  : 2026-02-13 4:31:59 AM
Updated by  : github-actions[bot]
Installed   : 3.36.1
Binaries    : ngrok.exe
Notes       : ngrok v2 is no longer supported.

~$ scoop install ngrok
```
- 設定
  - 參考 https://dashboard.ngrok.com/get-started/setup/windows
```bash
ngrok config add-authtoken <NGROK_AUTH_TOKEN>
```
- 測試
```bash
~$ python3 -m http.server
Serving HTTP on :: port 8000 (http://[::]:8000/) ...
```
```bash
~$ ngrok http 8000
```
```
ngrok                                                                                                                                       (Ctrl+C to quit)

Session Status                online
Account                       Jazz Wang (Plan: Free)
Version                       3.36.1
Region                        Japan (jp)
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://e3fb-36-239-83-115.ngrok-free.app -> http://localhost:8000

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```
