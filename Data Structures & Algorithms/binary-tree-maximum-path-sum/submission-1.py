# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [root.val]
        def dfs(root):
            if not root:
                return 0
            else:
                left_max = max(dfs(root.left), 0)
                right_max = max(dfs(root.right), 0)

                current_max = root.val + left_max + right_max
                max_sum[0] = max(max_sum[0], current_max)
                
                return root.val + max(left_max, right_max)

        dfs(root)
        return max_sum[0]