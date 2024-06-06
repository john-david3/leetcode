class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        pt = []
        for n in range(numRows):
            pt.append([])
            l = 0
            r = 1
            pt[n].append(1)
            if n > 0:
                while r < n:
                    prev = pt[n-1]
                    total = prev[l] + prev[r]
                    pt[n].append(total)
                    l += 1
                    r += 1
                pt[n].append(1)
        return pt