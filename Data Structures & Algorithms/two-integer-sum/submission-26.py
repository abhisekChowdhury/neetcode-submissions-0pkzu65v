class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = defaultdict(int)

        for i, num in enumerate(nums):
            current_remaining = target - num
            if current_remaining in remaining:
                return [remaining[current_remaining],i]
            remaining[num] = i
        return []