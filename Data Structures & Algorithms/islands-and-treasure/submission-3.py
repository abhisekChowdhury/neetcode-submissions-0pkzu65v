class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
    # [LAND,-1,0,LAND],
    # [LAND,LAND,LAND,-1],
    # [LAND,-1,LAND,-1],
    # [0,-1,LAND,LAND]

    # grid[0][0], 
    #     Tressure locations are grid[0][2] and grid[3][0]
    #     steps to grid[0][2] is 4, Long route.
    #     steps to grid[3][0] is 3
    #     grid[0][0] = 3
    
    # The plan is that I will do a bredth first search, which will guarantee the shortest path. 
    # The queue will hold all the treasure locations.
    # from the first treasure, I will go through the grid by:
        # checking boundaries
        # making sure it is not -1
    # update the grid value from inf to number of steps from the grid value
    # steps will be calculated at each level
    
        rows, cols = len(grid), len(grid[0])
        treasure_queue = deque()
        INF = 2147483647

        def bfs(row,col):
            steps = 0
            while treasure_queue:
                # at each level
                steps+=1
                for _ in range(len(treasure_queue)):
                    r,c = treasure_queue.popleft()

                    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                        if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                            continue
                        if grid[nr][nc] == -1:
                            continue

                        if grid[nr][nc] == INF:
                            grid[nr][nc] = steps
                            treasure_queue.append((nr,nc))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    treasure_queue.append((row,col))
        bfs(row,col)
    
    