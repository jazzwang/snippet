# 2020-11-10

[TOC]

## 動機 WHY

- Spark SQL 不支援 UPDATE 跟 DELETE，當然跟底層的 Storage Format 有關。
    - 像 `Parquet` 就不容易做 UPDATE 跟 DELETE。
- 而 Hive 要支援 Transaction 才支援 UPDATE 跟 DELETE，格式必須是 `ORC`
- 如何讓 Spark SQL 也可以支援 UPDATE 跟 DELETE 呢？近期聽到可以用 Delta Lake，所以來跑看看它的 Quick Start

## 參考 REFERENCE

- https://github.com/delta-io/delta
- https://docs.delta.io/latest/quick-start.html
- https://docs.databricks.com/delta/delta-intro.html
- https://stackoverflow.com/questions/37517371/update-query-in-spark-sql

## 實作 Implementation

### 測試方法一：用 `spark-shell`

- 由於我手邊的環境用的是 Scala `2.11` 的 Spark `2.2.1` 版本，所以只能用 `0.6.1` 的舊版本

- 從 https://search.maven.org/artifact/io.delta/delta-core_2.11/0.6.1/jar 的相依性看起來，至少要 Spark `2.4.2`

```xml
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>2.4.2</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-sql_2.11</artifactId>
            <version>2.4.2</version>
            <scope>test</scope>
            <classifier>tests</classifier>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-hive_2.11</artifactId>
            <version>2.4.2</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.4.2</version>
            <scope>provided</scope>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-core_2.11</artifactId>
            <version>2.4.2</version>
            <scope>test</scope>
            <classifier>tests</classifier>
        </dependency>
        <dependency>
            <groupId>org.apache.spark</groupId>
            <artifactId>spark-catalyst_2.11</artifactId>
            <version>2.4.2</version>
            <scope>provided</scope>
        </dependency>
```

- 難怪用以下指令跑的時候，Spark 2.2.1 會有 Class 找不到的錯誤訊息。

```bash
~$ spark-shell --packages io.delta:delta-core_2.11:0.6.1 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```

- 同樣的指令使用 Spark `2.4.5` 就沒問題，可以跑完 quick start 的範例指令

