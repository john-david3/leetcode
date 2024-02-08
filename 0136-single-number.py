class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0        
        for num in nums:
            res = res ^ num
        return res
    
sol = Solution()
print(sol.singleNumber([1,4,2,2,4]))