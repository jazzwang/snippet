import org.apache.spark.sql.SparkSession

object Hello extends App {
  val spark = SparkSession.builder
      .appName("Spark Example")
      .master("local[*]")
      .getOrCreate
  val sc = spark.sparkContext
  spark.stop()
}
