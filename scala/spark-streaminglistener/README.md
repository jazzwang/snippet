# README

```
~/.../scala/spark-streaminglistener$ sbt run
[info] Loading project definition from /home/jazzwang/snippet/scala/spark-streaminglistener/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to spark-stream-file-io (in build file:/home/jazzwang/snippet/scala/spark-streaminglistener/)
[info] Compiling 1 Scala source to /home/jazzwang/snippet/scala/spark-streaminglistener/target/scala-2.12/classes ...
[info] running example.StreamingMetrics 
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/tmp/sbt_62baf138/target/331d271f/255e2aee/spark-unsafe_2.12-3.0.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
start Spark Streaming Context
-------------------------------------------
Time: 1632232053000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232053693 was started at: 1632232053150 submission time: 1632232053074 batch time: 1632232053000 ms batch processing delay: 543 records : 0 total batch delay:619 product prefix:BatchInfo schedulingDelay:76 processingTime:543
-------------------------------------------
Time: 1632232054000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232054054 was started at: 1632232054012 submission time: 1632232054011 batch time: 1632232054000 ms batch processing delay: 42 records : 0 total batch delay:43 product prefix:BatchInfo schedulingDelay:1 processingTime:42
create 'new-file.txt'
-------------------------------------------
Time: 1632232055000 ms
-------------------------------------------
(STREAMING,1)
(SPARK,1)
(INPUT,1)
(DATA,1)

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232055343 was started at: 1632232055102 submission time: 1632232055097 batch time: 1632232055000 ms batch processing delay: 241 records : 0 total batch delay:246 product prefix:BatchInfo schedulingDelay:5 processingTime:241
-------------------------------------------
Time: 1632232056000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232056049 was started at: 1632232056012 submission time: 1632232056011 batch time: 1632232056000 ms batch processing delay: 37 records : 0 total batch delay:38 product prefix:BatchInfo schedulingDelay:1 processingTime:37
[success] Total time: 12 s, completed Sep 21, 2021, 1:47:36 PM
~/.../scala/spark-streaminglistener$ sbt run
[info] Loading project definition from /home/jazzwang/snippet/scala/spark-streaminglistener/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to spark-stream-file-io (in build file:/home/jazzwang/snippet/scala/spark-streaminglistener/)
[info] Compiling 1 Scala source to /home/jazzwang/snippet/scala/spark-streaminglistener/target/scala-2.12/classes ...
[info] running example.StreamingMetrics 
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/tmp/sbt_67072130/target/331d271f/255e2aee/spark-unsafe_2.12-3.0.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
start Spark Streaming Context
-------------------------------------------
Time: 1632232216000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232216746
 was started at: 1632232216093
 submission time: 1632232216078
 batch time: 1632232216000 ms
 batch processing delay: 653
 records : 0
 total batch delay:668
 product prefix:BatchInfo
 schedulingDelay:15
 processingTime:653
-------------------------------------------
Time: 1632232217000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232217065
 was started at: 1632232217014
 submission time: 1632232217014
 batch time: 1632232217000 ms
 batch processing delay: 51
 records : 0
 total batch delay:51
 product prefix:BatchInfo
 schedulingDelay:0
 processingTime:51
create 'new-file.txt'
-------------------------------------------
Time: 1632232218000 ms
-------------------------------------------
(STREAMING,1)
(SPARK,1)
(INPUT,1)
(DATA,1)

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232218326
 was started at: 1632232218095
 submission time: 1632232218091
 batch time: 1632232218000 ms
 batch processing delay: 231
 records : 0
 total batch delay:235
 product prefix:BatchInfo
 schedulingDelay:4
 processingTime:231
-------------------------------------------
Time: 1632232219000 ms
-------------------------------------------

CloudWatch Streaming Listener, onBatchCompleted:Spark Streaming Example
Batch completed at: 1632232219051
 was started at: 1632232219012
 submission time: 1632232219012
 batch time: 1632232219000 ms
 batch processing delay: 39
 records : 0
 total batch delay:39
 product prefix:BatchInfo
 schedulingDelay:0
 processingTime:39
[success] Total time: 12 s, completed Sep 21, 2021, 1:50:19 PM
```