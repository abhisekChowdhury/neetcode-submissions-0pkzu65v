# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        dummy = result
        curr1 = l1
        curr2 = l2

        while curr1 or curr2 or carry:
            # print(curr1.val+curr2.val)
            sum = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
            digit = sum%10
            carry = sum//10
            dummy.next = ListNode(digit)

            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
            dummy = dummy.next
        
        # while curr1:
        #     dummy.next = ListNode(curr1.val)
        #     curr1 = curr1.next
        #     dummy = dummy.next
        # while curr2:
        #     dummy.next = ListNode(curr2.val)
        #     curr2 = curr2.next
        #     dummy = dummy.next
        # if carry:
        #     dummy.next = ListNode(carry)
            
        
        return result.next