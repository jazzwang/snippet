# 2021-09-09

## 緣起

* 需求：Dockerfile 裡面需要放密碼。想確認 
  * (1) 使用 ARG 語法，是否能從 `docker image history` 看到明碼呢？（資安問題）
  * (2) 若要用 Docker 18.09 版以後支援的 [BuildKit](https://docs.docker.com/develop/develop-images/build_enhancements/)，該怎麼做呢？

## 實驗一：Dockerfile 使用 ARG

* 參考：https://peihsinsu.gitbooks.io/docker-note-book/content/dockerfile-env-vs-arg.html
* 參考：https://docs.docker.com/engine/reference/builder/#arg

* 使用以下 Dockfile
```
FROM alpine:latest
MAINTAINER Jazz Wang <jazzwang.tw@gmail.com>

ARG USERNAME
ARG PASSWORD

RUN echo "${USERNAME}:${PASSWORD}" > /var/log/secrets
```
* `docker build` 時加入 `--build-arg`
```bash
$ docker build -f Dockerfile_ARG --build-arg PASSWORD=1234 --build-arg USERNAME=jazz -t jazzwang/arg-test .
```
* 檢查 `docker image history` 的結果
```bash
$ docker image history jazzwang/arg-test:latest
IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT
3bb5731f2dbd   About a minute ago   |2 PASSWORD=1234 USERNAME=jazz /bin/sh -c ec…   10B
cc1a59f8090d   2 minutes ago        /bin/sh -c #(nop)  ARG PASSWORD                 0B
65b3616c360b   2 minutes ago        /bin/sh -c #(nop)  ARG USERNAME                 0B
ea7d14d15d7e   2 minutes ago        /bin/sh -c #(nop)  MAINTAINER Jazz Wang <jaz…   0B
14119a10abf4   12 days ago          /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      12 days ago          /bin/sh -c #(nop) ADD file:aad4290d27580cc1a…   5.6MB
```
```bash
$ docker history --no-trunc jazzwang/arg-test:latest
IMAGE                                                                     CREATED          CREATED BY                                                                                          SIZE      COMMENT
sha256:3bb5731f2dbd3e59a45f1a76fa8cf3e89a5492b4c8aaa481d4fd59143b9ccb2f   58 minutes ago   |2 PASSWORD=1234 USERNAME=jazz /bin/sh -c echo "${USERNAME}:${PASSWORD}" > /var/log/secrets         10B
sha256:cc1a59f8090dcea221949c9f99a9235330ab556677cb698c3bddafee00e6b8e7   59 minutes ago   /bin/sh -c #(nop)  ARG PASSWORD                                                                     0B
sha256:65b3616c360bcc2e72de7259697ec4676b188c621c27147d4822a2ae95830317   59 minutes ago   /bin/sh -c #(nop)  ARG USERNAME                                                                     0B
sha256:ea7d14d15d7ebee39e2f91d96d160c99758e6dc7195fcecb4b76d77d867e048c   59 minutes ago   /bin/sh -c #(nop)  MAINTAINER Jazz Wang <jazzwang.tw@gmail.com>                                     0B
sha256:14119a10abf4669e8cdbdff324a9f9605d99697215a0d21c360fe8dfa8471bab   12 days ago      /bin/sh -c #(nop)  CMD ["/bin/sh"]                                                                  0B
<missing>                                                                 12 days ago      /bin/sh -c #(nop) ADD file:aad4290d27580cc1a094ffaf98c3ca2fc5d699fe695dfb8e6e9fac20f1129450 in /    5.6MB
```
* 可以看到 `docker history` 裡，將 PASSWORD 跟 USERNAME 都以明碼的方式儲存。（有資安疑慮）
```
|2 PASSWORD=1234 USERNAME=jazz /bin/sh -c echo "${USERNAME}:${PASSWORD}" > /var/log/secrets         10B
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
```
* `docker run` 用 image 產生的容器，並不會有 `PASSWORD` 跟 `USERNAME` 兩個環境變數。
* 從 `docker image history` 看得出來，這兩個 ARG 算是放在指令前面的 **暫時性/一次性** 環境變數。
```
$ docker run -it --name arg-test jazzwang/arg-test /bin/sh
/ # cat /var/log/secrets
jazz:1234
/ #
/ # echo $PASSWORD

/ # echo $USERNAME

/ #
```

## 實驗二：使用 BuildKit

* 實際上在 [官方文件](https://docs.docker.com/engine/reference/builder/#arg) 裡也有提到這一段：
```
Warning:

It is not recommended to use build-time variables for passing secrets like github keys, user credentials etc. Build-time variable values are visible to any user of the image with the docker history command.

Refer to the “build images with BuildKit” section to learn about secure ways to use secrets when building images.
```
* 那就來實驗一下 [Build images with BuildKit](https://docs.docker.com/develop/develop-images/build_enhancements/) 裡的步驟吧！
* 首先確定 Docker 版本 -- (這裏使用 Google Cloud Platform Cloud Shell) 版本必須高於 18.09
```
cloudshell:~$ docker --version
Docker version 20.10.8, build 3967b7d
```
* 相較於 `--build-arg` 參數可以直接命令列指定變數內容，`--secret` 目前 **只支援從檔案讀取**
* `--secret` 是以 key/value 方式提供。例如：`--secret id=PASSWORD,src=/tmp/passwd`
* 方便實驗起見，這次就只用一個 secret，也就是密碼 `PASSWORD`
* 首先，先產生檔案存放 PASSWORD 變數
```bash
$ echo "1234" > /tmp/passwd
```
* 接著，以下是我們測試用的 Dockerfile
```
FROM alpine:latest
MAINTAINER Jazz Wang <jazzwang.tw@gmail.com>

RUN --mount=type=secret,id=PASSWORD read PASSWORD <  /run/secrets/PASSWORD
RUN echo ${PASSWORD}
```
* 注意：若沒有權限修改 `/etc/docker/daemon.json` 只能加環境變數 `DOCKER_BUILDKIT=1` 來啟用 `--secret` 參數
* 讓我們來產生 docker image
```bash
$ DOCKER_BUILDKIT=1 docker build -t jazzwang/buildkit-test -f Dockerfile_BuildKit --secret id=PASSWORD,src=/tmp/passwd .
[+] Building 0.8s (7/7) FINISHED
 => [internal] load build definition from Dockerfile_BuildKit                                                 0.1s
 => => transferring dockerfile: 214B                                                                          0.0s
 => [internal] load .dockerignore                                                                             0.0s
 => => transferring context: 2B                                                                               0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                                              0.0s
 => [1/3] FROM docker.io/library/alpine:latest                                                                0.0s
 => [2/3] RUN --mount=type=secret,id=PASSWORD read PASSWORD <  /run/secrets/PASSWORD                          0.3s
 => [3/3] RUN echo ${PASSWORD}                                                                                0.4s
 => exporting to image                                                                                        0.1s
 => => exporting layers                                                                                       0.1s
 => => writing image sha256:c8d64fd4c7703877bcd8bc7ff0e6ec79a7ad945645b01d610416bcc8708ee5a4                  0.0s
 => => naming to docker.io/jazzwang/buildkit-test                                                             0.0s
 ```
* 從 `docker history` 結果看來，確實沒有明碼的問題
```bash
$ docker history jazzwang/buildkit-test:latest
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
c8d64fd4c770   3 minutes ago   RUN /bin/sh -c echo ${PASSWORD} # buildkit      0B        buildkit.dockerfile.v0
<missing>      3 minutes ago   RUN /bin/sh -c read PASSWORD <  /run/secrets…   0B        buildkit.dockerfile.v0
<missing>      3 minutes ago   MAINTAINER Jazz Wang <jazzwang.tw@gmail.com>    0B        buildkit.dockerfile.v0
<missing>      12 days ago     /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      12 days ago     /bin/sh -c #(nop) ADD file:aad4290d27580cc1a…   5.6MB
```
* `docker run` 從 image 產生的容器，也不會保留密碼在 `/run/secrets` 底下。當然，也不會以環境變數存在。
```
$ docker run -it jazzwang/buildkit-test:latest /bin/sh
/ # ls /run/secrets/
/ # echo ${PASSWORD}

/ # exit
```