from itertools import accumulate

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums=[0]+list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right+1]-self.nums[left]

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0,2)