class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_res = 0
        res = 0
        for i in range(len(nums)+1):
            res ^= i
        
        for i in range(len(nums)):
            nums_res ^= nums[i]
            
        return res^nums_res