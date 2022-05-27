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