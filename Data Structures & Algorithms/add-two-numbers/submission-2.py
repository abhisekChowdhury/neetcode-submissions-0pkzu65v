# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        curr = dummy

        # print((l1.val + l2.val)//10)
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            print("total", total)
            sum = total % 10
            print("sum", sum)
            carry = total // 10
            print("carry", carry)
            curr.next = ListNode(sum)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            curr = curr.next

        if carry: curr.next = ListNode(carry)

        return dummy.next
        