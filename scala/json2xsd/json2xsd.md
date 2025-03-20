# Development Memo

- ( 2023-03-06 10:23:51 )
- https://github.com/ethlo/jsons2xsd
- test with `spark-shell --packages "com.ethlo.jsons2xsd:jsons2xsd:2.3.0"`
- Reference source code https://github.com/ethlo/jsons2xsd/blob/main/src/test/java/com/ethlo/jsons2xsd/ConversionTest.java
  - `com.ethlo.jsons2xsd.Jsons2Xsd.convert(Reader jsonSchema, Config cfg)` needs
    - (A) `java.io.Reader` & `java.io.InputStreamReader`
    - (B) `com.ethlo.jsons2xsd.Jsons2Xsd.Config`
```bash
jazzwang:~/git/snippet/scala/json2xsd$ spark-shell --packages "com.ethlo.jsons2xsd:jsons2xsd:2.3.0"
```
- ( 2023-03-06 10:50:05 )
```scala
import com.ethlo.jsons2xsd._
import java.io._

val r = new InputStreamReader(new FileInputStream("json/in-network-rates-multiple-plans-sample.json"))
val conf = new Config.Builder().createRootElement(false).targetNamespace("https://cms.gov/schema/in-network-rates.xsd").name("in-network-rates").ignoreUnknownFormats(true).build()

scala> Jsons2Xsd.convert(r, conf)
java.lang.IllegalArgumentException: type property of root node must be defined
  at com.ethlo.jsons2xsd.Assert.notNull(Assert.java:43)
  at com.ethlo.jsons2xsd.Jsons2Xsd.convert(Jsons2Xsd.java:110)
  at com.ethlo.jsons2xsd.Jsons2Xsd.convert(Jsons2Xsd.java:99)
  ... 51 elided
```

# Reference

- https://stackoverflow.com/questions/48376526/generate-xml-schemaxsd-from-json-schema