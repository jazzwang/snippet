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