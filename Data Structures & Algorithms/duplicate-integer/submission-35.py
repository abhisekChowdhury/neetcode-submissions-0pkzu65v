class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
            if count[x] > 1:
                return True
        return False