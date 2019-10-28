package example

import org.apache.spark.sql.SparkSession
import java.sql._

object Hello extends Greeting with App {
  println(greeting)

  val whereami = System.getProperty("user.dir")
  println(whereami)

  var spark = SparkSession.builder
    .appName("Spark Example")
    .master("local[*]")
//  .config("spark.eventLog.enabled","true")
    .getOrCreate

  var input = spark.read.option("header",true).csv("input/sample.csv")
  input.printSchema()

  val connection = DriverManager.getConnection("jdbc:sqlite:sample.db")
  val statement = connection.createStatement()

  connection.close()

  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
