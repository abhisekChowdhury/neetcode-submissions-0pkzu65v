class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = defaultdict(int)

        for i, num in enumerate(nums):
            difference = target - num
            if difference in remaining:
                return [remaining[difference],i]
            else:
                remaining[num] = i
        
        return []