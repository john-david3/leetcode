class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        not_in_list = 0
        duplicate = 0

        num_map = {}
        for num in range(1, len(nums) + 1):
            num_map[num] = 0

        for num in nums:
            num_map[num] += 1

        for item in num_map:
            if num_map[item] == 0:
                not_in_list = item
            elif num_map[item] > 1:
                duplicate = item

        return [duplicate, not_in_list]

if __name__ == "__main__":
    # nums = [1,2,2,4]
    # nums = [1,1]
    nums = [2,2]
    sol = Solution()
    ans = sol.findErrorNums(nums)
    print(ans)