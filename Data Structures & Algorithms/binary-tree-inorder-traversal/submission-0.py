# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder is dfs
        # left - root - right
        
        self.answer = []
        self.dfs(root)
        return self.answer

    def dfs(self, node):
        if node is None:
            return
        self.dfs(node.left)
        self.answer.append(node.val)
        self.dfs(node.right)
