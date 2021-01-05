# Development Notes

- Source: https://github.com/DiUS/java-faker
- Web: http://dius.github.io/java-faker/
- Java Docs: http://dius.github.io/java-faker/apidocs/index.html

## 2021-01-04

```bash
~/git/snippet/scala$ mkdir java-faker
~/git/snippet/scala$ cd java-faker/
~/git/snippet/scala/java-faker$ code MEMO.md
~/git/snippet/scala/java-faker$ git gi sbt,scala > .gitignore
~/git/snippet/scala/java-faker$ sbt --sbt-create
sbt:java-faker> set ThisBuild / scalaVersion     := "2.12.12"
sbt:java-faker> set ThisBuild / version          := "0.1.0"
sbt:java-faker> set libraryDependencies += "com.github.javafaker" % "javafaker" % "1.0.2"
sbt:java-faker> update
sbt:java-faker> session save-all
sbt:java-faker> exit
```

## 2021-01-05

- ( 2021-01-05 13:33:00 )
```scala
scala> import com.github.javafaker._
import com.github.javafaker._

scala> val faker = new Faker()
faker: com.github.javafaker.Faker = com.github.javafaker.Faker@2627f9fa

scala> val name = faker.name().fullName()
name: String = Ms. Tommie Luettgen

scala> val name = faker.name()
name: com.github.javafaker.Name = com.github.javafaker.Name@68f918f5

scala> name.fullName
res0: String = Aura Ondricka PhD

scala> name.firstName
res1: String = Kenia

scala> name.lastName
res2: String = Smitham

scala> faker.address.streetAddress
res3: String = 356 Cathey Forks

scala> faker.address.streetAddressNumber
res4: String = 555

scala> faker.address.streetAddressNumber
res5: String = 650

scala> faker.address.streetName
res6: String = Bruen Place

scala> faker.address.
buildingNumber   citySuffix        firstName     longitude          streetAddress         streetSuffix
city             country           fullAddress   secondaryAddress   streetAddressNumber   timeZone
cityName         countryCode       lastName      state              streetName            zipCode
cityPrefix       countyByZipCode   latitude      stateAbbr          streetPrefix          zipCodeByState

scala> faker.address.country
res7: String = Burkina Faso

scala> faker.address.state
res8: String = Louisiana

scala> faker.address.stateAbbr
res9: String = MD

scala> faker.address.stateAbbr
res10: String = WA

scala> faker.address.stateAbbr
res11: String = NC
```
- ( 2021-01-05 13:42:49 )
- 看起來每執行一個函數，就會產生一個隨機的結果。
- 這個行為似乎不是很便於產生假資料。需要再看一下程式碼，看能否固定下來。
- 思路：也許 `Faker()` 建構子有一些選項。
```scala
scala> new Faker

def <init>(): com.github.javafaker.Faker
def <init>(x$1: java.util.Locale): com.github.javafaker.Faker
def <init>(x$1: java.util.Random): com.github.javafaker.Faker
def <init>(x$1: java.util.Locale,x$2: java.util.Random): com.github.javafaker.Faker
def <init>(x$1: java.util.Locale,x$2: com.github.javafaker.service.RandomService): com.github.javafaker.Faker
def <init>(x$1: com.github.javafaker.service.FakeValuesService,x$2: com.github.javafaker.service.RandomService): com.github.javafaker.Faker
```
- 確實有可以指定 `java.util.Locale` 的做法。
- `java.util.Locale` 的[建構子](https://docs.oracle.com/javase/8/docs/api/java/util/Locale.html#constructor.summary)有以下幾種：
  - `Locale(String language)` - Construct a locale from a language code.
  - `Locale(String language, String country)` - Construct a locale from language and country.
  - `Locale(String language, String country, String variant)` - Construct a locale from language, country and variant.