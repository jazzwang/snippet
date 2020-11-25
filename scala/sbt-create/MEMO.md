## 2020-11-25

- My initial question: how to add remote Maven repository into Scala REPL like `spark-shell`?
- Reference: [Scala REPL: How to add remote Maven repository to Scala REPL classpath?](https://stackoverflow.com/questions/15666425/scala-repl-how-to-add-remote-maven-repository-to-scala-repl-classpath)
- learn the following steps from https://stackoverflow.com/a/55552940/4209274
    - it demonstrates how to create a `build.sbt` from scratch!

```
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
/                ::               consoleProject   consoleQuick
sbt:sbt-create> console
/                ::               consoleProject   consoleQuick
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