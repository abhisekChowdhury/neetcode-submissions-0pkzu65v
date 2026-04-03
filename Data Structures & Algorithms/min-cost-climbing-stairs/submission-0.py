class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)

        def f(i):
            if i in memo:
                return memo[i]
            
            if i <= 1:
                return 0
            
            memo[i] = min(
                f(i-1) + cost[i-1],
                f(i-2) + cost[i-2]
                )
            
            return memo[i]
        
        return f(n)