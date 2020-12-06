# Development Notes

[TOC]

## 2020-11-24

- https://github.com/synthetichealth/synthea/wiki/Embedding

## 2020-11-25

### Generator - `internalStore` - `updatedPopulationSnapshotPath`

- We can use `updatedPopulationSnapshotPath` to store `Person` class object into `snapshot` file
    - [Generator.run()](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L364-L376) will store `internalStore` if we specified `updatedPopulationSnapshotPath`.
```java
    // Save a snapshot of the generated population using Java Serialization
    if (options.updatedPopulationSnapshotPath != null) {
      FileOutputStream fos = null;
      try {
        fos = new FileOutputStream(options.updatedPopulationSnapshotPath);
        ObjectOutputStream oos = new ObjectOutputStream(fos);
        oos.writeObject(internalStore);
        oos.close();
        fos.close();
      } catch (Exception ex) {
        System.out.printf("Unable to save population snapshot, error: %s", ex.getMessage());
      }
```
```bash
[11/25 11:53:57] ./run_synthea -s $RANDOM -p 100 -u snapshot.2020-11-25_11
[11/25 12:11:52] file snapshot.2020-11-25_11
```
```bash
~/git/synthea$ file snapshot.2020-11-25_11
snapshot: Java serialization data, version 5
```
### mismatched jar file version

- ( 2020-11-26 01:19:07 )
- When importing from maven package, we need to make sure the jar file version. If the Java version is mismatched, there will be a `java.lang.UnsupportedClassVersionError`。
    - Here is an example using sbt `1.3.8` + scala `2.12.10` + JVM `1.8.0`

```
~/git/cch-ccda-generator$ sbt
[info] Updated file /Users/jazzwang/git/cch-ccda-generator/project/build.properties: set sbt.version to 1.3.8
[info] Loading project definition from /Users/jazzwang/git/cch-ccda-generator/project
[info] Loading settings for project sbt-create from build.sbt ...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/cch-ccda-generator/)
[info] sbt server started at local:///Users/jazzwang/.sbt/1.0/server/ae1837471fe1a34adce9/sock
sbt:sbt-create> console
[info] Starting scala interpreter...
Welcome to Scala 2.12.10 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala> import org.mitre.synthea.engine.Generator
import org.mitre.synthea.engine.Generator

scala> val option = new Generator.GeneratorOptions()
java.lang.UnsupportedClassVersionError: org/mitre/synthea/engine/Generator$GeneratorOptions has been compiled by a more recent version of the Java Runtime (class file version 58.0), this version of the Java Runtime only recognizes class file versions up to 52.0
  at java.lang.ClassLoader.defineClass1(Native Method)
  at java.lang.ClassLoader.defineClass(ClassLoader.java:757)
  at java.security.SecureClassLoader.defineClass(SecureClassLoader.java:142)
  ... (skipped) ...
```

## 2020-11-26

### Generator - `internalStore` - Person - Demographics

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
- [Generator.internalStore](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L80-L85) is for testing and debugging.
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

### Embedding & JSON integration (FHIRv4)

- https://github.com/synthetichealth/synthea/wiki/Embedding#json-integration
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
jazzwang:~$ cd ~/git/cch-ccda-generator
jazzwang:~/git/cch-ccda-generator$ sbt console
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
```
- ( 2020-11-26 15:13:22 ) loading synthea.jar (without dependencies) to scala REPL
```
jazzwang:~/git/synthea$ scala -cp build/libs/synthea.jar
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
- ( 2020-11-26 15:37:51 ) create `uberJar` with JDK8
```
jazzwang:~/git/synthea$ ./gradlew uberJar
jazzwang:~/git/synthea$ scala -cp build/libs/synthea-with-dependencies.jar
```
- ( 2020-11-26 15:41:04 ) Error: `java.lang.OutOfMemoryError: GC overhead limit exceeded`
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

- ( 2020-11-26 15:41:44 ) increase HEAP size by defining `JAVA_OPTS` environment variable:

```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
```

- ( 2020-11-26 15:47:30 ) store JSON string to a JSON file
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
- [Generator.generatePerson(int index, long personSeed)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L442) then create `person` with [`Generator.createPerson(long personSeed, Map<String, Object> demoAttributes)`](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L563-576)

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

## 2020-11-29

### `createPerson` with `demographicsOutput`

