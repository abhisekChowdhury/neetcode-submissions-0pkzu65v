class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Input: nums = [1,2,4,6]
        # Output: [48,24,12,8]

        prefix = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            result[i]*=postfix
            postfix *= nums[i]
        
        return result