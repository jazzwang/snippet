# Docker Playwright VNC

- https://github.com/Booza1981/docker-playwright-vnc

## 2025-07-14

- 緣起：
  - 需要「分身」來跑 MS Teams Live Caption 的 JavaScript
  - 希望可以「多重影分身」，所以把腦筋動到 Playwright 跟 Github Codespaces 身上，這樣就可以透過預先儲存的 Browser Profile 跟登入過的 local storage 來自動化開啟 Live Caption 並且儲存下來。甚至也可以寫成 Github Actions 來排程想紀錄的會議。
- 搜尋：
  - 找到 https://github.com/Booza1981/docker-playwright-vnc 似乎可以滿足部份需求，所以實測一下。

## 2025-07-15

- ( 2025-07-15 22:23:02 )
- 實測：
```bash
~/git/snippet$ gh cs create -R Booza1981/docker-playwright-vnc
  ✓ Codespaces usage for this repository is paid for by jazzwang
? Choose Machine Type: 2 cores, 8 GB RAM, 32 GB storage
probable-trout-r47j4v44r3p7x9
~/git/snippet$ gh cs ssh -R Booza1981/docker-playwright-vnc
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.8.0-1027-azure x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

@jazzwang ➜ /workspaces/docker-playwright-vnc (main) $ 
@jazzwang ➜ /workspaces/docker-playwright-vnc (main) $ ./build.sh
Removing previous container...
Building Docker image for Playwright VNC...
[+] Building 0.4s (14/14) FINISHED
Starting container...
137fa366f758e15ba37182a95dea9a3450da20a41f2242df0ff009ba7cb9d54e

Container started successfully!
------------------------------------------------
You can access:
  - VNC: localhost:5900
  - noVNC Web Interface: http://localhost:6080
  - Jupyter Lab: http://localhost:8888

To check container logs:
  docker logs playwright-vnc

To stop and remove the container:
  docker stop playwright-vnc
  docker rm playwright-vnc
------------------------------------------------
```
- 結果：用 VS Code 會比較方便把 port 轉出來
```bash
~/git/snippet$ gh cs code -R Booza1981/docker-playwright-vnc
```
