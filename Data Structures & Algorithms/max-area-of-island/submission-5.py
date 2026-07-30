class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def area(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            
            if grid[row][col] != 1:
                return 0
            
            grid[row][col] = 0

            return 1 + area(row+1,col) + area(row-1,col) + area(row,col+1) + area(row,col-1)
            
        
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, area(row,col))
        
        return max_area