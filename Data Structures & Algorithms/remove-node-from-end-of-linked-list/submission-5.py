# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        #bring fast until n
        # 1, 2, 3, 4
        # -  -  -  -
        # *  *
        # *.next = -

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = head

        for _ in range(n):
            if fast:
            # 0, 1
            # fast -> 2
                fast = fast.next
        
        while fast:
            slow = slow.next
            # slow -> 1
            # slow -> 2
            fast = fast.next
            # fast -> 3
            # fast -> 4 #stop

            #slow -> 2 and fast -> 4
            
        #slow.next -> 3
        slow.next = slow.next.next
        #slow.next should now be 4 because we are skipping 3

        return dummy.next