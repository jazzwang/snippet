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
~/git/snippet/scala/sbt-create$ sbt
[info] Updated file /Users/jazzwang/git/snippet/scala/sbt-create/project/build.properties: set sbt.version to 1.3.8
[info] Loading project definition from /Users/jazzwang/git/snippet/scala/sbt-create/project
[info] Loading settings for project sbt-create from build.sbt ...
[info] Set current project to sbt-create (in build file:/Users/jazzwang/git/snippet/scala/sbt-create/)
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
- ( 2020-11-26 15:37:51 ) create `uberJar` with JDK8
```
jazzwang:~/git/synthea$ ./gradlew uberJar
jazzwang:~/git/synthea$ cp build/libs/synthea-with-dependencies.jar ~/git/snippet/scala/synthea-embedded/
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
- After the exploration of `Generator`, `Exporter` and `Person` class, the best way to create one person with specified `firstName`, `lastName`, `gender`, `state`, `city` fields is to use `Generator.createPerson(int index)` with `state`, `city`, `age` and `gender`, then manually update `firstName` and `lastName`.

### Update `Person` attributes before running `Exporter`

- ( 2020-11-30 10:01:52 )
```bash
jazzwang:~/git/synthea$ JAVA_OPTS="-Xms1g -Xmx2g" scala -cp build/libs/synthea-with-dependencies.jar
Welcome to Scala 2.11.11 (OpenJDK 64-Bit Server VM, Java 1.8.0_275).
Type in expressions for evaluation. Or try :help.

scala>
```
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
- ( 2020-11-30 13:01:38 ) test with following syntax:
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

val time = generator.stop
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

| Person.Attributes | C-CDA Header | C-CDA Section |
|-------------------|--------------|---------------|
| AGE
| AGE_MONTHS
| DALY
| QALY
| QOLS
| RH_NEG
| active_weight_management
| address
| adherence probability
| birth_city
| birth_country
| birth_state
| birthdate
| birthplace
| bmi_percentile
| cardio_risk
| city
| ckd
| coordinate
| county
| covid19
| covid19_careplan
| covid19_death
| covid19_risk
| covid19_severity
| current-encounters
| current_weight_length_percentile
| deductible
| diabetic_eye_damage
| diabetic_nerve_damage
| education
| education_level
| ethnicity
| first_language
| first_name
| gender
| growth_trajectory
| id
| identifier_ssn
| immunizations
| income
| income_level
| last_month_paid
| last_name
| location
| most-recent-daly
| most-recent-qaly
| name
| name_father
| name_mother
| number_of_children
| occupation_level
| preferredProviderambulatory
| preferredProviderwellness
| pregnant
| race
| sexual_orientation
| sexually_active
| socioeconomic_category
| socioeconomic_score
| state
| target_age
| telecom
| zip

### fixing FreeMarker issue

- ( 2020-11-30 18:12:07 )
- update `Hello.scala` to generate the specified XML output.