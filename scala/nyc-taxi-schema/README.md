# README

[TOC]

## Execution

```
sbt run
```

## Clean up

```
sbt distclean
```

## Results

```
cat yellow_v*.txt

root
 |-- vendor_name: string (nullable = true)
 |-- Trip_Pickup_DateTime: string (nullable = true)
 |-- Trip_Dropoff_DateTime: string (nullable = true)
 |-- Passenger_Count: string (nullable = true)
 |-- Trip_Distance: string (nullable = true)
 |-- Start_Lon: string (nullable = true)
 |-- Start_Lat: string (nullable = true)
 |-- Rate_Code: string (nullable = true)
 |-- store_and_forward: string (nullable = true)
 |-- End_Lon: string (nullable = true)
 |-- End_Lat: string (nullable = true)
 |-- Payment_Type: string (nullable = true)
 |-- Fare_Amt: string (nullable = true)
 |-- surcharge: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- Tip_Amt: string (nullable = true)
 |-- Tolls_Amt: string (nullable = true)
 |-- Total_Amt: string (nullable = true)

root
 |-- vendor_id: string (nullable = true)
 |-- pickup_datetime: string (nullable = true)
 |-- dropoff_datetime: string (nullable = true)
 |-- passenger_count: string (nullable = true)
 |-- trip_distance: string (nullable = true)
 |-- pickup_longitude: string (nullable = true)
 |-- pickup_latitude: string (nullable = true)
 |-- rate_code: string (nullable = true)
 |-- store_and_fwd_flag: string (nullable = true)
 |-- dropoff_longitude: string (nullable = true)
 |-- dropoff_latitude: string (nullable = true)
 |-- payment_type: string (nullable = true)
 |-- fare_amount: string (nullable = true)
 |-- surcharge: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- tip_amount: string (nullable = true)
 |-- tolls_amount: string (nullable = true)
 |-- total_amount: string (nullable = true)

root
 |-- VendorID: string (nullable = true)
 |-- tpep_pickup_datetime: string (nullable = true)
 |-- tpep_dropoff_datetime: string (nullable = true)
 |-- passenger_count: string (nullable = true)
 |-- trip_distance: string (nullable = true)
 |-- pickup_longitude: string (nullable = true)
 |-- pickup_latitude: string (nullable = true)
 |-- RatecodeID: string (nullable = true)
 |-- store_and_fwd_flag: string (nullable = true)
 |-- dropoff_longitude: string (nullable = true)
 |-- dropoff_latitude: string (nullable = true)
 |-- payment_type: string (nullable = true)
 |-- fare_amount: string (nullable = true)
 |-- extra: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- tip_amount: string (nullable = true)
 |-- tolls_amount: string (nullable = true)
 |-- improvement_surcharge: string (nullable = true)
 |-- total_amount: string (nullable = true)

root
 |-- VendorID: string (nullable = true)
 |-- tpep_pickup_datetime: string (nullable = true)
 |-- tpep_dropoff_datetime: string (nullable = true)
 |-- passenger_count: string (nullable = true)
 |-- trip_distance: string (nullable = true)
 |-- RatecodeID: string (nullable = true)
 |-- store_and_fwd_flag: string (nullable = true)
 |-- PULocationID: string (nullable = true)
 |-- DOLocationID: string (nullable = true)
 |-- payment_type: string (nullable = true)
 |-- fare_amount: string (nullable = true)
 |-- extra: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- tip_amount: string (nullable = true)
 |-- tolls_amount: string (nullable = true)
 |-- improvement_surcharge: string (nullable = true)
 |-- total_amount: string (nullable = true)

root
 |-- VendorID: string (nullable = true)
 |-- tpep_pickup_datetime: string (nullable = true)
 |-- tpep_dropoff_datetime: string (nullable = true)
 |-- passenger_count: string (nullable = true)
 |-- trip_distance: string (nullable = true)
 |-- RatecodeID: string (nullable = true)
 |-- store_and_fwd_flag: string (nullable = true)
 |-- PULocationID: string (nullable = true)
 |-- DOLocationID: string (nullable = true)
 |-- payment_type: string (nullable = true)
 |-- fare_amount: string (nullable = true)
 |-- extra: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- tip_amount: string (nullable = true)
 |-- tolls_amount: string (nullable = true)
 |-- improvement_surcharge: string (nullable = true)
 |-- total_amount: string (nullable = true)
 |-- congestion_surcharge: string (nullable = true)
```

