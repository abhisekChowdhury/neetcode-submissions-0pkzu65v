class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def calculate_area(row,col):
            #out of bounds, return 0
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            
            #if 0, return 0
            if grid[row][col] == 0:
                return 0
            
            #if 1, return 1 and change coordinate to 0
            # if grid[row][col] == 1:
            #     grid[row][col] = 0
            #     return 1
            
            # change coordinate to 0
            grid[row][col] = 0
            
            return 1 + calculate_area(row-1,col) + calculate_area(row+1,col) + calculate_area(row,col-1) + calculate_area(row,col+1)

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, calculate_area(row,col))
        
        return max_area