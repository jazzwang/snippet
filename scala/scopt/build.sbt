libraryDependencies += "com.github.scopt" %% "scopt" % "4.0.0"

// https://stackoverflow.com/questions/24996437/how-to-execute-a-bash-script-as-sbt-task/25005
import scala.sys.process._
lazy val distclean = taskKey[Unit]("Clean up temporary files and directories")
distclean := {
  "rm -rf project/target project/project target output" !
}
