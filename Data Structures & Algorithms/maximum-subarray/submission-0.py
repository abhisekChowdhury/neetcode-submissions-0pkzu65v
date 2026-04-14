class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            current = max(nums[i], current+nums[i])
            max_sum = max(current, max_sum)
        
        return max_sum