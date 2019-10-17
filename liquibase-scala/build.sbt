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
      "org.xerial"        %   "sqlite-jdbc"   % "3.8.11"
    )
    // https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc/
  )

// https://index.scala-lang.org/permutive/sbt-liquibase-plugin

import com.permutive.sbtliquibase.SbtLiquibase
enablePlugins(SbtLiquibase)
// https://www.liquibase.org/sqlite.html
liquibaseUsername := ""
liquibasePassword := ""
liquibaseDriver   := "org.sqlite.JDBC"
liquibaseUrl      := "jdbc:sqlite:sample.db"

// https://stackoverflow.com/questions/24996437/how-to-execute-a-bash-script-as-sbt-task/25005

import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target sample.db" !
}

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.