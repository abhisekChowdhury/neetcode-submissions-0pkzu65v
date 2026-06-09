class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_value = 0

        for price in prices:
            min_price = min(min_price, price)
            max_value = max(max_value, price - min_price)
        
        return max_value