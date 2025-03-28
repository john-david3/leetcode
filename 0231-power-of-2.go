package main

import (
	"math"
)

func isPowerOfTwo(n int) bool {
	return math.Log2(float64(n)) == float64(int(math.Log2(float64(n))))
}
