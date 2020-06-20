# README

Try out Spark [newAPIhadoopFile](https://spark.apache.org/docs/2.3.0/api/java/org/apache/spark/SparkContext.html#newAPIHadoopFile-java.lang.String-java.lang.Class-java.lang.Class-java.lang.Class-org.apache.hadoop.conf.Configuration-)
https://dzone.com/articles/implementing-hadoops-input-format-and-output-forma

## Development Memo

1. initial version - create project by following command:
    ```
    sbt new scala/scala-seed.g8
    ```
2. modify build.sbt - add `Apache Spark Core` and `Spark SQL` to libraryDependencies
    ```
    libraryDependencies ++= Seq(
      "org.apache.spark"  %%  "spark-core"    % "2.2.1",
      "org.apache.spark"  %%  "spark-sql"     % "2.2.1",
    )
    ```