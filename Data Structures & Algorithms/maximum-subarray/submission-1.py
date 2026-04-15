class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current = nums[0]

        for num in nums[1:]:
            current = max(num, num + current)
            max_sum = max(max_sum, current)
        
        return max_sum