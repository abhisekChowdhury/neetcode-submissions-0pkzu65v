class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        
        while left < right:
            mid_rate = (left + right) // 2
            hours_needed = 0
            for p in piles:
                hours_needed += math.ceil(p/mid_rate)

            if hours_needed <= h:
                right = mid_rate
            else:
                left = mid_rate + 1
        return right