package main

import (
	"fmt"
	"math/rand"
	"net/http"

	"github.com/labstack/echo"
)

func main() {
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.POST("/pet", pet)
	e.Logger.Fatal(e.Start(":1323"))
}
func pet(c echo.Context) error {
	body := Body{}
	if err := c.Bind(&body); err != nil {
		fmt.Println(err)
	}
	if err := c.Validate(&body); err != nil {
		return c.JSON(http.StatusOK, body)
	}
	if body.Id == 0 {
		min := 1000000000
		max := 9999999999
		body.Id = rand.Intn(max-min) + min

	}
	return c.JSON(http.StatusOK, body)
}

type Body struct {
	Id     int    `json:"id" validate:"required"`
	Name   string `json:"name"`
	Status string `json:"status"`
}
