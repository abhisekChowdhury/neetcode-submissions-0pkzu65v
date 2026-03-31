"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        copy_list = {}

        curr = head

        while curr:
            copy_list[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        
        while curr:
            copy = copy_list[curr]
            copy.next = copy_list.get(curr.next)
            copy.random = copy_list.get(curr.random)
            curr = curr.next

        return copy_list[head]