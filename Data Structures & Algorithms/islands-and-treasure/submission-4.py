class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        LAND = 2147483647
            
        #put all the treasure in a queue
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))

        steps = 0
        while queue:
            #at each level
            steps += 1

            for _ in range(len(queue)):
                r,c = queue.popleft()

                for nr, nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    
                    if grid[nr][nc] == LAND:
                        grid[nr][nc] = steps
                        queue.append((nr,nc))
