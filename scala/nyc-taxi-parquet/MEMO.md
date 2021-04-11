- ( 2021-04-11 15:02:31 )
- initial project
```bash
~/git/snippet/scala$ sbt new jazzwang/scala-spark.g8
[info] Loading global plugins from /Users/jazzwang/.sbt/1.0/plugins
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)

A minimal Apache Spark project in Scala

name [Scala Spark Project]: NYC Taxi Parquet

Template applied in /Users/jazzwang/git/snippet/scala/./nyc-taxi-parquet
```
- add dependencies `scopt` to `build.sbt`
```diff
--- build.sbt.old	2021-04-11 15:06:21.000000000 +0800
+++ build.sbt	2021-04-11 15:06:08.000000000 +0800
@@ -10,6 +10,7 @@
       "org.apache.spark"  %%  "spark-core"    % "2.2.1",
       "org.apache.spark"  %%  "spark-sql"     % "2.2.1",
       "org.scalatest"     %%  "scalatest"     % "3.1.1",
+      "com.github.scopt"  %%  "scopt"         % "4.0.0"
     )
   )
```
- reference [${spark}/examples/src/main/scala/org/apache/spark/examples/ml/DataFrameExample.scala](https://github.com/apache/spark/blob/0494dc90af48ce7da0625485a4dc6917a244d580/examples/src/main/scala/org/apache/spark/examples/ml/DataFrameExample.scala)