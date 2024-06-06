class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        middle = (start + end) // 2

        while start <= end:
            if nums[middle] < target:
                start = middle + 1
            elif nums[middle] > target:
                end = middle - 1
            else:
                return middle
            middle = (start + end) // 2
        return -1