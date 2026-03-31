class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build the graph first
        graph = {i: [] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            visited.add(node)

            #explore all neighbors
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
                
        count = 0

        for node in range(n):
            if node not in visited:
                dfs(node)
                count+=1
        
        return count