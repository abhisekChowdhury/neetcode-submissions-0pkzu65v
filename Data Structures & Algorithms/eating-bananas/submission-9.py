class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # lower and upper bound of possible rates
        left, right = 1, max(piles)

        def feasible_hours(rate):
            hours_needed = 0
            for pile in piles:
                hours_needed += math.ceil(pile/rate)
            
            return hours_needed

        while left < right:
            # middle possible rate
            mid = (left + right)//2

            if feasible_hours(mid) <= h:
                right = mid
            else:
                left = mid + 1
        
        # return the lowest possible rate
        return left