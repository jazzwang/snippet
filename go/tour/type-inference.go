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
