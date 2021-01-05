import org.apache.hadoop.conf._

// Reference:
// https://github.com/jazzwang/hadoop_labs/blob/master/lab006/src/isFile.java
// http://trac.3du.me/cloud/wiki/III140705/Lab12

object MyApp extends App {
    val conf = new Configuration()
    val defaultFS = conf.get("fs.default.name")
    println(s"defaultFS=$defaultFS")
}