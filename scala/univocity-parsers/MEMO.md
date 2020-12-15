# Development Notes

## 2020-12-15

- Reference:
  - https://stackoverflow.com/questions/52666231/how-to-write-to-a-csv-file-in-scala
  - https://github.com/uniVocity/csv-parsers-comparison
- Scala implementation
  - https://index.scala-lang.org/search?q=csv&page=1&topics=csv&sort=stars
  - https://index.scala-lang.org/search?q=csv&page=1&sort=relevant
  - https://github.com/nrinaudo/kantan.csv
  - https://github.com/tototoshi/scala-csv
- Quote:
  > univocity-parsers is currently used by many commercial and open-source projects, including **Spark-CSV**, **Apache Camel** and **Apache Drill**.
- Apache Spark use [univocity-parsers](https://github.com/uniVocity/univocity-parsers)
  - https://github.com/databricks/spark-csv/blob/master/build.sbt
  ```sbt
  libraryDependencies ++= Seq(
    "org.apache.commons" % "commons-csv" % "1.1",
    "com.univocity" % "univocity-parsers" % "1.5.1",
    "org.slf4j" % "slf4j-api" % "1.7.5" % "provided",
    "org.scalatest" %% "scalatest" % "2.2.1" % "test",
    "com.novocode" % "junit-interface" % "0.9" % "test"
  )
  ```
  - Apache Spark 3.0.0 use univocity-parsers `2.8.3`
  ```bash
  ~/spark$ ls jars/ | grep parser
  scala-parser-combinators_2.12-1.1.2.jar
  univocity-parsers-2.8.3.jar
  ```
- create project with `sbt --sbt-create`
```bash
~/git/snippet/scala$ mkdir univocity-parsers
~/git/snippet/scala$ cd univocity-parsers/
~/git/snippet/scala/univocity-parsers$ git gi sbt,scala > .gitignore
~/git/snippet/scala/univocity-parsers$ sbt --sbt-create
sbt:univocity-parsers> set ThisBuild / scalaVersion     := "2.12.12"
sbt:univocity-parsers> set libraryDependencies += "com.univocity" % "univocity-parsers" % "2.8.3"
sbt:univocity-parsers> update
sbt:univocity-parsers> session save-all
sbt:univocity-parsers> console
[info] Starting scala interpreter...
Welcome to Scala 2.12.12 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> import com.univocity.parsers.csv._
