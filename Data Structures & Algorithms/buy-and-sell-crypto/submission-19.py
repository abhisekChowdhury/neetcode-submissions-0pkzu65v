class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_price = 0
        while right < len(prices):
            if prices[right] > prices[left]:
                max_price = max(max_price,prices[right]-prices[left])
            else:
                left = right
            right += 1
        return max_price