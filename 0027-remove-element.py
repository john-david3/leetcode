class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums)
        for i, num in enumerate(nums):
            if num == val:
                nums[i] = -1
                k -= 1
        nums.sort(reverse=True)
        return k

if __name__ == "__main__":
    sol = Solution()
    ans = sol.removeElement(nums = [3,2,2,3], val = 3)
    print(ans)