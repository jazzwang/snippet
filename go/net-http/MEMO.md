# MEMO

## 2022-06-06

- https://pkg.go.dev/net/http?GOOS=linux#example-FileServer
```go
package main

import (
	"log"
	"net/http"
)

func main() {
	// Simple static webserver:
	log.Fatal(http.ListenAndServe(":8080", http.FileServer(http.Dir("/usr/share/doc"))))
}
```
