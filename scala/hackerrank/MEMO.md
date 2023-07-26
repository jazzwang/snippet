# MEMO

## 2022-05-27

- https://www.hackerrank.com/domains/fp
```
~/git/snippet/scala/hackerrank$ sbt console
```
```scala
val n=4
(1 to n).foreach( i => println("Hello World") )
(1 to 0)
val n = 0
(1 to n).foreach( i => println("Hello World") )
```
- ( 2022-05-27 23:07:14 )
- 填滿 List 的語法：`List.fill(次數)(內容)`
```scala
val num = 3
val arr = List(1, 2, 3, 4)
List.fill(3)(1)
arr.flatMap(List.fill(num)(_))
```
- ( 2022-05-27 23:07:57 )
```scala
val delim = 3
val arr: List[Int] = List(10,9,8,2,7,5,1,3,0)
arr.filter(_ < delim)
```

## 2023-04-23

- https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
- ( 2023-04-23 21:02:29 )
```bash
~$ sbt console
scala> val input = "-4 3 -9 0 4 1"
input: String = -4 3 -9 0 4 1

scala> val arr = input.replaceAll("\\s+$", "").split(" ").map(_.trim.toInt)
arr: Array[Int] = Array(-4, 3, -9, 0, 4, 1)

scala> arr.filter( _ > 0 ).size.toDouble / arr.size
res4: Double = 0.5

scala> arr.filter( _ < 0 ).size.toDouble / arr.size
res5: Double = 0.3333333333333333

scala> arr.filter( _ == 0 ).size.toDouble / arr.size
res7: Double = 0.16666666666666666
```
- https://www.oreilly.com/library/view/scala-cookbook/9781449340292/ch02s10.html
```scala
val pos = arr.filter( _ > 0 ).size.toDouble / arr.size
val neg = arr.filter( _ < 0 ).size.toDouble / arr.size
val zero = arr.filter( _ == 0 ).size.toDouble / arr.size
println(f"$pos%1.6f")
println(f"$neg%1.6f")
println(f"$zero%1.6f")
```
- https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
- ( 2023-04-23 21:17:39 )
```bash
scala> val input = "1 2 3 4 5"
input: String = 1 2 3 4 5

scala> val arr = input.replaceAll("\\s+$", "").split(" ").map(_.trim.toInt)
arr: Array[Int] = Array(1, 2, 3, 4, 5)

scala> val sum = arr.sum
sum: Int = 15

scala> arr.map( x => sum - x )
res12: Array[Int] = Array(14, 13, 12, 11, 10)

scala> arr.map( x => sum - x ).max
res13: Int = 14

scala> arr.map( x => sum - x ).min
res14: Int = 10
```
- ( 2023-04-23 21:24:46 )
```scala
val sum = arr.sum
val min = arr.map(x => sum - x).min
val max = arr.map(x => sum - x).max
println(s"$min $max")
```
- Hints: Beware of integer overflow! Use 64-bit Integer.
```
scala> val input = "999999996 999999997 999999998 999999999 1000000000"
input: String = 999999996 999999997 999999998 999999999 1000000000

scala> val arr = input.replaceAll("\\s+$", "").split(" ").map(_.trim.toInt)
arr: Array[Int] = Array(999999996, 999999997, 999999998, 999999999, 1000000000)

scala> miniMaxSum(arr)
-294967306 -294967302
```
- Reference:
  - https://alvinalexander.com/scala/scala-data-types-bits-ranges-int-short-long-float-double/
- ( 2023-04-23 21:40:26 )
```scala
def miniMaxSum(arr: Array[Int]) {
    // Write your code here
    val sum = arr.map(_.toLong).sum
    val min = arr.map(x => sum - x).min
    val max = arr.map(x => sum - x).max
    println(s"$min $max")
}
```
- https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
- ( 2020-12-10 15:05:25 )
- learned how to do `scanf` (C) in Scala
- https://alvinalexander.com/scala/how-to-extract-parts-strings-match-regular-expression-regex-scala/
- ( 2023-04-23 21:50:57 )
```bash
scala> val pattern = "([0-9]+):([0-9]+):([0-9]+)([A-Z]+)".r
pattern: scala.util.matching.Regex = ([0-9]+):([0-9]+):([0-9]+)([A-Z]+)

scala> val pattern(hh,mm,ss,ap)=s
hh: String = 07
mm: String = 05
ss: String = 45
ap: String = PM

scala> if (ap == "PM") {
     |   println(hh.toInt + 12)
     | }
19

scala> val HH = (hh.toInt + 12).toString
HH: String = 19

scala> if (ap == "AM" && hh.toInt == 12) {
     |   val HH = "00"
     | }
```
- ( 2023-04-23 22:04:43 )
```scala
def timeConversion(s: String): String = {
  // Write your code here
  val pattern = "([0-9]+):([0-9]+):([0-9]+)([A-Z]+)".r
  val pattern(hh,mm,ss,ap)=s
  var HH = hh
  if (ap == "AM" && hh.toInt == 12) {
    HH = "00"
  } else if (ap == "PM" && hh.toInt < 12) {
    HH = (hh.toInt + 12).toString
  }
  HH+":"+mm+":"+ss
}
```