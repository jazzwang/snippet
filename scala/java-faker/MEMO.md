# Development Notes

- Source: https://github.com/DiUS/java-faker
- Web: http://dius.github.io/java-faker/
- Java Docs: http://dius.github.io/java-faker/apidocs/index.html

## 2021-01-04

```bash
~/git/snippet/scala$ mkdir java-faker
~/git/snippet/scala$ cd java-faker/
~/git/snippet/scala/java-faker$ code MEMO.md
~/git/snippet/scala/java-faker$ git gi sbt,scala > .gitignore
~/git/snippet/scala/java-faker$ sbt --sbt-create
sbt:java-faker> set ThisBuild / scalaVersion     := "2.12.12"
sbt:java-faker> set ThisBuild / version          := "0.1.0"
sbt:java-faker> set libraryDependencies += "com.github.javafaker" % "javafaker" % "1.0.2"
sbt:java-faker> update
sbt:java-faker> session save-all
sbt:java-faker> exit
```