[TOC]

- ( 2020-11-11 20:32:32 )

# 動機 WHY

- 花了一點時間稍微掃過 [Synthea](https://github.com/synthetichealth/synthea) 專案的原始碼結構，發現是靠 [FreeMaker](https://freemarker.apache.org/) 這個 Java Templating Engine 來產生 C-CDA XML 格式的病歷資料。
- 那麼 Scala 有哪些 Templating Engine 可以用來產生 XML 輸出呢？
    - Play Framework 有 [ScalaTemplates](https://www.playframework.com/documentation/2.8.x/ScalaTemplates) 跟 [Twirl](https://github.com/playframework/twirl)
    - [Scalate](https://scalate.github.io/scalate/) - [github](https://github.com/scalate/scalate)
- 有什麼方法可以讀 C-CDA 的 XSD 檔案，產生 XML 檔呢？
    - 找到一個專案叫做 [scalaxb](https://scalaxb.org/)
    ```
    scalaxb is an XML data-binding tool for Scala that supports W3C XML Schema (xsd) and Web Services Description Language (wsdl) as the input file.
    ```
    - 這個專案包含了許多不同的變形：
        - command line app [scalaxb](https://scalaxb.org/setup)
        - sbt plugin [sbt-scalaxb](http://scalaxb.org/sbt-scalaxb)
        - maven plugin [mvn-scalaxb](http://scalaxb.org/mvn-scalaxb)
        - web API [scalaxb-heroku](http://scalaxb.org/online) hosted on heroku

# 參考 REFERENCES

- https://scalaxb.org/setup
- https://scalaxb.org/sbt-scalaxb

# 實作 IMPLEMENTATION

## 法一：命令列工具 scalaxb

- 安裝：(失敗)
```
~/git/snippet/scala/scalaxb$ cs install eed3si9n/scalaxb
https://repo1.maven.org/maven2/io/get-coursier/apps/maven-metadata.xml
  100.0% [##########] 1.6 KiB (8.3 KiB / s)
https://repo1.maven.org/maven2/io/get-coursier/apps/maven-metadata.xml
  No new update since 2020-10-23 21:14:17
https://repo1.maven.org/maven2/io/get-coursier/apps/1.0.3/apps-1.0.3.pom
  100.0% [##########] 1.3 KiB (7.7 KiB / s)
Cannot find app eed3si9n/scalaxb in channels io.get-coursier:apps
```
- ( 2020-11-11 21:01:54 )
- ( 2020-11-11 22:18:51 ) 懷疑跟 `scala` 版本有關
	- https://github.com/eed3si9n/scalaxb/blob/master/src/main/conscript/scalaxb/launchconfig
	- 看起來主程式是 `scalaxb.compiler.SbtApp`
	- 

## 法二：SBT plugin - `sbt-scalaxb`

- ( 2020-11-11 21:32:04 )
- 用範本產生專案
```
jazzwang:~/git/snippet/scala$ sbt new eed3si9n/scalaxb.g8
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)
[info] Set current project to scala (in build file:/Users/jazzwang/git/snippet/scala/)
name [foo-project]: ccda-scalaxb    
scala_version [2.12.3]: 2.11.11
scalaxb_version [1.5.2]: 
dispatch_version [0.12.0]: 
generated_package_name [generated]: 

Template applied in /Users/jazzwang/git/snippet/scala/./ccda-scalaxb
```
- 移除範本的 `src/main/wsdl/sample.wsdl` 跟 `src/main/xsd/placeholder.txt`
```
jazzwang:~/git/snippet/scala/ccda-scalaxb$ rm src/main/wsdl/sample.wsdl 
jazzwang:~/git/snippet/scala/ccda-scalaxb$ rm src/main/xsd/placeholder.txt 
```
- 看了一下 [sbt-scalaxb](https://scalaxb.org/sbt-scalaxb) 說明跟 [running scalaxb](https://scalaxb.org/running-scalaxb)，還是不太確定該怎麼跑。

- ( 2020-11-11 22:07:35 ) <mark>失敗</mark>
- ( 2020-11-11 22:25:23 ) 試了一下 sbt shell 的 `help scalaxb*` 指令
```
sbt:ccda-scalaxb> help scalaxb*

scalaxbAutoPackages

  Generates packages for different namespaces automatically

scalaxbPackageName

  Specifies the target package

scalaxbChunkSize

  Segments long sequences into chunks (default: 10)

scalaxbConfig

  Configuration for scalaxb

... skipped ...
```

## 用 `spark-shell` 測試

- 本機測試環境 Apache Spark `2.2.1` 版
```bash
jazzwang:~$ spark-shell --packages "org.scalaxb:scalaxb_2.11:1.8.0"
Ivy Default Cache set to: /Users/jazzwang/.ivy2/cache
The jars for the packages stored in: /Users/jazzwang/.ivy2/jars
:: loading settings :: url = jar:file:/Users/jazzwang/spark/jars/ivy-2.4.0.jar!/org/apache/ivy/core/settings/ivysettings.xml
org.scalaxb#scalaxb_2.11 added as a dependency
:: resolving dependencies :: org.apache.spark#spark-submit-parent;1.0
	confs: [default]
	found org.scalaxb#scalaxb_2.11;1.8.0 in central
	found com.github.scopt#scopt_2.11;3.7.1 in central
	found log4j#log4j;1.2.17 in spark-list
	found org.scala-lang.modules#scala-xml_2.11;1.2.0 in central
	found org.scala-lang.modules#scala-parser-combinators_2.11;1.1.1 in central
:: resolution report :: resolve 384ms :: artifacts dl 13ms
	:: modules in use:
	com.github.scopt#scopt_2.11;3.7.1 from central in [default]
	log4j#log4j;1.2.17 from spark-list in [default]
	org.scala-lang.modules#scala-parser-combinators_2.11;1.1.1 from central in [default]
	org.scala-lang.modules#scala-xml_2.11;1.2.0 from central in [default]
	org.scalaxb#scalaxb_2.11;1.8.0 from central in [default]
	---------------------------------------------------------------------
	|                  |            modules            ||   artifacts   |
	|       conf       | number| search|dwnlded|evicted|| number|dwnlded|
	---------------------------------------------------------------------
	|      default     |   5   |   0   |   0   |   0   ||   5   |   0   |
	---------------------------------------------------------------------
:: retrieving :: org.apache.spark#spark-submit-parent
	confs: [default]
	0 artifacts copied, 5 already retrieved (0kB/14ms)
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
20/11/11 22:08:45 WARN NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Spark context Web UI available at http://127.0.0.1:4040
Spark context available as 'sc' (master = local[*], app id = local-1605103726836).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.2.1
      /_/
         
Using Scala version 2.11.8 (OpenJDK 64-Bit Server VM, Java 1.8.0_265)
Type in expressions to have them evaluated.
Type :help for more information.

scala> 
```
- ( 2020-11-11 22:26:21 ) 看樣子需要看一下原始碼比較知道 CLI 是怎麼呼叫的。
	- 