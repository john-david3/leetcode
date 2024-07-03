class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        output = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                x = grid[i][j]
                if x == 1:
                    output+=4
                    if i > 0 and grid[i-1][j] == 1:
                        output-=2
                    if j > 0 and grid[i][j-1] == 1:
                        output-=2
        return output