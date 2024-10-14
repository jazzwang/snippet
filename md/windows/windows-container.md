# Containers on Windows

## 2024-10-14

- 緣起：在 Windows 上可以跑 Windows Server Docker container。想了解一下基本需求有哪些。
- 參考：

```bash
jazzw@JazzBook:~$ scoop info docker


Name        : docker
Description : Docker CLI & Docker Engine for Windows containers. Docker is an open platform for developing, shipping, and running applications.
Version     : 27.3.1
Bucket      : main
Website     : https://docs.docker.com/engine
License     : Apache-2.0
Updated at  : 9/21/2024 4:28:51 AM
Updated by  : github-actions[bot]
Binaries    : docker.exe | dockerd.exe
Notes       : The 'dockerd' binary here only supports running Windows containers.
              However it is possible to connect to existing Linux containers using the 'docker' binary
              To register Docker as a service, run `dockerd --register-service`
              Similarly, to unregister, run `dockerd --unregister-service`



jazzw@JazzBook:~$ scoop install docker
Installing 'docker' (27.3.1) [64bit] from 'main' bucket
docker-27.3.1.zip (37.7 MB) [=====================================================================================================================] 100%
Checking hash of docker-27.3.1.zip ... ok.
Extracting docker-27.3.1.zip ... done.
Linking ~\scoop\apps\docker\current => ~\scoop\apps\docker\27.3.1
Creating shim for 'docker'.
Creating shim for 'dockerd'.
'docker' (27.3.1) was installed successfully!
Notes
-----
The 'dockerd' binary here only supports running Windows containers.
However it is possible to connect to existing Linux containers using the 'docker' binary
To register Docker as a service, run `dockerd --register-service`
Similarly, to unregister, run `dockerd --unregister-service`
```
- 為了註冊 `dockerd` 成服務，需要用到 Windows Administrator 權限。這邊用 `scoop` 安裝的 `sudo` 指令來簡化流程
```bash
jazzw@JazzBook:~$ dockerd --register-service
Access is denied.
jazzw@JazzBook:~$ sudo dockerd --register-service
jazzw@JazzBook:~$
```