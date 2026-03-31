from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) - 1
        minRate = max(piles)

        while left <= right:
            rate = (left + right) // 2
            currentHours = 0
            for pile in piles:
                currentHours += ceil(pile/rate)
            if currentHours > h:
                left = rate + 1
            else:
                right = rate - 1
                minRate = min(rate, minRate)
        return minRate
              