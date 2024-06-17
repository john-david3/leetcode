class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        output = curr = 0
        for n in nums:
            if n == 1:
                curr += 1
            else:
                if curr > output:
                    output = curr
                curr = 0
        if curr > output:
            output = curr
        return output