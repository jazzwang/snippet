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

- ( 2022-06-19 08:38:42 )
```bash
~/spark$ ./bin/docker-image-tool.sh -r jazzwang -t my-tag build
~/spark$ ./bin/docker-image-tool.sh -r jazzwang -t my-tag push   ## 不確定是否一定要 push, 也可能 minikube 可以用 local image
~/spark$ K8S_SRV=$(kubectl cluster-info | grep control | sed 's#.*https://#https://#')
~/spark$ echo $K8S_SRV
https://192.168.49.2:8443
~/spark$ ./bin/spark-submit --master k8s://https://192.168.49.2:8443 --deploy-mode cluster --name spark-pi --class org.apache.spark.examples.SparkPi --conf spark.kubernetes.container.image=jazzwang/spark:my-tag local:///home/${USER}/spark/examples/jars/spark-examples_2.12-3.0.3.jar
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/home/jazz_innova18/spark/jars/spark-unsafe_2.12-3.0.3.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
22/06/19 00:44:53 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
22/06/19 00:44:53 INFO SparkKubernetesClientFactory: Auto-configuring K8S client using current context from users K8S config file
22/06/19 00:44:54 INFO KerberosConfDriverFeatureStep: You have not specified a krb5.conf file locally or via a ConfigMap. Make sure that you have the krb5.conf locally on the driver image.
22/06/19 00:44:55 INFO LoggingPodStatusWatcherImpl: State changed, new state:
         pod name: spark-pi-87931781796b7201-driver
         namespace: default
         labels: spark-app-selector -> spark-e3ee25c9a8fd41938804d907974d8a72, spark-role -> driver
         pod uid: 62c802d5-20b7-4dae-9103-26547141316e
         creation time: 2022-06-19T00:44:55Z
         service account name: default
         volumes: spark-local-dir-1, spark-conf-volume, kube-api-access-4299z
         node name: minikube
         start time: 2022-06-19T00:44:55Z
         phase: Pending
         container status:
                 container name: spark-kubernetes-driver
                 container image: jazzwang/spark:my-tag
                 container state: waiting
                 pending reason: ContainerCreating
22/06/19 00:44:55 INFO LoggingPodStatusWatcherImpl: Waiting for application spark-pi with submission ID default:spark-pi-87931781796b7201-driver to finish...
22/06/19 00:44:55 INFO LoggingPodStatusWatcherImpl: State changed, new state:
         pod name: spark-pi-87931781796b7201-driver
         namespace: default
         labels: spark-app-selector -> spark-e3ee25c9a8fd41938804d907974d8a72, spark-role -> driver
         pod uid: 62c802d5-20b7-4dae-9103-26547141316e
         creation time: 2022-06-19T00:44:55Z
         service account name: default
         volumes: spark-local-dir-1, spark-conf-volume, kube-api-access-4299z
         node name: minikube
         start time: 2022-06-19T00:44:55Z
         phase: Pending
         container status:
                 container name: spark-kubernetes-driver
                 container image: jazzwang/spark:my-tag
                 container state: waiting
                 pending reason: ContainerCreating
22/06/19 00:44:56 INFO LoggingPodStatusWatcherImpl: Application status for spark-e3ee25c9a8fd41938804d907974d8a72 (phase: Pending)
22/06/19 00:44:57 INFO LoggingPodStatusWatcherImpl: State changed, new state:
         pod name: spark-pi-87931781796b7201-driver
         namespace: default
         labels: spark-app-selector -> spark-e3ee25c9a8fd41938804d907974d8a72, spark-role -> driver
         pod uid: 62c802d5-20b7-4dae-9103-26547141316e
         creation time: 2022-06-19T00:44:55Z
         service account name: default
         volumes: spark-local-dir-1, spark-conf-volume, kube-api-access-4299z
         node name: minikube
         start time: 2022-06-19T00:44:55Z
         phase: Running
         container status:
                 container name: spark-kubernetes-driver
                 container image: jazzwang/spark:my-tag
                 container state: running
                 container started at: 2022-06-19T00:44:56Z
22/06/19 00:44:57 INFO LoggingPodStatusWatcherImpl: Application status for spark-e3ee25c9a8fd41938804d907974d8a72 (phase: Running)
22/06/19 00:44:58 INFO LoggingPodStatusWatcherImpl: Application status for spark-e3ee25c9a8fd41938804d907974d8a72 (phase: Running)
22/06/19 00:44:59 INFO LoggingPodStatusWatcherImpl: Application status for spark-e3ee25c9a8fd41938804d907974d8a72 (phase: Running)
22/06/19 00:45:00 INFO LoggingPodStatusWatcherImpl: State changed, new state:
         pod name: spark-pi-87931781796b7201-driver
         namespace: default
         labels: spark-app-selector -> spark-e3ee25c9a8fd41938804d907974d8a72, spark-role -> driver
         pod uid: 62c802d5-20b7-4dae-9103-26547141316e
         creation time: 2022-06-19T00:44:55Z
         service account name: default
         volumes: spark-local-dir-1, spark-conf-volume, kube-api-access-4299z
         node name: minikube
         start time: 2022-06-19T00:44:55Z
         phase: Failed
         container status:
                 container name: spark-kubernetes-driver
                 container image: jazzwang/spark:my-tag
                 container state: terminated
                 container started at: 2022-06-19T00:44:56Z
                 container finished at: 2022-06-19T00:44:59Z
                 exit code: 101
                 termination reason: Error
22/06/19 00:45:00 INFO LoggingPodStatusWatcherImpl: Application status for spark-e3ee25c9a8fd41938804d907974d8a72 (phase: Failed)
22/06/19 00:45:00 INFO LoggingPodStatusWatcherImpl: Container final statuses:


         container name: spark-kubernetes-driver
         container image: jazzwang/spark:my-tag
         container state: terminated
         container started at: 2022-06-19T00:44:56Z
         container finished at: 2022-06-19T00:44:59Z
         exit code: 101
         termination reason: Error
22/06/19 00:45:00 INFO LoggingPodStatusWatcherImpl: Application spark-pi with submission ID default:spark-pi-87931781796b7201-driver finished
22/06/19 00:45:00 INFO ShutdownHookManager: Shutdown hook called
22/06/19 00:45:00 INFO ShutdownHookManager: Deleting directory /tmp/spark-bc87ac2e-47ac-4998-9b3a-89e20d4dafb3
```

## 2023-08-30

- 如果想產生像底下這種 Icon 的話，可參考 https://cloud.google.com/shell/docs/open-in-cloud-shell

  [![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://shell.cloud.google.com/cloudshell/editor?cloudshell_git_repo=http://path-to-repo/sample.git)

- 連結產生器 - [Open in Cloud Shell link generator](https://cloud.google.com/shell/docs/open-in-cloud-shell#open_in_link_generator)

## 2024-10-18

- https://cloud.google.com/shell/docs/cloud-shell-tutorials/tutorials
- 如果要撰寫可以在 Cloud Shell 環境中執行的 Tutorial，可以參考這篇。

( 2024-10-18 18:59:34 )
- 待查 Google Cloud Shell 是否可以支援 `.devcontainer`

## 2025-07-06

- 生態系變化得很快，後來 Google Cloud Shell 就改用 VS Code為主了。因此，上面提到的[在 Cloud Shell 環境中執行的 Tutorial](https://cloud.google.com/shell/docs/cloud-shell-tutorials/tutorials) 後來預設的 `tutorial.md` 也消失了。不過 GCP 團隊還是有保留這個功能，所以還可以拿來做一些程式實作教學使用。