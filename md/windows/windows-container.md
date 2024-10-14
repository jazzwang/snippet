# Containers on Windows

## 2024-10-14

- 緣起：在 Windows 上可以跑 Windows Server Docker container。想了解一下基本需求有哪些。
- 參考：
  - https://learn.microsoft.com/en-us/virtualization/windowscontainers/about/
    - Windows 10/11 - 必須安裝 WSL + Docker Desktop 才能跑 `docker` (可以切換 OS/Arch 是 Windows 或 Linux)
    - Windows Server 有內建 native windows docker
- 其他資訊：
  - 先前有在 hub.docker.com 查到 windows server 的不同版本
    - https://hub.docker.com/r/microsoft/windows-server
      - `docker pull mcr.microsoft.com/windows/server`
    - https://hub.docker.com/r/microsoft/windows-servercore
      - `docker pull mcr.microsoft.com/windows/servercore`

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
- ( 2024-10-14 21:25:38 )
- 要啟用 `dockerd` 服務，首先查了 Service 內的名稱為『Docker Engine』。接著用 `net start` 指令啟動。
```bash
jazzw@JazzBook:~/git/snippet$ sudo net start "Docker Engine"
The Docker Engine service is starting.
The Docker Engine service was started successfully.

jazzw@JazzBook:~/git/snippet$ sudo net start "Docker Engine"
The requested service has already been started.

More help is available by typing NET HELPMSG 2182.
```
- 要停用的話，則使用 `net stop` 指令停止。
```bash
jazzw@JazzBook:~/git/snippet$ sudo net stop "Docker Engine"
The Docker Engine service is stopping.
The Docker Engine service was stopped successfully.
```
- 使用 Administrator 權限，是可以正常執行 docker 指令
```bash
jazzw@JazzBook:~$ sudo net start "Docker Engine"
The Docker Engine service is starting.
The Docker Engine service was started successfully.

jazzw@JazzBook:~$ sudo docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```
- 本來希望可以透過新增群組的方式，讓一般使用者也可以使用。
- 參考：
  - https://learn.microsoft.com/en-us/troubleshoot/developer/visualstudio/ide/troubleshooting-docker-errors#docker-users-group
```powershell
net localgroup docker-users DOMAIN\username /add
```
```powershell
PS C:\Windows\system32> Get-LocalGroup

Name                          Description
----                          -----------
Administrators                Administrators have complete and unrestricted access to the computer/domain
Device Owners                 Members of this group can change system-wide settings.
Distributed COM Users         Members are allowed to launch, activate and use Distributed COM objects on this machine.
Event Log Readers             Members of this group can read event logs from local machine
Guests                        Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted
Hyper-V Administrators        Members of this group have complete and unrestricted access to all features of Hyper-V.
IIS_IUSRS                     Built-in group used by Internet Information Services.
Performance Log Users         Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer
Performance Monitor Users     Members of this group can access performance counter data locally and remotely
Remote Management Users       Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces t...
System Managed Accounts Group Members of this group are managed by the system.
Users                         Users are prevented from making accidental or intentional system-wide changes and can run most applications

PS C:\Users\jazzw> net localgroup docker-users /ADD

PS C:\Users\jazzw> net localgroup docker-users jazzw /ADD

PS C:\Windows\system32> Get-LocalGroup

Name                          Description
----                          -----------
docker-users
Administrators                Administrators have complete and unrestricted access to the computer/domain
Device Owners                 Members of this group can change system-wide settings.
Distributed COM Users         Members are allowed to launch, activate and use Distributed COM objects on this machine.
Event Log Readers             Members of this group can read event logs from local machine
Guests                        Guests have the same access as members of the Users group by default, except for the Guest account which is further restricted
Hyper-V Administrators        Members of this group have complete and unrestricted access to all features of Hyper-V.
IIS_IUSRS                     Built-in group used by Internet Information Services.
Performance Log Users         Members of this group may schedule logging of performance counters, enable trace providers, and collect event traces both locally and via remote access to this computer
Performance Monitor Users     Members of this group can access performance counter data locally and remotely
Remote Management Users       Members of this group can access WMI resources over management protocols (such as WS-Management via the Windows Remote Management service). This applies only to WMI namespaces t...
System Managed Accounts Group Members of this group are managed by the system.
Users                         Users are prevented from making accidental or intentional system-wide changes and can run most applications
```
- 參考：https://stackoverflow.com/a/40086454

