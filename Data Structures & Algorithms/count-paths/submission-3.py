class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # grid = [0] * m
        # grid[0] = [0] * n
        row, col = 0, 0
        memo = {}

        def traverse(row,col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            if (row, col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = traverse(row+1,col) + traverse(row,col+1)

            return memo[(row,col)]
        
        return traverse(row,col)