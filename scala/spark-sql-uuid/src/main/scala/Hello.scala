import org.apache.spark.sql.SparkSession

object Hello extends App {
  val spark = SparkSession.builder
      .appName("Spark SQL UUID Test")
      .master("local[*]")
      .getOrCreate
  val sc = spark.sparkContext

  // toDF needs `import spark.implicits._`
  import spark.implicits._
  import spark.sql

  val df = (1 to 1000000).toDF
  df.printSchema
  df.createTempView("df")
  val df2 = spark.sql("select *, uuid() as record_uuid from df")
  df2.printSchema
  df2.show(false)
  df2.coalesce(4).write.parquet("output")

  spark.stop()
}
