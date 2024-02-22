class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        stack = []
        s1 = ""
        for c in s:
            if c in vowels:
                stack.append(c)
        
        for c in s:
            if c in vowels:
                c = stack.pop()
            s1 += c

        return s1