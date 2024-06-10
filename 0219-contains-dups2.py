class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        num_map = {}
        for i in range(len(nums)):
            if nums[i] in num_map:
                j = num_map[nums[i]]
                if abs(i - j) <= k:
                    return True
                num_map[nums[i]] = i
            else:
                num_map[nums[i]] = i
        return False