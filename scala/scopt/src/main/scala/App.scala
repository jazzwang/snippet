// https://dkbalachandar.wordpress.com/2018/10/13/how-to-use-scopthttps-github-com-scopt-scopt/
// formatted with https://scastie.scala-lang.org/
object ScalaApp extends App {
  case class Arguments(inputDir: String = "", outputDir: String = "")
  val parser = new scopt.OptionParser[Arguments]("Parsing application") {

    opt[String]('i', "inputDir")
      .required()
      .valueName("")
      .action((value, arguments) => arguments.copy(inputDir = value))

    opt[String]('o', "outputDir")
      .required()
      .valueName("")
      .action((value, arguments) => arguments.copy(outputDir = value))

  }

  def run(arguments: Arguments): Unit = {
    println("Input Dir:" + arguments.inputDir)
    println("Output Dir:" + arguments.outputDir)
  }

  parser.parse(args, Arguments()) match {
    case Some(arguments) => run(arguments)
    case None            =>
  }
}