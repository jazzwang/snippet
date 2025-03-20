## 2020-11-25

- My initial question:
  - How to add remote Maven repository into Scala REPL like `spark-shell --packages '...'`?
- Reference:
  - [Scala REPL: How to add remote Maven repository to Scala REPL classpath?](https://stackoverflow.com/questions/15666425/scala-repl-how-to-add-remote-maven-repository-to-scala-repl-classpath)
- Learn the following steps from https://stackoverflow.com/a/55552940/4209274
    - it demonstrates how to create a `build.sbt` from scratch!

```scala
~/git/snippet/scala$ mkdir sbt-create
~/git/snippet/scala$ cd sbt-create/
~/git/snippet/scala/sbt-create$ sbt -sbt-create
[warn] No sbt.version set in project/build.properties, base directory: /Users/jazzwang/git/snippet/scala/sbt-create
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
[info] sbt server started at local:///Users/jazzwang/.sbt/1.0/server/ae1837471fe1a34adce9/sock
sbt:sbt-create> set resolvers += "Sonatype OSS Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots"
[info] Defining resolvers
[info] The new value will be used by externalResolvers
[info] Reapplying settings...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
sbt:sbt-create> set libraryDependencies += "org.mitre.synthea" % "synthea" % "2.6.1"
[info] Defining libraryDependencies
[info] The new value will be used by allDependencies, dependencyPositions
[info] Reapplying settings...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
sbt:sbt-create> console
[warn] There may be incompatibilities among your library dependencies; run 'evicted' to see detailed eviction warnings.
[info] Starting scala interpreter...
Welcome to Scala 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> import org.mitre.synthea._
import org.mitre.synthea._

scala> (... PRESS CTRL+D ...)
[success] Total time: 117 s (01:57), completed Nov 25, 2020 11:36:22 PM
sbt:sbt-create> session save
[info] Reapplying settings...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
sbt:sbt-create> exit
[info] shutting down sbt server
~/git/snippet/scala/sbt-create$ cat build.sbt
resolvers += "Sonatype OSS Snapshots" at "https://oss.sonatype.org/content/repositories/snapshots"

libraryDependencies += "org.mitre.synthea" % "synthea" % "2.6.1"
```

# 2020-11-26

- ( 2020-11-26 01:19:07 )
- 測試時，也要注意 import 的 maven package 所用的 JVM 版本是否相容，不然會遇到 `java.lang.UnsupportedClassVersionError`。
    - 底下的例子是 sbt 1.3.8 + scala 2.12.10 + JVM 1.8.0
```
~/git/snippet/scala/sbt-create$ sbt
[info] Updated file /Users/jazzwang/git/snippet/scala/sbt-create/project/build.properties: set sbt.version to 1.3.8
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/sbt-create/project
[info] Loading settings for project sbt-create from build.sbt ...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
[info] sbt server started at local:///Users/jazzwang/.sbt/1.0/server/ae1837471fe1a34adce9/sock
sbt:sbt-create> console
[info] Starting scala interpreter...
Welcome to Scala 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> import org.mitre.synthea.engine.Generator
import org.mitre.synthea.engine.Generator

scala> val option = new Generator.GeneratorOptions()
java.lang.UnsupportedClassVersionError: org/mitre/synthea/engine/Generator$GeneratorOptions has been compiled by a more recent version of the Java Runtime (class file version 58.0), this version of the Java Runtime only recognizes class file versions up to 52.0
  at java.lang.ClassLoader.defineClass1(Native Method)
  at java.lang.ClassLoader.defineClass(ClassLoader.java:757)
  at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
  ... (skipped) ...
```
- 可是 `org.mitre.synthea` 卻是 Java `15` 編出來的
- 參考: https://www.baeldung.com/java-lang-unsupportedclassversion
```
45 = Java 1.1
46 = Java 1.2
47 = Java 1.3
48 = Java 1.4
49 = Java 5
50 = Java 6
51 = Java 7
52 = Java 8
53 = Java 9
54 = Java 10
55 = Java 11
56 = Java 12
57 = Java 13
```
------

- MEMO: scala shell commands

```
scala> :help
All commands can be abbreviated, e.g., :he instead of :help.
:completions <string>    output completions for the given string
:edit <id>|<line>        edit history
:help [command]          print this summary or command-specific help
:history [num]           show the history (optional num is commands to show)
:h? <string>             search the history
:imports [name name ...] show import history, identifying sources of names
:implicits [-v]          show the implicits in scope
:javap <path|class>      disassemble a file or class name
:line <id>|<line>        place line(s) at the end of history
:load <path>             interpret lines in a file
:paste [-raw] [path]     enter paste mode or paste a file
:power                   enable power user mode
:quit                    exit the interpreter
:replay [options]        reset the repl and replay all previous commands
:require <path>          add a jar to the classpath
:reset [options]         reset the repl to its initial state, forgetting all session entries
:save <path>             save replayable session to a file
:sh <command line>       run a shell command (result is implicitly => List[String])
:settings <options>      update compiler options, if possible; see reset
:silent                  disable/enable automatic printing of results
:type [-v] <expr>        display the type of an expression without evaluating it
:kind [-v] <type>        display the kind of a type. see also :help kind
:warnings                show the suppressed warnings from the most recent line which had any
```