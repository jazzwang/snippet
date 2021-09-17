ThisBuild / scalaVersion     := "2.12.10"
ThisBuild / version          := "0.1.1"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "spark-stream-file-io",
    libraryDependencies ++= Seq(
      "org.apache.spark"  %%  "spark-core"      % "3.0.0",
      // https://mvnrepository.com/artifact/org.apache.spark/spark-streaming_2.12/3.0.0
      "org.apache.spark"  %%  "spark-streaming" % "3.0.0",
      "org.scalatest"     %%  "scalatest"       % "3.1.1"
    )
  )

// https://stackoverflow.com/questions/24996437/how-to-execute-a-bash-script-as-sbt-task/25005

import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target input/.new-file.txt.crc input/new-file.txt" !
}

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
