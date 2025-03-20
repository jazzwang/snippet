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
```scala
import com.github.tototoshi.csv._
val xml = scala.xml.XML.loadFile("samples.xml")
val members = xml \ "member"
members(0) \\ "state"
(members(0) \\ "state").text
(members(0) \\ "city").text
(members(0) \\ "line").text
(members(0) \\ "name").text
members(0) \\ "name"
members(0) \\ "family"
members(0) \\ "given"
val writer = CSVWriter.open("samples.csv", append = true)
members.foreach( member => {
  val state = (member \\ "state").text
  val city = (member \\ "city").text
  println(s"state=$state, city=$city")
})
members(0)
println(members(0))
CSV.foreach( x => println(x.length) )
```