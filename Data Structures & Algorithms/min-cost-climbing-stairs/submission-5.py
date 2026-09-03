class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index <= 1:
                return 0
            
            memo[index] = min(dfs(index-1) + cost[index-1], dfs(index-2) + cost[index-2])
            return memo[index]

        return dfs(len(cost))