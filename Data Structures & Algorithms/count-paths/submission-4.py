class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        rows, cols = m,n

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if row == m-1:
                return 1
                
            if col == n-1:
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = dfs(row+1,col) + dfs(row,col+1)
            return memo[(row,col)]

        paths = dfs(0,0)
        
        return paths