class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        nums.append(float("inf"))
        output = []
        start = end = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                end += 1
            else:
                if start != end:
                    rangeStr = f"{nums[start]}->{nums[end]}"
                    output.append(rangeStr)
                    end = i
                    start = end
                else:
                    output.append(str(nums[start]))
                    start = i
                    end = i
        return output