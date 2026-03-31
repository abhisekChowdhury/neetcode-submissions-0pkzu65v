# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        res = []
        q = deque([root])

        while(q):
            node = q.popleft()
            
            if node is None:
                res.append("null")
                continue
            
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        
        values = data.split(",")

        root = TreeNode(int(values[0]))
        queue = deque([root])
        i=1

        while queue and i < len(values):
            parent = queue.popleft()

            # left child
            if values[i] != "null":
                parent.left = TreeNode(int(values[i]))
                queue.append(parent.left)
            i += 1

            # right child
            if i < len(values) and values[i] != "null":
                parent.right = TreeNode(int(values[i]))
                queue.append(parent.right)
            i += 1

        return root


