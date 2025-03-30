
[TOC]

# README

# Development Notes

## 2021-08-10

- ( 2021-08-10 23:30:16 ) create project with `sbt new jazzwang/scala-spark.g8`
```
~/git/snippet/scala$ sbt new jazzwang/scala-spark.g8
[info] Loading global plugins from /Users/jazzwang/.sbt/1.0/plugins
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)

A minimal Apache Spark project in Scala

name [Scala Spark Project]: Spark DynamoDB Local

Template applied in /Users/jazzwang/git/snippet/scala/./spark-dynamodb-local
~/git/snippet/scala$ cd spark-dynamodb-local/
```
- ( 2021-08-10 23:32:04 ) add DynamoDB Local jar file and its dependency
  - Reference: http://softwarebyjosh.com/2018/03/25/how-to-unit-test-your-dynamodb-queries.html