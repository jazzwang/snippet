# MEMO

## 2020-08-11

- Spark SQL 的 SparkContext / SparkConfig 不能跟 Spark Streaming 混用。
```
scala> val conf = sc.getConf
scala> val ssc = new StreamingContext(conf, Seconds(1))
org.apache.spark.SparkException: Only one SparkContext may be running in this JVM (see SPARK-2243). To ignore this error, set spark.driver.allowMultipleContexts = true. The currently running SparkContext was created at:
org.apache.spark.sql.SparkSession$Builder.getOrCreate(SparkSession.scala:910)
org.apache.spark.repl.Main$.createSparkSession(Main.scala:101)
<init>(<console>:15)
<init>(<console>:42)
<init>(<console>:44)
.<init>(<console>:48)
.<clinit>(<console>)
.$print$lzycompute(<console>:7)
.$print(<console>:6)
$print(<console>)
sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
java.lang.reflect.Method.invoke(Method.java:498)
scala.tools.nsc.interpreter.IMain$ReadEvalPrint.call(IMain.scala:786)
scala.tools.nsc.interpreter.IMain$Request.loadAndRun(IMain.scala:1047)
scala.tools.nsc.interpreter.IMain$WrappedRequest$$anonfun$loadAndRunReq$1.apply(IMain.scala:638)
scala.tools.nsc.interpreter.IMain$WrappedRequest$$anonfun$loadAndRunReq$1.apply(IMain.scala:637)
scala.reflect.internal.util.ScalaClassLoader$class.asContext(ScalaClassLoader.scala:31)
scala.reflect.internal.util.AbstractFileClassLoader.asContext(AbstractFileClassLoader.scala:19)
  at org.apache.spark.SparkContext$$anonfun$assertNoOtherContextIsRunning$2.apply(SparkContext.scala:2479)
  at org.apache.spark.SparkContext$$anonfun$assertNoOtherContextIsRunning$2.apply(SparkContext.scala:2475)
  at scala.Option.foreach(Option.scala:257)
  at org.apache.spark.SparkContext$.assertNoOtherContextIsRunning(SparkContext.scala:2475)
  at org.apache.spark.SparkContext$.markPartiallyConstructed(SparkContext.scala:2564)
  at org.apache.spark.SparkContext.<init>(SparkContext.scala:85)
  at org.apache.spark.streaming.StreamingContext$.createNewSparkContext(StreamingContext.scala:839)
  at org.apache.spark.streaming.StreamingContext.<init>(StreamingContext.scala:85)
  ... 50 elided
```
- 解法：在 `spark-shell` 裡，把預設的 Spark SQL 產生的 `SparkContext` 停掉，再產生 `StreamingContext` 物件
```
scala> sc.stop()

scala> val ssc = new StreamingContext(conf, Seconds(1)
ssc: org.apache.spark.streaming.StreamingContext = org.apache.spark.streaming.StreamingContext@624a9068

scala> val sc = ssc.sparkContext
sc: org.apache.spark.SparkContext = org.apache.spark.SparkContext@662c5207
```

- 觀察二：在 `input` 目錄中，預先放了純文字檔案，當執行 `ssc.start()` 時，並不會去讀取該檔案。
反而是目錄內容 `有新檔案` 或者 `檔案內容有異動` 的時候才讀取。

## 2021-09-17

* 改用 Scala `2.12.10` 搭配 Spark `3.0.0`
* https://mvnrepository.com/artifact/org.apache.spark/spark-streaming_2.12/3.0.0
```
jazz.wang@cloudshell:~/snippet/scala/spark-stream-file-io $ sbt distclean
[info] Loading project definition from /home/jazz.wang/snippet/scala/spark-stream-file-io/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to spark-stream-file-io (in build file:/home/jazz.wang/snippet/scala/spark-stream-file-io/)
[success] Total time: 0 s, completed Sep 17, 2021, 8:37:59 AM
jazz.wang@cloudshell:~/snippet/scala/spark-stream-file-io $ sbt run
[info] Loading project definition from /home/jazz.wang/snippet/scala/spark-stream-file-io/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to spark-stream-file-io (in build file:/home/jazz.wang/snippet/scala/spark-stream-file-io/)
[warn] There may be incompatibilities among your library dependencies; run 'evicted' to see detailed eviction warnings.
[info] Compiling 1 Scala source to /home/jazz.wang/snippet/scala/spark-stream-file-io/target/scala-2.12/classes ...
[warn] there was one deprecation warning; re-run with -deprecation for details
[warn] one warning found
[info] running example.Hello
hello
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/tmp/sbt_c3f18ca1/target/331d271f/255e2aee/spark-unsafe_2.12-3.0.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
start Spark Streaming Context
-------------------------------------------
Time: 1631867921000 ms
-------------------------------------------

-------------------------------------------
Time: 1631867922000 ms
-------------------------------------------

create 'new-file.txt'
-------------------------------------------
Time: 1631867923000 ms
-------------------------------------------
(STREAMING,1)
(SPARK,1)
(INPUT,1)
(DATA,1)

-------------------------------------------
Time: 1631867924000 ms
-------------------------------------------

[success] Total time: 12 s, completed Sep 17, 2021, 8:38:44 AM
jazz.wang@cloudshell:~/snippet/scala/spark-stream-file-io $
```