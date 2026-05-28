class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for k in range(len(nums)):
                if i != k:
                    if nums[i] + nums[k] == target:
                        return [i,k]
        return []