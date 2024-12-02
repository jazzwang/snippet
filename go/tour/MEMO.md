# Learning Notes

- A Tour of Go
- https://go.dev/tour/list

[TOC]

## 2022-06-01

- https://go.dev/tour/welcome/1

## 2022-06-05

- ( 2022-06-05 20:53:33 )
- https://go.dev/tour/basics/1

### Packages, variables, and functions.

- ( 2022-06-05 20:54:50 )
```bash
~/git/snippet/go/tour$ cat > packages.go << EOF
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	fmt.Println("My favorite number is", rand.Intn(10))
}
EOF
```
- ( 2022-06-05 20:58:42 )
- add random seed - `rand.Seed(time.Now().Local().Unix())`
- https://go.dev/pkg/math/rand/#Seed
```go
package main

import (
        "fmt"
        "math/rand"
        "time"
)

func main() {
        rand.Seed(time.Now().Local().Unix())
        fmt.Println("My favorite number is", rand.Intn(10))
}
```
- ( 2022-06-05 21:05:26 )
```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
}
```
- ( 2022-06-05 21:06:57 )
- 觀念點：import package 時，只能 refer 到 `exported names`.
```
When importing a package, you can refer only to its exported names.
Any "unexported" names are not accessible from outside the package.
```
```go
package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(math.Pi)
}
```
- ( 2022-06-05 21:11:31 )
- 觀念：<mark>資料型態 `type` 放在變數名稱 `variable name` 後方</mark>
```
Notice that the type comes after the variable name.
```
```go
package main

import "fmt"

func add(x int, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}
```
- ( 2022-06-05 21:15:29 )
- 觀念：<mark>若函數參數或變數是相同資料型態，可以合併宣告</mark>
```
x int, y int
```
可簡寫成
```
x, y int
```
- ( 2022-06-05 21:16:35 )
```go
package main

import "fmt"

func add(x, y int) int {
	return x + y
}

func main() {
	fmt.Println(add(42, 13))
}
```
- ( 2022-06-05 21:17:51 )
- 觀念：<mark>函數可以回傳多個結果</mark>
```
A function can return any number of results.
```
```go
package main

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	a, b := swap("hello", "world")
	fmt.Println(a, b)
}
```
- ( 2022-06-05 21:18:54 )
- 觀念：有名稱的函數回傳值 - Named return values
- 觀念：沒有帶參數的 `return` 稱為 `naked return`，最好用在短內容的函數，以免影響可讀性 `readability`
```
A return statement without arguments returns the named return values.
This is known as a "naked" return.
Naked return statements should be used only in short functions,
as with the example shown here. They can harm readability in longer functions.
```
```go
package main

import "fmt"

func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}

func main() {
	fmt.Println(split(17))
}
```
- ( 2022-06-05 21:25:55 )
- 觀念：`var` 用來宣告一系列的變數
```
The `var` statement declares a list of variables
```
```go
package main

import "fmt"

var c, python, java bool

func main() {
	var i int
	fmt.Println(i, c, python, java)
}
```
- 從結果來看，`int` 型態的初始值為 `0`，`bool` 型態的初始值為 `false`
```
~/git/snippet/go/tour$ go run variables.go
0 false false false
```
- ( 2022-06-05 21:28:37 )
- 觀念：若變數有初始化 `initializer` ，可以忽略資料型態的宣告
```go
package main

import "fmt"

var i, j int = 1, 2

func main() {
	var c, python, java = true, false, "no!"
	fmt.Println(i, j, c, python, java)
}
```
- ( 2022-06-05 21:32:31 )
- Short variable declarations
- 觀念：在**函數中**，可以用 `:=` 宣告變數。
- 觀念：在**函數外**，不能用 `:=` 宣告
```go
package main

import "fmt"

func main() {
	var i, j int = 1, 2
	k := 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
```
- ( 2022-06-05 21:38:28 )
- Go 的基本資料型態 Basic types
```
bool

string

int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr

byte // alias for uint8

rune // alias for int32
     // represents a Unicode code point

float32 float64

complex64 complex128
```
- 其中，`int`, `uint`, `uintptr` 在 32 位元作業系統為 32 位元，64 位元作業系統為 64 位元。
- 備忘：fmt.Printf `%T` 可以印出型態
```go
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
	fmt.Printf("Type: %T Value: %v\n", z, z)
}
```
```
~/git/snippet/go/tour$ go run basic-types.go
Type: bool Value: false
Type: uint64 Value: 18446744073709551615
Type: complex128 Value: (2+3i)
```
- ( 2022-06-05 21:42:22 )
- 觀念：沒有給定初始值的變數，會給予 `zero value`
```
0 for numeric types,
false for the boolean type, and
"" (the empty string) for strings.
```
```go
package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)
}
```
- ( 2022-06-05 21:43:42 )
- 轉型 Type conversions
```
The expression T(v) converts the value v to the type T.
```
```go
package main

import (
	"fmt"
	"math"
)

func main() {
	var x, y int = 3, 4
	var f float64 = math.Sqrt(float64(x*x + y*y))
	var z uint = uint(f)
	fmt.Println(x, y, z)
}
```
- ( 2022-06-05 21:48:35 )
- Type inference 型態推理 - 由右手邊的值來推斷變數的型態
```
the variable's type is inferred from the value on the right hand side.
```
```go
package main

import "fmt"

func main() {
	v := 42 // int
	fmt.Printf("v is of type %T\n", v)
	f := 3.142 // float64
	fmt.Printf("f is of type %T\n", f)
	g := 0.867 + 0.5i // complex128
	fmt.Printf("g is of type %T\n", g)
}
```
- ( 2022-06-05 21:52:32 )
- 常數 Constant - 用關鍵字 `const` 宣告
- 常數不可以用 `:=` 宣告內容
```
Constants can be character, string, boolean, or numeric values.
Constants cannot be declared using the := syntax.
```
```go
package main

import "fmt"

const Pi = 3.14

func main() {
	const World = "世界"
	fmt.Println("Hello", World)
	fmt.Println("Happy", Pi, "Day")

	const Truth = true
	fmt.Println("Go rules?", Truth)
}
```
- ( 2022-06-05 21:57:59 )
- 數值常數是高精度的，若沒指定資料型態，由右手邊的內容決定
```
Numeric constants are high-precision values.
An untyped constant takes the type needed by its context.
```
```go
package main

import "fmt"

const (
	// Create a huge number by shifting a 1 bit left 100 places.
	// In other words, the binary number that is 1 followed by 100 zeroes.
	Big = 1 << 100
	// Shift it right again 99 places, so we end up with 1<<1, or 2.
	Small = Big >> 99
)

func needInt(x int) int { return x*10 + 1 }
func needFloat(x float64) float64 {
	return x * 0.1
}

func main() {
	fmt.Println(needInt(Small))
	fmt.Println(needFloat(Small))
	fmt.Println(needFloat(Big))
}
```

