# README

- Test https://github.com/All-Hands-AI/OpenHands with Google Cloud Shell
  - NOTE: port `3000` was in use. use port `3838` instead.
```bash
jazz_innova18@cloudshell:~$ WORKSPACE_BASE=$(pwd)/workspace
jazz_innova18@cloudshell:~$ docker run -it --pull=always -e SANDBOX_USER_ID=$(id -u) -e WORKSPACE_MOUNT_PATH=$WORKSPACE_BASE -v $WORKSPACE_BASE:/opt/workspace_base -v /var/run/docker.sock:/var/run/docker.sock -p 3838:3000 --add-host host.docker.internal:host-gateway --name openhands-app-$(date +%Y%m%d%H%M%S) ghcr.io/all-hands-ai/openhands:0.9
```
- This code is generated by [OpenHands (OpenDevin)](https://github.com/All-Hands-AI/OpenHands)
![Screen Shot 2024-08-29 at 10.29.56 PM](https://i.imgur.com/2dhzBXf.png)