```
λ spark-shell --packages io.delta:delta-core_2.11:0.6.1 --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
Ivy Default Cache set to: C:\Users\yawang\.ivy2\cache
The jars for the packages stored in: C:\Users\yawang\.ivy2\jars
:: loading settings :: url = jar:file:/E:/writable/scoop/apps/spark/current/jars/ivy-2.4.0.jar!/org/apache/ivy/core/settings/ivysettings.xml
io.delta#delta-core_2.11 added as a dependency
:: resolving dependencies :: org.apache.spark#spark-submit-parent-32070317-df83-400f-8589-07d02f2341d0;1.0
        confs: [default]
        found io.delta#delta-core_2.11;0.6.1 in spark-list
        found org.antlr#antlr4;4.7 in spark-list
        found org.antlr#antlr4-runtime;4.7 in spark-list
        found org.antlr#antlr-runtime;3.5.2 in spark-list
        found org.antlr#ST4;4.0.8 in spark-list
        found org.abego.treelayout#org.abego.treelayout.core;1.0.3 in spark-list
        found org.glassfish#javax.json;1.0.4 in spark-list
        found com.ibm.icu#icu4j;58.2 in spark-list
:: resolution report :: resolve 1345ms :: artifacts dl 65ms
        :: modules in use:
        com.ibm.icu#icu4j;58.2 from spark-list in [default]
        io.delta#delta-core_2.11;0.6.1 from spark-list in [default]
        org.abego.treelayout#org.abego.treelayout.core;1.0.3 from spark-list in [default]
        org.antlr#ST4;4.0.8 from spark-list in [default]
        org.antlr#antlr-runtime;3.5.2 from spark-list in [default]
        org.antlr#antlr4;4.7 from spark-list in [default]
        org.antlr#antlr4-runtime;4.7 from spark-list in [default]
        org.glassfish#javax.json;1.0.4 from spark-list in [default]
        ---------------------------------------------------------------------
        |                  |            modules            ||   artifacts   |
        |       conf       | number| search|dwnlded|evicted|| number|dwnlded|
        ---------------------------------------------------------------------
        |      default     |   8   |   0   |   0   |   0   ||   8   |   0   |
        ---------------------------------------------------------------------

:: problems summary ::
:::: ERRORS
        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null

        unknown resolver sbt-chain

        unknown resolver null


:: USE VERBOSE OR DEBUG MESSAGE LEVEL FOR MORE DETAILS
:: retrieving :: org.apache.spark#spark-submit-parent-32070317-df83-400f-8589-07d02f2341d0
        confs: [default]
        8 artifacts copied, 0 already retrieved (15686kB/2312ms)
20/11/10 15:59:14 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Using Spark's default log4j profile: org/apache/spark/log4j-defaults.properties
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://vheAEnSTDs01021.na.webmd.net:4040
Spark context available as 'sc' (master = local[*], app id = local-1604995165946).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.5
      /_/

Using Scala version 2.11.12 (Java HotSpot(TM) Client VM, Java 1.8.0_261)
Type in expressions to have them evaluated.
Type :help for more information.

scala> val data = spark.range(0, 5)
data: org.apache.spark.sql.Dataset[Long] = [id: bigint]

scala> data.write.format("delta").save("/tmp/delta-table")
20/11/10 16:00:26 WARN SizeEstimator: Failed to check whether UseCompressedOops is set; assuming yes

scala> val df = spark.read.format("delta").load("/tmp/delta-table")
df: org.apache.spark.sql.DataFrame = [id: bigint]

scala> df.show()
+---+
| id|
+---+
|  2|
|  3|
|  4|
|  0|
|  1|
+---+


scala> val data = spark.range(5, 10)
data: org.apache.spark.sql.Dataset[Long] = [id: bigint]

scala> data.write.format("delta").mode("overwrite").save("/tmp/delta-table")

scala> df.show()
+---+
| id|
+---+
|  7|
|  8|
|  9|
|  5|
|  6|
+---+

scala> import io.delta.tables._
import io.delta.tables._

scala> import org.apache.spark.sql.functions._
import org.apache.spark.sql.functions._

scala> val deltaTable = DeltaTable.forPath("/tmp/delta-table")
deltaTable: io.delta.tables.DeltaTable = io.delta.tables.DeltaTable@11fd261

scala>

scala> // Update every even value by adding 100 to it

scala> deltaTable.update(
     |   condition = expr("id % 2 == 0"),
     |   set = Map("id" -> expr("id + 100")))

scala> df.show()
+---+
| id|
+---+
|  7|
|108|
|  9|
|  5|
|106|
+---+

scala> // Delete every even value

scala> deltaTable.delete(condition = expr("id % 2 == 0"))

scala> df.show()
+---+
| id|
+---+
|  7|
|  9|
|  5|
+---+

scala> // Upsert (merge) new data

scala> val newData = spark.range(0, 20).toDF
newData: org.apache.spark.sql.DataFrame = [id: bigint]

scala>

scala> deltaTable.as("oldData").merge(newData.as("newData"),"oldData.id = newData.id").whenMatched.update(Map("id" -> col("newData.id"))).whenNotMatched.insert(Map("id" -> col("newData.id"))).execute()

scala> df.show()
+---+
| id|
+---+
| 11|
| 16|
|  9|
|  4|
|  5|
| 12|
| 13|
| 17|
| 15|
| 14|
|  1|
| 10|
|  0|
|  6|
| 18|
|  7|
|  2|
|  3|
| 19|
|  8|
+---+
```



## 底層

- **What format does Delta Lake use to store data?**
    - Delta Lake uses <mark>versioned Parquet files</mark> to store your data in your cloud storage. Apart from the versions, Delta Lake also stores a <mark>transaction log</mark> to keep track of all the commits made to the table or blob store directory to provide ACID transactions.

- 觀察 `/tmp/delta-table` 的檔案內容

