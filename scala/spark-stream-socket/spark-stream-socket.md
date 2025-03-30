# README

## Development Notes

### 2021-09-17

- tested on GCP Cloud Shell
- initial project using `sbt new`
```
cloudshell:~/snippet/scala$ sbt new jazzwang/scala-spark.g8
A minimal Apache Spark project in Scala

name [Scala Spark Project]: spark-stream-socket

Template applied in /home/jazzwang/snippet/scala/./spark-stream-socket
```
- create README.md
```
cloudshell:~/snippet/scala$ touch spark-stream-socket/README.md
cloudshell:~/snippet/scala$ rm -rf target
```
- Reference:
  - https://sparkbyexamples.com/spark/spark-streaming-from-tcp-socket/
    - learn from here: we can use `nc -l -p 9999` to create a server for Spark Streaming using `socketTextStream`
  - https://spark.apache.org/docs/3.0.0/streaming-programming-guide.html#a-quick-example
- create streaming socket source
```
cloudshell:~$ sudo apt-get -y install netcat
cloudshell:~$ nc -l -p 9999
This is a test
Word Count
A
B
C
D
A
A
B
C
C
D
D
D
```
- test with `sbt console`
```
~/.../scala/spark-stream-socket$ sbt console
scala> :paste

import org.apache.spark._
import org.apache.spark.streaming._
val conf = new SparkConf()
      .setAppName("Spark Streaming Example")
      .setMaster("local[*]")
      .set("spark.eventLog.enabled","true")
      .set("spark.eventLog.dir", "/tmp/spark-history")
val ssc = new StreamingContext(conf, Seconds(1))
val sc = ssc.sparkContext
val lines = ssc.socketTextStream("localhost", 9999)
val words = lines.flatMap(_.split(" "))
val pairs = words.map(word => (word, 1))
val wordCounts = pairs.reduceByKey(_ + _)
wordCounts.print()
ssc.start()
ssc.awaitTerminationOrTimeout(1000)
```

### 2021-09-18

- 看起來 Spark UI (:4040) 才有 Streaming Statistics。這些資訊沒有存在 History Server (:18080)
  - https://community.cloudera.com/t5/Support-Questions/HDP-2-6-Spark-2-1-Streaming-tab-not-available-in-the-Spark/td-p/230447
  - https://stackoverflow.com/questions/47780148/how-to-access-statistics-endpoint-for-a-spark-streaming-application
  - https://mallikarjuna_g.gitbooks.io/spark/content/spark-streaming/spark-streaming-webui.html
- Store Spark Streaming Metrics to influxdb
  - https://medium.com/analytics-vidhya/processing-time-series-data-in-real-time-with-influxdb-and-structured-streaming-d1864154cf8b
  - https://www.linkedin.com/pulse/monitoring-spark-streaming-influxdb-grafana-christian-g%C3%BCgi/
- Store Spark Streaming Metrics to Graphite
  - https://supergloo.com/spark-monitoring/spark-performance-monitoring/
  - https://ankur-singh1000.medium.com/spark-monitoring-with-graphite-telegraf-bc4a0149560b
- 