class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        temp = 0
        while b!=0:
            temp = (a&b) << 1
            a = (a^b) & mask
            b = temp & mask
        
        return a if a < 0xFFFFFFF else ~(a^mask)