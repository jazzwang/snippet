package main

import (
	"fmt"
	"log"
	"net/http"
)

func handlePost(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Post\n")
}

func main() {
	h1 := http.HandleFunc("/", handlePost).Methods("POST")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}

// Reference: https://earthly.dev/blog/golang-http/
