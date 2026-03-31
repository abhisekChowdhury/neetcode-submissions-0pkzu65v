from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rottenQueue = deque()
        fresh = 0

        #populate rottenQueue and fresh
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rottenQueue.append((r,c))
        
        directions = [
            (-1,0),
            (1,0),
            (0,-1),
            (0,1)
        ]
        
        minutes = 0

        while rottenQueue and fresh > 0:
            # process per minute
            for i in range(len(rottenQueue)):
                r, c = rottenQueue.popleft()

                # spread infection to its' neighbors - not sure how to do
                for dr, dc in directions:
                    new_row = dr + r 
                    new_col = dc + c

                    #check boundaries
                    if (0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1):
                        grid[new_row][new_col] = 2
                        rottenQueue.append((new_row, new_col))
                        fresh -= 1
            
            minutes += 1
        
        return minutes if fresh == 0 else -1