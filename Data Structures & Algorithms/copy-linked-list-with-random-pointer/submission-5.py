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
        # make a copy_ll and add the values first. Later, connect the next and random pointers
        if not head:
            return None

        curr = head
        copy_ll = {}
        while curr:
            copy_ll[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        copy = Node(0)
        copy_curr = copy

        while curr:
            copy_node = copy_ll[curr]
            if curr.next:
                copy_node.next = copy_ll[curr.next]
            if curr.random:
                copy_node.random = copy_ll[curr.random]

            curr = curr.next
        
        return copy_ll[head]