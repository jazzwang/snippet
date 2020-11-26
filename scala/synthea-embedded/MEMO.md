# Development MEMO

## 2020-11-24

- https://github.com/synthetichealth/synthea/wiki/Embedding

## 2020-11-26

- https://github.com/synthetichealth/synthea/wiki/Embedding#json-integration
- reference [sbt-create](../sbt-create/MEMO.md)
- manually use java11 instead of java8
```
jazzwang:~$ wget https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_osx-x64_bin.tar.gz
jazzwang:~$ tar zxvf openjdk-11.0.2_osx-x64_bin.tar.gz
jazzwang:~$ rm openjdk-11.0.2_osx-x64_bin.tar.gz
jazzwang:~$ mv jdk-11.0.2.jdk/ jdk11
jazzwang:~$ export PATH=~/jdk11/Contents/Home/bin:$PATH
jazzwang:~$ which java
/Users/jazzwang/jdk11/Contents/Home/bin/java
jazzwang:~$ java -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```
- ( 2020-11-26 14:32:45 ) encounter class version issue again with JDK11
```
jazzwang:~$ cd ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/snippet/scala/synthea-embedded$ sbt console
scala> import org.mitre.synthea.engine._
scala> val options = new org.mitre.synthea.engine.Generator.GeneratorOptions();
java.lang.UnsupportedClassVersionError: org/mitre/synthea/engine/Generator$GeneratorOptions has been compiled by a more recent version of the Java Runtime (class file version 58.0), this version of the Java Runtime only recognizes class file versions up to 55.0
  ... (skipped) ...
```
- ( 2020-11-26 14:49:57 ) compile synthea with jdk8
```bash
jazzwang:~$ cd git/synthea
jazzwang:~/git/synthea$ git checkout v2.6.1
jazzwang:~/git/synthea$ ./gradlew jar
jazzwang:~/git/synthea$ cp build/libs/synthea.jar ~/git/snippet/scala/synthea-embedded/
```
- ( 2020-11-26 15:13:22 ) loading synthea.jar (without dependencies) to scala REPL
```
jazzwang:~/git/synthea$ cd ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/snippet/scala/synthea-embedded$ scala -cp synthea.jar
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.
```
- ( 2020-11-26 15:14:46 ) interactive testing
```scala
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._
import org.mitre.synthea.datastore.DataStore
import java.util.concurrent._

val options = new Generator.GeneratorOptions();
Config.set("exporter.fhir.export", "false");
Config.set("exporter.hospital.fhir.export", "false");
Config.set("exporter.practitioner.fhir.export", "false");

val ero = new Exporter.ExporterRuntimeOptions();
ero.enableQueue(Exporter.SupportedFhirVersion.R4);

val generator = new Generator(options, ero);

```
- Error
```scala
scala> val generator = new Generator(options, ero);
java.lang.NoClassDefFoundError: com/google/gson/TypeAdapterFactory
  at org.mitre.synthea.world.geography.Location.loadAbbreviations(Location.java:403)
  at org.mitre.synthea.world.geography.Location.<clinit>(Location.java:26)
  at org.mitre.synthea.engine.Generator.init(Generator.java:196)
  at org.mitre.synthea.engine.Generator.<init>(Generator.java:171)
  ... 32 elided
Caused by: java.lang.ClassNotFoundException: com.google.gson.TypeAdapterFactory
  at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
  at java.lang.ClassLoader.loadClass(ClassLoader.java:419)
  at java.lang.ClassLoader.loadClass(ClassLoader.java:352)
  ... 36 more
```
- ( 2020-11-26 15:37:51 )
```
jazzwang:~/git/synthea$ ./gradlew uberJar
jazzwang:~/git/synthea$ cp build/libs/synthea-with-dependencies.jar ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/synthea$ scala -cp build/libs/synthea-with-dependencies.jar
```
- ( 2020-11-26 15:41:04 ) Error:
```
scala> val generator = new Generator(options, ero);
java.lang.OutOfMemoryError: GC overhead limit exceeded
  at java.util.LinkedHashMap.newNode(LinkedHashMap.java:256)
  at java.util.HashMap.putVal(HashMap.java:642)
  at java.util.HashMap.put(HashMap.java:612)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer._readAndBindStringKeyMap(MapDeserializer.java:534)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer.deserialize(MapDeserializer.java:364)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer.deserialize(MapDeserializer.java:29)
  at com.fasterxml.jackson.databind.MappingIterator.nextValue(MappingIterator.java:280)
  at com.fasterxml.jackson.databind.MappingIterator.readAll(MappingIterator.java:320)
  at com.fasterxml.jackson.databind.MappingIterator.readAll(MappingIterator.java:306)
  at org.mitre.synthea.helpers.SimpleCSV.parse(SimpleCSV.java:42)
  at org.mitre.synthea.world.geography.Demographics.load(Demographics.java:379)
  at org.mitre.synthea.world.geography.Location.<init>(Location.java:56)
  at org.mitre.synthea.engine.Generator.init(Generator.java:206)
  at org.mitre.synthea.engine.Generator.<init>(Generator.java:171)
  ... 18 elided
```
- ( 2020-11-26 15:41:44 )
```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
```
- ( 2020-11-26 15:47:30 )
- https://www.journaldev.com/8278/scala-file-io-write-file-read-file#scala-write-to-file
```scala
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._

val options = new Generator.GeneratorOptions();
Config.set("exporter.fhir.export", "false");
Config.set("exporter.hospital.fhir.export", "false");
Config.set("exporter.practitioner.fhir.export", "false");
val ero = new Exporter.ExporterRuntimeOptions();
ero.enableQueue(Exporter.SupportedFhirVersion.R4);

val generator = new Generator(options, ero);
generator.run()
val jsonRecord = ero.getNextRecord();
```