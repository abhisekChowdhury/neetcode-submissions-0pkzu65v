# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummy = ListNode(0)
        curr = dummy
        
        while curr1 and curr2:
            if curr1.val > curr2.val:
                x = ListNode(curr2.val)
                curr.next = x
                curr = curr.next
                curr2 = curr2.next
            else:
                x = ListNode(curr1.val)
                curr.next = x
                curr = curr.next
                curr1 = curr1.next
            
        if curr1 is None:
            while curr2:
                x = ListNode(curr2.val)
                curr.next = x
                curr = curr.next
                curr2 = curr2.next
        else:
            while curr1:
                x = ListNode(curr1.val)
                curr.next = x
                curr = curr.next
                curr1 = curr1.next

        return dummy.next
        