### Flow control statements: for, if, else, switch and defer

- ( 2022-06-05 22:05:06 )
- for 迴圈
- 注意：for 沒有用 parentheses 括號把條件包起來，而且 braces 大括號 是**必要的**！
```
Note: Unlike other languages like C, Java, or JavaScript
there are no parentheses surrounding the three components of the for statement
and the braces { } are always required.
```
```go
package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 10; i++ {
		sum += i
	}
	fmt.Println(sum)
}
```
- ( 2022-06-05 22:08:50 )
- for 迴圈的初始條件與結束條件可以忽略
```go
package main

import "fmt"

func main() {
	sum := 1
	for ; sum < 1000; {
		sum += sum
	}
	fmt.Println(sum)
}
```
- ( 2022-06-05 22:13:11 )
- 拿掉上個範例的分號，Go 的 `for` 等同 C 語法的 `while`
```go
package main

import "fmt"

func main() {
	sum := 1
	for sum < 1000 {
		sum += sum
	}
	fmt.Println(sum)
}
```
- ( 2022-06-05 22:14:58 )
- 無窮迴圈
```go
package main

func main() {
	for {
	}
}
```
- ( 2022-06-05 22:16:19 )
- `if` 宣告跟 `for` 一樣，沒有用 parentheses 括號把條件包起來，而且 braces 大括號 是**必要的**！
```go
package main

import (
	"fmt"
	"math"
)

func sqrt(x float64) string {
	if x < 0 {
		return sqrt(-x) + "i"
	}
	return fmt.Sprint(math.Sqrt(x))
}

func main() {
	fmt.Println(sqrt(2), sqrt(-4))
}
```
- ( 2022-06-05 22:17:42 )
- `if` 可以用一個短的宣告 short statement 開始，分號後再接條件 condition
- 備註：短宣告內的變數只存在 `if` 條件
```
Variables declared by the statement are only in scope until the end of the if.
```
```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
```
- ( 2022-06-05 22:22:27 )
- `if` 與 `else` 可以共用短宣告中的變數
```go
package main

import (
	"fmt"
	"math"
)

func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	} else {
		fmt.Printf("%g >= %g\n", v, lim)
	}
	// can't use v here, though
	return lim
}

func main() {
	fmt.Println(
		pow(3, 2, 10),
		pow(3, 3, 20),
	)
}
```
- 備忘：這個範例說明了一些執行的順序：
	- pow(3, 2, 10) 回傳 9
	- pow(3, 3, 20) 先列印 "27 >= 20" 再回傳 20
	- fmt.Println( 9, 20, ) 印出 90 20
