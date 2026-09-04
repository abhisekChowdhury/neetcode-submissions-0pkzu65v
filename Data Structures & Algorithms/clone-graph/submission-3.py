"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #given a node

        if not node:
            return None
        
        copy_map = {}

        def clone(node):
            if node in copy_map:
                return copy_map[node]
            
            copy_map[node] = Node(node.val)

            for neighbor in node.neighbors:
                copy_map[node].neighbors.append(clone(neighbor))
            
            return copy_map[node]

        #return a node
        return clone(node)