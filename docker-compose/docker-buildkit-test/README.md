# 2021-09-09

* 需求：Dockerfile 裡面需要放密碼。想確認 
  * (1) 使用 ARG 語法，是否能從 `docker image history` 看到明碼呢？（資安問題）
  * (2) 若要用 18.09 版以後支援的 [BuildKit](https://docs.docker.com/develop/develop-images/build_enhancements/)，該怎麼做呢？

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
```
$ docker build -f Dockerfile_ARG --build-arg PASSWORD=1234 --build-arg USERNAME=jazz -t jazzwang/arg-test .
```
* 檢查 `docker image history` 的結果
```
$ docker image history jazzwang/arg-test:latest
IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT
3bb5731f2dbd   About a minute ago   |2 PASSWORD=1234 USERNAME=jazz /bin/sh -c ec…   10B
cc1a59f8090d   2 minutes ago        /bin/sh -c #(nop)  ARG PASSWORD                 0B
65b3616c360b   2 minutes ago        /bin/sh -c #(nop)  ARG USERNAME                 0B
ea7d14d15d7e   2 minutes ago        /bin/sh -c #(nop)  MAINTAINER Jazz Wang <jaz…   0B
14119a10abf4   12 days ago          /bin/sh -c #(nop)  CMD ["/bin/sh"]              0B
<missing>      12 days ago          /bin/sh -c #(nop) ADD file:aad4290d27580cc1a…   5.6MB
```
* 可以看到 history 裡，將 PASSWORD 跟 USERNAME 都以明碼的方式儲存。（有資安疑慮）
* 當然因為知道結果存在哪裡，可以查得到。但 `docker run` 用 image 產生的容器，並不會有 `PASSWORD` 跟 `USERNAME` 兩個環境變數。（從 `docker image history` 看得出來，這兩個 ARG 算是放在指令前面的**暫時性/一次性**環境變數。
```
$ docker run -it --name arg-test jazzwang/arg-test /bin/sh
/ # cat /var/log/secrets
jazz:1234
/ #
/ # echo $PASSWORD

/ # echo $USERNAME

/ #
```