ThisBuild / scalaVersion     := "2.11.11"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "C-CDA Generator",
    libraryDependencies ++= Seq(
      "org.scalatest"     %%  "scalatest"     % "3.1.1"
      )
  )

import scala.sys.process._

lazy val downloadJar = taskKey[Unit]("Download synthea-with-dependencies.jar from bintray")
downloadJar := {
  val libDir = new java.io.File("lib")
  if (! libDir.exists ) {
    libDir.mkdirs
  }
  // http://alvinalexander.com/scala/scala-how-to-download-url-contents-to-string-file/
  if (! new File("lib/synthea-with-dependencies.jar").exists ) {
    "wget -O lib/synthea-with-dependencies.jar https://dl.bintray.com/jazzwang/generic/synthea-with-dependencies.jar" !
  }
}
// https://stackoverflow.com/a/47654822/4209274
(Compile / compile) := ((Compile / compile) dependsOn downloadJar).value

// https://stackoverflow.com/a/25005651/4209274
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target output/ccda/*.xml spark-warehouse" !
}

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
