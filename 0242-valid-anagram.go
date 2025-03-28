package main

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	counter := [26]int{}
	for i := range s {
		counter[s[i]-'a']++
		counter[t[i]-'a']--
	}

	for i := range counter {
		if counter[i] != 0 {
			return false
		}
	}
	return true
}

func main() {
	isAnagram("anagram", "nagaram")
}
