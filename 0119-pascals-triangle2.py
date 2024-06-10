class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prev = [1]
        for n in range(rowIndex):
            newRow = [1]
            if rowIndex > 1:
                l = 0
                r = 1
                while r < len(prev):
                    total = prev[l] + prev[r]
                    newRow.append(total)
                    l+=1
                    r+=1
            newRow.append(1)
            prev = newRow
        return prev
