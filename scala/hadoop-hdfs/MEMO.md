# Development Notes

## Initial Question

>  How can I switch HCFS location based on `HADOOP_CONF_DIR` environment variables?

## 2020-12-13

- ( 2020-12-13 13:02:08 )
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
~/git/snippet/scala/hadoop-hdfs$ git add .
~/git/snippet/scala/hadoop-hdfs$ git commit -a
~/git/snippet/scala/hadoop-hdfs$ git push
```

## 2020-12-22

- ( 2020-12-22 10:25:01 )
```bash
~/git/snippet/scala/hadoop-hdfs$ export HADOOP_CONF_DIR=$(pwd)/conf.pseudo/
~/git/snippet/scala/hadoop-hdfs$ sbt console

scala> import org.apache.hadoop.conf._
import org.apache.hadoop.conf._

scala> scala.sys.env.get("HADOOP_CONF_DIR")
res0: Option[String] = Some(/Users/jazzwang/git/snippet/scala/hadoop-hdfs/conf.pseudo/)

scala> val conf = new Configuration()
conf: org.apache.hadoop.conf.Configuration = Configuration: core-default.xml, core-site.xml

scala> conf.get("fs.default.name")
log4j:WARN No appenders could be found for logger (org.apache.hadoop.conf.Configuration.deprecation).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
res1: String = file:///
```
- ( 2020-12-22 10:50:32 )
- search `HADOOP_CONF_DIR` within Hadoop source code
- from [org.apache.hadoop.lib.service.hadoop.FileSystemAccessService.init()](https://github.com/apache/hadoop/blob/a89ca56a1b0eb949f56e7c6c5c25fdf87914a02f/hadoop-hdfs-project/hadoop-hdfs-httpfs/src/main/java/org/apache/hadoop/lib/service/hadoop/FileSystemAccessService.java#L182-L195)
```java
String hadoopConfDirProp = getServiceConfig().get(HADOOP_CONF_DIR, getServer().getConfigDir());
File hadoopConfDir = new File(hadoopConfDirProp).getAbsoluteFile();
... skipped ...
try {
      serviceHadoopConf = loadHadoopConf(hadoopConfDir);
```
- found [org.apache.hadoop.lib.service.hadoop.FileSystemAccessService.loadHadoopConf(File dir)](https://github.com/apache/hadoop/blob/a89ca56a1b0eb949f56e7c6c5c25fdf87914a02f/hadoop-hdfs-project/hadoop-hdfs-httpfs/src/main/java/org/apache/hadoop/lib/service/hadoop/FileSystemAccessService.java#L206-L215)
```java
  private Configuration loadHadoopConf(File dir) throws IOException {
    Configuration hadoopConf = new Configuration(false);
    for (String file : HADOOP_CONF_FILES) {
      File f = new File(dir, file);
      if (f.exists()) {
        hadoopConf.addResource(new Path(f.getAbsolutePath()));
      }
    }
    return hadoopConf;
  }
```
- [HADOOP_CONF_FILES](https://github.com/apache/hadoop/blob/a89ca56a1b0eb949f56e7c6c5c25fdf87914a02f/hadoop-hdfs-project/hadoop-hdfs-httpfs/src/main/java/org/apache/hadoop/lib/service/hadoop/FileSystemAccessService.java#L73) is a String array.
```java
  private static final String[] HADOOP_CONF_FILES = {"core-site.xml", "hdfs-site.xml"};
```
- It creates `Configuration` without loading default values. use `addResource(Path)` to load `core-site.xml` and `hdfs-site.xml` from specified directory.
- ( 2020-12-22 11:19:52 )
```bash
~/git/snippet/scala/hadoop-hdfs$ export HADOOP_CONF_DIR=$(pwd)/conf.pseudo/
~/git/snippet/scala/hadoop-hdfs$ sbt console

scala> import org.apache.hadoop.conf._
import org.apache.hadoop.conf._

scala> import java.io.File
import java.io.File

scala> import org.apache.hadoop.fs._

scala> val conf = new Configuration(false)
conf: org.apache.hadoop.conf.Configuration = Configuration:

scala> scala.sys.env.get("HADOOP_CONF_DIR")
res4: Option[String] = Some(/Users/jazzwang/git/snippet/scala/hadoop-hdfs/conf.pseudo/)

scala> System.getenv("HADOOP_CONF_DIR")
res10: String = /Users/jazzwang/git/snippet/scala/hadoop-hdfs/conf.pseudo/

scala> val f = new File(System.getenv("HADOOP_CONF_DIR"), "core-site.xml")
f: java.io.File = /Users/jazzwang/git/snippet/scala/hadoop-hdfs/conf.pseudo/core-site.xml

scala> f.exists
res11: Boolean = true

scala> conf.addResource(new Path(f.getAbsolutePath))

scala> conf.get("fs.default.name")
log4j:WARN No appenders could be found for logger (org.apache.hadoop.conf.Configuration.deprecation).
log4j:WARN Please initialize the log4j system properly.
log4j:WARN See http://logging.apache.org/log4j/1.2/faq.html#noconfig for more info.
res14: String = hdfs://localhost:9000
```
- ( 2020-12-22 11:45:43 )