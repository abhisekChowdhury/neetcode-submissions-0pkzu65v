class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        #note all the rotten coordinates and put in queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh += 1
                
        #from each rotten position, grow out and rot any other location that is 2. Ignore 0s
        minutes = 0

        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                row,col = queue.popleft()

                for nr,nc in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == 0:
                        continue

                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr,nc))
        
        return minutes if fresh == 0 else -1