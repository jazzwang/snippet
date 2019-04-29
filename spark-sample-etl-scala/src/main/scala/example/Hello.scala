package example

import org.apache.spark.sql.SparkSession

object Hello extends Greeting with App {
  println(greeting)

  val whereami = System.getProperty("user.dir")
  println(whereami)

  var spark = SparkSession.builder
    .appName("Spark Example")
    .master("local[*]")
    .getOrCreate

  var employeeDF = spark.read.json("input/employees.json")
  employeeDF.printSchema()
  employeeDF.createOrReplaceTempView("employee")
  
  var peopleDF = spark.read.json("input/people.json")
  peopleDF.printSchema()
  peopleDF.createOrReplaceTempView("people")

  var outputDF = spark.sql("select employee.name, people.age, employee.salary from employee, people where employee.name = people.name order by salary")
  outputDF.show()
  outputDF.write.parquet("output")
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
