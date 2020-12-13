# Development Notes

## 2020-12-11

- create project with `sbt --sbt-create`
```bash
~/git/snippet/scala$ mkdir -p hadoop-hdfs
~/git/snippet/scala$ cd hadoop-hdfs/
~/git/snippet/scala/hadoop-hdfs$ sbt --sbt-create
sbt:hadoop-hdfs> set libraryDependencies += "org.apache.hadoop" % "hadoop-client" % "2.7.4"
sbt:hadoop-hdfs> set libraryDependencies += "org.apache.hadoop" % "hadoop-hdfs" % "2.7.4"
sbt:hadoop-hdfs> update
sbt:hadoop-hdfs> session save
sbt:hadoop-hdfs> exit
~/git/snippet/scala/hadoop-hdfs$ cp ../spark-sample-etl/project/plugins.sbt project/
~/git/snippet/scala/hadoop-hdfs$ cp ../spark-sample-etl/Makefile .
~/git/snippet/scala/hadoop-hdfs$ git gi sbt,scala > .gitignore

```