# Development Notes

## 2020-12-13

- ( 2020-12-13 21:56:23 )
- https://mvnrepository.com/artifact/commons-cli/commons-cli/1.4
```
// https://mvnrepository.com/artifact/commons-cli/commons-cli
libraryDependencies += "commons-cli" % "commons-cli" % "1.4"
```
- ( 2020-12-13 21:58:37 )
```bash
~/git/snippet/scala/commons-cli$ sbt --sbt-create
sbt:commons-cli> set libraryDependencies += "commons-cli" % "commons-cli" % "1.4"
sbt:commons-cli> update
sbt:commons-cli> console
scala> import org.apache.commons.cli._
scala> val options = new Options()
scala> options.addOption("f", "inputFile",  false, "read demographics from input CSV file")
scala> val parser = new DefaultParser();
scala> :quit
sbt:commons-cli> session save
sbt:commons-cli> exit
~/git/snippet/scala/commons-cli$ git gi sbt,scala > .gitignore
~/git/snippet/scala/commons-cli$ mkdir -p src/main/scala
```
- ( 2020-12-13 22:23:51 )
```
scala> import org.apache.commons.cli._
scala> val options = new Options()
scala> val loadFile = Option.builder("f").longOpt("loadFile").argName("file").hasArg(true).desc("load demographic from file").build()
scala> options.addOption(loadFile)
scala> val formatter = new HelpFormatter()
scala> formatter.printHelp("MyApp", options)
usage: MyApp
 -f,--loadFile <file>   load demographic from file
```
- ( 2020-12-13 23:04:15 )
- https://www.tutorialspoint.com/commons_cli/commons_cli_properties_option.htm
- test with `sbt 'run -D a=b -D c=d'`