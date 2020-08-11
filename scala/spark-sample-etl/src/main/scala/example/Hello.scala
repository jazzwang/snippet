package example

import org.apache.spark.sql.SparkSession
import org.apache.hadoop.fs._

object Hello extends Greeting with App {
  println(greeting)

  val whereami = System.getProperty("user.dir")
  println(whereami)

  // To make sure eventLog dir exists
  val sparkEventLogDir = "/tmp/spark-history"

  val spark = SparkSession.builder
    .appName("Spark Example")
    .master("local[*]")
    .config("spark.eventLog.enabled","true")
    .config("spark.eventLog.dir", sparkEventLogDir)
    .getOrCreate

  val sc = spark.sparkContext

  // https://stackoverflow.com/questions/27023766/spark-iterate-hdfs-directory
  val fs = FileSystem.get(sc.hadoopConfiguration)
  val eventDir = new Path(sparkEventLogDir)
  if (! fs.exists(eventDir)) {
    fs.mkdirs(eventDir)
  }

  // To avoid error: "path XXXXX/output already exists."
  val outDir = new Path("output")
  if (fs.exists(outDir)) {
    println("Found existing 'output' folder! Will delete it.")
    fs.delete(outDir,true)
  }

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
