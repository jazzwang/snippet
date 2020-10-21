import Dependencies._

ThisBuild / scalaVersion     := "2.11.11"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"
ThisBuild / semanticdbEnabled := true
ThisBuild / semanticdbVersion := "4.1.9"
ThisBuild / scalafixOnCompile := true
ThisBuild / scalacOptions     += "-Ywarn-unused-import" // required by `RemoveUnused` rule

lazy val root = (project in file("."))
  .settings(
    name := "spark-keyvalue",
    libraryDependencies ++= Seq(
      "org.apache.spark"  %%  "spark-core"    % "2.2.1",
      "org.apache.spark"  %%  "spark-sql"     % "2.2.1",
      scalaTest % Test
    )
  )

// https://stackoverflow.com/questions/24996437/how-to-execute-a-bash-script-as-sbt-task/25005
import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target output" !
}
// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
