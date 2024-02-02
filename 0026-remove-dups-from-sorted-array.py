class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        limit = nums[-1] + 1
        prev = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] == prev:
                prev = nums[i]
                nums[i] = limit
            else:
                prev = nums[i]
            i += 1
        return sorted(nums)
    
s = Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))