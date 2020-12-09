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