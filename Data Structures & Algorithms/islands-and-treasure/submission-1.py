class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        gateQueue = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    gateQueue.append((r,c))
        
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]
        
        while gateQueue:
            r,c = gateQueue.popleft()

            for dr, dc in directions:
                new_row = dr + r
                new_col = dc + c

                if (0 <= new_row < rows and 0 <= new_col < cols):
                    if grid[new_row][new_col] == 2147483647:
                        grid[new_row][new_col] = grid[r][c] + 1
                        gateQueue.append((new_row,new_col))
