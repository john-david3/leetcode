class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)
        carry = "0"
        result = ""
        for i in range(max_len - 1, -1, -1):
            r = carry
            r = r + a[i] + b[i]
            if r == "000":
                result += "0"
            elif r == "100" or r == "010" or r == "001":
                result += "1"
                carry = "0"
            elif r == "110" or r == "101" or r == "011":
                result += "0"
                carry = "1"
            else:
                result += "1"
                carry = "1"
        if carry == "1":
            result += carry
        return result[::-1]
    
s = Solution()
print(s.addBinary(a = "11", b = "1"))