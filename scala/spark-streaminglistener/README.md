# README

```
~/.../scala/spark-streaminglistener$ sbt run
[info] Loading project definition from /home/jazzwang/snippet/scala/spark-streaminglistener/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to spark-stream-file-io (in build file:/home/jazzwang/snippet/scala/spark-streaminglistener/)
[info] Compiling 2 Scala sources to /home/jazzwang/snippet/scala/spark-streaminglistener/target/scala-2.12/classes ...
[warn] there was one deprecation warning; re-run with -deprecation for details
[warn] one warning found
[info] running example.StreamingMetrics 
WARNING: An illegal reflective access operation has occurred
WARNING: Illegal reflective access by org.apache.spark.unsafe.Platform (file:/tmp/sbt_543566b5/target/331d271f/255e2aee/spark-unsafe_2.12-3.0.0.jar) to constructor java.nio.DirectByteBuffer(long,int)
WARNING: Please consider reporting this to the maintainers of org.apache.spark.unsafe.Platform
WARNING: Use --illegal-access=warn to enable warnings of further illegal reflective access operations
WARNING: All illegal access operations will be denied in a future release
start Spark Streaming Context
-------------------------------------------
Time: 1632233345000 ms
-------------------------------------------

Batch completed at: 1632233345709
 was started at: 1632233345092
 submission time: 1632233345081
 batch time: 1632233345000 ms
 batch processing delay: 617
 records : 0
 total batch delay:628
 product prefix:BatchInfo
 schedulingDelay:11
 processingTime:617
-------------------------------------------
Time: 1632233346000 ms
-------------------------------------------

Batch completed at: 1632233346073
 was started at: 1632233346017
 submission time: 1632233346016
 batch time: 1632233346000 ms
 batch processing delay: 56
 records : 0
 total batch delay:57
 product prefix:BatchInfo
 schedulingDelay:1
 processingTime:56
create 'new-file.txt'
-------------------------------------------
Time: 1632233347000 ms
-------------------------------------------
(STREAMING,1)
(SPARK,1)
(INPUT,1)
(DATA,1)

Batch completed at: 1632233347355
 was started at: 1632233347106
 submission time: 1632233347105
 batch time: 1632233347000 ms
 batch processing delay: 249
 records : 0
 total batch delay:250
 product prefix:BatchInfo
 schedulingDelay:1
 processingTime:249
-------------------------------------------
Time: 1632233348000 ms
-------------------------------------------

Batch completed at: 1632233348049
 was started at: 1632233348012
 submission time: 1632233348011
 batch time: 1632233348000 ms
 batch processing delay: 37
 records : 0
 total batch delay:38
 product prefix:BatchInfo
 schedulingDelay:1
 processingTime:37
[success] Total time: 13 s, completed Sep 21, 2021, 2:09:08 PM
```