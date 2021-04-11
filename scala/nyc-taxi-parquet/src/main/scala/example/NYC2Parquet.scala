package example

import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession

object NYC2Parquet {

  case class Arguments(inputDir: String = "", outputDir: String = "", version: String = "")

  def main(args: Array[String]): Unit = {
    val parser = new scopt.OptionParser[Arguments]("NYC2Parquet") {
      opt[String]('i', "inputDir")
        .required()
        .valueName("")
        .action((value, arguments) => arguments.copy(inputDir = value))
      opt[String]('o', "outputDir")
        .required()
        .valueName("")
        .action((value, arguments) => arguments.copy(outputDir = value))

      opt[String]('v', "version")
        .required()
        .valueName("")
        .action((value, arguments) => arguments.copy(version = value))
    }
    parser.parse(args, Arguments()) match {
      case Some(arguments) => run(arguments)
      case None            => sys.exit(1)
    }
  }

  def run(arguments: Arguments): Unit = {
    println("- Input Dir: " + arguments.inputDir)
    println("- Output Dir: " + arguments.outputDir)
    println("- Schema Version: " + arguments.version)

    val spark = SparkSession.builder
                            .appName("Spark Example")
                            .master("local[*]")
                            .getOrCreate
    val sc = spark.sparkContext

    import spark.implicits._

    val source = spark.read.option("header","true").csv(arguments.inputDir)
    val target = source.select(
      $"vendor_name".as("vendor_id"),
      $"Trip_Pickup_DateTime".cast("timestamp").as("pickup_timestamp"),
      $"Trip_Dropoff_DateTime".cast("timestamp").as("dropoff_timestamp"),
      (unix_timestamp($"Trip_Dropoff_DateTime")-unix_timestamp($"Trip_Pickup_DateTime")).as("trip_second"),
      $"Trip_Distance".cast("float").as("trip_distance"),
      $"Passenger_Count".cast("int").as("passenger_count"),
      $"Rate_Code".as("rate_code"),
      $"store_and_forward".as("store_and_fwd_flag"),
      $"Payment_Type".as("payment_type"),
      $"Fare_Amt".cast("float").as("fare_amount")
    )
    target.write.parquet(arguments.outputDir)
    spark.stop()
  }
}