- ( 2020-11-29 16:12:35 )
- [Generator.generatePerson(int index)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L423-L427)
```java
  public Person generatePerson(int index) {
    // System.currentTimeMillis is not unique enough
    long personSeed = UUID.randomUUID().getMostSignificantBits() & Long.MAX_VALUE;
    return generatePerson(index, personSeed);
  }
```
- ( 2020-11-29 16:55:40 )
- [Generator.pickFixedDemographics(int index, Random random)](https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L729-L760)
```java
  private Map<String, Object> pickFixedDemographics(int index, Random random) {
    // Get the first FixedRecord from the current RecordGroup
    FixedRecordGroup recordGroup = this.recordGroups.get(index);
    FixedRecord fr = recordGroup.records.get(0);
    // Get the city from the location in the fixed record.
    this.location = new Location(fr.state, recordGroup.getSafeCity());
    Demographics city = this.location.randomCity(random);
    // Pick the rest of the demographics based on the location of the fixed record.
    Map<String, Object> demoAttributes = pickDemographics(random, city);
```
- test with following syntax using Scala REPL
```scala
import java.io._
import java.util._
import java.time._
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._
import org.mitre.synthea.world.agents._
import org.mitre.synthea.world.geography._
import org.mitre.synthea.world.concepts._

val options = new Generator.GeneratorOptions();

// disable default options
Config.set("exporter.fhir.export", "false");
Config.set("exporter.fhir.transaction_bundle", "false");
Config.set("exporter.hospital.fhir.export", "false");
Config.set("exporter.practitioner.fhir.export", "false");
Config.set("generate.append_numbers_to_person_names", "false");
// enable C-CDA exporter
Config.set("generate.only_alive_patients", "true");
Config.set("exporter.ccda.export", "true");

val ero = new Exporter.ExporterRuntimeOptions();
val generator = new Generator(options, ero);

// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L425
val personSeed = UUID.randomUUID().getMostSignificantBits() & Long.MaxValue;
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L564
val person = new Person(personSeed);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L222
val state = "Colorado";
val city = "Denver";
val location = new Location(state, city)
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L565
person.populationSeed = options.seed;
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L217
val random = new Random(options.seed);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L661
val demographicsOutput = new HashMap[String, Object]();
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L663-L666
// Pull the person's location data.
demographicsOutput.put(Person.CITY, city);
demographicsOutput.put(Person.STATE, state);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L668-L674
// Generate the person's race data based on their location.
val race_ethnicity = org.apache.commons.collections.MapUtils.invertMap(RaceAndEthnicity.LOOK_UP)
val race = race_ethnicity.get("2106-3").toString;
val ethnicity = race_ethnicity.get("2135-2").toString;
val language = "english";
demographicsOutput.put(Person.RACE, race)
demographicsOutput.put(Person.ETHNICITY, ethnicity);
demographicsOutput.put(Person.FIRST_LANGUAGE, language);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L688
demographicsOutput.put(Person.GENDER, "unknown");
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L741
val randomCity = location.randomCity(random);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L691
val education = randomCity.pickEducation(random);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L692
demographicsOutput.put(Person.EDUCATION, education);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L693
val educationLevel = randomCity.educationLevel(education, random).asInstanceOf[java.lang.Double];
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L694
demographicsOutput.put(Person.EDUCATION_LEVEL, educationLevel);
val income = randomCity.pickIncome(random).asInstanceOf[java.lang.Double];
demographicsOutput.put(Person.INCOME, income);
val incomeLevel = randomCity.incomeLevel(income).asInstanceOf[java.lang.Double];
demographicsOutput.put(Person.INCOME_LEVEL, incomeLevel);
val occupation = random.nextDouble().asInstanceOf[java.lang.Double];
demographicsOutput.put(Person.OCCUPATION_LEVEL, occupation);
val sesScore = randomCity.socioeconomicScore(incomeLevel, educationLevel, occupation);
demographicsOutput.put(Person.SOCIOECONOMIC_SCORE, sesScore);
demographicsOutput.put(Person.SOCIOECONOMIC_CATEGORY, randomCity.socioeconomicCategory(sesScore));
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/input/FixedRecord.java#L99-L100
val birthdate = LocalDateTime.of(1961,9,8,12,0).toInstant(ZoneOffset.UTC).toEpochMilli(); //1961-09-08T12:00:00
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L723
demographicsOutput.put(Person.BIRTHDATE, birthdate);
// https://github.com/synthetichealth/synthea/blob/fbfd20e1c210c952b16962ffb72d789634bcfc42/src/main/java/org/mitre/synthea/engine/Generator.java#L511
person.attributes.putAll(demographicsOutput);
person.attributes.put(Person.LOCATION, location);
person.lastUpdated = birthdate;
// LifecycleModule.birth(person, person.lastUpdated);
val firstName = "Salomon";
val lastName = "Cockshutt";
val birthPlace = location.randomBirthPlace(person);
val phoneNumber = "555-" + ((person.randInt(999 - 100 + 1) + 100)) + "-" + ((person.randInt(9999 - 1000 + 1) + 1000));
val ssn = "999-" + ((person.randInt(99 - 10 + 1) + 10)) + "-" + ((person.randInt(9999 - 1000 + 1) + 1000));
val address = "6 Lyons Street Denver, Colorado 32985"
val zip = "32985"
person.attributes.put(Person.ID, person.randUUID().toString());
person.attributes.put(Person.FIRST_NAME, firstName);
person.attributes.put(Person.LAST_NAME, lastName);
person.attributes.put(Person.NAME, firstName + " " + lastName);
person.attributes.put(Person.ADDRESS, address);
person.attributes.put(Person.TELECOM, phoneNumber);
person.attributes.put(Person.IDENTIFIER_SSN, ssn);
person.attributes.put(Person.ADDRESS, address);
person.attributes.put(Person.ZIP, zip);
person.attributes.put(Person.BIRTH_CITY, birthPlace[0]);
person.attributes.put(Person.BIRTH_STATE, birthPlace[1]);
person.attributes.put(Person.BIRTH_COUNTRY, birthPlace[2]);
person.attributes.put(Person.ACTIVE_WEIGHT_MANAGEMENT, false);
updatePerson(person);
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L218
val timestep = Config.get("generate.timestep").toLong;
// https://github.com/synthetichealth/synthea/blob/e9354e75076e1b8b98d4810d2987eb45c228ef70/src/main/java/org/mitre/synthea/engine/Generator.java#L468
val finishTime = person.lastUpdated + timestep;
// https://github.com/synthetichealth/synthea/blob/fbfd20e1c210c952b16962ffb72d789634bcfc42/src/main/java/org/mitre/synthea/engine/Generator.java#L442
Exporter.export(person, finishTime, ero);
```

