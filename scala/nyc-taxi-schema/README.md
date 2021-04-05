# README

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