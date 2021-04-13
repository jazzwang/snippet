package example

import java.io.PrintStream
import java.io.FileOutputStream
import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession

object NYC2JSON {

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
                            .appName("Convert NYC-TLC CSV to JSON")
                            .getOrCreate
    val sc = spark.sparkContext

    import spark.implicits._

    val source = spark.read.option("header","true").csv(arguments.inputDir)

    val target = arguments.version match {
      // yellow_v1

      case "1" => {
        source.select(
          $"vendor_name".as("vendor_id"),
          $"Trip_Pickup_DateTime".cast("timestamp").as("pickup_timestamp"),
          $"Trip_Dropoff_DateTime".cast("timestamp").as("dropoff_timestamp"),
          $"Passenger_Count".cast("int").as("passenger_count"),
          $"Trip_Distance".cast("float").as("trip_distance"),
          (unix_timestamp($"Trip_Dropoff_DateTime")-unix_timestamp($"Trip_Pickup_DateTime")).as("trip_second"),
          $"Rate_Code".as("rate_code"),
          $"store_and_forward".as("store_and_fwd_flag"),
          $"Payment_Type".as("payment_type"),
          $"Fare_Amt".cast("float").as("fare_amount"),
          $"mta_tax".cast("float").as("mta_tax"),
          $"Tip_Amt".cast("float").as("tip_amount"),
          $"Tolls_Amt".cast("float").as("tolls_amount"),
          $"Total_Amt".cast("float").as("total_amount"),
          $"Start_Lon".cast("float").as("pickup_lon"),
          $"Start_Lat".cast("float").as("pickup_lat"),
          $"End_Lon".cast("float").as("dropoff_lon"),
          $"End_Lat".cast("float").as("dropoff_lat"),
          $"surcharge".cast("float").as("surcharge")
        )
      }

      // yellow_v2

      case "2" => {
        source.select(
          $"vendor_id".as("vendor_id"),
          $"pickup_datetime".cast("timestamp").as("pickup_timestamp"),
          $"dropoff_datetime".cast("timestamp").as("dropoff_timestamp"),
          $"passenger_count".cast("int").as("passenger_count"),
          $"trip_distance".cast("float").as("trip_distance"),
          (unix_timestamp($"dropoff_datetime")-unix_timestamp($"pickup_datetime")).as("trip_second"),
          $"rate_code".as("rate_code"),
          $"store_and_fwd_flag".as("store_and_fwd_flag"),
          $"payment_type".as("payment_type"),
          $"fare_amount".cast("float").as("fare_amount"),
          $"mta_tax".cast("float").as("mta_tax"),
          $"tip_amount".cast("float").as("tip_amount"),
          $"tolls_amount".cast("float").as("tolls_amount"),
          $"total_amount".cast("float").as("total_amount"),
          $"pickup_longitude".cast("float").as("pickup_lon"),
          $"pickup_latitude".cast("float").as("pickup_lat"),
          $"dropoff_longitude".cast("float").as("dropoff_lon"),
          $"dropoff_latitude".cast("float").as("dropoff_lat"),
          $"surcharge".cast("float").as("surcharge")
        )
      }

      // yellow_v3

      case "3" => {
        source.select(
          $"VendorID".as("vendor_id"),
          $"tpep_pickup_datetime".cast("timestamp").as("pickup_timestamp"),
          $"tpep_dropoff_datetime".cast("timestamp").as("dropoff_timestamp"),
          $"passenger_count".cast("int").as("passenger_count"),
          $"trip_distance".cast("float").as("trip_distance"),
          (unix_timestamp($"tpep_dropoff_datetime")-unix_timestamp($"tpep_pickup_datetime")).as("trip_second"),
          $"RatecodeID".as("rate_code"),
          $"store_and_fwd_flag".as("store_and_fwd_flag"),
          $"payment_type".as("payment_type"),
          $"fare_amount".cast("float").as("fare_amount"),
          $"mta_tax".cast("float").as("mta_tax"),
          $"tip_amount".cast("float").as("tip_amount"),
          $"tolls_amount".cast("float").as("tolls_amount"),
          $"total_amount".cast("float").as("total_amount"),
          $"pickup_longitude".cast("float").as("pickup_lon"),
          $"pickup_latitude".cast("float").as("pickup_lat"),
          $"dropoff_longitude".cast("float").as("dropoff_lon"),
          $"dropoff_latitude".cast("float").as("dropoff_lat"),
          lit(0).cast("float").as("surcharge"),
          $"improvement_surcharge".cast("float").as("improvement_surcharge"),
          $"extra".cast("float").as("extra")
        )
      }

      // yellow_v4

      case "4" => {
        source.select(
          $"VendorID".as("vendor_id"),
          $"tpep_pickup_datetime".cast("timestamp").as("pickup_timestamp"),
          $"tpep_dropoff_datetime".cast("timestamp").as("dropoff_timestamp"),
          $"passenger_count".cast("int").as("passenger_count"),
          $"trip_distance".cast("float").as("trip_distance"),
          (unix_timestamp($"tpep_dropoff_datetime")-unix_timestamp($"tpep_pickup_datetime")).as("trip_second"),
          $"RatecodeID".as("rate_code"),
          $"store_and_fwd_flag".as("store_and_fwd_flag"),
          $"payment_type".as("payment_type"),
          $"fare_amount".cast("float").as("fare_amount"),
          $"mta_tax".cast("float").as("mta_tax"),
          $"tip_amount".cast("float").as("tip_amount"),
          $"tolls_amount".cast("float").as("tolls_amount"),
          $"total_amount".cast("float").as("total_amount"),
          lit(0).cast("float").as("pickup_lon"),
          lit(0).cast("float").as("pickup_lat"),
          lit(0).cast("float").as("dropoff_lon"),
          lit(0).cast("float").as("dropoff_lat"),
          lit(0).cast("float").as("surcharge"),
          $"improvement_surcharge".cast("float").as("improvement_surcharge"),
          $"extra".cast("float").as("extra"),
          $"PULocationID".cast("int").as("pickup_id"),
          $"DOLocationID".cast("int").as("dropoff_id")
        )
      }

      // yellow_v5

      case "5" => {
        source.select(
          $"VendorID".as("vendor_id"),
          $"tpep_pickup_datetime".cast("timestamp").as("pickup_timestamp"),
          $"tpep_dropoff_datetime".cast("timestamp").as("dropoff_timestamp"),
          $"passenger_count".cast("int").as("passenger_count"),
          $"trip_distance".cast("float").as("trip_distance"),
          (unix_timestamp($"tpep_dropoff_datetime")-unix_timestamp($"tpep_pickup_datetime")).as("trip_second"),
          $"RatecodeID".as("rate_code"),
          $"store_and_fwd_flag".as("store_and_fwd_flag"),
          $"payment_type".as("payment_type"),
          $"fare_amount".cast("float").as("fare_amount"),
          $"mta_tax".cast("float").as("mta_tax"),
          $"tip_amount".cast("float").as("tip_amount"),
          $"tolls_amount".cast("float").as("tolls_amount"),
          $"total_amount".cast("float").as("total_amount"),
          lit(0).cast("float").as("pickup_lon"),
          lit(0).cast("float").as("pickup_lat"),
          lit(0).cast("float").as("dropoff_lon"),
          lit(0).cast("float").as("dropoff_lat"),
          lit(0).cast("float").as("surcharge"),
          $"improvement_surcharge".cast("float").as("improvement_surcharge"),
          $"extra".cast("float").as("extra"),
          $"PULocationID".cast("int").as("pickup_id"),
          $"DOLocationID".cast("int").as("dropoff_id"),
          $"congestion_surcharge".cast("float").as("congestion_surcharge")
        )
      }

      case _  => {
        println("Invalid version: " + arguments.version)
        spark.stop()
        System.exit(1)
        source.select($"mta_tax".cast("float").as("mta_tax"))
      }
    }
    // write schema to yellow_v*.txt
    scala.Console.withOut(new PrintStream(new FileOutputStream(s"yellow_v${arguments.version}.txt"))) {
      target.printSchema
    }
    target.write.mode("append").json(arguments.outputDir)
    spark.stop()
  }
}