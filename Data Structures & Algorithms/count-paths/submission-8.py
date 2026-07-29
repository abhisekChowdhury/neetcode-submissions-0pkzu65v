class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows,cols = m,n
        memo = {}

        def unique(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            
            if row == m-1 and col == n-1:
                return 1
            
            if (row,col) in memo:
                return memo[(row,col)]
            
            memo[(row,col)] = unique(row+1,col) + unique(row,col+1)
            return memo[(row,col)]

        # num_paths = 1

        num_paths = unique(0,0)
        return num_paths