class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,0
        best = 0
        for right in range(len(prices)):
            while left < right and prices[right] < prices[left]:
                left += 1
            best = max(best, prices[right]-prices[left])
        
        return best