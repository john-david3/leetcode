class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        stack = []
        
        for c in s:
            stack.append(c)
        
        s = ""
        for n in range(len(stack)):
            s = s + stack.pop() + " "

        return s.strip()