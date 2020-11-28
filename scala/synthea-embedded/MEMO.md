# Development Notes

## 2020-11-24

- https://github.com/synthetichealth/synthea/wiki/Embedding

## 2020-11-26

# 2020-11-26

- ( 2020-11-26 10:02:31 )
- [Generator.Generator(GeneratorOptions o, Exporter.ExporterRuntimeOptions ero)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L180-L188)
```java
  public Generator(GeneratorOptions o, Exporter.ExporterRuntimeOptions ero) {
    options = o;
    exporterRuntimeOptions = ero;
    if (options.updatedPopulationSnapshotPath != null) {
      exporterRuntimeOptions.deferExports = true;
      internalStore = Collections.synchronizedList(new LinkedList<>());
    }
    init();
  }
```
- ( 2020-11-26 10:03:10 )
- [Generator](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L80-L85)
```java
  /**
   * Used only for testing and debugging. Populate this field to keep track of all patients
   * generated, living or dead, during a simulation. Note that this may result in significantly
   * increased memory usage as patients cannot be GC'ed.
   */
  List<Person> internalStore;
```
- ( 2020-11-26 10:04:05 )
- [Generator.recordPerson(Person person, int index)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L781-L791)
```java
  public void recordPerson(Person person, int index) {
    long finishTime = person.lastUpdated + timestep;
    boolean isAlive = person.alive(finishTime);

    if (database != null) {
      database.store(person);
    }

    if (internalStore != null) {
      internalStore.add(person);
    }
```
- ( 2020-11-26 10:07:04 )
- [GeneratorTest.testDemographicsRetry()](https://github.com/synthetichealth/synthea/blob/5921215d8c16b3c7918cfeb7940b0c85118ca39e/src/test/java/org/mitre/synthea/engine/GeneratorTest.java#L183-L228) is a good example to understand how Generator use `internalStore` to store `Person` objects.
```java
  @Test
  public void testDemographicsRetry() throws Exception {
    // confirm that the demographic choices will persist if the first generated patients die
    int numberOfPeople = 4;
    Generator.GeneratorOptions opts = new Generator.GeneratorOptions();
    opts.population = numberOfPeople;
    opts.minAge = 50;
    opts.maxAge = 100;
    Generator generator = new Generator(opts);
    generator.internalStore = new LinkedList<>();
    for (int i = 0; i < numberOfPeople; i++) {
      Person person = generator.generatePerson(i);

      // the person returned will be last in the internalStore
      int personIndex = generator.internalStore.size() - 1;

      for (int j = personIndex - 1; j >= 0; j--) { //
        Person compare = generator.internalStore.get(j);

        // basic demographics should always be exactly the same
        assertEquals(person.attributes.get(Person.CITY), compare.attributes.get(Person.CITY));
        assertEquals(person.attributes.get(Person.RACE), compare.attributes.get(Person.RACE));

        long expectedBirthdate;

        if (personIndex < 10) {
          // less than 10 attempts were made, so all of them should match exactly
          expectedBirthdate = (long)person.attributes.get(Person.BIRTHDATE);
        } else if (j > 10) {
          // the person we got back (potentially) has the changed target birthdate
          // and so would any with index > 10
          // so these should match exactly
          expectedBirthdate = (long)person.attributes.get(Person.BIRTHDATE);
        } else {
          // the person we got back (potentially) has the changed target birthdate
          // but any with index < 10 might not
          // in this case, ensure the first 10 match index 0 (which the loop will take care of)
          expectedBirthdate = (long)generator.internalStore.get(0).attributes.get(Person.BIRTHDATE);
        }

        assertEquals(expectedBirthdate, (long)compare.attributes.get(Person.BIRTHDATE));
      }

      generator.internalStore.clear();
    }
  }
```
- https://github.com/synthetichealth/synthea/wiki/Embedding#json-integration
- reference [sbt-create](../sbt-create/MEMO.md)
- manually use java11 instead of java8
```
jazzwang:~$ wget https://download.java.net/java/GA/jdk15.0.1/51f4f36ad4ef43e39d0dfdbaf6549e32/9/GPL/openjdk-15.0.1_osx-x64_bin.tar.gz
jazzwang:~$ tar zxvf openjdk-11.0.2_osx-x64_bin.tar.gz
jazzwang:~$ rm openjdk-11.0.2_osx-x64_bin.tar.gz
jazzwang:~$ mv jdk-11.0.2.jdk/ jdk11
jazzwang:~$ export PATH=~/jdk11/Contents/Home/bin:$PATH
jazzwang:~$ which java
/Users/jazzwang/jdk11/Contents/Home/bin/java
jazzwang:~$ java -version
openjdk version "11.0.2" 2019-01-15
OpenJDK Runtime Environment 18.9 (build 11.0.2+9)
OpenJDK 64-Bit Server VM 18.9 (build 11.0.2+9, mixed mode)
```
- ( 2020-11-26 14:32:45 ) encounter class version issue again with JDK11
```
jazzwang:~$ cd ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/snippet/scala/synthea-embedded$ sbt console
scala> import org.mitre.synthea.engine._
scala> val options = new org.mitre.synthea.engine.Generator.GeneratorOptions();
java.lang.UnsupportedClassVersionError: org/mitre/synthea/engine/Generator$GeneratorOptions has been compiled by a more recent version of the Java Runtime (class file version 58.0), this version of the Java Runtime only recognizes class file versions up to 55.0
  ... (skipped) ...
```
- ( 2020-11-26 14:49:57 ) compile synthea with jdk8
```bash
jazzwang:~$ cd git/synthea
jazzwang:~/git/synthea$ git checkout v2.6.1
jazzwang:~/git/synthea$ ./gradlew jar
jazzwang:~/git/synthea$ cp build/libs/synthea.jar ~/git/snippet/scala/synthea-embedded/
```
- ( 2020-11-26 15:13:22 ) loading synthea.jar (without dependencies) to scala REPL
```
jazzwang:~/git/synthea$ cd ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/snippet/scala/synthea-embedded$ scala -cp synthea.jar
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.
```
- ( 2020-11-26 15:14:46 ) interactive testing
```scala
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._
import org.mitre.synthea.datastore.DataStore
import java.util.concurrent._

val options = new Generator.GeneratorOptions();
Config.set("exporter.fhir.export", "false");
Config.set("exporter.hospital.fhir.export", "false");
Config.set("exporter.practitioner.fhir.export", "false");

val ero = new Exporter.ExporterRuntimeOptions();
ero.enableQueue(Exporter.SupportedFhirVersion.R4);

val generator = new Generator(options, ero);

```
- Error
```scala
scala> val generator = new Generator(options, ero);
java.lang.NoClassDefFoundError: com/google/gson/TypeAdapterFactory
  at org.mitre.synthea.world.geography.Location.loadAbbreviations(Location.java:403)
  at org.mitre.synthea.world.geography.Location.<clinit>(Location.java:26)
  at org.mitre.synthea.engine.Generator.init(Generator.java:196)
  at org.mitre.synthea.engine.Generator.<init>(Generator.java:171)
  ... 32 elided
Caused by: java.lang.ClassNotFoundException: com.google.gson.TypeAdapterFactory
  at java.net.URLClassLoader.findClass(URLClassLoader.java:382)
  at java.lang.ClassLoader.loadClass(ClassLoader.java:419)
  at java.lang.ClassLoader.loadClass(ClassLoader.java:352)
  ... 36 more
```
- ( 2020-11-26 15:37:51 )
```
jazzwang:~/git/synthea$ ./gradlew uberJar
jazzwang:~/git/synthea$ cp build/libs/synthea-with-dependencies.jar ~/git/snippet/scala/synthea-embedded/
jazzwang:~/git/synthea$ scala -cp build/libs/synthea-with-dependencies.jar
```
- ( 2020-11-26 15:41:04 ) Error:
```
scala> val generator = new Generator(options, ero);
java.lang.OutOfMemoryError: GC overhead limit exceeded
  at java.util.LinkedHashMap.newNode(LinkedHashMap.java:256)
  at java.util.HashMap.putVal(HashMap.java:642)
  at java.util.HashMap.put(HashMap.java:612)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer._readAndBindStringKeyMap(MapDeserializer.java:534)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer.deserialize(MapDeserializer.java:364)
  at com.fasterxml.jackson.databind.deser.std.MapDeserializer.deserialize(MapDeserializer.java:29)
  at com.fasterxml.jackson.databind.MappingIterator.nextValue(MappingIterator.java:280)
  at com.fasterxml.jackson.databind.MappingIterator.readAll(MappingIterator.java:320)
  at com.fasterxml.jackson.databind.MappingIterator.readAll(MappingIterator.java:306)
  at org.mitre.synthea.helpers.SimpleCSV.parse(SimpleCSV.java:42)
  at org.mitre.synthea.world.geography.Demographics.load(Demographics.java:379)
  at org.mitre.synthea.world.geography.Location.<init>(Location.java:56)
  at org.mitre.synthea.engine.Generator.init(Generator.java:206)
  at org.mitre.synthea.engine.Generator.<init>(Generator.java:171)
  ... 18 elided
```
- ( 2020-11-26 15:41:44 )
```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
```
- ( 2020-11-26 15:47:30 )
- https://www.journaldev.com/8278/scala-file-io-write-file-read-file#scala-write-to-file
- https://alvinalexander.com/scala/how-to-write-text-files-in-scala-printwriter-filewriter/

```scala
import java.io._
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._

val options = new Generator.GeneratorOptions();
Config.set("exporter.fhir.export", "false");
Config.set("exporter.hospital.fhir.export", "false");
Config.set("exporter.practitioner.fhir.export", "false");
val ero = new Exporter.ExporterRuntimeOptions();
ero.enableQueue(Exporter.SupportedFhirVersion.R4);

val generator = new Generator(options, ero);
generator.run()
val jsonRecord = ero.getNextRecord();
val bw = new BufferedWriter(new FileWriter(new File("output.json")))
bw.write(jsonRecord)
```

## 2020-11-27

### Generator - Person - Demographics

- ( 2020-11-27 21:43:41 )
- [Generator.run()](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L303) call [Generator.generatePerson(int index, long personSeed)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L442)
```java
    } else {
      // Generate patients up to the specified population size.
      for (int i = 0; i < this.options.population; i++) {
        final int index = i;
        final long seed = this.random.nextLong();
        threadPool.submit(() -> generatePerson(index, seed));
      }
    }
```
- [Generator.generatePerson(int index, long personSeed)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L442) create `demoAttributes` with `Generator.randomDemographics(Random random)`
```java
      Random randomForDemographics = new Random(personSeed);
      Map<String, Object> demoAttributes = randomDemographics(randomForDemographics);
```
- ( 2020-11-28 00:19:24 )
- [Generator.generatePerson(int index, long personSeed)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L442) then create `person` with [`Generator.(long personSeed, Map<String, Object> demoAttributes)`](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L563-576)

```java
        person = createPerson(personSeed, demoAttributes);
```

```java
  public Person createPerson(long personSeed, Map<String, Object> demoAttributes) {
    Person person = new Person(personSeed);
    person.populationSeed = this.options.seed;
    person.attributes.putAll(demoAttributes);
    person.attributes.put(Person.LOCATION, location);
    person.lastUpdated = (long) demoAttributes.get(Person.BIRTHDATE);


    LifecycleModule.birth(person, person.lastUpdated);
    person.currentModules = Module.getModules(modulePredicate);


    updatePerson(person);


    return person;
  }
```
- [Generator.randomDemographics(Random random)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L614-L618) create `demoAttributes` with [Generator.pickDemographics(Random random, Demographics city)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L659)
```java
  public Map<String, Object> randomDemographics(Random random) {
    Demographics city = location.randomCity(random);
    Map<String, Object> demoAttributes = pickDemographics(random, city);
    return demoAttributes;
  }
```
- [Generator.pickDemographics(Random random, Demographics city)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L659) will put the following attributes into `demoAttributes`:
  - `Person.CITY`, `Person.STATE`, `county`, `Person.RACE`, `Person.ETHNICITY`, `Person.FIRST_LANGUAGE`, `Person.GENDER`,
  - `Person.EDUCATION`, `Person.EDUCATION_LEVEL`, `Person.INCOME`, `Person.INCOME_LEVEL`, `Person.OCCUPATION_LEVEL`, `Person.SOCIOECONOMIC_SCORE`, `Person.SOCIOECONOMIC_CATEGORY`,
  - `TARGET_AGE`, `Person.BIRTHDATE`.
- ( 2020-11-27 22:34:31 ) I also found that there's a new feature to load JSON file from `fixedRecordPath` after last stable release `v2.6.1`
  - we can learn from its implementation as well.
  - it will call [Generator.pickFixedDemographics(int index, Random random)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L734) which call [Generator.pickDemographics(Random random, Demographics city)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L659) too. But it overwrite `Person.BIRTHDATE`, `Person.BIRTH_CITY`, `Person.GENDER`, and add `Person.RECORD_GROUP`, `Person.LINK_ID` to demoAttributes.
  - we can learn from [FixedRecordGroupTest.setup()](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/test/java/org/mitre/synthea/engine/FixedRecordGroupTest.java#L28) and see the test json file [src/test/resources/fixed_demographics/fixed_demographics_test.json](https://github.com/synthetichealth/synthea/blob/master/src/test/resources/fixed_demographics/fixed_demographics_test.json)

  ```
      System.out.println("Usage: run_synthea [options] [state [city]]");
      System.out.println("Options: [-s seed] [-cs clinicianSeed] [-p populationSize]");
      ... (skipped) ...
      System.out.println("         [-t updateTimePeriodInDays]");
      System.out.println("         [-f fixedRecordPath]");
      System.out.println("         [--config* value]");
      System.out.println("          * any setting from src/main/resources/synthea.properties");
  ```

### Exporter - Person

- [Exporter.exportRecord(Person person, String fileTag, long stopTime, ExporterRuntimeOptions options)](https://github.com/synthetichealth/synthea/blob/bef87a9b779514d78329f1835e334890f8d62fc6/src/main/java/org/mitre/synthea/export/Exporter.java#L235-L240)

```java
    if (Boolean.parseBoolean(Config.get("exporter.ccda.export"))) {
      String ccdaXml = CCDAExporter.export(person, stopTime);
      File outDirectory = getOutputFolder("ccda", person);
      Path outFilePath = outDirectory.toPath().resolve(filename(person, fileTag, "xml"));
      writeNewFile(outFilePath, ccdaXml);
    }
```

- [CCDAExporter.export(Person person, long time)](https://github.com/synthetichealth/synthea/blob/6e4507a6170322fec628c923256a8fb4c6fd34b6/src/main/java/org/mitre/synthea/export/CCDAExporter.java#L65-L114)

```java
  public static String export(Person person, long time) {
    // create a super encounter... this makes it easier to access
    // all the Allergies (for example) in the export templates,
    // instead of having to iterate through all the encounters.
    Encounter superEncounter = person.record.new Encounter(time, "super");
    for (Encounter encounter : person.record.encounters) {
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
      } else {
        break;
      }
    }


    // The export templates fill in the record by accessing the attributes
    // of the Person, so we add a few attributes just for the purposes of export.
    person.attributes.put("UUID", new UUIDGenerator(person));
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
    person.attributes.put("ethnicity_display_lookup",
        RaceAndEthnicity.LOOK_UP_CDC_ETHNICITY_DISPLAY);


    StringWriter writer = new StringWriter();
    try {
      Template template = TEMPLATES.getTemplate("ccda.ftl");
      template.process(person.attributes, writer);
    } catch (Exception e) {
      e.printStackTrace();
    }
    return writer.toString();
  }
}
```

## 2020-11-28

- ( 2020-11-28 00:06:23 )
```scala
import java.io._
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._
```
- ( 2020-11-28 20:35:04 )
```
