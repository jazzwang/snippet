import Dependencies._

ThisBuild / scalaVersion     := "2.11.11"
ThisBuild / version          := "0.1.0"
ThisBuild / organization     := "com.example"
ThisBuild / organizationName := "example"

lazy val root = (project in file("."))
  .settings(
    name := "edireader-spark",
    libraryDependencies += scalaTest % Test
    // https://search.maven.org/artifact/com.berryworks/edireader/4.7.3.1/pom
    // https://mvnrepository.com/artifact/com.berryworks/edireader/4.7.3.1
    libraryDependencies += "com.berryworks" % "edireader" % "4.7.3.1"
  )

// See https://www.scala-sbt.org/1.x/docs/Using-Sonatype.html for instructions on how to publish to Sonatype.