- ( 2022-06-05 22:30:04 )
- Exercise: Loops and Functions
- 十分逼近法 =  Newton's method 牛頓法
```go
package main

import (
	"fmt"
	"math"
)

func Sqrt(x float64) float64 {
	z := float64(1)
	for i :=1; i <= 10 ; i++ {
	  z -= (z*z - x) / (2*z)
	}
	return z
}

func main() {
	fmt.Println(Sqrt(2))
	fmt.Println(math.Sqrt(2))
}
```
- ( 2022-06-05 22:40:06 )
- `switch` 表示式 statement
	- 差異：不必用 `break`
	- 差異：不必是常數，也不必是整數
```go
package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Print("Go runs on ")
	switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default:
		// freebsd, openbsd,
		// plan9, windows...
		fmt.Printf("%s.\n", os)
	}
}
```
- ( 2022-06-05 22:46:31 )
- Switch evaluation order
- `switch` 從上而下逐一判斷是否符合條件，直到判斷是成立為止。
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	fmt.Println("When's Saturday?")
	today := time.Now().Weekday()
	switch time.Saturday {
	case today + 0:
		fmt.Println("Today.")
	case today + 1:
		fmt.Println("Tomorrow.")
	case today + 2:
		fmt.Println("In two days.")
	default:
		fmt.Println("Too far away.")
	}
}
```
- ( 2022-06-05 22:49:10 )
- 如果 `switch` 沒給變數，等同 `switch true`
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	t := time.Now()
	switch {
	case t.Hour() < 12:
		fmt.Println("Good morning!")
	case t.Hour() < 17:
		fmt.Println("Good afternoon.")
	default:
		fmt.Println("Good evening.")
	}
}
```
- ( 2022-06-05 22:50:21 )
- Defer 推遲
```
A defer statement defers the execution of a function until the surrounding function returns.
```
```go
package main

import "fmt"

func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```
- ( 2022-06-05 22:52:02 )
- Stacking defers
```go
package main

import "fmt"

func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}
```

### More types: structs, slices, and maps.

- ( 2022-06-05 22:53:02 )
- Pointers - 這段跟 C 比較接近
- Pointer 的 zero value 是 `nil`
	The type `*T` is a pointer to a `T` value. Its zero value is `nil`.
	```
	var p *int
	```
-	The `&` operator generates a pointer to its operand (操作數).
	```
	i := 42
	p = &i
	```
-	The `*` operator denotes the pointer's underlying value.
	```
	fmt.Println(*p) // read i through the pointer p
	*p = 21         // set i through the pointer p
	```
-	This is known as "dereferencing" or "indirecting".

