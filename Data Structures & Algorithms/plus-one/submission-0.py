class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            current = digits[i] + carry
            digits[i] = current%10
            carry = current//10

            if carry == 0:
                return digits
            
        if carry:
            digits.insert(0, carry)
        
        return digits