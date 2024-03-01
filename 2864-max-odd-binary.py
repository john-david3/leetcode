class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        res = ""
        count1 = 0
        for c in s:
            if c == "1":
                count1 += 1

        n = len(s) - count1

        if count1 > 1:
            for c in range(count1 - 1):
                res += "1"
            for c in range(n):
                res += "0"
            res += "1"
        elif count1 == 1:
            for c in range(n):
                res += "0"
            res += "1"
        else:
            for c in range(n):
                res += "0"
        return res
    
sol = Solution()
print(sol.maximumOddBinaryNumber("010"))