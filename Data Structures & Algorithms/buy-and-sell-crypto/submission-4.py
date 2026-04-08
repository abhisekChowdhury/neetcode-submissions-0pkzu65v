class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 0
        maxProfit = 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                maxProfit = max((prices[sell]-prices[buy]),maxProfit)
            else:
                buy = sell
            sell+=1
        return maxProfit