class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        if len(nums1) < len(nums2):
            smaller = nums1
            larger = nums2
        else:
            smaller = nums2
            larger = nums1

        output = set()
        for num in larger:
            if num in smaller:
                output.add(num)
        return list(output)