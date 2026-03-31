# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        count = 0
        
        for ll in lists:
            curr = ll
            while curr:
                arr.append(curr.val)
                count += 1
                curr = curr.next

        arr.sort()

        self.head = None

        for num in reversed(arr):
            self.insert_at_beginning(num)

        return self.head

    def insert_at_beginning(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node


        