```bash
jazzw@JazzBook:~/git/snippet$ export DOCKER_HOST="tcp://0.0.0.0:53"
jazzw@JazzBook:~/git/snippet$ docker ps
error during connect: in the default daemon configuration on Windows, the docker client must be run with elevated privileges to connect: Get "http://%2F%2F.%2Fpipe%2Fdocker_engine/v1.47/containers/json": open //./pipe/docker_engine: Access is denied.
```
- 但看起來應該卡在 pipe 裝置上。
- 以下是將 PowerShell 以 Administrator 身份執行時，看到的結果：
  - Docker 的 OS/Arch 是 `windows/amd64`
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Windows\system32> whoami
jazzbook\jazzw
PS C:\Windows\system32> docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
PS C:\Windows\system32> docker status
docker: 'status' is not a docker command.
See 'docker --help'
PS C:\Windows\system32> docker version
Client:
 Version:           27.3.1
 API version:       1.47
 Go version:        go1.22.7
 Git commit:        ce12230
 Built:             Fri Sep 20 11:42:27 2024
 OS/Arch:           windows/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          27.3.1
  API version:      1.47 (minimum version 1.24)
  Go version:       go1.22.7
  Git commit:       41ca978
  Built:            Fri Sep 20 11:40:58 2024
  OS/Arch:          windows/amd64
  Experimental:     false
PS C:\Windows\system32> docker info
Client:
 Version:    27.3.1
 Context:    default
 Debug Mode: false

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 27.3.1
 Storage Driver: windowsfilter
  Windows:
 Logging Driver: json-file
 Plugins:
  Volume: local
  Network: ics internal l2bridge l2tunnel nat null overlay private transparent
  Log: awslogs etwlogs fluentd gcplogs gelf json-file local splunk syslog
 Swarm: inactive
 Default Isolation: hyperv
 Kernel Version: 10.0 22631 (22621.1.amd64fre.ni_release.220506-1250)
 Operating System: Microsoft Windows Version 23H2 (OS Build 22631.4317)
 OSType: windows
 Architecture: x86_64
 CPUs: 16
 Total Memory: 31.25GiB
 Name: JazzBook
 ID: 634e6087-5c24-4e7b-9c17-50cbbd677989
 Docker Root Dir: C:\ProgramData\docker
 Debug Mode: false
 Experimental: false
 Insecure Registries:
  127.0.0.0/8
 Live Restore Enabled: false
 Product License: Community Engine

PS C:\Windows\system32> docker login

USING WEB-BASED LOGIN
To sign in with credentials on the command line, use 'docker login -u <username>'

Your one-time device confirmation code is: MLLJ-JCCB
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…

WARNING! Your password will be stored unencrypted in C:\Users\jazzw\.docker\config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded
PS C:\Windows\system32> docker search windows
NAME                           DESCRIPTION                                     STARS     OFFICIAL
dockurr/windows                Windows inside a Docker container.              282
actiontestscript/windows       ATS Docker Windows image ready to launch ATS…   0
calico/windows                                                                 3
mgba/windows                   Windows autobuilds                              2
toxchat/windows                                                                0
toktoknet/windows              Windows cross compilers: i686 and x86_64.       0
spellegrino021/windows                                                         2
dcoswindowsci/windows          CI Nano Server Image                            0
hchandawad1/windows                                                            0
zixia/windows                  Run Windows Application in a Linux Docker Co…   3
njawalequalys/windows                                                          0
ironsoftwareofficial/windows   Pre-configured Windows containers for runnin…   0
oufqatu/windows                This is just a testing windows image            0
metthal/windows                Unofficial Windows images with MSVC, CMake a…   0
h3llix/windows                                                                 0
cdaf/windows                   Base on Windows Server 2022                     0
jerbi/windows                                                                  0
newbe36524/windows                                                             0
kpack/windows                                                                  0
atxwebdesigner/windows                                                         0
microsoft/windows              The official Windows base image for containe…   21
yatima1460/windows                                                             0
seokjunyoon/windows            Windows Containers                              0
frank0757/windows                                                              0
fredericoliz/windows                                                           0
PS C:\Windows\system32> docker search windows --help

