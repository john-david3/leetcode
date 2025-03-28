package main

import "math"

func isPowerOfFour(n int) bool {
	if n <= 0 {
		return false
	}
	log4 := math.Log(float64(n)) / math.Log(4)
	return log4 == math.Floor(log4)
}
