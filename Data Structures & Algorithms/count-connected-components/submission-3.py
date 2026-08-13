class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # nothing around "the shortest path" so no need to use bfs specifically
        # I can use both bfs or dfs
        # I will choose to go with dfs on this one.

        num_connections = 0
        visited = set()

        adj_dict = defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        def dfs(node):
            visited.add(node)
            for neighbor in adj_dict[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                num_connections+=1
                dfs(node)
        
        return num_connections
        