```
Unlike C, Go has no pointer arithmetic.
```
```go
package main

import "fmt"

func main() {
	i, j := 42, 2701

	p := &i         // point to i
	fmt.Println(*p) // read i through the pointer
	*p = 21         // set i through the pointer
	fmt.Println(i)  // see the new value of i

	p = &j         // point to j
	*p = *p / 37   // divide j through the pointer
	fmt.Println(j) // see the new value of j
}
```
- ( 2022-06-05 23:12:24 )
- structs 結構
```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	fmt.Println(Vertex{1, 2})
}
```
- 感想：`golang` 不是物件導向，所以多數結構都用 `struct`
- ( 2022-06-05 23:12:59 )
- 用 dot (.) 存取 struct 的欄位
```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
	fmt.Println(v.X)
}
```
- ( 2022-06-05 23:15:01 )
- Pointers to structs
- 這裡說明了一個「特例」，`(*p).X` 可以簡化成 `p.X`
```go
package main

import "fmt"

type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```
- ( 2022-06-05 23:19:03 )
- Struct Literals
```go
package main

import "fmt"

type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)

func main() {
	fmt.Println(v1, p, v2, v3)
}
```
- ( 2022-06-05 23:21:18 )
- Array 陣列
```go
package main

import "fmt"

func main() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)
}
```
- 注意：陣列不可以變更大小。arrays cannot be resized.
- ( 2022-06-05 23:24:46 )
- Slices
	- An array has a **fixed size**.
	- A slice, on the other hand, is a **dynamically-sized**, flexible view into the elements of an array.
	- In practice, slices are much more common than arrays.
- ( 2022-06-05 23:26:24 )
```go
a[low : high]
```
- This selects a half-open range which **includes the first element**, but **excludes the last one**.
```go
package main

import "fmt"

func main() {
	primes := [6]int{2, 3, 5, 7, 11, 13}

	var s []int = primes[1:4] // includes primes element 1,2,3
	fmt.Println(s)
}
```
- ( 2022-06-05 23:29:20 )
- Slices are like references to arrays
- A slice **does not store any data**, it just describes a section of an underlying array.
```go
package main

import "fmt"

func main() {
	names := [4]string{
		"John",
		"Paul",
		"George",
		"Ringo",
	}
	fmt.Println(names)

	a := names[0:2]
	b := names[1:3]
	fmt.Println(a, b)

	b[0] = "XXX"
	fmt.Println(a, b)
	fmt.Println(names)
}
```
```bash
~/git/snippet/go/tour$ go run slices-pointers.go
[John Paul George Ringo]
[John Paul] [Paul George]
[John XXX] [XXX George]
[John XXX George Ringo]
```
- ( 2022-06-05 23:32:44 )
- Slice literals
	- A slice literal is like an array literal **without the length**.
```go
package main

import "fmt"

func main() {
	q := []int{2, 3, 5, 7, 11, 13}
	fmt.Println(q)

	r := []bool{true, false, true, true, false, true}
	fmt.Println(r)

	s := []struct {
		i int
		b bool
	}{
		{2, true},
		{3, false},
		{5, true},
		{7, true},
		{11, false},
		{13, true},
	}
	fmt.Println(s)
}
```
- ( 2022-06-05 23:34:23 )
- Slice defaults
```go
package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}

	s = s[1:4]
	fmt.Println(s)

	s = s[:2]
	fmt.Println(s)

	s = s[1:]
	fmt.Println(s)
}
```
- ( 2022-06-05 23:39:20 )
- Slice length and capacity
```go
package main

import "fmt"

func main() {
	s := []int{2, 3, 5, 7, 11, 13}
	printSlice(s)

	// Slice the slice to give it zero length.
	s = s[:0]
	printSlice(s)

	// Extend its length.
	s = s[:4]
	printSlice(s)

	// Drop its first two values.
	s = s[2:]
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
```
- ( 2022-06-05 23:44:15 )
- Nil Slices
```go
package main

import "fmt"

func main() {
	var s []int
	fmt.Println(s, len(s), cap(s))
	if s == nil {
		fmt.Println("nil!")
	}
}
```
- ( 2022-06-05 23:48:12 )
- Creating a slice with make
```go
package main

import "fmt"

func main() {
	a := make([]int, 5)
	printSlice("a", a)

	b := make([]int, 0, 5)
	printSlice("b", b)

	c := b[:2]
	printSlice("c", c)

	d := c[2:5]
	printSlice("d", d)
}

func printSlice(s string, x []int) {
	fmt.Printf("%s len=%d cap=%d %v\n",
		s, len(x), cap(x), x)
}
```
- ( 2022-06-06 10:50:10 )
- Slices of slices
	- Slices can contain <mark>any type</mark>, including other slices.
