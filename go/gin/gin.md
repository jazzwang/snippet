# README

- https://gin-gonic.com/docs/

## 2022-06-12

- https://gin-gonic.com/docs/features/

### Quickstart

```bash
~/git/snippet/go/gin$ curl https://raw.githubusercontent.com/gin-gonic/examples/master/basic/main.go > main.go
~/git/snippet/go/gin$ go mod init main
~/git/snippet/go/gin$ go mod tidy
~/git/snippet/go/gin$ go run main.go
[GIN-debug] [WARNING] Creating an Engine instance with the Logger and Recovery middleware already attached.

[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:	export GIN_MODE=release
 - using code:	gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /ping                     --> main.setupRouter.func1 (3 handlers)
[GIN-debug] GET    /user/:name               --> main.setupRouter.func2 (3 handlers)
[GIN-debug] POST   /admin                    --> main.setupRouter.func3 (4 handlers)
[GIN-debug] [WARNING] You trusted all proxies, this is NOT safe. We recommend you to set a value.
Please check https://pkg.go.dev/github.com/gin-gonic/gin#readme-don-t-trust-all-proxies for details.
[GIN-debug] Listening and serving HTTP on :8080
[GIN] 2022/06/12 - 17:26:17 | 404 |         919ns |             ::1 | GET      "/"
[GIN] 2022/06/12 - 17:26:17 | 404 |         848ns |             ::1 | GET      "/favicon.ico"
[GIN] 2022/06/12 - 17:26:20 | 404 |         618ns |             ::1 | GET      "/admin"
[GIN] 2022/06/12 - 17:26:32 | 200 |      21.717µs |             ::1 | GET      "/ping"
```