package main

func isIsomorphic(s string, t string) bool {
	sMap := make(map[byte]int)
	tMap := make(map[byte]int)

	c := 0
	var checkStr string
	for i := 0; i < len(s); i++ {
		_, ok := sMap[s[i]]
		if !ok {
			sMap[s[i]] = c
			c++
		}
		checkStr += string(sMap[s[i]])
	}

	c = 0
	var checkStr2 string
	for i := 0; i < len(t); i++ {
		_, ok := tMap[t[i]]
		if !ok {
			tMap[t[i]] = c
			c++
		}
		checkStr2 += string(tMap[t[i]])
	}

	return checkStr == checkStr2
}
