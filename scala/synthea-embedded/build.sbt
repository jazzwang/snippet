ThisBuild / scalaVersion     := "2.11.11"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "Spark in Scala Seed Project",
    libraryDependencies ++= Seq(
      // "org.mitre.synthea" %   "synthea"       % "2.6.1",
      "org.scalatest"     %%  "scalatest"     % "3.1.1"
    )
  )

// https://stackoverflow.com/questions/24996437/how-to-execute-a-bash-script-as-sbt-task/25005

import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target output spark-warehouse" !
}

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
