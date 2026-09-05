class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        LAND = 2147483647

        rows, cols = len(grid), len(grid[0])
        
        treasure_queue = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasure_queue.append((row,col))

        steps = 0
        while treasure_queue:
            steps += 1

            for _ in range(len(treasure_queue)):
                row,col = treasure_queue.popleft()

                for nr,nc in [(row-1,col), (row+1,col), (row,col-1), (row,col+1)]:
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if grid[nr][nc] == -1:
                        continue
                    
                    if grid[nr][nc] == LAND:
                        grid[nr][nc] = steps
                        treasure_queue.append((nr,nc))
                
        