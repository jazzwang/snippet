#!/bin/bash
sbt package
spark-submit --packages "com.github.scopt:scopt_2.12:4.0.0" --class example.NYC2Parquet target/scala-2.12/nyc2parquet_2.12-0.1.0.jar -i nyc-tlc/yellow_v1 -o parquet/v1 -v 1
spark-submit --packages "com.github.scopt:scopt_2.12:4.0.0" --class example.NYC2Parquet target/scala-2.12/nyc2parquet_2.12-0.1.0.jar -i nyc-tlc/yellow_v2 -o parquet/v2 -v 2
spark-submit --packages "com.github.scopt:scopt_2.12:4.0.0" --class example.NYC2Parquet target/scala-2.12/nyc2parquet_2.12-0.1.0.jar -i nyc-tlc/yellow_v3 -o parquet/v3 -v 3
spark-submit --packages "com.github.scopt:scopt_2.12:4.0.0" --class example.NYC2Parquet target/scala-2.12/nyc2parquet_2.12-0.1.0.jar -i nyc-tlc/yellow_v4 -o parquet/v4 -v 4
spark-submit --packages "com.github.scopt:scopt_2.12:4.0.0" --class example.NYC2Parquet target/scala-2.12/nyc2parquet_2.12-0.1.0.jar -i nyc-tlc/yellow_v5 -o parquet/v5 -v 5