Usage:  docker search [OPTIONS] TERM

Search Docker Hub for images

Options:
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print search using a Go template
      --limit int       Max number of search results
      --no-trunc        Don't truncate output

PS C:\Windows\system32>
```
- 暫且就先這樣湊合著用吧～這樣果然就可以下載 OS/Arch 是 Windows 的 nanoserver image
```powershell
PS C:\Windows\system32> docker pull mcr.microsoft.com/windows/nanoserver:ltsc2022
ltsc2022: Pulling from windows/nanoserver
bbb4d9e65e9c: Downloading [==================>                                ]   42.7MB/116.8MB
```
- 看起來資料都存在 `C:\ProgramData\docker`
```powershell
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Windows\system32> docker pull mcr.microsoft.com/windows/nanoserver
Using default tag: latest
Error response from daemon: manifest for mcr.microsoft.com/windows/nanoserver:latest not found: manifest unknown: manifest tagged by "latest" is not found

PS C:\Windows\system32> docker pull mcr.microsoft.com/windows/nanoserver:ltsc2022
ltsc2022: Pulling from windows/nanoserver
bbb4d9e65e9c: Pull complete
Digest: sha256:f59e2f21720e4d1192e0dde47e32c7dbf27144d52d79be14b2538fa07145c869
Status: Downloaded newer image for mcr.microsoft.com/windows/nanoserver:ltsc2022
mcr.microsoft.com/windows/nanoserver:ltsc2022
PS C:\Windows\system32> cd \
PS C:\> cd .\ProgramData\docker\
PS C:\ProgramData\docker> tree
Folder PATH listing for volume OS
Volume serial number is C04F-8CF9
C:.
├───buildkit
│   └───content
│       └───ingest
├───containers
├───content
│   └───data
│       ├───blobs
│       │   └───sha256
│       └───ingest
├───credentialspecs
├───exec-root
├───image
│   └───windowsfilter
│       ├───distribution
│       │   ├───diffid-by-digest
│       │   │   └───sha256
│       │   └───v2metadata-by-diffid
│       │       └───sha256
│       ├───imagedb
│       │   ├───content
│       │   │   └───sha256
│       │   └───metadata
│       │       └───sha256
│       └───layerdb
│           ├───sha256
│           │   └───a65c487b4072295f88b404eeac3a71552858ae6b5b1383f2462e863aca6e4b9b
│           └───tmp
├───network

... 略 ...

                    │   ├───en-US
                    │   ├───migration
                    │   ├───oobe
                    │   └───wbem
                    ├───Temp
                    └───WaaS
                        └───services

