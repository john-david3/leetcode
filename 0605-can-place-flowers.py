class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and i > 0 and i < len(flowerbed) - 1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
            elif flowerbed[i] == 0 and ((i == 0 and flowerbed[1] == 0) or (i == len(flowerbed) - 1 and flowerbed[i-1] == 0)):
                n-=1
                flowerbed[i] = 1
        return n <= 0
                
if __name__ == "__main__":
    sol = Solution()
    print(sol.canPlaceFlowers([0], 1))