class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicates = set()
        for n in nums:
            if n not in duplicates:
                duplicates.add(n)
            else:
                return True
        return False