class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        candidates = defaultdict(int)

        for i, num in enumerate(nums):
            if target - num in candidates:
                return [candidates[target-num],i]
            candidates[num] = i
        return []