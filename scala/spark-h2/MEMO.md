# Development MEMO

[TOC]

## 2020-11-18

- test with `spark-shell --packages "com.h2database:h2:1.4.200"`
    - Ref: https://medium.com/@sukumaarneo/testing-embedded-h2-db-with-scala-and-scalatest-3a863aafc9ab
    - Ref: https://github.com/sukumaar/scala-h2-db-embedded/blob/master/src/test/scala/sukumaar/Test.scala

```
~$ spark-shell --packages "com.h2database:h2:1.4.200"
scala> import java.sql._
scala> val con: Connection = DriverManager.getConnection("jdbc:h2:./test")
scala> val stm: Statement = con.createStatement
scala> val sql: String =
        """
          |create table test2(ID INT PRIMARY KEY,NAME VARCHAR(500));
          |insert into test2 values (1,'A');
          |insert into test2 values (2,'B');
          |insert into test2 values (3,'C');""".stripMargin
scala> stm.execute(sql)
scala> val rs = stm.executeQuery("select * from test_table1")
scala> rs.next
scala> rs.getInt("ID")
res6: Int = 1
scala> rs.getString("NAME")
res7: String = A
```

- [狀況] 發現用最新版 `1.4.200` 讀取已經存在的 H2 embedded DB 檔案，會遇到以下錯誤訊息

```
[11/18 14:23:35]
~/git/synthea$ cp ~/.ivy2/jars/com.h2database_h2-1.4.200.jar .
~/git/synthea$ java -cp com.h2database_h2-1.4.200.jar org.h2.tools.Shell
Welcome to H2 Shell 1.4.200 (2019-10-14)
Exit with Ctrl+C
[Enter] jdbc:h2:~/test
URL jdbc:h2:./database
[Enter] org.h2.Driver
Driver org.h2.Driver
[Enter]
User
Password
SQL Exception: General error: "java.lang.IllegalStateException: Unable to read the page at position 172898283949066 [1.4.200/6]" [50000-200]
```

- 改用 `1.4.196` 就正常了

```
~/git/synthea$ cp ~/.ivy2/jars/com.h2database_h2-1.4.196.jar h2-1.4.196.jar
~/git/synthea$ java -cp h2-1.4.196.jar org.h2.tools.Shell
Welcome to H2 Shell 1.4.196 (2017-06-10)
Exit with Ctrl+C
[Enter]   jdbc:h2:~/test
URL       jdbc:h2:./database
[Enter]   org.h2.Driver
Driver    org.h2.Driver
[Enter]
User
[Enter]   Hide
Password
Password
Connected
Commands are case insensitive; SQL statements end with ';'
help or ?      Display this help
list           Toggle result list / stack trace mode
maxwidth       Set maximum column width (default is 100)
autocommit     Enable or disable autocommit
history        Show the last 20 statements
quit or exit   Close the connection and exit

sql>
sql> show databases;
SCHEMA_NAME
INFORMATION_SCHEMA
PUBLIC
(2 rows, 44 ms)
sql> show tables;
TABLE_NAME         | TABLE_SCHEMA
ATTRIBUTE          | PUBLIC
CAREPLAN           | PUBLIC
CLAIM              | PUBLIC
CONDITION          | PUBLIC
COVERAGE           | PUBLIC
ENCOUNTER          | PUBLIC
IMAGING_STUDY      | PUBLIC
IMMUNIZATION       | PUBLIC
MEDICATION         | PUBLIC
OBSERVATION        | PUBLIC
PERSON             | PUBLIC
PROCEDURE          | PUBLIC
PROVIDER           | PUBLIC
PROVIDER_ATTRIBUTE | PUBLIC
QUALITY_OF_LIFE    | PUBLIC
REPORT             | PUBLIC
UTILIZATION        | PUBLIC
UTILIZATION_DETAIL | PUBLIC
(18 rows, 10 ms)
sql> SHOW COLUMNS FROM ATTRIBUTE;
FIELD     | TYPE                | NULL | KEY | DEFAULT
PERSON_ID | VARCHAR(2147483647) | YES  |     | NULL
NAME      | VARCHAR(2147483647) | YES  |     | NULL
VALUE     | VARCHAR(2147483647) | YES  |     | NULL
(3 rows, 17 ms)
```

- 不過確實也有發現 H2 比 SQLite 容易壞掉
  -
```
~/git/synthea$ java -cp h2-1.4.196.jar org.h2.tools.Shell

Welcome to H2 Shell 1.4.196 (2017-06-10)
Exit with Ctrl+C
[Enter]   jdbc:h2:~/test
URL       jdbc:h2:./database
[Enter]   org.h2.Driver
Driver    org.h2.Driver
[Enter]
User
[Enter]   Hide
Password
Password
SQL Exception: #Row {1} not found in primary index "PUBLIC.SYS_DATA: 75" [90143-196]
```

# 2020-11-20

- https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html