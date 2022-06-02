# MEMO

## 2022-06-02

- https://go.dev/doc/tutorial/getting-started

- 安裝環境
```
~/git/snippet/go/tutorial/getting-started$ brew install go
```
- ( 2022-06-02 22:35:12 )
- 建立 `example/hello` 模組
```
~/git/snippet/go/tutorial/getting-started$ go mod init example/hello
go: creating new go.mod: module example/hello
~/git/snippet/go/tutorial/getting-started$ tree
.
├── MEMO.md
└── go.mod

0 directories, 2 files
```
- ( 2022-06-02 22:36:10 )
- 產生 hello.go
```
~/git/snippet/go/tutorial/getting-started$ cat > hello.go << EOF
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
EOF
```
- ( 2022-06-02 22:39:20 )
- 執行程式
```
~/git/snippet/go/tutorial/getting-started$ go run .
Hello, World!
```
- ( 2022-06-02 22:41:01 )
```
~/git/snippet/go/tutorial/getting-started$ go help
Go is a tool for managing Go source code.

Usage:

	go <command> [arguments]

The commands are:

	bug         start a bug report
	build       compile packages and dependencies
	clean       remove object files and cached files
	doc         show documentation for package or symbol
	env         print Go environment information
	fix         update packages to use new APIs
	fmt         gofmt (reformat) package sources
	generate    generate Go files by processing source
	get         add dependencies to current module and install them
	install     compile and install packages and dependencies
	list        list packages or modules
	mod         module maintenance
	work        workspace maintenance
	run         compile and run Go program
	test        test packages
	tool        run specified go tool
	version     print Go version
	vet         report likely mistakes in packages

Use "go help <command>" for more information about a command.

Additional help topics:

	buildconstraint build constraints
	buildmode       build modes
	c               calling between Go and C
	cache           build and test caching
	environment     environment variables
	filetype        file types
	go.mod          the go.mod file
	gopath          GOPATH environment variable
	gopath-get      legacy GOPATH go get
	goproxy         module proxy protocol
	importpath      import path syntax
	modules         modules, module versions, and more
	module-get      module-aware go get
	module-auth     module authentication using go.sum
	packages        package lists and patterns
	private         configuration for downloading non-public code
	testflag        testing flags
	testfunc        testing functions
	vcs             controlling version control with GOVCS

Use "go help <topic>" for more information about that topic.
```
- ( 2022-06-02 22:41:31 )
- 學習搜尋 external package
  - https://pkg.go.dev/search?q=quote
- ( 2022-06-02 22:49:08 )
- 產生 `hello2.go` 實驗呼叫外部套件的函數
```
~/git/snippet/go/tutorial/getting-started$ cat > hello2.go << EOF
package main

import "fmt"

import "rsc.io/quote"

func main() {
    fmt.Println(quote.Go())
}
EOF
```
- ( 2022-06-02 22:49:59 )
- 下載外部套件
```
~/git/snippet/go/tutorial/getting-started$ go mod tidy
go: finding module for package rsc.io/quote
go: downloading rsc.io/quote v1.5.2
go: found rsc.io/quote in rsc.io/quote v1.5.2
go: downloading rsc.io/sampler v1.3.0
go: downloading golang.org/x/text v0.0.0-20170915032832-14c0d48ead0c
```
- ( 2022-06-02 22:51:30 )
- 執行 `hello2.go`
```
~/git/snippet/go/tutorial/getting-started$ go run hello2.go
Don't communicate by sharing memory, share memory by communicating.
```