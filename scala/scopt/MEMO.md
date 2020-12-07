- https://github.com/scopt/scopt

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

## 2020-12-07

- ( 2020-12-07 18:18:56 ) Q: Can I pass command line arguments to sbt run task?
- A: Yes. Run with `sbt "run foo bar tic tac"`
    - https://alvinalexander.com/scala/sbt-how-pass-command-line-arguments-sbt-run/
    - https://github.com/alvinj/SbtCommandLineArgs
- ( 2020-12-07 23:41:19 ) here is one example code:
    - https://dkbalachandar.wordpress.com/2018/10/13/how-to-use-scopthttps-github-com-scopt-scopt/
- ( 2020-12-07 23:49:14 ) test with sample code with `sbt run`
```
jazzwang:~/git/snippet/scala/scopt$ sbt run
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/scopt/project
[info] Loading settings for project scopt from build.sbt ...
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
[info] Compiling 1 Scala source to /Users/jazzwang/git/snippet/scala/scopt/target/scala-2.12/classes ...
[info] running ScalaApp
Error: Missing option --inputDir
Error: Missing option --outputDir
Usage: Parsing application [options]

  -i, --inputDir
  -o, --outputDir
[success] Total time: 6 s, completed Dec 7, 2020 11:45:25 PM
jazzwang:~/git/snippet/scala/scopt$ sbt "run -i test"
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/scopt/project
[info] Loading settings for project scopt from build.sbt ...
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
[info] running ScalaApp -i test
Error: Missing option --outputDir
Usage: Parsing application [options]

  -i, --inputDir
  -o, --outputDir
[success] Total time: 1 s, completed Dec 7, 2020 11:45:54 PM
jazzwang:~/git/snippet/scala/scopt$ sbt "run -i test -o output"
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/scopt/project
[info] Loading settings for project scopt from build.sbt ...
[info] Set current project to scopt (in build file:/Users/jazzwang/git/snippet/scala/scopt/)
[info] Compiling 1 Scala source to /Users/jazzwang/git/snippet/scala/scopt/target/scala-2.12/classes ...
[info] running ScalaApp -i test -o output
Input Dir:test
Output Dir:output
[success] Total time: 6 s, completed Dec 7, 2020 11:47:20 PM
```