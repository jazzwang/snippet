# Learning Notes

- A Tour of Go
- https://go.dev/tour/list

## 2022-06-01

- https://go.dev/tour/welcome/1

## 2022-06-05

- ( 2022-06-05 20:53:33 )
- https://go.dev/tour/basics/1

### Packages

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

## 延伸閱讀

以下是 Tour 文件中提到的連結：

- https://go.dev/pkg/math/rand/#Seed - To see a different number, seed the number generator; see `rand.Seed`.
- https://blog.golang.org/gos-declaration-syntax - For more about why types look the way they do, see `the article on Go's declaration syntax`.