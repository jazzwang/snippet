## Learning Scala-XML

## 2020-11-26

- ( 2020-11-26 10:44:25 )
- [https://stackoverflow.com/a/2909165/4209274](https://stackoverflow.com/a/2909165/4209274)

```
scala> val src = scala.io.Source.fromFile("sample-data.xml")
src: scala.io.BufferedSource = <iterator>

scala> val er = new XMLEventReader(src)
warning: there was one deprecation warning (since 1.1.1); for details, enable `:setting -deprecation' or `:replay -deprecation'
er: scala.xml.pull.XMLEventReader = <iterator>
```

- ( 2020-11-26 10:52:05 )
- [https://alvinalexander.com/scala/how-to-extract-data-from-xml-nodes-in-scala/](https://alvinalexander.com/scala/how-to-extract-data-from-xml-nodes-in-scala/)

```scala
~$ JAVA_OPTS="-Xms1g -Xmx2g" scala
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> val xml = scala.xml.XML.loadFile("sample-data.xml")
xml: scala.xml.Elem =
... (skip) ...

scala> val members = xml \ "member"
members: scala.xml.NodeSeq =
... (skip) ...

scala> members(0)
res5: scala.xml.Node =
... (skip) ...

scala> val names = members(0) \ "names"
names: scala.xml.NodeSeq =
... (skip) ...

scala> names.length
res6: Int = 1

scala> val addresses = members(0) \ "addresses"
addresses: scala.xml.NodeSeq =

scala> addresses.length
res7: Int = 1
```

## 2020-12-09

- ( 2020-12-09 16:46:12 )
- Goal:
    - filter only `male` and `female`
    - sample 100 records from 10000 members.
    - store as `sample.xml`
- Reference:
    - `filter`: https://stackoverflow.com/a/10142885/4209274
    - `save`: https://alvinalexander.com/scala/scala-save-write-xml-data-string-to-file/
```
~/git/snippet/scala/scala-xml$ JAVA_OPTS="-Xms1g -Xmx2g" scala
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> import java.io._
scala> val xml = scala.xml.XML.loadFile("/tmp/sample.xml")
scala> val members = xml \ "member"
scala> members.length
res0: Int = 10000
scala> (members \\ "gender").map(x => (x.text, 1)).groupBy(x => x._1).map(x => (x._1, x._2.length))
res13: scala.collection.immutable.Map[String,Int] = Map(male -> 2450, unknown -> 2580, female -> 2495, other -> 2475)
scala> 2450+2495
res15: Int = 4945
scala> members.filterNot(x => (x \\ "gender").text.contains("unknown")).filterNot(x => (x \\ "gender").text.contains("other")).length
res14: Int = 4945
scala> val samples = members.filterNot(x => (x \\ "gender").text.contains("unknown")).filterNot(x => (x \\ "gender").text.contains("other")).take(100)
samples: scala.xml.NodeSeq =
... (skip) ...
scala> val prettyPrinter = new scala.xml.PrettyPrinter(80, 2)
scala> val bw = new BufferedWriter(new FileWriter(new File("samples.xml")))
scala> bw.write("<sample>")
scala> samples.foreach( x => bw.write(prettyPrinter.format(x)) )
scala> bw.write("</sample>")
scala> bw.close
scala> import scala.io.Source
scala> val xmlString = Source.fromFile("samples.xml").getLines.mkString
scala> xmlString.length
res9: Int = 236336
scala> val xml2 = scala.xml.XML.loadString(xmlString)
scala> (xml2 \ "member").length
res1: Int = 100
```
- NOTE: convert to single String will have length limitations
```
scala> val prettyXML = prettyPrinter.formatted(samples.toString)
scala> prettyXML.length
res32: Int = 307887
scala> samples.toString.length
res49: Int = 307887
scala> samples.mkString.length
res50: Int = 307887
```