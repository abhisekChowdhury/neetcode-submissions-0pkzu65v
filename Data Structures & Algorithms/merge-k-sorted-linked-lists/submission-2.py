# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        # count = 0

        for head in lists:
            curr = head
            while curr:
                arr.append(curr.val)
                # count+=1
                curr = curr.next

        arr.sort()

        head = ListNode(0)
        curr = head

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        
        return head.next