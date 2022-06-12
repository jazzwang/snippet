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
