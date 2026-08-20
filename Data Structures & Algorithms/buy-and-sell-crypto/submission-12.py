class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right = 0,0

        max_profit = 0 #1
        while right < len(prices): #right = 3 < 6
            if prices[right] < prices[left]:
                left = right #left = 2
            max_profit = max(max_profit, prices[right] - prices[left]) #max_profit = 1
            right+=1 # 3

        return max_profit
        #[2,1,2,1,0,1,2]
        #max_profit = 1
        #right = 3  #val= 2
        #left = 1   #val= 1
            