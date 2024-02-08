class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char
        new_s = new_s.lower()
        return new_s == new_s[::-1]

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))