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
