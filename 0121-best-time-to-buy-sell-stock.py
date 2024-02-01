class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest = None
        highest = None
        max_profit = 0
        for i in range(len(prices)):
            if lowest is None or prices[i] < prices[lowest]:
                lowest = i
            if highest is None or prices[i] > prices[highest] or highest < lowest:
                highest = i
            if prices[highest] - prices[lowest] > max_profit:
                max_profit = prices[highest] - prices[lowest]
        return max_profit
    
s = Solution()
s.maxProfit([7,1,5,3,6,4])