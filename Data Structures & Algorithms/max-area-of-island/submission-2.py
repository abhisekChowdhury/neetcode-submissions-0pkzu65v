class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row<0 or row>=rows or col<0 or col>=cols:
                return 0
            
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = 0

            area = 1
            area += dfs(row-1,col)
            area += dfs(row+1,col)
            area += dfs(row,col-1)
            area += dfs(row,col+1)

            return area
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                area = 0
                if grid[row][col] == 1:
                    area = dfs(row,col)
                    max_area = max(max_area, area)
        
        return max_area