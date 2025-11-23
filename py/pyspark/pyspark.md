# pyspark

- PyPI
  - https://pypi.org/project/pyspark/
- Git Repo
  - https://github.com/apache/spark
- Website
  - https://spark.apache.org/
- Document
  - https://spark.apache.org/docs/latest/api/python/getting_started/install.html

## 2025-11-23

- 安裝：
  - 用 uv tool 安裝
```bash
~/git/snippet/py/pyspark$ uv tool install pyspark==3.5.7
```
  - 用 pip 安裝
```bash
~/git/snippet/py/pyspark$ pip install pyspark==3.5.7
```
- 備註：
  - 因為新版 4.0 以上還多了 Spark Connect，還沒學會怎麼設定，先降版到 `3.5.7`

### 用 Spark-Shell 看 JSON 檔的 Schema

- 使用 `jq` 時，常需要知道 JSON 檔的階層架構。以前是比較常用 spark-shell 的 printSchema 來觀察。紀錄一下 Chrome Browser 的 HAR 檔，Schema 結果：
  - 備忘：在 Windows 上必須切換到 cmd 才有辦法正常使用 `pyspark` 或 `spark-shell` 指令（即使在 git bash 環境下）
  - 待測試：不確定 WSL 底下會怎麼認定。
```cmd
~/Downloads$ cmd
Microsoft Windows [Version 10.0.26200.7171]
(c) Microsoft Corporation. All rights reserved.

C:\Users\jazzw\Downloads>spark-shell
25/11/23 16:08:01 WARN Shell: Did not find winutils.exe: java.io.FileNotFoundException: java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset. -see https://wiki.apache.org/hadoop/WindowsProblems
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
25/11/23 16:08:08 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://JazzBook:4040
Spark context available as 'sc' (master = local[*], app id = local-1763885289951).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.5.7
      /_/

Using Scala version 2.12.18 (OpenJDK 64-Bit Server VM, Java 18.0.2.1)
Type in expressions to have them evaluated.
Type :help for more information.

scala> val df = spark.read.json("sample.har")
df: org.apache.spark.sql.DataFrame = [log: struct<creator: struct<name: string, version: string>, entries: array<struct<_connectionId:string,_initiator:struct<stack:struct<callFrames:array<struct<columnNumber:bigint,functionName:string,lineNumber:bigint,scriptId:string,url:string>>,parent:struct<callFrames:array<struct<columnNumber:bigint,functionName:string,lineNumber:bigint,scriptId:string,url:string>>,description:string>>,type:string>,_priority:string,_resourceType:string,connection:string,pageref:string,request:struct<bodySize:bigint,cookies:array<string>,headers:array<struct<name:string,value:string>>,headersSize:bigint,httpVersion:string,method:string,queryString:array<struct<name:string,value:string>>,url:string>,response:struct<_error:string,_fetchedViaServiceWorker:boolean,_tra...

scala> df.printSchema
   def printSchema(level: Int): Unit   def printSchema(): Unit

scala> df.printSchema()
root
 |-- log: struct (nullable = true)
 |    |-- creator: struct (nullable = true)
 |    |    |-- name: string (nullable = true)
 |    |    |-- version: string (nullable = true)
 |    |-- entries: array (nullable = true)
 |    |    |-- element: struct (containsNull = true)
 |    |    |    |-- _connectionId: string (nullable = true)
 |    |    |    |-- _initiator: struct (nullable = true)
 |    |    |    |    |-- stack: struct (nullable = true)
 |    |    |    |    |    |-- callFrames: array (nullable = true)
 |    |    |    |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |    |    |    |-- columnNumber: long (nullable = true)
 |    |    |    |    |    |    |    |-- functionName: string (nullable = true)
 |    |    |    |    |    |    |    |-- lineNumber: long (nullable = true)
 |    |    |    |    |    |    |    |-- scriptId: string (nullable = true)
 |    |    |    |    |    |    |    |-- url: string (nullable = true)
 |    |    |    |    |    |-- parent: struct (nullable = true)
 |    |    |    |    |    |    |-- callFrames: array (nullable = true)
 |    |    |    |    |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |    |    |    |    |-- columnNumber: long (nullable = true)
 |    |    |    |    |    |    |    |    |-- functionName: string (nullable = true)
 |    |    |    |    |    |    |    |    |-- lineNumber: long (nullable = true)
 |    |    |    |    |    |    |    |    |-- scriptId: string (nullable = true)
 |    |    |    |    |    |    |    |    |-- url: string (nullable = true)
 |    |    |    |    |    |    |-- description: string (nullable = true)
 |    |    |    |    |-- type: string (nullable = true)
 |    |    |    |-- _priority: string (nullable = true)
 |    |    |    |-- _resourceType: string (nullable = true)
 |    |    |    |-- connection: string (nullable = true)
 |    |    |    |-- pageref: string (nullable = true)
 |    |    |    |-- request: struct (nullable = true)
 |    |    |    |    |-- bodySize: long (nullable = true)
 |    |    |    |    |-- cookies: array (nullable = true)
 |    |    |    |    |    |-- element: string (containsNull = true)
 |    |    |    |    |-- headers: array (nullable = true)
 |    |    |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |    |    |-- name: string (nullable = true)
 |    |    |    |    |    |    |-- value: string (nullable = true)
 |    |    |    |    |-- headersSize: long (nullable = true)
 |    |    |    |    |-- httpVersion: string (nullable = true)
 |    |    |    |    |-- method: string (nullable = true)
 |    |    |    |    |-- queryString: array (nullable = true)
 |    |    |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |    |    |-- name: string (nullable = true)
 |    |    |    |    |    |    |-- value: string (nullable = true)
 |    |    |    |    |-- url: string (nullable = true)
 |    |    |    |-- response: struct (nullable = true)
 |    |    |    |    |-- _error: string (nullable = true)
 |    |    |    |    |-- _fetchedViaServiceWorker: boolean (nullable = true)
 |    |    |    |    |-- _transferSize: long (nullable = true)
 |    |    |    |    |-- bodySize: long (nullable = true)
 |    |    |    |    |-- content: struct (nullable = true)
 |    |    |    |    |    |-- mimeType: string (nullable = true)
 |    |    |    |    |    |-- size: long (nullable = true)
 |    |    |    |    |    |-- text: string (nullable = true)
 |    |    |    |    |-- cookies: array (nullable = true)
 |    |    |    |    |    |-- element: string (containsNull = true)
 |    |    |    |    |-- headers: array (nullable = true)
 |    |    |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |    |    |-- name: string (nullable = true)
 |    |    |    |    |    |    |-- value: string (nullable = true)
 |    |    |    |    |-- headersSize: long (nullable = true)
 |    |    |    |    |-- httpVersion: string (nullable = true)
 |    |    |    |    |-- redirectURL: string (nullable = true)
 |    |    |    |    |-- status: long (nullable = true)
 |    |    |    |    |-- statusText: string (nullable = true)
 |    |    |    |-- serverIPAddress: string (nullable = true)
 |    |    |    |-- startedDateTime: string (nullable = true)
 |    |    |    |-- time: double (nullable = true)
 |    |    |    |-- timings: struct (nullable = true)
 |    |    |    |    |-- _blocked_queueing: double (nullable = true)
 |    |    |    |    |-- _workerFetchStart: long (nullable = true)
 |    |    |    |    |-- _workerReady: long (nullable = true)
 |    |    |    |    |-- _workerRespondWithSettled: long (nullable = true)
 |    |    |    |    |-- _workerStart: long (nullable = true)
 |    |    |    |    |-- blocked: double (nullable = true)
 |    |    |    |    |-- connect: long (nullable = true)
 |    |    |    |    |-- dns: long (nullable = true)
 |    |    |    |    |-- receive: double (nullable = true)
 |    |    |    |    |-- send: double (nullable = true)
 |    |    |    |    |-- ssl: long (nullable = true)
 |    |    |    |    |-- wait: double (nullable = true)
 |    |-- pages: array (nullable = true)
 |    |    |-- element: struct (containsNull = true)
 |    |    |    |-- id: string (nullable = true)
 |    |    |    |-- pageTimings: struct (nullable = true)
 |    |    |    |    |-- onContentLoad: double (nullable = true)
 |    |    |    |    |-- onLoad: double (nullable = true)
 |    |    |    |-- startedDateTime: string (nullable = true)
 |    |    |    |-- title: string (nullable = true)
 |    |-- version: string (nullable = true)


scala>

scala> :quit

C:\Users\jazzw\Downloads>
```