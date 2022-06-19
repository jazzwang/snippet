# Google Cloud Shell

- ( 2022-06-19 07:54:33 )
- 以前會自己買 VPS (Virtual Private Server)，方便做一些實驗。不過 GCP Cloud Shell 功能越來越強大了，近期常拿來在上面跑一些簡單的 docker 小實驗、跑跑 pyspark、練習寫 golang 程式。最近想實驗 Spark on K8S，想說可不可以跑 minikube，剛發現也已經納入預設的 image 了。記錄一些學習怎麼好好利用 Cloud Shell 的免費資源。

- ( 2022-06-19 07:58:50 )
- https://codelabs.developers.google.com/cloudshell-cloudcode-deepdive
- 這篇提到了不少技巧。

- ( 2022-06-19 08:03:53 )
- https://kubernetes.io/docs/tasks/tools/included/optional-kubectl-configs-bash-linux/
```bash
echo 'source <(kubectl completion bash)' >>~/.bashrc
```