package main

func hammingWeight(n int) int {
	c := 0
	for n > 0 {
		mod := n % 2
		if mod == 1 {
			c++
		}
		n /= 2
	}
	return c
}

func main() {

}
