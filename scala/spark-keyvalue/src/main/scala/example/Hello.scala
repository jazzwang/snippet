package example

import org.apache.spark.sql.SparkSession
import org.apache.hadoop.io._
import org.apache.hadoop.mapreduce.lib.input._

object Hello extends Greeting with App {
  println(greeting)
  
  val spark = SparkSession.builder
      .appName("Spark Example")
      .master("local[*]")
      .config("spark.eventLog.enabled","true")
      .config("spark.eventLog.dir", "/tmp/spark-history")
      .getOrCreate
  val sc = spark.sparkContext
  val conf = sc.hadoopConfiguration
  // https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/lib/input/KeyValueTextInputFormat.html
  // NOTE: default delimiter is '\t'
  //       in the sample dataset, we'll use ','
  conf.set("mapreduce.input.keyvaluelinerecordreader.key.value.separator",",")
  val records = sc.newAPIHadoopFile("dataset",classOf[KeyValueTextInputFormat], classOf[Text], classOf[Text])
  records.keys.foreach(println)
  records.values.foreach(println)
  spark.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
