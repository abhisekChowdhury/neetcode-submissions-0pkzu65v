"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        copy_dict = {}

        def dfs(curr):
            if curr in copy_dict:
                return copy_dict[curr]
            
            copy = Node(curr.val)

            copy_dict[curr] = copy

            for neighbor in curr.neighbors:
                copy_neighbor = dfs(neighbor)
                copy.neighbors.append(copy_neighbor)
            
            return copy
        
        return dfs(node)