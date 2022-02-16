# DEVELOP NOTES

- ( 2022-02-17 00:11:44 )
```
~/git/snippet/scala$ cookiecutter gh:jazzwang/init-spark-sql
You've downloaded /Users/jazzwang/.cookiecutters/init-spark-sql before. Is it okay to delete and re-download it? [yes]:
repo_name [spark-sql]: spark-sql-uuid
~/git/snippet/scala$ cd spark-sql-uuid/
~/git/snippet/scala/spark-sql-uuid$ code README.md
~/git/snippet/scala/spark-sql-uuid$ code src/main/scala/Hello.scala
```
- ( 2022-02-17 00:11:52 )
```
~/git/snippet/scala/spark-sql-uuid$ sbt run
[info] Loading global plugins from /Users/jazzwang/.sbt/1.0/plugins
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/spark-sql-uuid/project
[info] Loading settings for project root from build.sbt ...
[info] Set current project to Spark in Scala Seed Project (in build file:/Users/jazzwang/git/snippet/scala/spark-sql-uuid/)
[info] Compiling 1 Scala source to /Users/jazzwang/git/snippet/scala/spark-sql-uuid/target/scala-2.12/classes ...
[info] running Hello
root
 |-- value: integer (nullable = false)

root
 |-- value: integer (nullable = false)
 |-- record_uuid: string (nullable = false)

+-----+------------------------------------+
|value|record_uuid                         |
+-----+------------------------------------+
|1    |ef174ea5-f7c5-4392-9882-2343934f2809|
|2    |115dcf4d-adb1-4cf1-b7db-1b3b93c2be16|
|3    |cef9cc30-32f9-4670-aea0-51fbcb5a7083|
|4    |360dbf52-0675-4b12-afdb-a30ad3fd23f3|
|5    |b55324fe-39af-4bcc-9959-bce4fe44cddf|
|6    |0a36d73d-f23a-4ae3-af3d-b877adea4111|
|7    |052852cb-af19-43d0-a3dc-1fce833d6148|
|8    |d9edac48-988c-439f-baec-ae2fd17c67c3|
|9    |67e4375b-1ae3-4157-9cd4-a156d66a6ce7|
|10   |47151d4d-8960-4cd5-90e5-e5182ac0e962|
|11   |b740c97c-77ea-4e4a-b326-a21fbd4adcbe|
|12   |3c0004b6-3f1b-43bb-8903-9518761ed856|
|13   |97d079dc-87b0-4cf7-b987-d4342cd9d2b2|
|14   |9facb88b-ef98-4e6b-9d30-1d4fdb7408d2|
|15   |b798cae0-6efa-4b19-876b-fb3ad7b9e86a|
|16   |fe635c8d-0b3e-4885-9f5e-3c623bafa721|
|17   |8dfce11f-2c17-4312-9812-0035c9e5cfb9|
|18   |ef82bd58-48f6-40af-b66e-16893584c112|
|19   |4c0ab65f-27ef-43d6-91ee-4dd4f1c39e9a|
|20   |ef2d96c5-c2b9-4ca6-93de-8bfce85095b9|
+-----+------------------------------------+
only showing top 20 rows

[success] Total time: 91 s (01:31), completed Feb 17, 2022 12:21:03 AM
```