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