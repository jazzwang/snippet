# MEMO

[TOC]

## 2022-06-04

- ( 2022-06-04 17:39:33 )
- This was an [Interactive Tutorial](https://shell.cloud.google.com/?walkthrough_tutorial_url=https%3A%2F%2Fraw.githubusercontent.com%2Fgolang%2Ftour%2Fmaster%2Ftutorial%2Fweb-service-gin.md&pli=1&show=ide&environment_deployment=ide) which uses [GCP Cloud Shell](https://shell.cloud.google.com/) to walk through the steps listed in https://github.com/golang/tour/blob/master/tutorial/web-service-gin.md
  - 學習點：cloud shell 參數 `walkthrough_tutorial_url=` 後面接網址 https://raw.githubusercontent.com/golang/tour/master/tutorial/web-service-gin.md 就可以做出類似 Step by Step 教學的效果。
  - 學習點：`<walkthrough-editor-spotlight spotlightId="menu-file">File Menu</walkthrough-editor-spotlight>` 這段語法可以讓 cloud shell 用 spotlight 鎂光燈焦點特效，秀出 File Menu 的位置。
  - 問題一：不知道能不能鑲嵌 YouTube 或 語音 檔 (待實驗)
  - 問題二：看不出原始檔怎麼控制換頁
  - 小撇步：在 Markdown 中若使用 `"```bash"` 的話，會出現複製到 Cloud Shell 的第二個按鈕，若沒指定語言，則只會出現「複製」按鈕
- ( 2022-06-04 17:55:17 )
- create new module
```
~/git/snippet/go$ cd tutorial/web-service-gin/
~/git/snippet/go/tutorial/web-service-gin$ go mod init example.com/web-service-gin
```
- ( 2022-06-04 18:08:03 )
- 觀念點：`gin.Context` 用來處理 request, 驗證並序列化 JSON 物件
```
gin.Context is the most important part of Gin.
It carries request details, validates and serializes JSON, and more.
```
- 觀念點：可以用 [`Context.JSON`](https://pkg.go.dev/github.com/gin-gonic/gin#Context.JSON) 取代 [`Context.IndentedJSON`](https://pkg.go.dev/github.com/gin-gonic/gin#Context.IndentedJSON)，來傳送更精簡的 JSON 物件
- 觀念點：用 [`gin.Default`](https://pkg.go.dev/github.com/gin-gonic/gin#Default) 來初始化 Gin router
- 觀念點：用 [`gin.RouterGroup.GET](https://pkg.go.dev/github.com/gin-gonic/gin#RouterGroup.GET) 來指定 endpoint `/albums` 對應的函數 `getAlbums()`
- 觀念點：用 [`gin.Engine.RUn`](https://pkg.go.dev/github.com/gin-gonic/gin#Engine.Run) 來綁定 router 到 http.Server，並啟動 server

### Write a handler to add a new item

- ( 2022-06-04 18:27:50 )
```go
package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// album represents data about a record album.
type album struct {
	ID     string  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

// albums slice to seed record album data.
var albums = []album{
	{ID: "1", Title: "Blue Train", Artist: "John Coltrane", Price: 56.99},
	{ID: "2", Title: "Jeru", Artist: "Gerry Mulligan", Price: 17.99},
	{ID: "3", Title: "Sarah Vaughan and Clifford Brown", Artist: "Sarah Vaughan", Price: 39.99},
}

func main() {
	router := gin.Default()

	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.POST("/albums", postAlbums)

	router.Run("localhost:8080")
}

// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, albums)
}

// postAlbums adds an album from JSON received in the request body.
func postAlbums(c *gin.Context) {
	var newAlbum album

	// Call BindJSON to bind the received JSON to
	// newAlbum.
	if err := c.BindJSON(&newAlbum); err != nil {
		return
	}

	// Add the new album to the slice.
	albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusCreated, newAlbum)
}

// getAlbumByID locates the album whose ID value matches the id
// parameter sent by the client, then returns that album as a response.
func getAlbumByID(c *gin.Context) {
	id := c.Param("id")

	// Loop over the list of albums, looking for
	// an album whose ID value matches the parameter.
	for _, a := range albums {
		if a.ID == id {
			c.IndentedJSON(http.StatusOK, a)
			return
		}
	}
	c.IndentedJSON(http.StatusNotFound, gin.H{"message": "album not found"})
}
```

## 延伸閱讀

以下是 Tutorial 文件中提到的連結：

- https://pkg.go.dev/github.com/gin-gonic/gin#Context - Write a getAlbums function that takes a `gin.Context` parameter.
- https://golang.org/pkg/context/ - Despite the similar name, this is different from Go's built-in `context` package.
- https://pkg.go.dev/github.com/gin-gonic/gin#Context.IndentedJSON - Call `Context.IndentedJSON` to serialize the struct into JSON and add it to the response.
- https://pkg.go.dev/net/http#StatusOK - Here, you're passing the StatusOK constant from the `net/http` package to indicate `200` OK.
- https://pkg.go.dev/github.com/gin-gonic/gin#Context.JSON - Note that you can replace `Context.IndentedJSON` with a call to `Context.JSON` to send more compact JSON. I
- https://pkg.go.dev/github.com/gin-gonic/gin#Default - Initialize a Gin router using `Default`.
- https://pkg.go.dev/github.com/gin-gonic/gin#RouterGroup.GET - Use the `GET` function to associate the GET HTTP method and /albums path with a handler function.
- https://pkg.go.dev/github.com/gin-gonic/gin#Engine.Run - Use the `Run` function to attach the router to an http.Server and start the server.
- https://pkg.go.dev/github.com/gin-gonic/gin#Context.BindJSON - Use `Context.BindJSON` to bind the request body to newAlbum.
- https://pkg.go.dev/github.com/gin-gonic/gin#Context.Param - Use `Context.Param` to retrieve the id path parameter from the URL.
- https://pkg.go.dev/net/http#StatusNotFound - Return an HTTP `404` error with `http.StatusNotFound` if the album isn't found.
- https://golang.org/doc/effective_go - If you're new to Go, you'll find useful best practices described in `Effective Go`
- https://golang.org/doc/code - `How to write Go code`
- https://tour.golang.org/welcome/1 - The Go Tour is a great step-by-step introduction to Go fundamentals.
- https://pkg.go.dev/github.com/gin-gonic/gin - For more about Gin, see the Gin Web Framework package documentation.
- https://gin-gonic.com/docs/ - Gin Web Framework docs