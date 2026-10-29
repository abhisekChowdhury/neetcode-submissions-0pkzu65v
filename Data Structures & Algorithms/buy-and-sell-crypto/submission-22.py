class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Setup: the state you carry from one step to the next
        min_price = prices[0]
        best = 0

        # Walk through the input once
        for item in prices:
            # Update the state with the current item
            min_price = min(item, min_price)
            # Record the answer if the current state is better than the best so far
            best = max(best, item-min_price)

        # Return the best answer
        return best