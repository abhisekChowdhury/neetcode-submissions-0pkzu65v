class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 ;best = 0

        for left in range(len(prices)):
            for right in range(left, len(prices)):
            # if prices[right] < prices[left]:
            #     left = right
            
                best = max(best, prices[right]-prices[left])
        
        return best