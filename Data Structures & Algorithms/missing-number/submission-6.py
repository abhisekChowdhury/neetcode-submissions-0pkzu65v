class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        full_res = 0

        for i in range(len(nums)+1):
            full_res ^= i
        
        for i in range(len(nums)):
            res ^= nums[i]
        
        return res^full_res