```
/c/tmp/delta-table$ ls -alR
.:
total 106
drwxr-xr-x 1 jazzwang 1073742337   0 Nov 10 16:25 .
drwxr-xr-x 1 jazzwang 1073742337   0 Nov 10 16:00 ..
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:02 .part-00000-1e977e2f-0287-46f5-a74d-a8328762dc35-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:19 .part-00000-20b2f3ee-c026-4e85-95d4-a4975261e918-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00000-488e326e-5d6a-4050-9ef1-e3dc0f68b460-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:00 .part-00000-6cc373fb-ee2b-40ca-a5d9-b118db7628e1-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:17 .part-00000-70d01d4c-9208-4d69-baaf-43c14ed50426-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:17 .part-00001-59ffd7ab-79e0-47c6-b8f0-ce740f9f754a-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:02 .part-00001-a4a49dc5-28b6-468d-b6c7-4b0321b90fae-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:19 .part-00001-b421c978-7b2c-435a-bf6a-9428bcaadf23-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:00 .part-00001-e932d336-c60b-4b18-8b87-d21edbfb682c-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00004-da22fbc6-e761-41df-a8b6-fb35d9e02d2f-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00005-f18f00d5-4f1d-4b25-96c5-3940637390f5-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00011-06c32145-bc82-4ae6-a7f5-7162db9d69bd-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00045-f7c9ef02-8625-4494-8121-3b3144d25b6a-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00049-487daf02-5baf-4827-bfee-006f99b1ce99-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00058-3479f1bd-53a9-4237-bdac-0811f1e1c145-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00068-cd930e1a-6845-4857-a75e-b2994d2fa989-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00069-e03c4d38-0731-41fd-b701-0d47bdabb766-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00077-d07224e0-89b2-4189-9ee9-23efe13311a6-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00107-eac8f609-187d-40b2-add3-cfbf69c155bd-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00112-08782934-5de3-41db-8ec6-a9897a7d70fc-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:24 .part-00116-ce2ce9ca-b3c8-438e-815a-e65f7348a591-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00121-ec51ded4-4b12-4c4b-be80-7173e53525b2-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00128-3a212e1e-c770-4a3b-8e98-71fb9299c060-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00140-f4ba2e9e-7aba-4300-8c52-d1a66479b6a4-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00143-48dad918-ef17-4586-915a-93be5efc7253-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00150-1a07f643-f29b-4dd4-98fb-8ac7b0c27be1-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00154-1469d30e-0444-4b47-878b-a3cb48e11ca6-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00164-d051412a-4cad-4906-852f-f38c667ab6df-c000.snappy.parquet.crc
-rw-r--r-- 1 jazzwang 1073742337  12 Nov 10 16:25 .part-00190-2aab25e3-54d9-4fe4-ad28-4ce28fb0e8ea-c000.snappy.parquet.crc
drwxr-xr-x 1 jazzwang 1073742337   0 Nov 10 16:25 _delta_log
-rw-r--r-- 1 jazzwang 1073742337 437 Nov 10 16:02 part-00000-1e977e2f-0287-46f5-a74d-a8328762dc35-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 437 Nov 10 16:19 part-00000-20b2f3ee-c026-4e85-95d4-a4975261e918-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 262 Nov 10 16:24 part-00000-488e326e-5d6a-4050-9ef1-e3dc0f68b460-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 437 Nov 10 16:00 part-00000-6cc373fb-ee2b-40ca-a5d9-b118db7628e1-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 442 Nov 10 16:17 part-00000-70d01d4c-9208-4d69-baaf-43c14ed50426-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 437 Nov 10 16:17 part-00001-59ffd7ab-79e0-47c6-b8f0-ce740f9f754a-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 442 Nov 10 16:02 part-00001-a4a49dc5-28b6-468d-b6c7-4b0321b90fae-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:19 part-00001-b421c978-7b2c-435a-bf6a-9428bcaadf23-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 442 Nov 10 16:00 part-00001-e932d336-c60b-4b18-8b87-d21edbfb682c-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00004-da22fbc6-e761-41df-a8b6-fb35d9e02d2f-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00005-f18f00d5-4f1d-4b25-96c5-3940637390f5-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00011-06c32145-bc82-4ae6-a7f5-7162db9d69bd-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00045-f7c9ef02-8625-4494-8121-3b3144d25b6a-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00049-487daf02-5baf-4827-bfee-006f99b1ce99-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00058-3479f1bd-53a9-4237-bdac-0811f1e1c145-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00068-cd930e1a-6845-4857-a75e-b2994d2fa989-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00069-e03c4d38-0731-41fd-b701-0d47bdabb766-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00077-d07224e0-89b2-4189-9ee9-23efe13311a6-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00107-eac8f609-187d-40b2-add3-cfbf69c155bd-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00112-08782934-5de3-41db-8ec6-a9897a7d70fc-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:24 part-00116-ce2ce9ca-b3c8-438e-815a-e65f7348a591-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00121-ec51ded4-4b12-4c4b-be80-7173e53525b2-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00128-3a212e1e-c770-4a3b-8e98-71fb9299c060-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00140-f4ba2e9e-7aba-4300-8c52-d1a66479b6a4-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00143-48dad918-ef17-4586-915a-93be5efc7253-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00150-1a07f643-f29b-4dd4-98fb-8ac7b0c27be1-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00154-1469d30e-0444-4b47-878b-a3cb48e11ca6-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00164-d051412a-4cad-4906-852f-f38c667ab6df-c000.snappy.parquet
-rw-r--r-- 1 jazzwang 1073742337 429 Nov 10 16:25 part-00190-2aab25e3-54d9-4fe4-ad28-4ce28fb0e8ea-c000.snappy.parquet

./_delta_log:
total 68
drwxr-xr-x 1 jazzwang 1073742337    0 Nov 10 16:25 .
drwxr-xr-x 1 jazzwang 1073742337    0 Nov 10 16:25 ..
-rw-r--r-- 1 jazzwang 1073742337  921 Nov 10 16:00 00000000000000000000.json
-rw-r--r-- 1 jazzwang 1073742337  866 Nov 10 16:02 00000000000000000001.json
-rw-r--r-- 1 jazzwang 1073742337  920 Nov 10 16:17 00000000000000000002.json
-rw-r--r-- 1 jazzwang 1073742337  923 Nov 10 16:19 00000000000000000003.json
-rw-r--r-- 1 jazzwang 1073742337 4250 Nov 10 16:25 00000000000000000004.json

/c/tmp/delta-table$ cat _delta_log/00000000000000000000.json
{"commitInfo":{"timestamp":1604995236122,"operation":"WRITE","operationParameters":{"mode":"ErrorIfExists","partitionBy":"[]"},"isBlindAppend":true,"operationMetrics":{"numFiles":"2","numOutputBytes":"879","numOutputRows":"5"}}}
{"protocol":{"minReaderVersion":1,"minWriterVersion":2}}
{"metaData":{"id":"1da275b2-558a-4ce4-a909-d27665ee6c3a","format":{"provider":"parquet","options":{}},"schemaString":"{\"type\":\"struct\",\"fields\":[{\"name\":\"id\",\"type\":\"long\",\"nullable\":true,\"metadata\":{}}]}","partitionColumns":[],"configuration":{},"createdTime":1604995223476}}
{"add":{"path":"part-00000-6cc373fb-ee2b-40ca-a5d9-b118db7628e1-c000.snappy.parquet","partitionValues":{},"size":437,"modificationTime":1604995235353,"dataChange":true}}
{"add":{"path":"part-00001-e932d336-c60b-4b18-8b87-d21edbfb682c-c000.snappy.parquet","partitionValues":{},"size":442,"modificationTime":1604995235350,"dataChange":true}}

/c/tmp/delta-table$ cat _delta_log/00000000000000000001.json
{"commitInfo":{"timestamp":1604995332618,"operation":"WRITE","operationParameters":{"mode":"Overwrite","partitionBy":"[]"},"readVersion":0,"isBlindAppend":false,"operationMetrics":{"numFiles":"2","numOutputBytes":"879","numOutputRows":"5"}}}
{"add":{"path":"part-00000-1e977e2f-0287-46f5-a74d-a8328762dc35-c000.snappy.parquet","partitionValues":{},"size":437,"modificationTime":1604995331661,"dataChange":true}}
{"add":{"path":"part-00001-a4a49dc5-28b6-468d-b6c7-4b0321b90fae-c000.snappy.parquet","partitionValues":{},"size":442,"modificationTime":1604995331704,"dataChange":true}}
{"remove":{"path":"part-00001-e932d336-c60b-4b18-8b87-d21edbfb682c-c000.snappy.parquet","deletionTimestamp":1604995332617,"dataChange":true}}
{"remove":{"path":"part-00000-6cc373fb-ee2b-40ca-a5d9-b118db7628e1-c000.snappy.parquet","deletionTimestamp":1604995332618,"dataChange":true}}

/c/tmp/delta-table$ cat _delta_log/00000000000000000002.json
{"commitInfo":{"timestamp":1604996277298,"operation":"UPDATE","operationParameters":{"predicate":"((id#357L % cast(2 as bigint)) = cast(0 as bigint))"},"readVersion":1,"isBlindAppend":false,"operationMetrics":{"numRemovedFiles":"2","numAddedFiles":"2","numUpdatedRows":"2","numCopiedRows":"3"}}}
{"remove":{"path":"part-00000-1e977e2f-0287-46f5-a74d-a8328762dc35-c000.snappy.parquet","deletionTimestamp":1604996275992,"dataChange":true}}
{"remove":{"path":"part-00001-a4a49dc5-28b6-468d-b6c7-4b0321b90fae-c000.snappy.parquet","deletionTimestamp":1604996275992,"dataChange":true}}
{"add":{"path":"part-00000-70d01d4c-9208-4d69-baaf-43c14ed50426-c000.snappy.parquet","partitionValues":{},"size":442,"modificationTime":1604996277234,"dataChange":true}}
{"add":{"path":"part-00001-59ffd7ab-79e0-47c6-b8f0-ce740f9f754a-c000.snappy.parquet","partitionValues":{},"size":437,"modificationTime":1604996277222,"dataChange":true}}

/c/tmp/delta-table$ cat _delta_log/00000000000000000003.json
{"commitInfo":{"timestamp":1604996359429,"operation":"DELETE","operationParameters":{"predicate":"[\"((`id` % CAST(2 AS BIGINT)) = CAST(0 AS BIGINT))\"]"},"readVersion":2,"isBlindAppend":false,"operationMetrics":{"numRemovedFiles":"2","numDeletedRows":"2","numAddedFiles":"2","numCopiedRows":"3"}}}
{"remove":{"path":"part-00000-70d01d4c-9208-4d69-baaf-43c14ed50426-c000.snappy.parquet","deletionTimestamp":1604996359424,"dataChange":true}}
{"remove":{"path":"part-00001-59ffd7ab-79e0-47c6-b8f0-ce740f9f754a-c000.snappy.parquet","deletionTimestamp":1604996359424,"dataChange":true}}
{"add":{"path":"part-00000-20b2f3ee-c026-4e85-95d4-a4975261e918-c000.snappy.parquet","partitionValues":{},"size":437,"modificationTime":1604996359406,"dataChange":true}}
{"add":{"path":"part-00001-b421c978-7b2c-435a-bf6a-9428bcaadf23-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996359403,"dataChange":true}}

:/c/tmp/delta-table$ cat _delta_log/00000000000000000004.json
{"commitInfo":{"timestamp":1604996702388,"operation":"MERGE","operationParameters":{"predicate":"(oldData.`id` = newData.`id`)"},"readVersion":3,"isBlindAppend":false,"operationMetrics":{"numTargetRowsCopied":"0","numTargetRowsDeleted":"0","numTargetFilesAdded":"21","numTargetRowsInserted":"17","numTargetRowsUpdated":"3","numOutputRows":"20","numSourceRows":"20","numTargetFilesRemoved":"2"}}}
{"remove":{"path":"part-00000-20b2f3ee-c026-4e85-95d4-a4975261e918-c000.snappy.parquet","deletionTimestamp":1604996702365,"dataChange":true}}
{"remove":{"path":"part-00001-b421c978-7b2c-435a-bf6a-9428bcaadf23-c000.snappy.parquet","deletionTimestamp":1604996702388,"dataChange":true}}
{"add":{"path":"part-00000-488e326e-5d6a-4050-9ef1-e3dc0f68b460-c000.snappy.parquet","partitionValues":{},"size":262,"modificationTime":1604996692483,"dataChange":true}}
{"add":{"path":"part-00004-da22fbc6-e761-41df-a8b6-fb35d9e02d2f-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996696082,"dataChange":true}}
{"add":{"path":"part-00005-f18f00d5-4f1d-4b25-96c5-3940637390f5-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996696078,"dataChange":true}}
{"add":{"path":"part-00011-06c32145-bc82-4ae6-a7f5-7162db9d69bd-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996696832,"dataChange":true}}
{"add":{"path":"part-00045-f7c9ef02-8625-4494-8121-3b3144d25b6a-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996696849,"dataChange":true}}
{"add":{"path":"part-00049-487daf02-5baf-4827-bfee-006f99b1ce99-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996697495,"dataChange":true}}
{"add":{"path":"part-00058-3479f1bd-53a9-4237-bdac-0811f1e1c145-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996697521,"dataChange":true}}
{"add":{"path":"part-00068-cd930e1a-6845-4857-a75e-b2994d2fa989-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996698171,"dataChange":true}}
{"add":{"path":"part-00069-e03c4d38-0731-41fd-b701-0d47bdabb766-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996698241,"dataChange":true}}
{"add":{"path":"part-00077-d07224e0-89b2-4189-9ee9-23efe13311a6-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996698824,"dataChange":true}}
{"add":{"path":"part-00107-eac8f609-187d-40b2-add3-cfbf69c155bd-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996698939,"dataChange":true}}
{"add":{"path":"part-00112-08782934-5de3-41db-8ec6-a9897a7d70fc-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996699517,"dataChange":true}}
{"add":{"path":"part-00116-ce2ce9ca-b3c8-438e-815a-e65f7348a591-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996699651,"dataChange":true}}
{"add":{"path":"part-00121-ec51ded4-4b12-4c4b-be80-7173e53525b2-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996700196,"dataChange":true}}
{"add":{"path":"part-00128-3a212e1e-c770-4a3b-8e98-71fb9299c060-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996700314,"dataChange":true}}
{"add":{"path":"part-00140-f4ba2e9e-7aba-4300-8c52-d1a66479b6a4-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996700849,"dataChange":true}}
{"add":{"path":"part-00143-48dad918-ef17-4586-915a-93be5efc7253-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996700977,"dataChange":true}}
{"add":{"path":"part-00150-1a07f643-f29b-4dd4-98fb-8ac7b0c27be1-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996701512,"dataChange":true}}
{"add":{"path":"part-00154-1469d30e-0444-4b47-878b-a3cb48e11ca6-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996701645,"dataChange":true}}
{"add":{"path":"part-00164-d051412a-4cad-4906-852f-f38c667ab6df-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996702247,"dataChange":true}}
{"add":{"path":"part-00190-2aab25e3-54d9-4fe4-ad28-4ce28fb0e8ea-c000.snappy.parquet","partitionValues":{},"size":429,"modificationTime":1604996702342,"dataChange":true}}
```

