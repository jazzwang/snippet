# Development Notes

## 2021-04-10

- Q: spark-shell 到底 import 了哪些類別呢？
```
~$ spark-shell
21/04/10 16:41:34 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://localhost:4040
Spark context available as 'sc' (master = local[*], app id = local-1618044112157).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 3.0.0
      /_/

Using Scala version 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_282)
Type in expressions to have them evaluated.
Type :help for more information.

scala> :imports
 1) import java.lang._             (118 types, 124 terms)
 2) import scala._                 (178 types, 172 terms)
 3) import scala.Predef._          (125 terms, 62 are implicit)
 4) import org.apache.spark.SparkContext._ (71 terms, 1 are implicit)
 5) import spark.implicits._       (1 types, 69 terms, 39 are implicit)
 6) import spark.sql               (1 terms)
 7) import org.apache.spark.sql.functions._ (422 terms)
 ```