### read `snapshot` into `Person`

- ( 2020-11-29 23:41:43 )
```scala
import java.io._
import java.util._
import org.mitre.synthea.world.agents._

val fis = new FileInputStream("snapshot.2020-11-26_12")
val ois = new ObjectInputStream(fis);
val persons = ois.readObject().asInstanceOf[java.util.List[org.mitre.synthea.world.agents.Person]]
ois.close();
persons.size
val bw = new BufferedWriter(new FileWriter(new File("snapshot_0.txt")))
bw.write(persons.get(0).attributes.toString)
```
- ( 2020-11-30 00:20:51 )

## 2020-11-30

- ( 2020-11-30 09:34:04 )
- After the exploration of `Generator`, `Exporter` and `Person` classes, the best way to create one person with **specified fields** are:
  1. use `Generator.createPerson(int index)` with `state`, `city`, `age` and `gender`
  2. manually update `firstName`, `lastName`, `race`, `ethnicity` and other fields into `Person.attributes`.

### Update `Person` attributes before running `Exporter`

- ( 2020-11-30 10:01:52 )
```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala>
```
- test with Scala REPL
```scala
import java.io._
import java.time._
import org.mitre.synthea.engine._
import org.mitre.synthea.helpers._
import org.mitre.synthea.export._

val options = new Generator.GeneratorOptions();
val ero = new Exporter.ExporterRuntimeOptions();
val generator = new Generator(options, ero);

Config.set("generate.append_numbers_to_person_names", "false");

generator.options.gender = "F";
generator.options.state = "Pennsylvania";
generator.options.city = "Scranton";
generator.options.ageSpecified = true;
generator.options.minAge = 5;
generator.options.maxAge = 6;


val person = generator.generatePerson(0)

generator.options.gender = "M";
generator.options.state = "Virginia";
generator.options.city = "Richmond";
generator.options.ageSpecified = true;
generator.options.minAge = 72;
generator.options.maxAge = 73;

val person = generator.generatePerson(1)
```
- ( 2020-11-30 11:16:32 ) confirmed that we can create different person with specified age.

### generate C-CDA XML based on self-defined FreeMaker template

- ( 2020-11-30 12:55:34 )
- create symbolic link to `src/main/resources/templates/`
```bash
jazzwang:~/git/synthea$ ln -s src/main/resources/templates/
```
- ( 2020-11-30 13:01:38 ) test following syntax with Scala REPL:
```scala
import java.io._;
import java.time._;
import freemarker.template._;
import org.mitre.synthea.engine._;
import org.mitre.synthea.helpers._;
import org.mitre.synthea.export._;
import org.mitre.synthea.world.agents._;
import org.mitre.synthea.world.concepts._;

var options = new Generator.GeneratorOptions();
var ero = new Exporter.ExporterRuntimeOptions();

Config.set("generate.append_numbers_to_person_names", "false");

options.gender = "F";
options.state = "Pennsylvania";
options.city = "Scranton";
options.ageSpecified = true;
options.minAge = 5;
options.maxAge = 6;

var generator = new Generator(options, ero);

var person = generator.generatePerson(0);

// modify first name and last name
person.attributes.put(Person.FIRST_NAME, "Janey");
person.attributes.get(Person.FIRST_NAME);
person.attributes.put(Person.LAST_NAME, "Mayger");
person.attributes.get(Person.LAST_NAME);
person.attributes.put(Person.NAME, "Janey Mayger");

var time = generator.stop
person.attributes.put("time", time);
person.attributes.put("race_lookup", RaceAndEthnicity.LOOK_UP_CDC_RACE);
person.attributes.put("ethnicity_lookup", RaceAndEthnicity.LOOK_UP_CDC_ETHNICITY_CODE);
person.attributes.put("ethnicity_display_lookup", RaceAndEthnicity.LOOK_UP_CDC_ETHNICITY_DISPLAY);

// write `Person.attributes` KeySet to `person-attributes-key.txt`
var bw = new BufferedWriter(new FileWriter(new File("person-attributes-key.txt")));
bw.write(person.attributes.keySet.toString);
bw.close();

// generate CCD XML based on `ccda.ftl`
var configuration = new Configuration(Configuration.VERSION_2_3_26);
configuration.setDefaultEncoding("UTF-8");
configuration.setLogTemplateExceptions(false);
configuration.setSetting("object_wrapper", "DefaultObjectWrapper(2.3.26, forceLegacyNonListCollections=false, iterableSupport=true, exposeFields=true)");
configuration.setAPIBuiltinEnabled(true);
configuration.setDirectoryForTemplateLoading(new File("templates/ccda"));
var template = configuration.getTemplate("ccda.ftl")
var writer = new StringWriter();
template.process(person.attributes, writer);
var bw = new BufferedWriter(new FileWriter(new File("Janey_Mayger.xml")));
bw.write(writer.toString);
bw.close();
```

