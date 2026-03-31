class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # get len of rows and columns for indexing
        rows = len(grid)
        cols = len(grid[0])
        numOfIslands = 0

        def dfs(r,c):
            # check out of bounds and return
            if r >= rows or c >= cols or r < 0 or c < 0:
                return
            if grid[r][c] == "0":
                return
            
            # change island "1" to water "0"
            grid[r][c] = "0"

            # visit neighbors of grid[r][c]
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

        # The main iteration happens outside dfs
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    numOfIslands += 1
            
        return numOfIslands
