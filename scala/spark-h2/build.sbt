import Dependencies._

ThisBuild / scalaVersion     := "2.13.3"
ThisBuild / version          := "0.1.0-SNAPSHOT"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "scala-h2-db-embedded",
    libraryDependencies += scalaTest % Test,
    libraryDependencies += "com.h2database" % "h2" % "1.4.200"
  )

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
