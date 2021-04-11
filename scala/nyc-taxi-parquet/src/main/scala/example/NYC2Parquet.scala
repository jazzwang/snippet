package example

import org.apache.spark.sql.SparkSession

object NYC2Parquet {

  case class Arguments(inputDir: String = "", outputDir: String = "", version: String = "")

  def main(args: Array[String]): Unit = {
    val parser = new scopt.OptionParser[Arguments]("Parsing application") {
      head(": an example app using DataFrame for ML.")
      opt[String]('i', "inputDir")
        .required()
        .valueName("")
        .action((value, arguments) => arguments.copy(inputDir = value))
      opt[String]('o', "outputDir")
        .required()
        .valueName("")
        .action((value, arguments) => arguments.copy(outputDir = value))
    }
    parser.parse(args, Arguments()) match {
      case Some(arguments) => run(arguments)
      case None            => sys.exit(1)
    }
  }

  def run(arguments: Arguments): Unit = {
    println("Input Dir:" + arguments.inputDir)
    println("Output Dir:" + arguments.outputDir)
    val spark = SparkSession.builder
                            .appName("Spark Example")
                            .getOrCreate
    val sc = spark.sparkContext
    spark.stop()
  }
}