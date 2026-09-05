class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1)) #parent = [0,1,2,3,4...len(edges)+1]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            parent_x,parent_y = find(x),find(y) # find parent of x and y
            if parent_x == parent_y: # if their parents are the same, we continue? return nothing?
                return False
            
            parent[parent_x] = parent_y #otherwise we will set the location of parent_x to parent_y (struggling to understand and visualize this)
            return True #why return a,b and not x,y?
        
        for a,b in edges:
            if not union(a,b):
                return [a,b] #if a and b are not the same, return a and b?
        
        return [] #otherwise return nothing?