## Visualization

<style id="nyc-tlc-schema-changes_5515_Styles">
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
@page
	{margin:.75in .7in .75in .7in;
	mso-header-margin:.3in;
	mso-footer-margin:.3in;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
.style0
	{mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	white-space:nowrap;
	mso-rotate:0;
	mso-background-source:auto;
	mso-pattern:auto;
	color:black;
	font-size:12.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;
	border:none;
	mso-protection:locked visible;
	mso-style-name:Normal;
	mso-style-id:0;}
td
	{mso-style-parent:style0;
	padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:12.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl63
	{mso-style-parent:style0;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;}
.xl64
	{mso-style-parent:style0;
	color:white;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	background:#0070C0;
	mso-pattern:black none;}
.xl65
	{mso-style-parent:style0;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	background:#DDEBF7;
	mso-pattern:black none;}
.xl66
	{mso-style-parent:style0;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	background:#E2EFDA;
	mso-pattern:black none;}
.xl67
	{mso-style-parent:style0;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	background:#FFF2CC;
	mso-pattern:black none;}
.xl68
	{mso-style-parent:style0;
	font-family:"Lucida Console", sans-serif;
	mso-font-charset:0;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	background:#FCE4D6;
	mso-pattern:black none;}
-->
</style>

<table border="0" cellpadding="0" cellspacing="0" width="1235" style="border-collapse:
 collapse;table-layout:fixed;width:925pt">
 <colgroup><col width="247" span="5" style="mso-width-source:userset;mso-width-alt:7893;
 width:185pt">
 </colgroup><tbody><tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl64" width="247" style="height:24.0pt;width:185pt">v1</td>
  <td class="xl64" width="247" style="border-left:none;width:185pt">v2</td>
  <td class="xl64" width="247" style="border-left:none;width:185pt">v3</td>
  <td class="xl64" width="247" style="border-left:none;width:185pt">v4</td>
  <td class="xl64" width="247" style="border-left:none;width:185pt">v5</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">vendor_name</td>
  <td class="xl63" style="border-top:none;border-left:none">vendor_id</td>
  <td class="xl63" style="border-top:none;border-left:none">VendorID</td>
  <td class="xl63" style="border-top:none;border-left:none">VendorID</td>
  <td class="xl63" style="border-top:none;border-left:none">VendorID</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">Trip_Pickup_DateTime</td>
  <td class="xl65" style="border-top:none;border-left:none">pickup_datetime</td>
  <td class="xl65" style="border-top:none;border-left:none">tpep_pickup_datetime</td>
  <td class="xl65" style="border-top:none;border-left:none">tpep_pickup_datetime</td>
  <td class="xl65" style="border-top:none;border-left:none">tpep_pickup_datetime</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Trip_Dropoff_DateTime</td>
  <td class="xl63" style="border-top:none;border-left:none">dropoff_datetime</td>
  <td class="xl63" style="border-top:none;border-left:none">tpep_dropoff_datetime</td>
  <td class="xl63" style="border-top:none;border-left:none">tpep_dropoff_datetime</td>
  <td class="xl63" style="border-top:none;border-left:none">tpep_dropoff_datetime</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">Passenger_Count</td>
  <td class="xl65" style="border-top:none;border-left:none">passenger_count</td>
  <td class="xl65" style="border-top:none;border-left:none">passenger_count</td>
  <td class="xl65" style="border-top:none;border-left:none">passenger_count</td>
  <td class="xl65" style="border-top:none;border-left:none">passenger_count</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Trip_Distance</td>
  <td class="xl63" style="border-top:none;border-left:none">trip_distance</td>
  <td class="xl63" style="border-top:none;border-left:none">trip_distance</td>
  <td class="xl63" style="border-top:none;border-left:none">trip_distance</td>
  <td class="xl63" style="border-top:none;border-left:none">trip_distance</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl66" style="height:24.0pt;border-top:none">Start_Lon</td>
  <td class="xl66" style="border-top:none;border-left:none">pickup_longitude</td>
  <td class="xl66" style="border-top:none;border-left:none">pickup_longitude</td>
  <td rowspan="2" class="xl66" style="border-top:none">PULocationID</td>
  <td rowspan="2" class="xl66" style="border-top:none">PULocationID</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl66" style="height:24.0pt;border-top:none">Start_Lat</td>
  <td class="xl66" style="border-top:none;border-left:none">pickup_latitude</td>
  <td class="xl66" style="border-top:none;border-left:none">pickup_latitude</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Rate_Code</td>
  <td class="xl63" style="border-top:none;border-left:none">rate_code</td>
  <td class="xl63" style="border-top:none;border-left:none">RatecodeID</td>
  <td class="xl63" style="border-top:none;border-left:none">RatecodeID</td>
  <td class="xl63" style="border-top:none;border-left:none">RatecodeID</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">store_and_forward</td>
  <td class="xl65" style="border-top:none;border-left:none">store_and_fwd_flag</td>
  <td class="xl65" style="border-top:none;border-left:none">store_and_fwd_flag</td>
  <td class="xl65" style="border-top:none;border-left:none">store_and_fwd_flag</td>
  <td class="xl65" style="border-top:none;border-left:none">store_and_fwd_flag</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl66" style="height:24.0pt;border-top:none">End_Lon</td>
  <td class="xl66" style="border-top:none;border-left:none">dropoff_longitude</td>
  <td class="xl66" style="border-top:none;border-left:none">dropoff_longitude</td>
  <td rowspan="2" class="xl66" style="border-top:none">DOLocationID</td>
  <td rowspan="2" class="xl66" style="border-top:none">DOLocationID</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl66" style="height:24.0pt;border-top:none">End_Lat</td>
  <td class="xl66" style="border-top:none;border-left:none">dropoff_latitude</td>
  <td class="xl66" style="border-top:none;border-left:none">dropoff_latitude</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Payment_Type</td>
  <td class="xl63" style="border-top:none;border-left:none">payment_type</td>
  <td class="xl63" style="border-top:none;border-left:none">payment_type</td>
  <td class="xl63" style="border-top:none;border-left:none">payment_type</td>
  <td class="xl63" style="border-top:none;border-left:none">payment_type</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">Fare_Amt</td>
  <td class="xl65" style="border-top:none;border-left:none">fare_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">fare_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">fare_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">fare_amount</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">surcharge</td>
  <td class="xl63" style="border-top:none;border-left:none">surcharge</td>
  <td class="xl63" style="border-top:none;border-left:none">extra</td>
  <td class="xl63" style="border-top:none;border-left:none">extra</td>
  <td class="xl63" style="border-top:none;border-left:none">extra</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">mta_tax</td>
  <td class="xl65" style="border-top:none;border-left:none">mta_tax</td>
  <td class="xl65" style="border-top:none;border-left:none">mta_tax</td>
  <td class="xl65" style="border-top:none;border-left:none">mta_tax</td>
  <td class="xl65" style="border-top:none;border-left:none">mta_tax</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Tip_Amt</td>
  <td class="xl63" style="border-top:none;border-left:none">tip_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">tip_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">tip_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">tip_amount</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl65" style="height:24.0pt;border-top:none">Tolls_Amt</td>
  <td class="xl65" style="border-top:none;border-left:none">tolls_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">tolls_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">tolls_amount</td>
  <td class="xl65" style="border-top:none;border-left:none">tolls_amount</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">&nbsp;</td>
  <td class="xl63" style="border-top:none;border-left:none">&nbsp;</td>
  <td class="xl67" style="border-top:none;border-left:none">improvement_surcharge</td>
  <td class="xl67" style="border-top:none;border-left:none">improvement_surcharge</td>
  <td class="xl67" style="border-top:none;border-left:none">improvement_surcharge</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">Total_Amt</td>
  <td class="xl63" style="border-top:none;border-left:none">total_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">total_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">total_amount</td>
  <td class="xl63" style="border-top:none;border-left:none">total_amount</td>
 </tr>
 <tr height="32" style="mso-height-source:userset;height:24.0pt">
  <td height="32" class="xl63" style="height:24.0pt;border-top:none">&nbsp;</td>
  <td class="xl63" style="border-top:none;border-left:none">&nbsp;</td>
  <td class="xl63" style="border-top:none;border-left:none">&nbsp;</td>
  <td class="xl63" style="border-top:none;border-left:none">&nbsp;</td>
  <td class="xl68" style="border-top:none;border-left:none">congestion_surcharge</td>
 </tr>
 <!--[if supportMisalignedColumns]-->
 <tr height="0" style="display:none">
  <td width="247" style="width:185pt"></td>
  <td width="247" style="width:185pt"></td>
  <td width="247" style="width:185pt"></td>
  <td width="247" style="width:185pt"></td>
  <td width="247" style="width:185pt"></td>
 </tr>
 <!--[endif]-->
</tbody></table>

# Development Notes

## 2021-04-10

- Q: spark-shell 到底 import 了哪些類別呢？
```
~$ spark-shell
21/04/10 16:41:34 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = local[*], app id = local-1618044112157).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.0
      /_/

Using Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_282)
Type in expressions to have them evaluated.
Type :help for more information.

scala> :imports
 1) import java.lang._             (118 types, 124 terms)
 2) import scala._                 (178 types, 172 terms)
 3) import scala.Predef._          (125 terms, 62 are implicit)
 4) import org.apache.spark.SparkContext._ (71 terms, 1 are implicit)
 5) import spark.implicits._       (1 types, 69 terms, 39 are implicit)
 6) import spark.sql               (1 terms)
 7) import org.apache.spark.sql.functions._ (422 terms)
 ```

## 2021-04-11

### Schema v1

- 觀察資料分布狀況:
```
~/git/snippet/scala/nyc-taxi-schema$ sbt console

scala> :paste
```
- 貼上程式碼
```
import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder.master("local[*]").getOrCreate
val sc = spark.sparkContext
import spark.implicits._
val df1 = spark.read.option("header","true").csv("nyc-tlc/yellow_v1")
df1.printSchema
df1.select($"Rate_Code").distinct.show
df1.select($"vendor_name").distinct.show
df1.select($"Trip_Pickup_DateTime").distinct.show
df1.select($"Trip_Dropoff_DateTime").distinct.show
df1.select($"Passenger_Count").distinct.show
df1.select($"Trip_Distance").distinct.show
df1.select($"Start_Lon").distinct.show
df1.select($"Start_Lat").distinct.show
df1.select($"Rate_Code").distinct.show
df1.select($"store_and_forward").distinct.show
df1.select($"End_Lon").distinct.show
df1.select($"End_Lat").distinct.show
df1.select($"Payment_Type").distinct.show
df1.select($"Fare_Amt").distinct.show
df1.select($"surcharge").distinct.show
df1.select($"mta_tax").distinct.show
df1.select($"Tip_Amt").distinct.show
df1.select($"Tolls_Amt").distinct.show
df1.select($"Total_Amt").distinct.show
```
- 觀察結果，以利判斷各欄位合適的資料型態
```
root
 |-- vendor_name: string (nullable = true)
 |-- Trip_Pickup_DateTime: string (nullable = true)
 |-- Trip_Dropoff_DateTime: string (nullable = true)
 |-- Passenger_Count: string (nullable = true)
 |-- Trip_Distance: string (nullable = true)
 |-- Start_Lon: string (nullable = true)
 |-- Start_Lat: string (nullable = true)
 |-- Rate_Code: string (nullable = true)
 |-- store_and_forward: string (nullable = true)
 |-- End_Lon: string (nullable = true)
 |-- End_Lat: string (nullable = true)
 |-- Payment_Type: string (nullable = true)
 |-- Fare_Amt: string (nullable = true)
 |-- surcharge: string (nullable = true)
 |-- mta_tax: string (nullable = true)
 |-- Tip_Amt: string (nullable = true)
 |-- Tolls_Amt: string (nullable = true)
 |-- Total_Amt: string (nullable = true)

+---------+
|Rate_Code|
+---------+
|     null|
+---------+

+-----------+
|vendor_name|
+-----------+
|        CMT|
|        VTS|
|        DDS|
+-----------+

+--------------------+
|Trip_Pickup_DateTime|
+--------------------+
| 2009-11-23 16:19:00|
| 2009-08-12 13:56:00|
| 2009-01-04 03:31:00|
| 2009-12-21 14:19:00|
| 2009-07-15 17:22:00|
| 2009-02-28 00:26:00|
| 2009-11-22 05:13:00|
| 2009-03-26 15:30:14|
| 2009-09-23 17:58:00|
| 2009-04-08 12:19:00|
| 2009-07-14 21:49:00|
| 2009-05-27 07:41:05|
| 2009-05-15 15:22:02|
| 2009-04-06 21:31:00|
| 2009-04-08 09:37:00|
| 2009-09-24 09:00:00|
| 2009-11-17 08:24:00|
| 2009-03-07 00:09:04|
| 2009-04-06 23:26:00|
| 2009-06-10 18:08:00|
+--------------------+
only showing top 20 rows

+---------------------+
|Trip_Dropoff_DateTime|
+---------------------+
|  2009-05-15 15:30:15|
|  2009-06-10 19:52:00|
|  2009-12-18 03:34:00|
|  2009-06-14 21:08:00|
|  2009-11-17 13:57:00|
|  2009-12-14 21:33:00|
|  2009-12-17 12:36:00|
|  2009-08-12 09:08:00|
|  2009-01-04 04:36:00|
|  2009-06-14 23:48:00|
|  2009-07-14 21:52:00|
|  2009-10-26 11:52:00|
|  2009-08-12 14:12:00|
|  2009-09-26 12:07:00|
|  2009-04-06 21:35:00|
|  2009-04-06 23:41:00|
|  2009-02-28 09:43:00|
|  2009-10-26 13:17:00|
|  2009-04-06 19:41:00|
|  2009-10-26 11:41:00|
+---------------------+
only showing top 20 rows

+---------------+
|Passenger_Count|
+---------------+
|              3|
|              5|
|              1|
|              2|
+---------------+

+-------------------+
|      Trip_Distance|
+-------------------+
|              17.52|
|               1.53|
|               0.11|
| 1.8899999999999999|
|              11.09|
|               1.74|
| 8.9800000000000004|
|               1.28|
| 2.2000000000000002|
|                  0|
| 3.4900000000000002|
| 3.0099999999999998|
|0.90000000000000002|
|0.29999999999999999|
| 1.5600000000000001|
| 1.3200000000000001|
|                  5|
|0.93999999999999995|
|0.69999999999999996|
| 3.6899999999999999|
+-------------------+
only showing top 20 rows

+-------------------+
|          Start_Lon|
+-------------------+
|-73.984049999999996|
|-73.982212000000004|
|-73.978116999999997|
|-73.992767999999998|
|-73.973804999999999|
|-73.983037999999993|
|-73.977772999999999|
|-73.955744999999993|
|-73.787441999999999|
|-73.993183000000002|
|-74.007315000000006|
|         -73.973343|
|-74.005256000000003|
|-73.984650000000002|
|          -73.97748|
|                  0|
|-73.966408000000001|
|-73.989806000000002|
|-73.978967999999995|
|-73.949727999999993|
+-------------------+
only showing top 20 rows

+------------------+
|         Start_Lat|
+------------------+
|40.738854000000003|
|40.739964000000001|
|40.719382000000003|
|40.776826999999997|
|40.761691999999996|
|40.711829999999999|
|         40.748362|
|40.749082000000001|
|40.749802000000003|
|40.784092999999999|
|40.756548000000002|
|40.767453000000003|
|40.728048000000001|
|                 0|
|40.720452999999999|
|40.648707999999999|
|40.782170000000001|
|40.735005999999998|
|40.715288000000001|
|40.766579999999998|
+------------------+
only showing top 20 rows

+---------+
|Rate_Code|
+---------+
|     null|
+---------+

+-----------------+
|store_and_forward|
+-----------------+
|                0|
|             null|
+-----------------+

+-------------------+
|            End_Lon|
+-------------------+
|-73.911742000000004|
|          -73.98733|
|-73.993205000000003|
|-73.989653000000004|
|-73.968086999999997|
|-73.967303000000001|
|-73.991356999999994|
|-73.981227000000004|
|-73.997487000000007|
|-73.957516999999996|
|-73.972117999999995|
|-73.962441999999996|
|-73.852693000000002|
|-73.960651999999996|
|-73.996103000000005|
|-73.987342999999996|
|                  0|
|         -74.004745|
|-73.995585000000005|
|-73.955849999999998|
+-------------------+
only showing top 20 rows

+------------------+
|           End_Lat|
+------------------+
|         40.770277|
|40.751879000000002|
|         40.725158|
|         40.721342|
|40.739637000000002|
|40.742963000000003|
|40.774900000000002|
|40.759954999999998|
|         40.769911|
|40.736347000000002|
|40.771680000000003|
|40.737094999999997|
|40.767453000000003|
|          40.76549|
|40.739615000000001|
|                 0|
|40.727347000000002|
|40.746405000000003|
|40.667095000000003|
|40.745057000000003|
+------------------+
only showing top 20 rows

+------------+
|Payment_Type|
+------------+
|   No Charge|
|        CASH|
|      Credit|
|        Cash|
|     Dispute|
|      CREDIT|
+------------+

+------------------+
|          Fare_Amt|
+------------------+
|               8.5|
|              26.5|
|                 7|
|25.699999999999999|
|8.0999999999999996|
|23.699999999999999|
|6.9000000000000004|
|                 3|
|9.6999999999999993|
|15.699999999999999|
|3.2999999999999998|
|5.4000000000000004|
|               4.5|
|              10.9|
|               6.5|
|5.7000000000000002|
|7.7000000000000002|
|16.100000000000001|
|36.899999999999999|
|              12.6|
+------------------+
only showing top 20 rows

+---------+
|surcharge|
+---------+
|        0|
|      0.5|
|        1|
+---------+

+-------+
|mta_tax|
+-------+
|   null|
|    0.5|
+-------+

+-------------------+
|            Tip_Amt|
+-------------------+
| 7.4800000000000004|
| 3.2200000000000002|
|               1.23|
|                  3|
| 4.7400000000000002|
|                  0|
|0.90000000000000002|
|0.69999999999999996|
| 8.9399999999999995|
| 2.8399999999999999|
|                1.5|
|                  9|
|                  1|
|                5.5|
| 1.1399999999999999|
| 3.0499999999999998|
|                  2|
+-------------------+

+------------------+
|         Tolls_Amt|
+------------------+
|4.5700000000000003|
|                 0|
|4.1500000000000004|
+------------------+

+------------------+
|         Total_Amt|
+------------------+
|               8.5|
|58.149999999999999|
|                 7|
|8.0999999999999996|
|                11|
|6.9000000000000004|
|                 3|
|9.4000000000000004|
|3.2999999999999998|
|5.4000000000000004|
|                 8|
|6.7000000000000002|
|               4.5|
|              10.9|
|               6.5|
|              11.1|
|7.7999999999999998|
|44.880000000000003|
|10.699999999999999|
|8.9299999999999997|
+------------------+
only showing top 20 rows
```
- ( 2021-04-11 19:39:04 )
- 想到一個更精簡的寫法：
```scala
import org.apache.spark.sql.functions._
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder.master("local[*]").getOrCreate
val sc = spark.sparkContext
val df1 = spark.read.option("header","true").csv("nyc-tlc/yellow_v1")
for (i <- df1.columns)
     df1.select(col(s"$i")).distinct.show
```