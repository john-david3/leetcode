class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        startPos = 0
        endPos = len(nums)
        midPos = (startPos + endPos) // 2

        while startPos < endPos:
            #number is found
            if nums[midPos] == target:
                return midPos
            #number is higher than mid pos
            elif target > nums[midPos]:
                startPos = midPos + 1
            #number is lower than mid pos
            else:
                endPos = midPos
            midPos = (startPos + endPos) // 2
            
        return midPos



if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1,3,5,6], 0))
    print(s.searchInsert([1,3,5,6], 2))
    print(s.searchInsert([1,3,5,6], 7))
    print(s.searchInsert([1,3,5,6], 1))