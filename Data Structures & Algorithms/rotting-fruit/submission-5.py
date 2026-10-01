class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_queue = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    rotten_queue.append((row,col))
                if grid[row][col] == 0:
                    continue
                
        minutes = 0
        while rotten_queue and fresh > 0:
            
            for _ in range(len(rotten_queue)):
                (row,col) = rotten_queue.popleft()
                for r,c in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                    if r < 0 or r >= rows or c < 0 or c >= cols:
                        continue
                    # if grid[r][c] == 2:
                    #     rotten_queue.append((r,c))
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        rotten_queue.append((r,c))
                    
                    # if fresh == 0 and rotten_queue:
                    #     return 
            minutes += 1
                    
        if fresh == 0:
            return minutes
        else:
            return -1