```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	// Create a tic-tac-toe board.
	board := [][]string{
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
		[]string{"_", "_", "_"},
	}

	// The players take turns.
	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}
```
- ( 2022-06-06 10:50:56 )
- Appending to a slice
```go
package main

import "fmt"

func main() {
	var s []int
	printSlice(s)

	// append works on nil slices.
	s = append(s, 0)
	printSlice(s)

	// The slice grows as needed.
	s = append(s, 1)
	printSlice(s)

	// We can add more than one element at a time.
	s = append(s, 2, 3, 4)
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
```
- ( 2022-06-06 10:55:30 )
- Range
	- The `range` form of the `for` loop iterates over a slice or map.
	- When ranging over a slice, two values are returned for each iteration.
	- The first is `the index`, and the second is a copy of `the element` at that index.
- ( 2022-06-06 11:06:05 )
```go
package main

import "fmt"

func main() {
	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(i) // == 2**i
	}
	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}
}
```

## 2022-06-12

- ( 2022-06-12 17:38:54 )
- Exercise: Slices
```go
package main

import "golang.org/x/tour/pic"

func Pic(dx, dy int) [][]uint8 {
	ss := make([][]uint8, dy)
	for y := 0; y < dy; y++ {
		s := make([]uint8, dx)
		for x := 0; x < dx; x++ {
			s[x] = uint8((x + y) / 2)
		}
		ss[y] = s
	}
	return ss
}

func main() {
	pic.Show(Pic)
}

// Example from https://pkg.go.dev/golang.org/x/tour/pic#example-Show
```
- ( 2022-06-12 17:40:19 )
- Maps
	- A map maps keys to values.
	- The zero value of a map is `nil`
	- The `make` function returns a map of the given type, initialized and ready for use.
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
	m = make(map[string]Vertex)
	m["Bell Labs"] = Vertex{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])
}
```
```bash
~/git/snippet/go/tour$ go run maps.go
{40.68433 -74.39967}
```
- ( 2022-06-12 17:42:37 )
- Map literals
	- Map literals are like struct literals, but <mark>the keys are required</mark>.
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

func main() {
	fmt.Println(m)
}
```
```bash
~/git/snippet/go/tour$ go run maps-literals.go
map[Bell Labs:{40.68433 -74.39967} Google:{37.42202 -122.08408}]
```
- ( 2022-06-12 17:45:44 )
- If the top-level type is just a type name, you can omit it from the elements of the literal.
```go
package main

import "fmt"

type Vertex struct {
	Lat, Long float64
}

var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}

func main() {
	fmt.Println(m)
}
```
```bash
~/git/snippet/go/tour$ go run maps-literals-continued.go
map[Bell Labs:{40.68433 -74.39967} Google:{37.42202 -122.08408}]
```
- ( 2022-06-12 17:49:34 )
- Mutating Maps
	- Insert or update an element in map `m`: `m[key] = elem`
	- Retrieve an element: `elem = m[key]`
	- Delete an element: `delete(m, key)`
	- Test that a key is present with a two-value assignment: `elem, ok = m[key]`
		- If `key` is in `m`, `ok` is `true`.
		- If not, `ok` is `false`.
