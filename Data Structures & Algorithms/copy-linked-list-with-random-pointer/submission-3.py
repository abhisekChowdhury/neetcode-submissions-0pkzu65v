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
        copy_ll = {}
        curr = head

        while curr:
            copy_ll[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            copy = copy_ll[curr]
            if curr.next:
                copy.next = copy_ll[curr.next]
            if curr.random:
                copy.random = copy_ll[curr.random]
            curr = curr.next
        
        if not head:
            return None
        return copy_ll[head]