class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(p for p in piles)
        # rate = 0
        while left < right:
            hours_needed = 0
            mid = (left + right) // 2
            # [0,1,2,3,4]
            #mid = 4/2 = 2
            for p in piles:
                hours_needed += math.ceil(p/mid)
            if hours_needed <= h:
                right = mid
            else:
                left = mid + 1
        return left