### Data Model Mapping

- ( 2020-11-30 17:20:37 )

| Key of `Person.Attributes` | ccda.ftl | `section`.ftl |
|-------------------|--------------|---------------|
| AGE | N | N |
| AGE_MONTHS | N | N |
| DALY | N | N |
| QALY | N | N |
| QOLS | N | N |
| RH_NEG | N | N |
| active_weight_management | N | N |
| address | Y | N |
| adherence probability | N | N |
| birth_city | N | N |
| birth_country | N | N |
| birth_state | N | N |
| birthdate | Y | Y |
| birthplace | N | N |
| bmi_percentile | N | N |
| cardio_risk | N | N |
| city | Y | N |
| ckd | N | N |
| coordinate | N | N |
| county | N | N |
| covid19 | N | N |
| covid19_careplan | N | N |
| covid19_death | N | N |
| covid19_risk | N | N |
| covid19_severity | N | N |
| current-encounters | N | N |
| current_weight_length_percentile | N | N |
| deductible | N | N |
| diabetic_eye_damage | N | N |
| diabetic_nerve_damage | N | N |
| education | N | N |
| education_level | N | N |
| ethnicity | Y | N |
| first_language | N (should be Y) | N |
| first_name | N (shoule be Y) | N |
| gender | Y | N |
| growth_trajectory | N | N |
| id | Y (for `root="2.16.840.1.113883.19.5"`) | N |
| identifier_ssn | N | N |
| immunizations | N | Y (section `immunizations`) |
| income | N | N |
| income_level | N | N |
| last_month_paid | N | N |
| last_name | N (should be Y) | N |
| location | N | N |
| most-recent-daly | N | N |
| most-recent-qaly | N | N |
| name | Y | N |
| name_father | N | N |
| name_mother | N | N |
| number_of_children | N | N |
| occupation_level | N | N |
| preferredProviderambulatory | N | N |
| preferredProviderwellness | Y | N |
| pregnant | N | N |
| race | Y | N |
| sexual_orientation | N | N |
| sexually_active | N | N |
| socioeconomic_category | N | N |
| socioeconomic_score | N | N |
| state | Y | N |
| target_age | N | N |
| telecom | N (should be Y) | N |
| zip | Y | N |

- Table: *( 2020-12-01 13:48:40 ) updated based on `ccda.ftl` and other templates*

### fixing FreeMarker issue

- ( 2020-11-30 18:12:07 )
- update `Hello.scala` to generate the specified XML output.
- ( 2020-11-30 23:19:25 )
- found missing sections data within generated XML output.
  - Reason: missing `ehr_allergies`. `ehr_conditions`, etc.

## 2020-12-01

### `person.attributes` used in `FreeMarker` templates

