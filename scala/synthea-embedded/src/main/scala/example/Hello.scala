package example

import java.io._
import java.time._
import freemarker.template._
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._
import org.mitre.synthea.world.agents._
import org.mitre.synthea.world.concepts._

object Hello extends Greeting with App {
  println(greeting)

  var options = new Generator.GeneratorOptions();

  // disable default options
  Config.set("exporter.fhir.export", "false");
  Config.set("exporter.fhir.transaction_bundle", "false");
  Config.set("exporter.hospital.fhir.export", "false");
  Config.set("exporter.practitioner.fhir.export", "false");
  Config.set("generate.append_numbers_to_person_names", "false");

  var ero = new Exporter.ExporterRuntimeOptions();

  options.gender = "F";
  options.state = "Pennsylvania";
  options.city = "Scranton";
  options.ageSpecified = true;
  options.minAge = 5;
  options.maxAge = 6;

  var generator = new Generator(options, ero);
  var person = generator.generatePerson(0);

  person.attributes.put(Person.NAME, "Janey Mayger");
  person.attributes.put(Person.FIRST_NAME, "Janey");
  person.attributes.put(Person.LAST_NAME, "Mayger");

  val time = generator.stop.asInstanceOf[java.lang.Long]
  person.attributes.put("time", time);
  person.attributes.put("race_lookup", RaceAndEthnicity.LOOK_UP_CDC_RACE);
  person.attributes.put("ethnicity_lookup", RaceAndEthnicity.LOOK_UP_CDC_ETHNICITY_CODE);
  person.attributes.put("ethnicity_display_lookup", RaceAndEthnicity.LOOK_UP_CDC_ETHNICITY_DISPLAY);

  val configuration = new Configuration(Configuration.VERSION_2_3_26);
  configuration.setDefaultEncoding("UTF-8");
  configuration.setLogTemplateExceptions(false);
  configuration.setSetting("object_wrapper", "DefaultObjectWrapper(2.3.26, forceLegacyNonListCollections=false, iterableSupport=true, exposeFields=true)");
  configuration.setAPIBuiltinEnabled(true);
  configuration.setDirectoryForTemplateLoading(new File("templates/ccda"));
  var template = configuration.getTemplate("ccda.ftl")
  var writer = new StringWriter();
  template.process(person.attributes, writer);
  var bw = new BufferedWriter(new FileWriter(new File("Janey_Mayger.xml")));
  var xml = writer.toString;
  //val printer = new scala.xml.PrettyPrinter(80, 2)
  //printer.format(xml)
  bw.write(writer.toString);
  bw.close();
}

trait Greeting {
  lazy val greeting: String = "hello"
}
