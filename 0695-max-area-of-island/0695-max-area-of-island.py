class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        
        maxArea = 0
        area = [0]
        def dfs(r, c, area):
            grid[r][c] = 0
            area[0] += 1
            if r - 1 >= 0 and grid[r - 1][c] == 1: dfs(r - 1, c, area)
            if r + 1 < rows and grid[r + 1][c] == 1: dfs(r + 1, c, area)
            if c - 1 >= 0 and grid[r][c - 1] == 1: dfs(r, c - 1, area)
            if c + 1 < cols  and grid[r][c + 1] == 1: dfs(r, c + 1, area)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c, area)
                    maxArea = max(maxArea, area[0])
                    area[0] = 0
        return maxArea 