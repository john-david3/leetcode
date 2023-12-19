class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        #Build a hash table
        numMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

if __name__ == "__main__":
    s = Solution()
    ans = s.twoSum([2,7,11,15], 9)
    print(ans)