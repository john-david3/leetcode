class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = -1
        for num in nums2:
            if nums1[i] == 0:
                nums1[i] = num
                i -= 1
            else:
                nums1.append(num)
        nums1.sort()
            
if __name__ == "__main__":
    sol = Solution()
    sol.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)