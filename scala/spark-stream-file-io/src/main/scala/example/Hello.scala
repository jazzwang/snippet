package example

import org.apache.spark._
import org.apache.spark.streaming._
import org.apache.hadoop.fs._

object Hello extends Greeting with App {
  println(greeting)

  val conf = new SparkConf()
      .setAppName("Spark Streaming Example")
      .setMaster("local[*]")
      .set("spark.eventLog.enabled","true")
      .set("spark.eventLog.dir", "/tmp/spark-history")
  val ssc = new StreamingContext(conf, Seconds(1))
  val sc = ssc.sparkContext
  val fs = FileSystem.get(sc.hadoopConfiguration)
  // http://spark.apache.org/docs/latest/streaming-programming-guide.html#file-streams
  // Case 1: static plain text input files
  val lines = ssc.textFileStream("input")
  val words = lines.flatMap(_.split(" "))
  val pairs = words.map(word => (word, 1))
  val wordCounts = pairs.reduceByKey(_ + _)
  wordCounts.print()
  // start Spark Streaming Context
  ssc.start()
  println("start Spark Streaming Context")
  // sleep 1 seconds for Spark Streaming initiation
  // https://docs.oracle.com/javase/tutorial/essential/concurrency/sleep.html
  Thread.sleep(1000)
  /* 
  // create a new file 'hello.txt' in "input" folder
  val outFile = new Path("input/hello.txt")
  // remove 'hello.txt' if it exists
  if (fs.exists(outFile)) { 
    fs.delete(outFile) 
  }
  println("create 'hello.txt'")
  val outStream = fs.create(outFile)
  outStream.writeUTF("hello world")
  outStream.close()
  Thread.sleep(1000) 
  */
  // copy file from "existing.txt" to "new-file.txt"
  val srcFile = new Path("input/existing.txt")
  val dstFile = new Path("input/new-file.txt")
  if (fs.exists(dstFile)) { fs.delete(dstFile) }
  Thread.sleep(1000)
  println("create 'new-file.txt'")
  // https://hadoop.apache.org/docs/current/api/org/apache/hadoop/fs/FileUtil.html
  // copy(FileSystem srcFS, FileStatus srcStatus, FileSystem dstFS, Path dst, boolean deleteSource, boolean overwrite, Configuration conf)
  FileUtil.copy(fs, srcFile, fs, dstFile, false, sc.hadoopConfiguration)
  // wait 2 seconds to see if the new-file.txt is detected.
  Thread.sleep(2000)
  // stop Spark Streaming Context
  ssc.stop()
}

trait Greeting {
  lazy val greeting: String = "hello"
}
