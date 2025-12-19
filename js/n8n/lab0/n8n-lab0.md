# Lab 0 - Run n8n on a Linux server using Docker Compose

- https://docs.n8n.io/hosting/installation/server-setups/docker-compose/#3-dns-setup

## 2025-12-17

- test on Github CodeSpace
- Create an `.env` file
```bash
@jazzwang ➜ .../snippet/js/n8n/lab0 (master) $ cat > .env << EOF
> # DOMAIN_NAME and SUBDOMAIN together determine where n8n will be reachable from
> # The top level domain to serve from
> DOMAIN_NAME=example.com
>
> # The subdomain to serve from
> SUBDOMAIN=n8n
>
> # The above example serve n8n at: https://n8n.example.com
>
> # Optional timezone to set which gets used by Cron and other scheduling nodes
> # New York is the default value if not set
> GENERIC_TIMEZONE=Europe/Berlin
>
> # The email address to use for the TLS/SSL certificate creation
> SSL_EMAIL=user@example.com
> EOF
```
- Create an `docker-compose.yml` file

## 2025-12-19

- 在 Windows 11 + WSL + Docker 環境中實測了 [lab0](./lab0/n8n-lab0.md)
- 很煩的地方是一定要走過註冊新用戶的步驟
- 查了一下討論，以前可以用 `N8N_USER_MANAGEMENT_DISABLED` 環境變數關閉，但現在已經沒辦法跳過這一步
  - https://community.n8n.io/t/how-can-i-skip-the-login-register-new-customer-step-in-my-self-hosted-n8n-instance/224139
- 當然也因此留意到範例中，n8n 的資料存在 docker volumn 裡。這樣不太好留下預設的 SQLite 資料庫，所以小改了一下 docker-compose.yml
```diff
diff --git a/js/n8n/lab0/docker-compose.yml b/js/n8n/lab0/docker-compose.yml
index e831973..6c8985a 100644
--- a/js/n8n/lab0/docker-compose.yml
+++ b/js/n8n/lab0/docker-compose.yml
@@ -17,7 +17,7 @@ services:
       - "80:80"
       - "443:443"
     volumes:
-      - traefik_data:/letsencrypt
+      - ./traefik_data:/letsencrypt
       - /var/run/docker.sock:/var/run/docker.sock:ro
 
   n8n:
@@ -51,9 +51,5 @@ services:
       - GENERIC_TIMEZONE=${GENERIC_TIMEZONE}
       - TZ=${GENERIC_TIMEZONE}
     volumes:
-      - n8n_data:/home/node/.n8n
-      - ./local-files:/files
-
-volumes:
-  n8n_data:
-  traefik_data:
+      - ./n8n_data:/home/node/.n8n
+      - ./local-files:/files
```
- 這樣應該可以把一些狀態留下來，供下一次重啟 docker-compose 時使用。
- 實測步驟：
```bash
~$ cd git/snippet/js/n8n/lab0/
~/git/snippet/js/n8n/lab0$ uname -a
Linux JazzBook 6.6.87.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Thu Jun  5 18:30:46 UTC 2025 x86_64 x86_64 x86_64 GNU/Linux
~/git/snippet/js/n8n/lab0$ docker-compose up -d
Creating network "lab0_default" with the default driver
Creating lab0_traefik_1 ... done
Creating lab0_n8n_1     ... done
~/git/snippet/js/n8n/lab0$ open http://localhost:5678
```
- 果然有歷史資料存在 SQLite
```bash
~/git/snippet/js/n8n/lab0$ tree n8n_data/
n8n_data/
├── binaryData
├── config
├── crash.journal
├── database.sqlite
├── database.sqlite-shm
├── database.sqlite-wal
├── git
├── n8nEventLog.log
├── nodes
│   └── package.json
└── ssh

5 directories, 7 files
```