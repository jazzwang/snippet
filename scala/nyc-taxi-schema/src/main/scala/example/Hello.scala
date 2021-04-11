package example

import org.apache.spark.sql.SparkSession
import java.io.PrintStream
import java.io.FileOutputStream

object Hello extends Greeting with App {
  println(greeting)

  val spark = SparkSession.builder
      .appName("Spark Example")
      .master("local[*]")
      .config("spark.eventLog.enabled","true")
      .config("spark.eventLog.dir", "/tmp/spark-history")
      .getOrCreate
  val sc = spark.sparkContext
  // https://stackoverflow.com/a/45422969
  for (i <- 1 to 5) {
    val df = spark.read.option("header","true").csv(s"nyc-tlc/yellow_v$i")
    scala.Console.withOut(new PrintStream(new FileOutputStream(s"yellow_v$i.txt"))) {
      df.printSchema
    }
    scala.Console.withOut(new PrintStream(new FileOutputStream(s"yellow_v$i_distinct.txt"))) {
      for (j <- df.columns) {
        df.select(col(s"$j")).distinct.show
      }
    }
  }
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
