# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Reverse each group in list
# Steps:
    # Use a dummy node before the head
    # group_prev is the node just before the current group
    # Walk k steps from it to find the kth, the last node of the group.
    # If we run out of nodes, stop there. Don't change the rest of the links
    # Save group_next, the node after the group. 
    # Reverse the k nodes with the fist node and point group_next at the start (Connect to the rest of the list)
    # The old first node of the group is now the tail. 
    # Point group_prev at kth(the new first node), then move group_prev to the old first node for the next group


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case:
        if not head or k == 1:
            return head
        
        # 1. add a dummy node before head
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # 2. find the kth node of the current group
            kth = group_prev
            for iterator in range(k):
                kth = kth.next
                if not kth: # fewer than k nodes left
                    return dummy.next
            
            group_next = kth.next

            # 3. reverse the k nodes of the group
            prev = group_next # first node will point to group_next
            current = group_prev.next #first node of this group
            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            
            # 4. connect reversed group
            old_first = group_prev.next
            group_prev.next = kth

            # 5. move to the next group

            group_prev = old_first
                