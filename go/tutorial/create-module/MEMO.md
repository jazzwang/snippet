# MEMO

[TOC]

## 2022-06-03

### Create a module

- ( 2022-06-02 23:30:13 )
- create module `example.com/greetings`
```bash
~/git/snippet/go/tutorial/create-module$ mkdir greetings
~/git/snippet/go/tutorial/create-module$ cd greetings/
~/git/snippet/go/tutorial/create-module/greetings$ go mod init example.com/greetings
~/git/snippet/go/tutorial/create-module/greetings$ tree
.
├── MEMO.md
└── go.mod

0 directories, 2 files
```
- ( 2022-06-02 23:32:12 )
- create `greetings.go`
```bash
~/git/snippet/go/tutorial/create-module/greetings$ cat > greetings.go << EOF
package greetings

import "fmt"

// Hello returns a greeting for the named person.
func Hello(name string) string {
    // Return a greeting that embeds the name in a message.
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message
}
EOF
```
- ( 2022-06-02 23:35:59 )
- <mark>觀念點：`:=` 運算子會用右方值的型態來決定變數的型態</mark>
```
In Go, the `:=` operator is a shortcut for declaring and initializing a variable in one line
(Go uses the value on the right to determine the variable's type).
```

### Call your code from another module

- ( 2022-06-02 23:39:22 )
- https://go.dev/doc/tutorial/call-module-code
- ( 2022-06-02 23:41:55 )
- use `go mod init` to create module `example.com/hello` and store in `go.mod`
```bash
~/git/snippet/go/tutorial/create-module/greetings$ cd ..
~/git/snippet/go/tutorial/create-module$ mkdir hello
~/git/snippet/go/tutorial/create-module$ cd hello/
~/git/snippet/go/tutorial/create-module/hello$ go mod init example.com/hello
```
- ( 2022-06-02 23:43:47 )
- create `hello.go`
```bash
~/git/snippet/go/tutorial/create-module/hello$ cat > hello.go << EOF
package main

import (
    "fmt"

    "example.com/greetings"
)

func main() {
    // Get a greeting message and print it.
    message := greetings.Hello("Gladys")
    fmt.Println(message)
}
EOF
```
- ( 2022-06-02 23:45:26 )
```bash
~/git/snippet/go/tutorial/create-module/hello$ tree
.
├── go.mod
└── hello.go

0 directories, 2 files
~/git/snippet/go/tutorial/create-module/hello$ cd ..
~/git/snippet/go/tutorial/create-module$ tree
.
├── MEMO.md
├── greetings
│   ├── go.mod
│   └── greetings.go
└── hello
    ├── go.mod
    └── hello.go

2 directories, 5 files
~/git/snippet/go/tutorial/create-module$ cd hello/
```
- ( 2022-06-02 23:47:58 )
- use `go mod edit` to change from `example.com/greetings` to `../greetings`
```bash
~/git/snippet/go/tutorial/create-module/hello$ go mod edit -replace example.com/greetings=../greetings
~/git/snippet/go/tutorial/create-module/hello$ cat go.mod
module example.com/hello

go 1.18

replace example.com/greetings => ../greetings
```
- ( 2022-06-02 23:52:10 )
- run `go mod tidy` to load dependencies
```bash
~/git/snippet/go/tutorial/create-module/hello$ go mod tidy
go: found example.com/greetings in example.com/greetings v0.0.0-00010101000000-000000000000
~/git/snippet/go/tutorial/create-module/hello$ tree
.
├── go.mod
└── hello.go

0 directories, 2 files
```
- ( 2022-06-02 23:53:44 )
- NOTE: `go mod tidy` did not create `go.sum`. It modifies `go.`mod` instead.
```bash
~/git/snippet/go/tutorial/create-module/hello$ cat go.mod
module example.com/hello

go 1.18

replace example.com/greetings => ../greetings

require example.com/greetings v0.0.0-00010101000000-000000000000
```
- ( 2022-06-02 23:56:58 )
- 觀念點：[`require` directive](https://go.dev/doc/modules/gomod-ref#require)
- 觀念點：對於已發佈(published)的 module，就會根據網路上的版本號碼
```
To reference a published module, a go.mod file would typically omit the replace directive
and use a require directive with a tagged version number at the end.
```
- ( 2022-06-03 00:00:50 )
```
~/git/snippet/go/tutorial/create-module/hello$ go run .
Hi, Gladys. Welcome!
```
### Return and handle an error

- ( 2022-06-03 00:01:15 )
- https://go.dev/doc/tutorial/handle-errors
- ( 2022-06-03 00:05:40 )
- modify the context of `greetings.go` and add error handling
```bash
~/git/snippet/go/tutorial/create-module/hello$ cd ../greetings/
~/git/snippet/go/tutorial/create-module/greetings$ cat > greetings.go << EOF
package greetings

import (
    "errors"
    "fmt"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
    // If no name was given, return an error with a message.
    if name == "" {
        return "", errors.New("empty name")
    }

    // If a name was received, return a value that embeds the name
    // in a greeting message.
    message := fmt.Sprintf("Hi, %v. Welcome!", name)
    return message, nil
}
EOF
```
- ( 2022-06-03 00:09:32 )
- NOTE: since the `greetings.go`, it might change the version in `go.mod`
- 好奇點：這段比較像刻意產生了新版本的 greeting module，看後面是否可以觀察到版本變化
- ( 2022-06-03 00:11:06 )
- modify `hello/hello.go` to add error handling and `log`
```bash
~/git/snippet/go/tutorial/create-module/greetings$ cd ../hello
~/git/snippet/go/tutorial/create-module/hello$ cat > hello.go << EOF
package main

