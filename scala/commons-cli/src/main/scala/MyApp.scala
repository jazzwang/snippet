import org.apache.commons.cli._

object MyApp extends App {
  val options = new Options()
  checkOptions()

  def checkOptions() {
    val loadFile = Option.builder("f").longOpt("loadFile").argName("file")
                        .hasArg(true).desc("load demographic from file").build()
    options.addOption(loadFile)
    val propertyOption = Option.builder("D").argName("property=value")
                        .hasArgs().valueSeparator().numberOfArgs(2)
                        .desc("use value for given properties" ).build()
    options.addOption(propertyOption)
    options.addOption("h",  "help", false, "display this help")
    val parser = new DefaultParser();
    try {
      val cmd = parser.parse( options, args);
      if (cmd.hasOption("f")) {
        println(cmd.getOptionValue("f"));
      }
      if (cmd.hasOption("D")) {
        val properties = cmd.getOptionProperties("D");
        properties.stringPropertyNames().forEach( key => {
          println(s"$key = " + properties.getProperty(key))
        })
      }
      if (cmd.hasOption("h")) {
        usage();
      }
    } catch {
      case ex: UnrecognizedOptionException => {
        usage();
      }
      case ex: MissingArgumentException => {
        println("missing argument")
        usage();
      }
      case ex: Exception => {
        ex.printStackTrace();
      }
    }
  }

  def usage() {
    val formatter = new HelpFormatter()
    formatter.printHelp("MyApp", options)
  }
}
