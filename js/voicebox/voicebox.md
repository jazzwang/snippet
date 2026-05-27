# voicebox

> The open-source AI voice studio. Clone, dictate, create.

- Git Repo
  - https://github.com/jamiepine/voicebox
- Website
  - https://voicebox.sh/

## 2026-05-27

- 實測一：
  - 環境: Github Codespace 2 vCPU, 8 GB RAM
```
[05/27 17:36:17] blank create
[05/27 17:36:42] blank edit
[05/27 17:37:03] blank edit -d "blank"
[05/27 17:37:13] blank code
```
  - 步驟：
```
~$ cd /tmp
~/tmp$ git clone https://github.com/jamiepine/voicebox.git
~/tmp$ cd voicebox
~/tmp/voicebox$ docker-compose up -d
```
  - 結果：把 tmp 塞爆了 XD (`No Space left`)
- 實測二：
  - 環境：Windows 11 + WSL 2 + Docker
```
~/Downloads$ wsl
Welcome to Ubuntu 24.04.2 LTS (GNU/Linux 6.6.114.1-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Wed May 27 05:27:35 PM CST 2026

  System load:  0.16                Processes:             80
  Usage of /:   3.2% of 1006.85GB   Users logged in:       0
  Memory usage: 3%                  IPv4 address for eth0: 172.29.78.252
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

This message is shown once a day. To disable it please create the
/home/jazz/.hushlogin file.
/mnt/c/Users/jazzw/Downloads$ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
/mnt/c/Users/jazzw/Downloads$ cd ..
/mnt/c/Users/jazzw$ cd git/
/mnt/c/Users/jazzw/git$ git clone https://github.com/jamiepine/voicebox.git
Cloning into 'voicebox'...
remote: Enumerating objects: 8900, done.
remote: Counting objects: 100% (3634/3634), done.
remote: Compressing objects: 100% (781/781), done.
remote: Total 8900 (delta 3012), reused 2853 (delta 2853), pack-reused 5266 (from 1)
Receiving objects: 100% (8900/8900), 98.75 MiB | 1.78 MiB/s, done.
Resolving deltas: 100% (5960/5960), done.
Updating files: 100% (638/638), done.
/mnt/c/Users/jazzw/git$ cd voicebox/
/mnt/c/Users/jazzw/git/voicebox$ docker-compose ps
Name   Command   State   Ports
------------------------------
/mnt/c/Users/jazzw/git/voicebox$ docker-compose up -d
Creating network "voicebox_voicebox-net" with driver "bridge"
Creating volume "voicebox_voicebox-data" with default driver
Creating volume "voicebox_huggingface-cache" with default driver
Building voicebox
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  6.796MB
Step 1/29 : FROM oven/bun:1 AS frontend
 ---> 59cef0f85ea4
Step 2/29 : WORKDIR /build
 ---> Running in 50687c1fda0a
 ---> Removed intermediate container 50687c1fda0a
 ---> 88bd810d6505
Step 3/29 : COPY package.json bun.lock CHANGELOG.md ./
 ---> 1d4c46eb8591
Step 4/29 : COPY app/ ./app/
 ---> dd2b9bc22c42
Step 5/29 : COPY web/ ./web/
 ---> b8695f638426
Step 6/29 : RUN sed -i '/"tauri"/d; /"landing"/d' package.json &&     sed -i -z 's/,\n  ]/\n  ]/' package.json
 ---> Running in ebd2880bc09b
 ---> Removed intermediate container ebd2880bc09b
 ---> 9e5b8a8f5547
Step 7/29 : RUN bun install --no-save
 ---> Running in 1b196b7e120f
bun install v1.3.14 (0d9b296a)
error: Fail extracting tarball for "@biomejs/cli-linux-x64-musl"
error: failed to download @biomejs/cli-linux-x64-musl@2.3.12: Fail
  https://registry.npmjs.org/@biomejs/cli-linux-x64-musl/-/cli-linux-x64-musl-2.3.12.tgz

+ @biomejs/biome@2.3.12
+ @types/node@20.19.30
+ tailwindcss@4.1.18
+ typescript@5.9.3
+ loaders.css@0.1.2
+ react-loaders@3.0.1

654 packages installed [166.47s]
Removed: 2
Failed to install 1 package
The command '/bin/sh -c bun install --no-save' returned a non-zero code: 1
ERROR: Service 'voicebox' failed to build : Build failed
```
- 再測試一次
```bash
/mnt/c/Users/jazzw/git/voicebox$ cd
~$ cd git/voicebox
~/git/voicebox$ docker-compose build
Building voicebox
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  6.796MB
Step 1/29 : FROM oven/bun:1 AS frontend
 ---> 59cef0f85ea4
Step 2/29 : WORKDIR /build
 ---> Using cache
 ---> 88bd810d6505
Step 3/29 : COPY package.json bun.lock CHANGELOG.md ./
 ---> Using cache
 ---> 1d4c46eb8591
Step 4/29 : COPY app/ ./app/
 ---> Using cache
 ---> dd2b9bc22c42
Step 5/29 : COPY web/ ./web/
 ---> Using cache
 ---> b8695f638426
Step 6/29 : RUN sed -i '/"tauri"/d; /"landing"/d' package.json &&     sed -i -z 's/,\n  ]/\n  ]/' package.json
 ---> Using cache
 ---> 9e5b8a8f5547
Step 7/29 : RUN bun install --no-save
 ---> Running in 29aba4cf7ba9
bun install v1.3.14 (0d9b296a)

... 略 ...

Step 22/29 : COPY --from=backend-builder /install /usr/local
 ---> 696d28eb54af
Step 23/29 : COPY --chown=voicebox:voicebox backend/ /app/backend/
 ---> 2c22897af84f
Step 24/29 : COPY --from=frontend --chown=voicebox:voicebox /build/web/dist /app/frontend/
 ---> 24764df48d08
Step 25/29 : RUN mkdir -p /app/data/generations /app/data/profiles /app/data/cache     && chown -R voicebox:voicebox /app/data
 ---> Running in 24104a860cc1
 ---> Removed intermediate container 24104a860cc1
 ---> 5091358cb868
Step 26/29 : USER voicebox
 ---> Running in f92d8676f08f
 ---> Removed intermediate container f92d8676f08f
 ---> 4eb54c5779a9
Step 27/29 : EXPOSE 17493
 ---> Running in 6df3e890d9d6
 ---> Removed intermediate container 6df3e890d9d6
 ---> 62c6d9840f01
Step 28/29 : HEALTHCHECK --interval=30s --timeout=10s --retries=3 --start-period=60s     CMD curl -f http://localhost:17493/health || exit 1
 ---> Running in a62c581e6b0d
 ---> Removed intermediate container a62c581e6b0d
 ---> 0afd1a09d1a1
Step 29/29 : CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "17493"]
 ---> Running in 09d72d27af1e
 ---> Removed intermediate container 09d72d27af1e
 ---> 57584e36b153
Successfully built 57584e36b153
Successfully tagged voicebox_voicebox:latest
~/git/voicebox$
~/git/voicebox$ docker-compose up
Creating voicebox ... done
Attaching to voicebox
voicebox    | INFO:     MCP: mounted at /mcp
voicebox    | INFO:     Frontend: serving SPA from /app/frontend
voicebox    | INFO:     Started server process [1]
voicebox    | INFO:     Waiting for application startup.
voicebox    | INFO:     Voicebox v0.5.0 starting up
voicebox    | INFO:     Python 3.11.14 on Linux 6.6.114.1-microsoft-standard-WSL2 (x86_64)
voicebox    | INFO:     Database: /app/data/voicebox.db
voicebox    | INFO:     Data directory: /app/data
voicebox    | INFO:     Profiles: 0, Generations: 0
voicebox    | INFO:     Backend: PYTORCH
voicebox    | INFO:     GPU: None (CPU only)
voicebox    | WARNING:     Could not create HuggingFace cache directory: [Errno 13] Permission denied: '/home/voicebox/.cache/huggingface/hub'
voicebox    | INFO:     Ready
voicebox    | INFO:     StreamableHTTP session manager started
voicebox    | INFO:     Application startup complete.
voicebox    | INFO:     Uvicorn running on http://0.0.0.0:17493 (Press CTRL+C to quit)
voicebox    | INFO:     127.0.0.1:53142 - "GET /health HTTP/1.1" 200 OK
voicebox    | INFO:     127.0.0.1:37978 - "GET /health HTTP/1.1" 200 OK
^CGracefully stopping... (press Ctrl+C again to force)
Stopping voicebox ... done
~/git/voicebox$ docker-compose up -d
Starting voicebox ... done
~/git/voicebox$ docker-compose ps -a
  Name                Command                       State                     Ports
----------------------------------------------------------------------------------------------
voicebox   uvicorn backend.main:app - ...   Up (health: starting)   127.0.0.1:17493->17493/tcp
~/git/voicebox$
```
```
 4485  [05/27 22:51:13] docker-compose up
 4486  [05/27 22:52:12] docker-compose up -d
 4487  [05/27 22:52:19] docker-compose ps -a
```
