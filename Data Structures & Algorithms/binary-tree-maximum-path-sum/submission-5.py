# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val

        def dfs(root):
            if not root:
                return 0
            
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)

            self.best = max(self.best, root.val + left + right)

            return root.val + max(0,left,right)
        
        dfs(root)
        return self.best