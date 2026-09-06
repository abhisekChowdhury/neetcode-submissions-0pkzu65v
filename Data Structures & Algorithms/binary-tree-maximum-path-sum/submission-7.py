# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = float('-inf')

        def dfs(root):
            if not root:
                return 0
            
            left_best = max(dfs(root.left),0)
            right_best = max(dfs(root.right),0)

            self.best = max(self.best,root.val+left_best+right_best)

            return root.val + max(left_best,right_best)
        
        dfs(root)
        return self.best