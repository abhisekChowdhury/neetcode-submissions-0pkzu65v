# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        def dfs(p, q):
            if p is None and q is None:
                return True
            
            if p is None or q is None:
                return False
            
            if p.val != q.val:
                return False
            
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)

            return left and right

        if dfs(root, subRoot):
            return True
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right
        