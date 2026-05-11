class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            for other in range(len(nums)):
                if num!=other:
                    if nums[num] + nums[other] == target:
                        return [num, other]
        
        