### 測試方法二：用 `SBT`

- 產生 spark-delta-lake 專案
```
jazzwang:~/git/snippet/scala$ sbt new jazzwang/scala-spark.g8
A minimal Apache Spark project in Scala 

name [Scala Spark Project]: spark-delta-lake

Template applied in /Users/jazzwang/git/snippet/scala/./spark-delta-lake
```
- 編輯 `build.sbt` 跟 `src/main/scala/example/Hello.scala`
    - 參考 https://docs.delta.io/latest/quick-start.html#language-scala
- 編譯並執行 `sbt run`
```bash
jazzwang:~/git/snippet/scala/spark-delta-lake$ sbt run
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/spark-delta-lake/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to Delta Lake Test (in build file:/Users/jazzwang/git/snippet/scala/spark-delta-lake/)
[info] Compiling 1 Scala source to /Users/jazzwang/git/snippet/scala/spark-delta-lake/target/scala-2.11/classes ...
[info] running example.Hello 
hello
+---+
| id|
+---+
|  3|
|  4|
|  0|
|  1|
|  2|
+---+

+---+
| id|
+---+
|  8|
|  9|
|  5|
|  6|
|  7|
+---+

+---+
| id|
+---+
|108|
|  9|
|  5|
|106|
|  7|
+---+

+---+
| id|
+---+
|  5|
|  9|
|  7|
+---+

20/11/10 17:22:15 ERROR AsyncEventQueue: Listener EventLoggingListener threw an exception
java.lang.ClassCastException: java.util.Collections$SynchronizedSet cannot be cast to java.util.List
	at org.apache.spark.util.JsonProtocol$.accumValueToJson(JsonProtocol.scala:330)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at scala.Option.map(Option.scala:146)
	at org.apache.spark.util.JsonProtocol$.accumulableInfoToJson(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at scala.collection.immutable.List.map(List.scala:288)
	at org.apache.spark.util.JsonProtocol$.accumulablesToJson(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$.taskInfoToJson(JsonProtocol.scala:291)
	at org.apache.spark.util.JsonProtocol$.taskEndToJson(JsonProtocol.scala:145)
	at org.apache.spark.util.JsonProtocol$.sparkEventToJson(JsonProtocol.scala:76)
	at org.apache.spark.scheduler.EventLoggingListener.logEvent(EventLoggingListener.scala:138)
	at org.apache.spark.scheduler.EventLoggingListener.onTaskEnd(EventLoggingListener.scala:158)
	at org.apache.spark.scheduler.SparkListenerBus$class.doPostEvent(SparkListenerBus.scala:45)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.util.ListenerBus$class.postToAll(ListenerBus.scala:91)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$super$postToAll(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply$mcJ$sp(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at scala.util.DynamicVariable.withValue(DynamicVariable.scala:58)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$dispatch(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1$$anonfun$run$1.apply$mcV$sp(AsyncEventQueue.scala:83)
	at org.apache.spark.util.Utils$.tryOrStopSparkContext(Utils.scala:1302)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1.run(AsyncEventQueue.scala:82)
20/11/10 17:22:15 ERROR AsyncEventQueue: Listener EventLoggingListener threw an exception
java.lang.ClassCastException: java.util.Collections$SynchronizedSet cannot be cast to java.util.List
	at org.apache.spark.util.JsonProtocol$.accumValueToJson(JsonProtocol.scala:330)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at scala.Option.map(Option.scala:146)
	at org.apache.spark.util.JsonProtocol$.accumulableInfoToJson(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at scala.collection.immutable.List.map(List.scala:288)
	at org.apache.spark.util.JsonProtocol$.accumulablesToJson(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$.taskInfoToJson(JsonProtocol.scala:291)
	at org.apache.spark.util.JsonProtocol$.taskEndToJson(JsonProtocol.scala:145)
	at org.apache.spark.util.JsonProtocol$.sparkEventToJson(JsonProtocol.scala:76)
	at org.apache.spark.scheduler.EventLoggingListener.logEvent(EventLoggingListener.scala:138)
	at org.apache.spark.scheduler.EventLoggingListener.onTaskEnd(EventLoggingListener.scala:158)
	at org.apache.spark.scheduler.SparkListenerBus$class.doPostEvent(SparkListenerBus.scala:45)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.util.ListenerBus$class.postToAll(ListenerBus.scala:91)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$super$postToAll(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply$mcJ$sp(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at scala.util.DynamicVariable.withValue(DynamicVariable.scala:58)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$dispatch(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1$$anonfun$run$1.apply$mcV$sp(AsyncEventQueue.scala:83)
	at org.apache.spark.util.Utils$.tryOrStopSparkContext(Utils.scala:1302)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1.run(AsyncEventQueue.scala:82)
20/11/10 17:22:15 ERROR AsyncEventQueue: Listener EventLoggingListener threw an exception
java.lang.ClassCastException: java.util.Collections$SynchronizedSet cannot be cast to java.util.List
	at org.apache.spark.util.JsonProtocol$.accumValueToJson(JsonProtocol.scala:330)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$3.apply(JsonProtocol.scala:306)
	at scala.Option.map(Option.scala:146)
	at org.apache.spark.util.JsonProtocol$.accumulableInfoToJson(JsonProtocol.scala:306)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at scala.collection.immutable.List.map(List.scala:288)
	at org.apache.spark.util.JsonProtocol$.accumulablesToJson(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$.taskInfoToJson(JsonProtocol.scala:291)
	at org.apache.spark.util.JsonProtocol$.taskEndToJson(JsonProtocol.scala:145)
	at org.apache.spark.util.JsonProtocol$.sparkEventToJson(JsonProtocol.scala:76)
	at org.apache.spark.scheduler.EventLoggingListener.logEvent(EventLoggingListener.scala:138)
	at org.apache.spark.scheduler.EventLoggingListener.onTaskEnd(EventLoggingListener.scala:158)
	at org.apache.spark.scheduler.SparkListenerBus$class.doPostEvent(SparkListenerBus.scala:45)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.util.ListenerBus$class.postToAll(ListenerBus.scala:91)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$super$postToAll(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply$mcJ$sp(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at scala.util.DynamicVariable.withValue(DynamicVariable.scala:58)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$dispatch(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1$$anonfun$run$1.apply$mcV$sp(AsyncEventQueue.scala:83)
	at org.apache.spark.util.Utils$.tryOrStopSparkContext(Utils.scala:1302)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1.run(AsyncEventQueue.scala:82)
20/11/10 17:22:15 ERROR AsyncEventQueue: Listener EventLoggingListener threw an exception
java.lang.ClassCastException: java.util.Collections$SynchronizedSet cannot be cast to java.util.List
	at org.apache.spark.util.JsonProtocol$.accumValueToJson(JsonProtocol.scala:330)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$5.apply(JsonProtocol.scala:307)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulableInfoToJson$5.apply(JsonProtocol.scala:307)
	at scala.Option.map(Option.scala:146)
	at org.apache.spark.util.JsonProtocol$.accumulableInfoToJson(JsonProtocol.scala:307)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$$anonfun$accumulablesToJson$2.apply(JsonProtocol.scala:299)
	at scala.collection.immutable.List.map(List.scala:288)
	at org.apache.spark.util.JsonProtocol$.accumulablesToJson(JsonProtocol.scala:299)
	at org.apache.spark.util.JsonProtocol$.stageInfoToJson(JsonProtocol.scala:275)
	at org.apache.spark.util.JsonProtocol$.stageCompletedToJson(JsonProtocol.scala:116)
	at org.apache.spark.util.JsonProtocol$.sparkEventToJson(JsonProtocol.scala:70)
	at org.apache.spark.scheduler.EventLoggingListener.logEvent(EventLoggingListener.scala:138)
	at org.apache.spark.scheduler.EventLoggingListener.onStageCompleted(EventLoggingListener.scala:166)
	at org.apache.spark.scheduler.SparkListenerBus$class.doPostEvent(SparkListenerBus.scala:35)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.scheduler.AsyncEventQueue.doPostEvent(AsyncEventQueue.scala:37)
	at org.apache.spark.util.ListenerBus$class.postToAll(ListenerBus.scala:91)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$super$postToAll(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply$mcJ$sp(AsyncEventQueue.scala:92)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anonfun$org$apache$spark$scheduler$AsyncEventQueue$$dispatch$1.apply(AsyncEventQueue.scala:87)
	at scala.util.DynamicVariable.withValue(DynamicVariable.scala:58)
	at org.apache.spark.scheduler.AsyncEventQueue.org$apache$spark$scheduler$AsyncEventQueue$$dispatch(AsyncEventQueue.scala:87)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1$$anonfun$run$1.apply$mcV$sp(AsyncEventQueue.scala:83)
	at org.apache.spark.util.Utils$.tryOrStopSparkContext(Utils.scala:1302)
	at org.apache.spark.scheduler.AsyncEventQueue$$anon$1.run(AsyncEventQueue.scala:82)
+---+
| id|
+---+
| 10|
|  8|
|  1|
|  4|
| 13|
|  3|
| 12|
|  2|
|  9|
| 16|
| 18|
| 11|
|  7|
| 19|
|  6|
| 14|
|  0|
|  5|
| 17|
| 15|
+---+

[success] Total time: 80 s (01:20), completed Nov 10, 2020 5:22:24 PM
```

## 延伸 QUESTIONS

- Delta Lake 跟 AWS Athena 的整合性？
    - https://docs.delta.io/0.7.0/presto-integration.html