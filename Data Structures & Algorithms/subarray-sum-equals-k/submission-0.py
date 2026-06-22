class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        seen[0] = 1
        count = 0
        curr = 0

        for num in nums:
            curr += num
            count += seen[curr-k]
            seen[curr] += 1
        
        return count