- ( 2020-12-01 10:23:46 )
```
templates/ccda$ grep --color "\${.*}" * | sed 's#.*\$#\$#g' | sed 's#}.*#}#' | sort | uniq | sort >> ../../MEMO.md
```
```java
${(entry.unit)!""}
${UUID?api.toString()}
${address}
${birthdate?number_to_date?string["yyyyMMddHHmmss"]}
${city}
${code.display}
${codes[0].display}
${entry.codes[0].code}
${entry.codes[0].display}
${entry.manufacturer}
${entry.start?number_to_date?string["yyyyMMddHHmmss"]}
${entry.start?number_to_datetime?iso_local}
${entry.stop?number_to_date?string["yyyyMMddHHmmss"]}
${entry.stop?number_to_datetime?iso_local}
${entry.unit}
${entry.value.display}
${entry.value}
${entry?counter}
${ethnicity_display_lookup[race]}
${gender}
${id}
${instance.dicomUid}
${instance.sopClass.display}
${name?keep_after_last(" ")}
${name?keep_before_last(" ")}
${name}
${obs.start?number_to_date?string["yyyyMMddHHmmss"]}
${obs.unit}
${obs.value}
${preferredProviderwellness.address?replace("&", "&amp;")}
${preferredProviderwellness.city}
${preferredProviderwellness.name?replace("&", "&amp;")}
${preferredProviderwellness.state}
${preferredProviderwellness.zip}
${race}
${section}
${series.dicomUid}
${series.modality.display}
${state}
${study.dicomUid}
${study.start?number_to_date?string["yyyyMMddHHmmss"]}
${tag}
${time?number_to_date?string["yyyyMMddHHmmss"]}
${zip}
```
- ( 2020-12-01 10:53:43 ) `person.attributes` difference after running `CCDAExporter.export()`
```
$ diff -Naur key1 key2 >> MEMO.md
```
```diff
--- key1	2020-12-01 10:44:56.000000000 +0800
+++ key2	2020-12-01 10:44:50.000000000 +0800
@@ -49,6 +49,7 @@
  Sore Throat Condition
  Sore Throat Module
  Total Joint Replacement Module
+ UUID
  Urinary Tract Infections Module
  Veteran Hyperlipidemia Module
  Veteran Lung Cancer Module
@@ -88,7 +89,19 @@
  diabetic_nerve_damage
  education
  education_level
+ ehr_allergies
+ ehr_careplans
+ ehr_conditions
+ ehr_encounters
+ ehr_imaging_studies
+ ehr_immunizations
+ ehr_medications
+ ehr_observations
+ ehr_procedures
+ ehr_reports
  ethnicity
+ ethnicity_display_lookup
+ ethnicity_lookup
  first_language
  first_name
  gender
@@ -113,6 +126,7 @@
  preferredProviderwellness
  pregnant
  race
+ race_lookup
  sexual_orientation
  sexually_active
  socioeconomic_category
@@ -120,4 +134,5 @@
  state
  target_age
  telecom
+ time
  zip
```
- ( 2020-12-01 11:17:43 )
```bash
$ grep "\${.*}" templates/ccda/* | sed 's#.*\$#\$#g' | sed 's#}.*#}#' | sort | uniq | sort | sed 's#\${[(]*##' | sed 's#?.*##' | sed 's#\..*##' | sed 's#\[.*##' | tr -d '}' | sort -n | uniq | nl
     1	UUID
     2	address
     3	birthdate
     4	city
     5	code
     6	codes
     7	entry
     8	ethnicity_display_lookup
     9	gender
    10	id
    11	instance
    12	name
    13	obs
    14	preferredProviderwellness
    15	race
    16	section
    17	series
    18	state
    19	study
    20	tag
    21	time
    22	zip
```
- ( 2020-12-01 11:23:01 ) `person.attributes` KeySet used in FreeMarker templates
```bash
$ grep "\${.*}" templates/ccda/* | sed 's#.*\$#\$#g' | sed 's#}.*#}#' | sort | uniq | sort | sed 's#\${[(]*##' | sed 's#?.*##' | sed 's#\..*##' | sed 's#\[.*##' | tr -d '}' | sort -n | uniq > used_key
```
```
$ for i in $(cat used_key);do A=$(grep " $i$" key2) ; if [ $? -eq 0 ]; then echo "| $i | YES |"; else echo "| $i | NO |"; fi; done
```
| `FreeMarker` variable | within `Person.Attributes` |
|--|--|
| UUID | YES |
| address | YES |
| birthdate | YES |
| city | YES |
| code | NO |
| codes | NO |
| entry | NO |
| ethnicity_display_lookup | YES |
| gender | YES |
| id | YES |
| instance | NO |
| name | YES |
| obs | NO |
| preferredProviderwellness | YES |
| race | YES |
| section | NO |
| series | NO |
| state | YES |
| study | NO |
| tag | NO |
| time | YES |
| zip | YES |
- ( 2020-12-01 11:38:56 ) `codes` = `code_with_reference.ftl`
```
$ grep "as codes" templates/ccda/*
templates/ccda/allergies.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/conditions.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/encounters.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/immunizations.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/medical_equipment.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/medications.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/procedures.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/results.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/social_history.ftl:<#import "code_with_reference.ftl" as codes>
templates/ccda/vital_signs.ftl:<#import "code_with_reference.ftl" as codes>
```
- ( 2020-12-01 11:41:00 ) `code` is part of `codes`
```
$ grep "as code>" templates/ccda/*
templates/ccda/code_with_reference.ftl:            <#list codes[1..] as code>
```
- ( 2020-12-01 11:43:02 ) `entry` = attributes `ehr_*` created within `CCDAExporter.export()`
```
grep "as entry" templates/ccda/* | column -t
templates/ccda/allergies.ftl:          <#list  ehr_allergies          as  entry>
templates/ccda/conditions.ftl:         <#list  ehr_conditions         as  entry>
templates/ccda/encounters.ftl:         <#list  ehr_encounters         as  entry>
templates/ccda/immunizations.ftl:      <#list  ehr_immunizations      as  entry>
templates/ccda/medical_equipment.ftl:  <#list  ehr_medical_equipment  as  entry>
templates/ccda/medications.ftl:        <#list  ehr_medications        as  entry>
templates/ccda/narrative_block.ftl:    <#list  entries                as  entry>
templates/ccda/procedures.ftl:         <#list  ehr_procedures         as  entry>
templates/ccda/results.ftl:            <#list  ehr_reports            as  entry>
templates/ccda/social_history.ftl:     <#list  ehr_social_history     as  entry>
templates/ccda/vital_signs.ftl:        <#list  ehr_observations       as  entry>
```
- ( 2020-12-01 11:51:16 ) `entry` = `entries` in `narrative_block.ftl`
```
$ grep 'entries' templates/ccda/narrative_block.ftl
<#macro narrative section entries>
        <#if entries[0].value??>
      <#list entries as entry>
```
- ( 2020-12-01 11:44:16 ) `instance` = `series.instances` = `ehr_imaging_studies.series.instances`
```
$ grep "as instance" templates/ccda/*
templates/ccda/diagnostic_imaging_reports.ftl:            <#list series.instances as instance>
```
- ( 2020-12-01 11:45:22 ) `obs` = `entry.observations` = `ehr_*.observations`
```
$ grep "as obs" templates/ccda/*
templates/ccda/narrative_block.ftl:          <#list entry.observations as obs>
templates/ccda/results.ftl:        <#list entry.observations as obs>
templates/ccda/vital_signs.ftl:        <#list entry.observations as obs>
```
- ( 2020-12-01 11:52:51 ) `series` = `study.series` = `ehr_imaging_studies.series`
```
$ grep 'as series' templates/ccda/*
templates/ccda/diagnostic_imaging_reports.ftl:        <#list study.series as series>
```
- ( 2020-12-01 11:55:30 ) `study` = `ehr_imaging_studies`
```
$ grep 'as study' templates/ccda/*
templates/ccda/diagnostic_imaging_reports.ftl:    <#list ehr_imaging_studies as study>
```
- ( 2020-12-01 11:59:27 ) `tag` = "code"
```
$ grep 'tag=' templates/ccda/*
templates/ccda/code_with_reference.ftl:<#macro code_section codes section counter tag="code" extra="">
templates/ccda/conditions.ftl:            <@codes.code_section codes=entry.codes section="conditions" counter=entry?counter tag="value" extra="xsi:type=\"CD\""/>
```
```
$ grep '${tag' templates/ccda/*
templates/ccda/code_with_reference.ftl:        <${tag} ${extra} code="${codes[0].code}" codeSystem="<@lookup.oid_for_code_system system=codes[0].system/>" displayName="${codes[0].display}">
templates/ccda/code_with_reference.ftl:        </${tag}>
templates/ccda/code_with_reference.ftl:        <${tag} nullFlavor="UNK"/>
```

