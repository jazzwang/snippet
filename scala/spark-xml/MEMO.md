# Learning Spark-XML

## 2020-11-26

- ( 2020-11-26 10:15:54 )
- https://sparkbyexamples.com/spark/spark-read-write-xml/#spark-xml-dependency
- download the sample XML file
```bash
~/git/snippet/scala/spark-xml$ wget https://raw.githubusercontent.com/sparkbyexamples/spark-examples/master/spark-sql-examples/src/main/resources/persons.xml
```
- ( 2020-11-26 10:17:10 )
- test with `spark-shell`
      - Apache Spark `3.0.0` with Hadoop `2.7` (the same version of AWS EMR 6.1)
      - Using Scala version `2.12.10` (OpenJDK 64-Bit Server VM, Java `1.8.0_275`)
```bash
~/git/snippet/scala/spark-xml$ spark-shell --packages com.databricks:spark-xml_2.12:0.10.0
```
- ( 2020-11-26 10:20:34 )
-
```scala
scala> import com.databricks.spark.xml._
import com.databricks.spark.xml._

scala> val df = spark.read.format("com.databricks.spark.xml").option("rowTag","person").xml("persons.xml")
df: org.apache.spark.sql.DataFrame = [_id: bigint, addresses: struct<address: array<struct<city:string,state:string,street:string>>> ... 7 more fields]

scala> df.printSchema
root
 |-- _id: long (nullable = true)
 |-- addresses: struct (nullable = true)
 |    |-- address: array (nullable = true)
 |    |    |-- element: struct (containsNull = true)
 |    |    |    |-- city: string (nullable = true)
 |    |    |    |-- state: string (nullable = true)
 |    |    |    |-- street: string (nullable = true)
 |-- dob_month: long (nullable = true)
 |-- dob_year: long (nullable = true)
 |-- firstname: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- salary: struct (nullable = true)
 |    |-- _VALUE: long (nullable = true)
 |    |-- _currency: string (nullable = true)
 ```