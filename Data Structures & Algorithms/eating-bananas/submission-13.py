class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left <= right:
            hours_needed = 0
            mid = (left + right) // 2
            for p in piles:
                hours_needed += math.ceil(p/mid)
            if hours_needed <= h:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result
