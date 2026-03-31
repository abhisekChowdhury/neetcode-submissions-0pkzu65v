class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}

        def dfs(src, target, visited):
            #if we have reached a path, circle exists
            if src == target:
                return True
            
            visited.add(src)

            for neighbor in graph.get(src,[]):
                if neighbor not in visited:
                    if dfs(neighbor, target, visited):
                        return True
            
            #no path was found
            return False
        
        for a,b in edges:
            if a in graph and b in graph:
                if dfs(a,b,set()):
                    return [a,b]
            
            #otherwise add edge to graph
            graph.setdefault(a,[]).append(b)
            graph.setdefault(b,[]).append(a)