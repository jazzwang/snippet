package main

import "fmt"

// fibonacci is a function that returns
// a function that returns an int.
func fibonacci() func(int) int {
	fn1 := 0
	fn2 := 0
	sum := 0
	return func(x int) int {
		if x == 0 {
			return 0
		} else if x == 1 {
			fn1 = 1
			return 1
		} else {
			sum = fn1 + fn2
			fmt.Printf("// %d = %d + %d\n", sum, fn1, fn2)
			fn2 = fn1
			fn1 = sum
			return sum
		}
	}
}

func main() {
	f := fibonacci()
	for i := 0; i < 10; i++ {
		fmt.Println(f(i))
	}
}
