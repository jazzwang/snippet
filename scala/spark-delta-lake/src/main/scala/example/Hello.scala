package example

import org.apache.spark.sql.SparkSession
import io.delta.tables._
import org.apache.spark.sql.functions._

object Hello extends Greeting with App {
  println(greeting)

  val spark = SparkSession.builder
      .appName("Spark Delta Lake Example")
      .master("local[*]")
      .config("spark.eventLog.enabled","true")
      .config("spark.eventLog.dir", "/tmp/spark-history")
      .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
      .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
      .getOrCreate
  val sc = spark.sparkContext
  // https://docs.delta.io/latest/quick-start.html#language-scala
  // 1. Create a table
  val data1 = spark.range(0, 5)
  data1.write.format("delta").save("/tmp/delta-table")
  // 2. Read data
  val df = spark.read.format("delta").load("/tmp/delta-table")
  df.show()
  // 3. Update table data
  val data2 = spark.range(5, 10)
  data2.write.format("delta").mode("overwrite").save("/tmp/delta-table")
  df.show()
  // 4. Conditional update without overwrite
  val deltaTable = DeltaTable.forPath("/tmp/delta-table")
  // 5. Update every even value by adding 100 to it
  deltaTable.update(
    condition = expr("id % 2 == 0"),
    set = Map("id" -> expr("id + 100")))
  df.show()
  // 6. Delete every even value
  deltaTable.delete(condition = expr("id % 2 == 0"))
  df.show()
  // 7. Upsert (merge) new data
  val newData = spark.range(0, 20).toDF
  deltaTable.as("oldData")
    .merge(
      newData.as("newData"),
      "oldData.id = newData.id")
    .whenMatched
    .update(Map("id" -> col("newData.id")))
    .whenNotMatched
    .insert(Map("id" -> col("newData.id")))
    .execute()
  df.show()
  // END
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
