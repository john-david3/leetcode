package main

import (
	"strconv"
	"strings"
)

func splitNum(n int) []string {
	s := strconv.Itoa(n)
	sp := strings.Split(s, "")
	return sp
}

func nextNum(sp []string) int {
	total := 0
	for i := 0; i < len(sp); i++ {
		intRes, _ := strconv.Atoi(sp[i])
		total += intRes * intRes
	}
	return total
}

func isHappy(n int) bool {
	seenMap := make(map[int]bool)
	_, ok := seenMap[n]
	for !ok {
		if n == 1 {
			return true
		}

		seenMap[n] = true
		n = nextNum(splitNum(n))

		_, ok = seenMap[n]
		if !ok {
			seenMap[n] = true
		} else {
			return false
		}
	}

	return true
}