import (
    "fmt"
    "log"

    "example.com/greetings"
)

func main() {
    // Set properties of the predefined Logger, including
    // the log entry prefix and a flag to disable printing
    // the time, source file, and line number.
    log.SetPrefix("greetings: ")
    log.SetFlags(0)

    // Request a greeting message.
    message, err := greetings.Hello("")
    // If an error was returned, print it to the console and
    // exit the program.
    if err != nil {
        log.Fatal(err)
    }

    // If no error was returned, print the returned message
    // to the console.
    fmt.Println(message)
}
EOF
```
- ( 2022-06-03 00:13:57 )
- run `hello.go`
```bash
~/git/snippet/go/tutorial/create-module/hello$ go run .
greetings: empty name
exit status 1
```

### Return a random greeting

- ( 2022-06-03 00:16:45 )
```
A slice is like an array, except that its size changes dynamically as you add and remove items.
The slice is one of Go's most useful types.
```
- ( 2022-06-03 00:18:05 )
- modify `greetings/greetings.go` to add `math/rand` and `time`
```bash
~/git/snippet/go/tutorial/create-module/hello$ cat > ../greetings/greetings.go << EOF
package greetings

import (
    "errors"
    "fmt"
    "math/rand"
    "time"
)

// Hello returns a greeting for the named person.
func Hello(name string) (string, error) {
    // If no name was given, return an error with a message.
    if name == "" {
        return name, errors.New("empty name")
    }
    // Create a message using a random format.
    message := fmt.Sprintf(randomFormat(), name)
    return message, nil
}

// init sets initial values for variables used in the function.
func init() {
    rand.Seed(time.Now().UnixNano())
}

// randomFormat returns one of a set of greeting messages. The returned
// message is selected at random.
func randomFormat() string {
    // A slice of message formats.
    formats := []string{
        "Hi, %v. Welcome!",
        "Great to see you, %v!",
        "Hail, %v! Well met!",
    }

    // Return a randomly selected message format by specifying
    // a random index for the slice of formats.
    return formats[rand.Intn(len(formats))]
}
EOF
```
- ( 2022-06-03 00:21:42 )
- <mark>觀念點：小寫開頭的函數，只能在自己的 package 中使用</mark>
```
Note that randomFormat starts with a lowercase letter,
making it accessible only to code in its own package (in other words, it's not exported).
```
- ( 2022-06-03 00:25:28 )
- <mark>觀念點：括號沒有宣告 slice 大小時，代表 slice 下的 arrary 是可以動態改變的</mark>
```
When declaring a slice, you omit its size in the brackets, like this: []string.
This tells Go that the size of the array underlying the slice can be dynamically changed.
```
- ( 2022-06-03 00:27:04 )
- modify `hello/hello.go`
```
~/git/snippet/go/tutorial/create-module/hello$ cat > hello.go << EOF
package main

import (
    "fmt"
    "log"

    "example.com/greetings"
)

func main() {
    // Set properties of the predefined Logger, including
    // the log entry prefix and a flag to disable printing
    // the time, source file, and line number.
    log.SetPrefix("greetings: ")
    log.SetFlags(0)

    // Request a greeting message.
    message, err := greetings.Hello("Gladys")
    // If an error was returned, print it to the console and
    // exit the program.
    if err != nil {
        log.Fatal(err)
    }

    // If no error was returned, print the returned message
    // to the console.
    fmt.Println(message)
}
EOF
```
- ( 2022-06-03 00:28:22 )
- run `hello.go`
```bash
~/git/snippet/go/tutorial/create-module/hello$ go run .
Great to see you, Gladys!
~/git/snippet/go/tutorial/create-module/hello$ go run .
Hi, Gladys. Welcome!
```

## 延伸閱讀

以下是 Tutorial 文件中提到的連結：

- https://go.dev/doc/modules/developing - 關於 Module 的開發與發佈
```
For more about developing modules, see Developing and publishing modules.
```
- https://go.dev/ref/mod#go-mod-init - 關於 `go mod init` 指令
- https://go.dev/doc/modules/managing-dependencies#naming_module - 關於 module naming
```
For more on naming your module with a module path, see Managing dependencies.
```
- https://go.dev/tour/basics/3 - 關於 `exported names`
```
For more about exported names, see Exported names in the Go tour.
```
- https://pkg.go.dev/fmt/#Sprintf - `fmt` package's `Sprintf` function
- https://go.dev/ref/mod#go-mod-edit - 關於 `go mod edit` 指令
- https://go.dev/doc/modules/gomod-ref#replace - 關於 `replace` directive
```
After you run the command, the go.mod file in the hello directory should include a replace directive:
```
- https://go.dev/ref/mod#go-mod-tidy - 關於 `go mod tidy` 指令
- https://go.dev/doc/modules/gomod-ref#require - 關於 `require` directive
- https://go.dev/doc/modules/version-numbers - 關於 module 版本號碼
```
For more on version numbers, see Module version numbering.
```
- https://go.dev/doc/effective_go.html#multiple-returns - Effective Go - 關於回傳多個值
```
Any Go function can return multiple values. For more, see Effective Go.
```
- https://pkg.go.dev/errors/#example-New - `errors.New` function
- https://pkg.go.dev/log/ - `log` package
- https://pkg.go.dev/log?tab=doc#Fatal - `log` package's `Fatal` function
- https://blog.golang.org/slices-intro - 關於 `Go slice`
```
A slice is like an array, except that its size changes dynamically as you add and remove items.
For more on slices, see Go slices in the Go blog.
```
- https://go.dev/doc/effective_go.html#init - Effective Go - 關於 module 的 init() 函數
```
For more about init functions, see Effective Go.
```