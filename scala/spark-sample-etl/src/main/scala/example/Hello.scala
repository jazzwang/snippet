package example

import org.apache.spark.sql.SparkSession
import org.apache.commons.io.FileUtils

object Hello extends Greeting with App {
  println(greeting)

  val whereami = System.getProperty("user.dir")
  println(whereami)

  // To make sure eventLog dir exists
  val sparkEventLogDir = "/tmp/spark-history"
  val directory = new java.io.File(sparkEventLogDir)
  if (! directory.exists) {
    directory.mkdir
  }

  // To avoid error: "path XXXXX/output already exists."
  val outDir = new java.io.File("output")
  if (outDir.exists) {
    println("Found existing 'output' folder! Will delete it.")
    FileUtils.deleteDirectory(outDir)
  }

  var spark = SparkSession.builder
    .appName("Spark Example")
    .master("local[*]")
    .config("spark.eventLog.enabled","true")
    .config("spark.eventLog.dir", sparkEventLogDir)
    .getOrCreate

  var employeeDF = spark.read.json("input/employees.json")
  employeeDF.printSchema()
  employeeDF.createOrReplaceTempView("employee")
  
  var peopleDF = spark.read.json("input/people.json")
  peopleDF.printSchema()
  peopleDF.createOrReplaceTempView("people")

  var outputDF = spark.sql("select employee.name, people.age, employee.salary from employee, people where employee.name = people.name order by salary")
  outputDF.show()
  outputDF.coalesce(1).write.parquet("output")
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
