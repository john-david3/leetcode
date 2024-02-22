class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = []
        highest = max(candies)
        for item in candies:
            if item + extraCandies >= highest:
                greatest.append(True)
            else:
                greatest.append(False)
        return greatest