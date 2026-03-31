# COME BACK TO THIS ONE!


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # create dummy node
        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while True:
            #1. Find the k-th from prev_group_end
            # prev_group_end node -> node -> node -> k-th node
            kth = self.getKth(prev_group_end, k)

            if not kth:
                break # fewer than k nodes left

            next_group_start = kth.next

            # 2. Reverse the group
            prev = next_group_start # none
            curr = prev_group_end.next # head

            while curr != next_group_start:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node

            # 3. Put them together
            group_start = prev_group_end.next
            prev_group_end.next = kth
            prev_group_end = group_start

        return dummy.next

    def getKth(self, prev_group_end: Optional[ListNode], k: int) -> ListNode:
        curr = prev_group_end
        while k > 0 and curr:
            curr = curr.next
            k -= 1
        return curr
        