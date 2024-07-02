from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        output = []

        count1 = Counter(nums1)
        count2 = Counter(nums2)

        inCommon = set1.intersection(set2)
        for num in inCommon:
            output += [num] * min(count1[num], count2[num])

        return output