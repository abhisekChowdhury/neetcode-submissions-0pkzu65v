class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        #store cells that are reachable from each ocean
        pacific = set()
        atlantic = set()

        #directions
        directions = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)]
        
        #dfs function to explore reachable cells
        def dfs(r,c,visited):
            #mark current cell as visited
            visited.add((r,c))

            #explore all 4 directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                #skip out of bounds
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                #skip visited
                if (nr,nc) in visited:
                    continue
                
                #skip if lower than current (water cannot flow from lower to higher)
                if heights[nr][nc] < heights[r][c]:
                    continue
                
                #continue dfs
                dfs(nr,nc,visited)
            
        #start from pacific

        #top row
        for c in range(cols):
            dfs(0,c,pacific)
        
        #left column
        for r in range(rows):
            dfs(r,0,pacific)
        
        #move to atlantic

        #bottom row
        for c in range(cols):
            dfs(rows-1,c,atlantic)
        
        #right column
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        
        #find cells reachable from both oceans
        result = []

        for r in range(rows):
            for c in range(cols):
                #if cell is in both cells, it can be reached by both oceans
                if (r,c) in pacific and (r,c) in atlantic:
                    result.append([r,c])
        
        return result