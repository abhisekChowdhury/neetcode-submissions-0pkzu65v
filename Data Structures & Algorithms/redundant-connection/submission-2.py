class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            parent_x, parent_y = find(x),find(y)
            if parent_x == parent_y:
                return False #redundant
            parent[parent_x] = parent_y
            return True
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]
        return []