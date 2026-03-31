# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next

        delete_index = len(arr)-n
        arr.pop(delete_index)

        dummy = ListNode(0)
        curr = dummy
        size = 0

        
        while size < len(arr):
            curr.next = ListNode(arr[size])
            curr = curr.next
            size += 1

        return dummy.next