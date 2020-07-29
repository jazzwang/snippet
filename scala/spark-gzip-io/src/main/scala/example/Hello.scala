package example

import org.apache.spark.sql.SparkSession

object Hello extends Greeting with App {
  println(greeting)

  val spark = SparkSession.builder
      .appName("Spark Example")
      .master("local[*]")
      .config("spark.eventLog.enabled","true")
      .config("spark.eventLog.dir", "/tmp/spark-history")
      .getOrCreate
  val sc = spark.sparkContext
  val i_input = spark.read.format("csv").option("header","true").option("delimiter","|").load("input/i_input.csv.gz")
  i_input.show
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
