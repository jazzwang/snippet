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

### 2025-07-16

- 在 Codespace 裡重新啟動 docker instance
```bash
@jazzwang ➜ /workspaces/docker-playwright-vnc (main) $ docker-compose up -d
[+] Running 1/1
 ✔ Container playwright-vnc  Started  
@jazzwang ➜ /workspaces/docker-playwright-vnc (main) $ docker-compose ps
WARN[0000] /workspaces/docker-playwright-vnc/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
NAME             IMAGE                                  COMMAND                  SERVICE          CREATED         STATUS         PORTS
playwright-vnc   docker-playwright-vnc-playwright-vnc   "/usr/bin/supervisor…"   playwright-vnc   5 minutes ago   Up 5 minutes   0.0.0.0:5900->5900/tcp, [::]:5900->5900/tcp, 0.0.0.0:6080->6080/tcp, [::]:6080->6080/tcp, 0.0.0.0:8888->8888/tcp, [::]:8888->8888/tcp
@jazzwang ➜ /workspaces/docker-playwright-vnc (main) $ docker exec -it playwright-vnc /bin/bash
root@fb8b77fa6927:/app# which playwright
/usr/local/bin/playwright
root@fb8b77fa6927:/app# ps ax        
    PID TTY      STAT   TIME COMMAND
      1 ?        Ss     0:00 /usr/bin/python3 /usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf
      6 ?        S      0:01 /usr/bin/python /usr/local/bin/jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser --NotebookApp.token= --NotebookApp.password= --allow-root
      7 ?        S      0:00 /bin/bash /opt/bin/start-vnc.sh
      8 ?        S      0:02 Xvfb :1 -screen 0 1920x1080x24
      9 ?        S      0:00 fluxbox
     10 ?        S      0:04 x11vnc -display :1 -nopw -listen localhost -xkb -ncache 10 -ncache_cr -forever
     11 ?        S      0:00 bash /usr/share/novnc/utils/launch.sh --vnc localhost:5900 --listen 6080
     12 ?        S      0:00 tail -f /dev/null
     24 ?        S      0:00 /usr/bin/python3 /usr/bin/websockify --web /usr/share/novnc/utils/../ 6080 localhost:5900
     40 ?        S      0:00 /usr/bin/python3 /usr/bin/websockify --web /usr/share/novnc/utils/../ 6080 localhost:5900
     41 pts/0    Ss     0:00 /bin/bash
     50 pts/0    R+     0:00 ps ax
root@fb8b77fa6927:/app# export DISPLAY=:1
root@fb8b77fa6927:/app# playwright open https://teams.microsoft.com/l/meetup-join/
```