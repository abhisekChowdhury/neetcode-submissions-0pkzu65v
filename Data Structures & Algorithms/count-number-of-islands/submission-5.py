class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def search(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            if grid[row][col]!="1":
                return
            
            if grid[row][col]=="1":
                grid[row][col] = "0"
            
            search(row-1,col)
            search(row+1,col)
            search(row,col-1)
            search(row,col+1)

        num_islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    num_islands += 1
                    search(row,col)
        
        return num_islands