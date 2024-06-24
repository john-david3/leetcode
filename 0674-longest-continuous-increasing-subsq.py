class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:
        longest = 0
        counter = 1

        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                counter += 1
            else:
                counter = 1
            if counter > longest:
                longest = counter
        return longest
