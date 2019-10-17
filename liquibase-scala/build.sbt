import Dependencies._

ThisBuild / scalaVersion     := "2.11.11"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "liquibase-scala",
    libraryDependencies ++= Seq(
      "org.apache.spark"  %%  "spark-core"    % "2.2.1",
      "org.apache.spark"  %%  "spark-sql"     % "2.2.1",
      "mysql"             % "mysql-connector-java" % "8.0.15" 
    )
    // https://mvnrepository.com/artifact/mysql/mysql-connector-java
    // https://stackoverflow.com/questions/20779764/how-to-set-dependency-as-runtime-in-sbt-to-mimic-runtime-scope-in-maven
    // https://stackoverflow.com/questions/27718382/how-to-work-with-mysql-and-apache-spark
  )

// https://index.scala-lang.org/permutive/sbt-liquibase-plugin
import com.permutive.sbtliquibase.SbtLiquibase
enablePlugins(SbtLiquibase)
liquibaseUsername := ""
liquibasePassword := ""
liquibaseDriver   := "com.mysql.cj.jdbc.Driver"
liquibaseUrl      := "jdbc:mysql://localhost:3306/test_db?createDatabaseIfNotExist=true"

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
