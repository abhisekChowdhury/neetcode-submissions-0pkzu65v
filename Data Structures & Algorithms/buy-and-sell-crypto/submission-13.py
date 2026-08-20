class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #variable window, increase window when price increases, otherwise start new window
        left = 0
        best = 0

        for right in range(len(prices)):
            if prices[right] < prices[left]:
                #start new window
                left = right
            #valid, calculate best price
            best = max(best,prices[right] - prices[left])
        
        return best