class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1; right = max(piles)
        while left < right:
            hour = 0
            mid_rate = (left + right)//2
            for pile in piles:
                hour += math.ceil(pile/mid_rate)

            if hour <= h:
                right = mid_rate
            else:
                left = mid_rate + 1
        return right