### Scala does not support `inner class`?

- ( 2020-12-01 13:52:52 ) Based on [CCDAExporter.export(Person person, long time)](https://github.com/synthetichealth/synthea/blob/6e4507a6170322fec628c923256a8fb4c6fd34b6/src/main/java/org/mitre/synthea/export/CCDAExporter.java#L65-L114), Attributes `ehr_*`are from `org.mitre.synthea.world.concepts.HealthRecord.Encounter`
- https://stackoverflow.com/questions/1069987/static-inner-classes-in-scala
- [HealthRecord.Encounter](https://github.com/synthetichealth/synthea/blob/fbfd20e1c210c952b16962ffb72d789634bcfc42/src/main/java/org/mitre/synthea/world/concepts/HealthRecord.java#L492-L521)
```java
public class HealthRecord implements Serializable {

... (skipped) ...

  public class Encounter extends Entry {
    public List<Observation> observations;
    public List<Report> reports;
    public List<Entry> conditions;
    public List<Entry> allergies;
    public List<Procedure> procedures;
    public List<Immunization> immunizations;
    public List<Medication> medications;
    public List<CarePlan> careplans;
    public List<ImagingStudy> imagingStudies;
    public List<Device> devices;
    public List<Supply> supplies;
    public Claim claim; // for now assume 1 claim per encounter
    public Code reason;
    public Code discharge;
    public Provider provider;
    public Clinician clinician;
    public boolean ended;
    // Track if we renewed meds at this encounter. Used in State.java encounter state.
    public boolean chronicMedsRenewed;
    public String clinicalNote;


    /**
     * Construct an encounter.
     * @param time the time of the encounter.
     * @param type the type of the encounter.
     */
    public Encounter(long time, String type) {
      super(time, type);
      if (type.equalsIgnoreCase(EncounterType.EMERGENCY.toString())) {
```
- ( 2020-12-01 14:01:47 ) But we can't find `org.mitre.synthea.world.concepts.HealthRecord.Encounter` within Scala REPL
```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.
```
```scala
scala> import org.mitre.synthea.world.concepts.HealthRecord.Encounter
<console>:11: error: value Encounter is not a member of object org.mitre.synthea.world.concepts.HealthRecord
       import org.mitre.synthea.world.concepts.HealthRecord.Encounter
scala> import org.mitre.synthea.world.agents.Person
import org.mitre.synthea.world.agents.Person
scala> val healthrecord = new HealthRecord(new Person(0L))
healthrecord: org.mitre.synthea.world.concepts.HealthRecord = org.mitre.synthea.world.concepts.HealthRecord@3f40568e
scala> healthrecord.encounters
res0: java.util.List[org.mitre.synthea.world.concepts.HealthRecord#Encounter] = []
scala> healthrecord.currentEncounter
   def currentEncounter(x$1: Long): org.mitre.synthea.world.concepts.HealthRecord#Encounter
```
- ( 2020-12-01 14:28:24 ) Use `person.record.encounters.get(0)` as `superEncounter` of `CCDAExporter.export()`

## 2020-12-02

### Support "Consultation Note"

- reference:
  - [HL7 Implementation Guide for CDA® Release 2: Consolidated CDA Templates for Clinical Notes](http://www.hl7.org/documentcenter/public/standards/dstu/CDAR2_IG_CCDA_CLINNOTES_R1_DSTU2.1_2015AUG_2019JUNwith_errata-errata2020.zip)
    - check `CDAR2_IG_CCDA_CLINNOTES_R1_DSTU2.1_2015AUG_Vol2_2019JUNwith_errata.pdf` after unzip the downloaded ZIP file.
    - Page 34~35 listed required sections
  - https://github.com/HL7/C-CDA-Examples/blob/master/Documents/Consultation%20Note/Consultation_Note.xml
- add `templates/ccda/consultation_note.ftl` and `templates/ccda/present_illness_no_current.ftl`
  - ONLY include **required** sections:
    - `History of Present Illness` Section
    - `Allergies and Intolerances` Section (entries required) (V3)
    - `Problem` Section (entries required) (V3)
- ( 2020-12-02 15:57:16 ) confirmed to generate sample output `Janey_Mayger.xml` and `Janey_Mayger-consultation_note.xml`

### Validation - using XSD

- ( 2020-12-02 11:55:21 ) `C32_CDA.xsd` could be download in following Test Package
  - https://cda-validation.nist.gov/cda-validation/downloads/HITSP_C32v2.1_TestPackage.zip
  - https://cda-validation.nist.gov/cda-validation/downloads.html
```xml
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- edited with XMLSPY v2004 rel. 3 U (http://www.xmlspy.com) by Bob Dolin (HL7 CDA TC) -->
<xs:schema targetNamespace="urn:hl7-org:v3" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="urn:hl7-org:v3" xmlns:mif="urn:hl7-org:v3/mif" elementFormDefault="qualified">
	<xs:include schemaLocation="C32_POCD_MT000040.xsd"/>
	<xs:element name="ClinicalDocument" type="POCD_MT000040.ClinicalDocument"/>
</xs:schema>
```
- it will reference `C32_POCD_MT000040.xsd`
- https://github.com/scala/scala-xml/wiki/XML-validation
- [XML validation mechanisms](https://ec.europa.eu/cefdigital/wiki/download/attachments/55891984/CEFeInvoicingWebinar%238XMLValidationMechanisms_v1.0.pdf?version=1&modificationDate=1518541361643&api=v2)

### Validation - using `Schematron`

- ( 2020-12-02 16:34:50 )
- https://github.com/ewadkins/cda-schematron

- https://www.infoq.com/news/2008/04/xsd-schematron-real-world/
- https://schematron.com/ - ISO Schematron

## 2020-12-03

- ( 2020-12-03 00:56:46 )
- Care Plan (V2) - there are only two required sections
  - `Health Concerns` Section (V2)
  - `Goals` Section

## 2020-12-04

## 2020-12-05

- [HL7 CDA Document Validation and Content Quality Assessment](https://www.hl7.org/documentcenter/public/wg/pug/CDA%20Validation%2020160406%20FINAL.pdf), HL7 Payer Summit User Group, Panel Discussion Moderated by Lisa Nelson, April 6, 2016
  - [ART-DECOR](https://art-decor.org/mediawiki/index.php?title=Download#Software)
    - ART-DECOR® is an open-source tool suite that supports the creation and maintenance of HL7 templates, value sets, scenarios and data sets.
  - [HL7 MDHT(Model-Driven Health Tool)](https://wiki.hl7.org/MDHT_Template_Sub_Project)
  - [Lantana Consulting Group](https://www.lantanagroup.com/about-us/) - provides services and software for standards-based health information exchange.
    - https://www.lantanagroup.com/tag/cdainthewild/
    - **https://validator.lantanagroup.com/**
    - [Trifolia, lantanagroup](https://trifolia.lantanagroup.com/)
    - Trifolia template/profile editor and publication tool
    - https://github.com/lantanagroup/trifolia
- https://developers.google.com/product-review-feeds/validation
  ```
  xmllint --xinclude --schematron HITSP_C32.sch --schema https://xreg2.github.io/schema/cdar2c32/infrastructure/cda/C32_CDA.xsd Janey_Mayger.xml > Janey_Mayger_CCD.xml
  ```
- Schematron
  - https://gazelle.ihe.net/EVSClient/administration/schematrons.seam
  - https://gazelle.ihe.net/gazelle-documentation/Schematron-Validator/user.html
- https://github.com/ramandeep30/xml-validator-scala
  - https://blog.knoldus.com/validating-xml-using-xsd/
- https://github.com/scala/scala-xml/wiki/XML-validation
- Q: will `xmllint` follow `<xsd:include ... />`?
- A: **[indirect imports](https://lists.w3.org/Archives/Public/xmlschema-dev/2004Jul/0010.html)** are not supposed to work.
  - https://stackoverflow.com/a/57776770/4209274
  - for multiple XSD, we should use `<xsd:import ... />`
  - https://stackoverflow.com/a/17003036/4209274
    - http://xerces.apache.org/
- https://learning.oreilly.com/library/view/beginning-xml-5th/9781118239483/

## 2020-12-06

### Discharge Summary

- Reference: https://raw.githubusercontent.com/HL7/C-CDA-Examples/master/Documents/Discharge%20Summary/Discharge_Summary.xml
- add required sections to `discharge_summary.ftl`
  - Allergies and Intolerances Section (entries optional) (V3)
  - Hospital Course Section = `hospital_course.ftl`
  - Discharge Diagnosis Section (V3) = `discharge_diagnosis.ftl`
  - Plan of Treatment Section (V2) = ~~`treatment_plan.ftl`~~ `care_goals.ftl`
- ( 2020-12-06 14:49:35 )
  - remove `treatment_plan.ftl` and use `care_goals.ftl`

### History and Physical

- ( 2020-12-06 19:07:46 )
- Reference: https://raw.githubusercontent.com/HL7/C-CDA-Examples/master/Documents/History%20and%20Physical/History_and_Physical.xml
- add required sections to `history_and_physical.ftl`
  - Allergies and Intolerances Section (entries optional) (V3)
  - Family History Section (V3) = `family_history.ftl`
  - General Status Section = `general_status.ftl`
  - Past Medical History (V3) = `past_medical_history.ftl`
  - Medications Section (entries optional) (V2)
  - Physical Exam Section (V3) = `physical_exam.ftl`
  - Results Section (entries optional) (V3)
  - Review of Systems Section Social History Section (V3) = `review_of_systems.ftl`
  - Vital Signs Section (entries optional) (V3)
- ( 2020-12-06 20:37:05 )

### Operative Note

- ( 2020-12-06 20:41:33 )
- Reference: https://raw.githubusercontent.com/HL7/C-CDA-Examples/master/Documents/Operative%20Note/Operative_Note.xml
- add required sections to `operative_note.ftl`
  - Anesthesia Section (V2) = `anesthesia.ftl`
  - Complications Section (V3) = `complications.ftl`
  - Preoperative Diagnosis Section (V3) = `preoperative_diagnosis.ftl`
  - Procedure Estimated Blood Loss Section = `procedure_estimated_blood_loss.ftl`
  - Procedure Findings Section (V3) = `procedure_findings.ftl`
  - Procedure Specimens Taken Section = `procedure_specimens_taken.ftl`
  - Procedure Description Section = `procedure_description.ftl`
  - Postoperative Diagnosis Section = `postoperative_diagnosis.ftl`
- ( 2020-12-06 22:25:53 )

### Procedure Note

- ( 2020-12-06 22:26:37 )
- Reference: https://raw.githubusercontent.com/HL7/C-CDA-Examples/master/Documents/Procedure%20Note/Procedure_Note.xml
- add required sections to `procedure_note.ftl`
  - Complications Section (V3) = `complications.ftl`
  - Procedure Description Section = `procedure_description.ftl`
  - Procedure Indications Section (V2) = `procedure_indications.ftl`
  - Postprocedure Diagnosis Section (V3) = `postoperative_diagnosis_v3.ftl`
- ( 2020-12-06 22:43:36 )

### Progress Note

- ( 2020-12-06 22:43:41 )
- Reference: https://raw.githubusercontent.com/HL7/C-CDA-Examples/master/Documents/Progress%20Note/Progress_Note.xml
- add `progress_note.ftl`
- no required sections

### C-CDA R2.1 Validation

- use https://validator-legacy.lantanagroup.com/validator/
- fix multiple templates issue
- ( 2020-12-06 23:59:34 )
- format the output with `xmllint`
```
~/git/cch-ccda-generator/output/ccda$ for i in $(ls *.xml); do xmllint --format $i > $i.2; mv $i.2 $i; done
```
- compress 7 documents into single ZIP file
```
~/git/cch-ccda-generator/output/ccda$ zip Janey_Mayger.zip *.xml
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-ccd.xml (deflated 95%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-consult.xml (deflated 87%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-discharge.xml (deflated 72%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-history.xml (deflated 95%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-operative.xml (deflated 76%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-procedure.xml (deflated 72%)
  adding: Janey_Mayger_6b668817-b781-aac7-9d50-d3aae2a32f28-progress.xml (deflated 70%)
```
- passed validation with https://validator-legacy.lantanagroup.com/validator/