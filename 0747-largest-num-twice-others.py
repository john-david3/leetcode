class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = max(nums)
        output = -1
        for i in range(len(nums)):
            if largest == nums[i]:
                output = i
            elif largest < nums[i] * 2:
                return -1
        return output