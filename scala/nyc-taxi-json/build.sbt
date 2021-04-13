ThisBuild / scalaVersion     := "2.12.12"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "NYC2JSON",
    libraryDependencies ++= Seq(
      "org.apache.spark"  %%  "spark-core"    % "3.0.0",
      "org.apache.spark"  %%  "spark-sql"     % "3.0.0",
      "com.github.scopt"  %%  "scopt"         % "4.0.0"
    )
  )

// https://stackoverflow.com/a/25005651/4209274
import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target output spark-warehouse yellow_v*.txt" !
}