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

  // disable default exporter options - to reduce output files
  Config.set("exporter.fhir.export", "false");
  Config.set("exporter.fhir.transaction_bundle", "false");
  Config.set("exporter.hospital.fhir.export", "false");
  Config.set("exporter.practitioner.fhir.export", "false");
  // disable generator option
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
  var superEncounter = person.record.encounters.get(0)
  for ( i <- 1 to person.record.encounters.size -1 ) {
    val encounter = person.record.encounters.get(i);
    if (encounter.start <= time) {
      superEncounter.observations.addAll(encounter.observations);
      superEncounter.reports.addAll(encounter.reports);
      superEncounter.conditions.addAll(encounter.conditions);
      superEncounter.allergies.addAll(encounter.allergies);
      superEncounter.procedures.addAll(encounter.procedures);
      superEncounter.immunizations.addAll(encounter.immunizations);
      superEncounter.medications.addAll(encounter.medications);
      superEncounter.careplans.addAll(encounter.careplans);
      superEncounter.imagingStudies.addAll(encounter.imagingStudies);
    }
  }

  person.attributes.put("UUID", person.randUUID);
  person.attributes.put("ehr_encounters", person.record.encounters);
  person.attributes.put("ehr_observations", superEncounter.observations);
  person.attributes.put("ehr_reports", superEncounter.reports);
  person.attributes.put("ehr_conditions", superEncounter.conditions);
  person.attributes.put("ehr_allergies", superEncounter.allergies);
  person.attributes.put("ehr_procedures", superEncounter.procedures);
  person.attributes.put("ehr_immunizations", superEncounter.immunizations);
  person.attributes.put("ehr_medications", superEncounter.medications);
  person.attributes.put("ehr_careplans", superEncounter.careplans);
  person.attributes.put("ehr_imaging_studies", superEncounter.imagingStudies);
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
