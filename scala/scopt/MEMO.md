## 2020-12-04

- ( 2020-12-04 10:38:30 ) create project with `sbt-create`
```
~/git/snippet/scala/scopt$ sbt -sbt-create
[info] Updated file /Users/jazzwang/git/snippet/scala/scopt/project/build.properties: set sbt.version to 1.3.8
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/scopt/project
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
[info] sbt server started at local:///Users/jazzwang/.sbt/1.0/server/af8a05880341d78ed61a/sock
sbt:scopt> set libraryDependencies += "com.github.scopt" %% "scopt" % "4.0.0"
[info] Defining libraryDependencies
[info] The new value will be used by allDependencies, dependencyPositions
[info] Reapplying settings...
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
sbt:scopt> session save
[info] Reapplying settings...
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
sbt:scopt> exit
[info] shutting down sbt server
```