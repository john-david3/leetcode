class Solution:
    def minOperations(self, nums: list[int]) -> int:
        minimum = -1
        num_map = {}
        for num in nums:
            if num not in num_map:
                num_map[num] = 1
            else:
                num_map[num] += 1

        for item in num_map:
            total = num_map[item]
            count = 0
            while total > 2:
                if total == 4:
                    count += 2
                    total -= 4
                    continue
                total -= 3
                count += 1
            if total == 2:
                count += 1
            elif total == 1:
                return -1
            minimum += count
        return minimum + 1
                
s = Solution()
print(s.minOperations([2,3,3,2,2,4,2,3,4]))