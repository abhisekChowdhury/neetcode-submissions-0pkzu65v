class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i): #start with len(nums)-1 TOP DOWN
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + dfs(i+2), dfs(i+1))
            return memo[i]
    
        return dfs(0)