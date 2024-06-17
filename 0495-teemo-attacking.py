class Solution:
    def findPoisonedDuration(self, timeSeries: list[int], duration: int) -> int:
        output = 0
        for i in range(len(timeSeries)):
            output += duration
            if i == 0:
                continue
            if timeSeries[i] - timeSeries[i-1] < duration:
                toTake = duration -     (timeSeries[i] - timeSeries[i-1])
                output -= toTake
        return output
    
s = Solution()
print(s.findPoisonedDuration([1,2], 2))
