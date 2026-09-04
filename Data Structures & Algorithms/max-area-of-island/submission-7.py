class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        rows,cols = len(grid),len(grid[0])

        def find_area(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            
            if grid[row][col] == 0:
                return 0
            
            # if grid[row][col] == 1:
            #     return 1
            
            grid[row][col] = 0

            return 1 + find_area(row-1,col) + find_area(row+1,col) + find_area(row,col-1) + find_area(row,col+1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1:
                    max_area = max(max_area, find_area(row,col))
        
        return max_area