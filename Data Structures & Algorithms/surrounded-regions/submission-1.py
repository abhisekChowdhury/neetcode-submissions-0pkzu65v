class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            if board[row][col] != "O":
                return
            
            board[row][col] = "S"
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row,col-1)

        
        for r in range(rows):
            dfs(r,0)
            dfs(r,cols-1)
        for c in range(cols):
            dfs(0,c)
            dfs(rows-1,c)
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "S":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"