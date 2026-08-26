# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev

        #head
        #[0,1,2,3]
        #curr = 0, curr.next = None
        #temp = 1
        #prev = 0
        #curr = 1

        #curr = 1, curr.next = 0
        #temp = 2
        #prev = 1
        #curr = 2