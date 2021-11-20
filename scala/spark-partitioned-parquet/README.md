# README

## REFERENCES

- https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#partition-discovery 官方文件對於 Partition Discovery 的說明
- https://sparkbyexamples.com/spark/spark-partitioning-understanding/ 不同的 Partition 情境

## DEVELOPMENT NOTES

### 2021-11-18

- ( 2021-11-18 22:40:23 ) test with `spark-shell`
```
### TEST 1:
###  - create DataFrame df1.
###  - store df1 to parquet file in `table/batch=1`
###  - store df1 to parquet file in `table/batch=2`
###  - use `spark.read.parquet` to read the parquet file from `table` folder

### idea/concept reference from https://stackoverflow.com/a/32920122

val df1 = Seq(
  ("A", 1), ("B", 2), ("A", 3), ("C", 1)
).toDF("k", "v")
df1.printSchema
df1.write.parquet("table/batch=1")
df1.write.parquet("table/batch=2")
val df2 = spark.read.parquet("table")
df2.printSchema
df2.show

### TEST 2:
###  - create DataFrame df1.
###  - store df1 to parquet file in `data/batch-1`
###  - store df1 to parquet file in `data/batch-2`
###  - use `spark.read.parquet` to read the parquet file from `data/batch-1` and `data/batch-2` folder

df1.write.parquet("data/batch-1")
df1.write.parquet("data/batch-2")
val df3 = spark.read.parquet("data/batch-1","data/batch-2")
df3.printSchema
df3.show

### TEST 3:
###  - use Hive DDL to create table `default.data` and specified partition column `batch`
###  - use Hive DDL to add partition and corresponding location to table `default.data`
### reference:
###  - https://stackoverflow.com/a/49557506
###  - https://cwiki.apache.org/confluence/display/hive/languagemanual+ddl

spark.sql("create table data (k string, v integer) partitioned by (batch integer)")
spark.sql("show tables").show
spark.sql("alter table data add partition (batch=1) location 'data/batch-1'")
spark.sql("alter table data add partition (batch=2) location 'data/batch-2'")
spark.sql("select * from data").show
spark.sql("drop table data")
spark.sql("show tables").show
spark.sql("create table data (k string, v integer) partitioned by (batch integer) stored as parquet location 'data'")
spark.sql("show tables").show
spark.sql("select * from data").show
spark.sql("alter table data add partition (batch=1) location 'batch-1'")
spark.sql("alter table data add partition (batch=2) location 'batch-2'")
spark.sql("select * from data").show
df2.show
df2.createTempView("partitioned")
spark.sql("show tables").show
spark.sql("describe partitioned").show

### TEST 4:
###  - manually add column to DataFrame `df3` and `df4`
###    https://stackoverflow.com/a/32788650
###  - union `df3` and `df4` (it becomes DataSet) and convert it to a DataFrame as `df5`
###    https://stackoverflow.com/a/33551141
###  - use `partitionBy` of DataFrameWriter to output partitioned parquet files
###    https://sparkbyexamples.com/spark/spark-partitioning-understanding/

val df3 = spark.read.parquet("data/batch-1").withColumn("batch", lit(1))
df3.show
val df4 = spark.read.parquet("data/batch-2").withColumn("batch", lit(2))
df4.show
val df5 = df3.union(df4).toDF
df5.show
df5.write.partitionBy("batch").parquet("new-table")
val df6 = spark.read.parquet("new-table/batch=1")
df6.printSchema
df6.show
```