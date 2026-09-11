class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left_rate = 1; right_rate = max(piles)

        while left_rate < right_rate:
            mid_rate = (left_rate + right_rate) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/mid_rate)
            
            if hours <= h:
                right_rate = mid_rate
            else:
                left_rate = mid_rate + 1
        
        return right_rate