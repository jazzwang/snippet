# MEMO

## 2022-06-17

- ( 2022-06-17 09:56:56 )
- 有點好奇 Google Cloud Shell 是用 docker 還是已經移轉到 podman 了
```
Welcome to Cloud Shell! Type "help" to get started.
To set your Cloud Platform project in this session use “gcloud config set project [PROJECT_ID]”
~$ dpkg -l | grep -i docker
ii  docker-ce                                 5:20.10.16~3-0~debian-bullseye                                             amd64        Docker: the open-source application container engine
ii  docker-ce-cli                             5:20.10.16~3-0~debian-bullseye                                             amd64        Docker CLI: the open-source application container engine
ii  docker-ce-rootless-extras                 5:20.10.16~3-0~debian-bullseye                                             amd64        Rootless support for Docker.
ii  docker-scan-plugin                        0.17.0~debian-bullseye                                                     amd64        Docker scan cli plugin.
```
- https://rootlesscontaine.rs/
```

```

- ( 2022-06-17 11:13:58 )
```
~$ apt-cache show docker-scan-plugin
Package: docker-scan-plugin
Architecture: amd64
Version: 0.17.0~debian-bullseye
Priority: optional
Section: admin
Source: docker-ce (5:20.10.13~3-0~debian-bullseye)
Maintainer: Docker <support@docker.com>
Installed-Size: 12954
Enhances: docker-ce-cli
Filename: dists/bullseye/pool/stable/amd64/docker-scan-plugin_0.17.0~debian-bullseye_amd64.deb
Size: 3520328
MD5sum: 582624a56124a4296e86bbf440a2208a
SHA1: 4c103cb1bc486aa82bb5daa7fbf0964e2dcacfc6
SHA256: fd37e0d05683d212211177fce6b8a2818b925f254e398e7da4f20389d9dbf686
SHA512: 8b35f35eaa6191d104a79b3d37b7ca78ee80344f7a8913d16d07634f325cefd7f52b7db38a8a1f4b68a0ac85c91c00df6bbcb1e74061a65f6c577908aeff2255
Homepage: https://github.com/docker/scan-cli-plugin
Description: Docker scan cli plugin.
Description-md5: a14a20493a8414c48fe52bbe672ee319
```