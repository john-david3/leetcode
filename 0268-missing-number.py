class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0

        i = 0
        while i + 1 < len(nums):
            if nums[i+1] - nums[i] == 2:
                return nums[i] + 1
            i += 1
        return len(nums) 