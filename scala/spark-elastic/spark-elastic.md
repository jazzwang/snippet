# README

[TOC]

# DEVELOPMENT NOTES

### 2021-03-24

#### Q: How to write data from Spark to ElasticSearch

- https://docs.databricks.com/data/data-sources/elasticsearch.html
  - ES-Hadoop - https://www.elastic.co/downloads/hadoop
  - https://search.maven.org/search?q=elasticsearch-spark
- https://medium.com/olivers-tech-blog/writing-a-spark-dataframe-to-an-elasticsearch-index-77a9de7dc3aa

#### Q: ELK 的 docker-compose YAML 檔？

- https://www.elastic.co/guide/en/elastic-stack-get-started/current/get-started-docker.html
- https://github.com/deviantony/docker-elk
- https://elk-docker.readthedocs.io/
  - https://hub.docker.com/r/sebp/elk/

#### Q: ELK 跑在 K8S 上？

- https://medium.com/@tharangarajapaksha/elk-stack-in-k8s-cluster-13bb509185e0

#### Q: 用 Logstash 從 S3 讀進 ElasticSearch

- https://geektechstuff.com/2020/07/17/aws-using-logstash-to-ingest-logs-from-s3-bucket-into-elastic/
- https://www.elastic.co/guide/en/logstash/current/plugins-inputs-s3.html

## 實作 Implementation

- ( 2021-03-24 14:36:43 )
```
~/git/snippet/scala$ sbt new jazzwang/scala-spark.g8
[info] Loading global plugins from /Users/jazzwang/.sbt/1.0/plugins
[info] Set current project to spark-elastic (in build file:/Users/jazzwang/git/snippet/scala/)
[info] Set current project to spark-elastic (in build file:/Users/jazzwang/git/snippet/scala/)

A minimal Apache Spark project in Scala

name [Scala Spark Project]: spark-elastic

Template applied in /Users/jazzwang/git/snippet/scala/./spark-elastic
```
- ( 2021-03-24 17:40:36 )
- https://github.com/ehsanyou/sbt-docker-compose
- https://github.com/Tapad/sbt-docker-compose
- ( 2021-03-24 18:21:08 )
```
:~$ docker search elastic
NAME                                 DESCRIPTION                                     STARS               OFFICIAL            AUTOMATED
elasticsearch                        Elasticsearch is a powerful open source se...   4914                [OK]
```