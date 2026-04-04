class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(n):
            if n<0:
                return 0
            if n in memo:
                return memo[n]
            
            memo[n] = max(dfs(n-1),nums[n] + dfs(n-2))
            return memo[n]
        
        return dfs(n-1)
