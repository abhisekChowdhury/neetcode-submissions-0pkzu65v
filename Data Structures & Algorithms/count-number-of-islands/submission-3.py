class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #indexing
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c):
            #out of bounds cases
            # if (0 <= r < rows) or (0 <= c < cols):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return
            
            #change land to water
            grid[r][c] = "0"

            #visit neighbors
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        numOfIslands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    numOfIslands += 1
        
        return numOfIslands