import org.apache.spark.sql._
import org.apache.spark.SparkContext._
import org.apache.spark.sql.functions._

object Hello extends App {
  val spark = SparkSession.builder
      .appName("Spark Example")
      .master("local[*]")
      .getOrCreate
  val sc = spark.sparkContext

  import spark.implicits._

  println("Test #1: manually create parquet files in partitioned directory")

  val df1 = Seq(("A", 1), ("B", 2), ("A", 3), ("C", 1)).toDF("k", "v") // toDF needs `import spark.implicits._`
  df1.write.mode("overwrite").parquet("table/batch=1")
  df1.write.mode("overwrite").parquet("table/batch=2")
  val df2 = spark.read.parquet("table")
  df2.printSchema
  df2.show

  println("Test #2: load parquet from non-partitioned path, manually add column and output parquet files with partition column.")

  df1.write.parquet("data/batch-1")
  df1.write.parquet("data/batch-2")
  val df3 = spark.read.parquet("data/batch-1").withColumn("batch", lit(1))
  val df4 = spark.read.parquet("data/batch-2").withColumn("batch", lit(2))
  val df5 = df3.union(df4).toDF
  df5.show

  df5.write.partitionBy("batch").mode("overwrite").parquet("new-table")
  val df6 = spark.read.parquet("new-table/batch=1")
  df6.printSchema
  df6.show

  spark.stop()
}
