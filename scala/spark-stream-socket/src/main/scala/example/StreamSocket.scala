package example

import org.apache.spark._
import org.apache.spark.streaming._

object StreamSocket extends App {
  val conf = new SparkConf()
      .setAppName("Spark Streaming Example")
      .setMaster("local[*]")
      .set("spark.eventLog.enabled","true")
      .set("spark.eventLog.dir", "/tmp/spark-history")
  val ssc = new StreamingContext(conf, Seconds(1))
  val sc = ssc.sparkContext
  // http://spark.apache.org/docs/latest/streaming-programming-guide.html#discretized-streams-dstreams
  // Case 2: Discretized Streams (DStreams)
  val lines = ssc.socketTextStream("localhost", 9999)
  val words = lines.flatMap(_.split(" "))
  val pairs = words.map(word => (word, 1))
  val wordCounts = pairs.reduceByKey(_ + _)
  wordCounts.print()
  // start Spark Streaming Context
  ssc.start()
  println("start Spark Streaming Context")
  // Wait for the computation to terminate
  ssc.awaitTerminationOrTimeout(5000)
  ssc.stop(true, true)
}