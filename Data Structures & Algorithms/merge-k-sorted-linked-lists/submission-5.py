# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []

        for head in lists:
            curr = head
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        # print(arr)
        arr.sort()
        # print(arr)

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        
        return dummy.next