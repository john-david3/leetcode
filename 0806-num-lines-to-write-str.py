class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        numLines = 1
        counter = 0

        for c in s:
            i = ord(c)-97
            width = widths[i]
            if counter + width > 100:
                numLines+=1
                counter=width
            else:
                counter += width

        return [numLines, counter]