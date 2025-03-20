- https://stackoverflow.com/a/16309699

```
From the Spark Scala Programming guide's section on "Hadoop Datasets":

Spark can create distributed datasets from any file stored in the Hadoop distributed file system (HDFS) or other storage systems supported by Hadoop (including your local file system, Amazon S3, Hypertable, HBase, etc). Spark supports text files, SequenceFiles, and any other Hadoop InputFormat.

Support for gzip input files should work the same as it does in Hadoop. For example, sc.textFile("myFile.gz") should automatically decompress and read gzip-compressed files (textFile() is actually implemented using Hadoop's TextInputFormat, which supports gzip-compressed files).

As mentioned by @nick-chammas in the comments:

note that if you call sc.textFile() on a gzipped file, Spark will give you an RDD with only 1 partition (as of 0.9.0). This is because gzipped files are not splittable. If you don't repartition the RDD somehow, any operations on that RDD will be limited to a single core
```

- https://medium.com/@talentorigin/reading-compressed-files-with-spark-2-0-part-1-c25c5ea7ad93
- https://gist.github.com/owainlewis/1e7d1e68a6818ee4d50e
- https://docs.oracle.com/javase/8/docs/api/java/util/zip/GZIPInputStream.html
- https://hadoop.apache.org/docs/r3.0.0/api/org/apache/hadoop/fs/FSDataInputStream.html
- https://issues.apache.org/jira/browse/HADOOP-7076

## 2020-07-30

- test with `spark-shell`

```
val large_input = spark.read.format("csv").option("header","false").option("delimiter",",").load("input/large.csv.gz")
large_input.coalesce(10).count
large_input.coalesce(10).rdd.getNumPartitions
large_input.repartition(4).rdd.partitions.size
large_input.repartition(4).count
val large_input_rdd = spark.sparkContext.textFile("input/large.csv.gz",10)
large_input_rdd.partitions.size
val DF4P = large_input.repartition(4)
DF4P.rdd.partitions.size
System.gc
```
