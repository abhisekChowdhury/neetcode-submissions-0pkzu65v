class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            memo = {}

            def dfs(i):
                if i < 0:
                    return 0
                
                if i in memo:
                    return memo[i]
                
                memo[i] = max(nums[i]+dfs(i-2), dfs(i-1))
                return memo[i]
            
            return dfs(len(nums)-1)
        
        if len(nums) < 2:
            return nums[0] 
        
        return max(helper(nums[1:]),helper(nums[:-1]))