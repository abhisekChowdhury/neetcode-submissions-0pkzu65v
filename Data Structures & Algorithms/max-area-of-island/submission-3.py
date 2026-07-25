class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] != 1:
                return 0
            
            # if grid[row][col] == 1:
            #     return 1

            # temp = grid[row][col]
            grid[row][col] = 0
            
            area = 1 + dfs(row-1,col) + dfs(row+1,col) + dfs(row,col+1) + dfs(row,col-1)

            return area

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, dfs(row,col))
        
        return max_area