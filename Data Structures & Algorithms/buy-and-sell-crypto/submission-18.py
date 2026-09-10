class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,0

        max_price = 0
        for price in prices:
            if prices[left] >= prices[right]:
                left = right
            
            max_price = max(max_price, prices[right]-prices[left])
            right += 1
        
        return max_price
