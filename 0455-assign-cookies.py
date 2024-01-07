class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        counter = i = j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                counter += 1
                i+=1
                j+=1
            else:
                j+=1
        return counter



    
if __name__ == "__main__":
    s = Solution()
    a = s.findContentChildren(g = [1,2,3], s = [1,1])
    print(a)
