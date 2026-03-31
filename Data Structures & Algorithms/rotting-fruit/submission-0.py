from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        #initialize queue - forgot the syntax
        rottenQueue = deque()
        #initialize fresh list
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                # handle fresh fruit
                if grid[r][c] == 1:
                    fresh+=1
                # handle rotten fruit
                if grid[r][c] == 2:
                    rottenQueue.append((r,c))
            
        #initialize directions - left,right,up,down
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        minutes = 0
        while rottenQueue and fresh > 0:
            #process 1 minute
            current_size = len(rottenQueue)

            for i in range(current_size):
                r,c = rottenQueue.popleft()

                for drow, dcol in directions:
                    new_row = r + drow
                    new_col = c + dcol

                    if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 1:
                        #make it rotten
                        grid[new_row][new_col] = 2
                        rottenQueue.append((new_row, new_col))
                        fresh -= 1

            minutes+=1
        
        return minutes if fresh == 0 else -1

                    
