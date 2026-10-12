# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #1. Keep a variable best for the answer and set it to the root value.
        #2. Do a DFS that visits both children first and handles the current node
        #3. At each node, get left and right values. For negatives, use 0.
        #4. Update best with the path that bends at this node: node value + left gain + right gain
        #5. Return node value + the larger gain to the parent. 
        #6. Run the DFS from the root and return best.

        # Edge case: no value provided, return 0
        if not root:
            return 0

        #1. Keep a variable best for the answer and set it to the root value.
        best = [root.val]

        #2. Do a DFS that visits both children first and handles the current node
        def dfs(node):
            if not node:
                return 0
            
            #3. At each node, get left and right values. For negatives, use 0.
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
        
            #4. Update best with the path that bends at this node: node value + left gain + right gain
            through = node.val + left + right #both sides used, cannot go up
            best[0] = max(best[0],through) #keep the larger answer
    
            #5. Return node value + the larger gain to the parent. 
            return node.val + max(left,right)

        #6. Run the DFS from the root and return best.
        dfs(root)
        return best[0]