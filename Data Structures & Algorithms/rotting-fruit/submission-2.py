class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minutes = 0
        fresh_oranges = 0
        rotten_orange_queue = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh_oranges += 1
                if grid[row][col] == 2:
                    rotten_orange_queue.append((row,col))

        while rotten_orange_queue and fresh_oranges > 0:
            minutes += 1

            for _ in range(len(rotten_orange_queue)):
                (row,col) = rotten_orange_queue.popleft()

                for nr,nc in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        rotten_orange_queue.append((nr,nc))
                        fresh_oranges -= 1
        
        return -1 if fresh_oranges > 0 else minutes