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
  val IDF = spark.read.format("csv").option("header","true").option("delimiter","|").load("input/i_input.csv")
  val CDF = spark.read.format("csv").option("header","true").option("delimiter","|").load("input/c_input.csv")
  IDF.printSchema
  CDF.printSchema
  IDF.orderBy("i_id").show()
  CDF.orderBy("c_id").show()
  IDF.orderBy("i_id").distinct().show()
  CDF.orderBy("c_id").distinct().show()
  val RDF = IDF.join(CDF, IDF("i_id") === CDF("c_id"), "inner")
  RDF.orderBy("i_id").show()
  RDF.distinct.orderBy("i_id").show()
  IDF.createOrReplaceTempView("IDF")
  CDF.createOrReplaceTempView("CDF")
  spark.sql("select c_id, c_name, c_address from IDF, CDF where i_id = c_id").show()
  spark.sql("select count(*) from IDF, CDF where i_id = c_id").show
  spark.sql("select c_id, c_name, c_address from IDF, CDF where i_id = c_id order by c_id").show
  spark.sql("select c_id, c_name, c_address from IDF, CDF where i_id = c_id order by c_id").distinct.show
  val RDF2 = IDF.distinct.join(CDF.distinct, IDF("i_id") === CDF("c_id"), "left")
  RDF2.printSchema
  RDF2.orderBy("i_id").show
  RDF2.orderBy("i_id").distinct.show
  val RDF3 = IDF.distinct.join(CDF.distinct, IDF("i_id") === CDF("c_id"), "right")
  RDF3.orderBy("c_id").select("c_id","c_name","c_address").distinct.show
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
