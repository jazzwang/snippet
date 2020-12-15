# Development Notes

## 2020-12-15

```bash
~/git/snippet/scala$ mkdir -p scala-csv
~/git/snippet/scala$ cd scala-csv/
~/git/snippet/scala/scala-csv$ git gi sbt,scala > .gitignore
~/git/snippet/scala/scala-csv$ sbt --sbt-create
sbt:scala-csv> set scalaVersion := "2.12.12"
sbt:scala-csv> set libraryDependencies += "com.github.tototoshi" %% "scala-csv" % "1.3.6"
sbt:scala-csv> update
sbt:scala-csv> session save
sbt:scala-csv> exit
```