```go
package main

import "fmt"

func main() {
	m := make(map[string]int)

	m["Answer"] = 42
	fmt.Println("The value:", m["Answer"])

	m["Answer"] = 48
	fmt.Println("The value:", m["Answer"])

	delete(m, "Answer")
	fmt.Println("The value:", m["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}
```
```bash
~/git/snippet/go/tour$ go run mutating-maps.go
The value: 42
The value: 48
The value: 0
The value: 0 Present? false
```
- ( 2022-06-12 17:53:26 )
- https://pkg.go.dev/strings#Fields
- ( 2022-06-12 22:03:34 )
- install Golang REPL
```bash
## Install Golang REPL `gore`
~/git/snippet/go/tour$ go install github.com/x-motemen/gore/cmd/gore@latest
## For autocompletion
~/git/snippet/go/tour$ go install github.com/mdempsky/gocode@latest
```
- ( 2022-06-12 22:03:52 )
- test with `gore`
```bash
~/git/snippet/go/tour$ gore -autoimport
gore version 0.5.5  :help for help
gore> :import strings
gore> :doc strings.Fields
gore> s := "I am learning Go!"
"I am learning Go!"
gore> w := strings.Fields(s)
[]string{
  "I",
  "am",
  "learning",
  "Go!",
}
gore> w[0]
"I"
gore> w[1]
"am"
gore> m := make(map[string]int)
map[string]int{}
gore> v, ok := m[w[0]]
0
false
gore> i := 0
0
gore> m[w[i]]
0
gore> i++
gore> m[w[i]] ++
gore> m
map[string]int{
  "am": 1,
}
gore> :print
package main

import (
    "strings"

    "github.com/k0kubun/pp/v3"
)

func __gore_p(xs ...interface{}) {
    for _, x := range xs {
        pp.Println(x)
    }
}
func main() {
    s := "I am learning Go!"
    w := strings.Fields(s)
    m := make(map[string]int)
    v, ok := m[w[0]]
    i := 0
    i++
    m[w[i]]++
    for i := 0; i < len(w); i++ {
        m[w[i]]++
    }
}
```
```go
package main

import (
	"strings"

	"golang.org/x/tour/wc"
)

func WordCount(s string) map[string]int {
	m := make(map[string]int)
	w := strings.Fields(s)
	for i := 0; i < len(w); i++ {
		m[w[i]]++
	}
	return m
}

func main() {
	wc.Test(WordCount)
}
```
- ( 2022-06-12 22:35:26 )
```bash
~/git/snippet/go/tour$ go run exercise-maps.go
PASS
 f("I am learning Go!") =
  map[string]int{"Go!":1, "I":1, "am":1, "learning":1}
PASS
 f("The quick brown fox jumped over the lazy dog.") =
  map[string]int{"The":1, "brown":1, "dog.":1, "fox":1, "jumped":1, "lazy":1, "over":1, "quick":1, "the":1}
PASS
 f("I ate a donut. Then I ate another donut.") =
  map[string]int{"I":2, "Then":1, "a":1, "another":1, "ate":2, "donut.":2}
PASS
 f("A man a plan a canal panama.") =
  map[string]int{"A":1, "a":2, "canal":1, "man":1, "panama.":1, "plan":1}
```
- ( 2022-06-12 22:35:43 )
- Function values
	- 觀念：有點類似 C 的 function pointer
```go
package main

import (
	"fmt"
	"math"
)

func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func main() {
	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}
```
```bash
~/git/snippet/go/tour$ go run function-values.go
13
5
81
```
- ( 2022-06-12 22:38:59 )
- Function closures
	- Go functions may be closures.
	- <mark>A closure is a function value that references variables from outside its body.</mark>
```go
package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
```
```bash
~/git/snippet/go/tour$ go run function-closures.go
0 0
1 -2
3 -6
6 -12
10 -20
15 -30
21 -42
28 -56
36 -72
45 -90
```
- ( 2022-06-12 23:06:31 )
- Exercise: Fibonacci closure
```go
package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func(int) int {
	fn1 := 0
	fn2 := 0
	sum := 0
	return func(x int) int {
		if x == 0 {
			return 0
		} else if x == 1 {
			fn1 = 1
			return 1
		} else {
			sum = fn1 + fn2
			fmt.Printf("// %d = %d + %d\n", sum, fn1, fn2)
			fn2 = fn1
			fn1 = sum
			return sum
		}
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f(i))
	}
}
```
- ( 2022-06-12 23:34:48 )
```bash
~/git/snippet/go/tour$ go run excercise-fibonacci-closure.go
0
1
1
// 2 = 1 + 1
2
// 3 = 2 + 1
3
// 5 = 3 + 2
5
// 8 = 5 + 3
8
// 13 = 8 + 5
13
// 21 = 13 + 8
21
// 34 = 21 + 13
34
```

## 延伸閱讀

以下是 Tour 文件中提到的連結：

- https://pkg.go.dev/cmd/gofmt - `Gofmt` formats Go programs.
- https://go.dev/pkg/math/rand/#Seed - To see a different number, seed the number generator; see `rand.Seed`.
- https://blog.golang.org/gos-declaration-syntax - For more about why types look the way they do, see `the article on Go's declaration syntax`.
- https://go.dev/blog/defer-panic-and-recover - To learn more about `defer` statements read this blog post.
- https://go.dev/pkg/builtin/#append - Go provides a built-in append function to append new elements to a slice
- https://go.dev/blog/go-slices-usage-and-internals - To learn more about slices, read the `Slices: usage and internals` article.