PS C:\ProgramData\docker> dir


    Directory: C:\ProgramData\docker


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        10/14/2024   9:23 PM                buildkit
d-----        10/14/2024   9:23 PM                containers
d-----        10/14/2024   9:23 PM                content
d-----        10/14/2024   9:23 PM                credentialspecs
d-----        10/14/2024   9:23 PM                exec-root
d-----        10/14/2024   9:23 PM                image
d-----        10/14/2024   9:23 PM                network
d-----        10/14/2024   9:23 PM                plugins
d-----        10/14/2024   9:23 PM                swarm
d-----        10/14/2024  11:55 PM                tmp
d-----        10/14/2024   9:23 PM                volumes
d-----        10/15/2024  12:21 AM                windowsfilter
-a----        10/14/2024   9:23 PM             36 engine-id
-a----        10/15/2024  12:19 AM           1083 panic.log
-a----        10/14/2024  11:46 PM            943 panic.log.old
```
- ( 2024-10-15 00:28:43 )
- 參考：https://github.com/docker/labs/blob/master/windows/windows-containers/WindowsContainers.md
- 嘗試運行 Windows NanoServer 的 Docker container
```powershell
PS C:\> cd $env:HOMEPATH
PS C:\Users\jazzw> docker images
REPOSITORY                             TAG        IMAGE ID       CREATED      SIZE
mcr.microsoft.com/windows/nanoserver   ltsc2022   b9775a86954e   8 days ago   292MB
PS C:\Users\jazzw> docker run mcr.microsoft.com/windows/nanoserver:ltsc2022 hostname
docker: Error response from daemon: hcs::CreateComputeSystem 2355fb2397c668245c66340dec9d60e29fd32523d63bdf0dcfdd660e77325958: The request is not supported.
```
- 用 `docker container run` 還是一樣的錯誤訊息。
```powershell
PS C:\Users\jazzw> docker container

Usage:  docker container COMMAND

Manage containers

Commands:
  attach      Attach local standard input, output, and error streams to a running container
  commit      Create a new image from a container's changes
  cp          Copy files/folders between a container and the local filesystem
  create      Create a new container
  diff        Inspect changes to files or directories on a container's filesystem
  exec        Execute a command in a running container
  export      Export a container's filesystem as a tar archive
  inspect     Display detailed information on one or more containers
  kill        Kill one or more running containers
  logs        Fetch the logs of a container
  ls          List containers
  pause       Pause all processes within one or more containers
  port        List port mappings or a specific mapping for the container
  prune       Remove all stopped containers
  rename      Rename a container
  restart     Restart one or more containers
  rm          Remove one or more containers
  run         Create and run a new container from an image
  start       Start one or more stopped containers
  stats       Display a live stream of container(s) resource usage statistics
  stop        Stop one or more running containers
  top         Display the running processes of a container
  unpause     Unpause all processes within one or more containers
  update      Update configuration of one or more containers
  wait        Block until one or more containers stop, then print their exit codes

Run 'docker container COMMAND --help' for more information on a command.
PS C:\Users\jazzw> docker container run
"docker container run" requires at least 1 argument.
See 'docker container run --help'.

Usage:  docker container run [OPTIONS] IMAGE [COMMAND] [ARG...]

Create and run a new container from an image
PS C:\Users\jazzw> docker container run mcr.microsoft.com/windows/nanoserver:ltsc2022 hostname
docker: Error response from daemon: hcs::CreateComputeSystem 4c267977624bea28527503901e33f5fdff859ee5dce4014d206057a8b012314c: The request is not supported.
```
- 看樣子還是用 `Docker Desktop` 會比 `Docker Engine` 來得容易。
- ( 2024-10-15 00:41:08 )
- 反安裝 `Docker Engine`
```bash
jazzw@JazzBook:~$ sudo net stop "Docker Engine"
The Docker Engine service is stopping.
The Docker Engine service was stopped successfully.

jazzw@JazzBook:~$ dockerd --unregister-service
Access is denied.
jazzw@JazzBook:~$ sudo dockerd --unregister-service
jazzw@JazzBook:~$ scoop uninstall docker
Uninstalling 'docker' (27.3.1).
Removing shim 'docker.shim'.
Removing shim 'docker.exe'.
Removing shim 'dockerd.shim'.
Removing shim 'dockerd.exe'.
Unlinking ~\scoop\apps\docker\current
ERROR Couldn't remove '~\scoop\apps\docker\27.3.1'; it may be in use.
```

## 2024-10-15

- 其他作法：
  - Updated on `2022-04-10` : [Install Docker on Windows (WSL) without Docker Desktop](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9)
  - 根據文章的描述，步驟蠻繁瑣的，作者也說 Docker Desktop 還是比較好的選擇。
  - 文章中也提到其他類似 Docker 的替代方案，像是 `podman` 等。應該只能在 WSL 裡模擬 OS/Arch 是 Linux 的容器才是。