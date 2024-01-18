class Solution:
    def climbStairs(self, n: int) -> int:
        curr = 1
        prev = 0
        passes = 1
        while passes < n:
            prev = curr - prev
            curr = curr + prev
            passes += 1
        return curr