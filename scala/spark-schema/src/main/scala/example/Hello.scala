package example

import java.io._
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

  // load JSON schema from faker JSON file into Spark StructType schema
  val fakerDF = spark.read.json("examples/json-schema-faker.ndjson")
  val inn_schema = fakerDF.schema
  val innDF = spark.read.json("input/in-network-rates-multiple-plans-sample.ndjson")
  val innDF2 = spark.read.schema(inn_schema).json("input/in-network-rates-multiple-plans-sample.ndjson")
  // Ref: https://alvinalexander.com/scala/how-to-write-text-files-in-scala-printwriter-filewriter/
  val pw = new PrintWriter(new File("in-network-rates.schema"))
  pw.write(inn_schema.toString())
  pw.close()
  // https://stackoverflow.com/a/45422969
  scala.Console.withOut(new PrintStream(new FileOutputStream(s"in-network-rates-faker.df.printSchema"))) {
    fakerDF.printSchema
  }
  scala.Console.withOut(new PrintStream(new FileOutputStream(s"in-network-ratess-sample.df.printSchema"))) {
    innDF.printSchema
  }
  scala.Console.withOut(new PrintStream(new FileOutputStream(s"in-network-rates-sample.df.schema.printSchema"))) {
    innDF2.printSchema
  }
  fakerDF.printSchema
  innDF.printSchema
  innDF2.printSchema

  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
