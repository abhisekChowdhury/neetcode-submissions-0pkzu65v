class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            if remaining in memo:
                return memo[remaining]

            best = float('inf')
            for c in coins:
                best = min(best, 1 + dfs(remaining - c))
            memo[remaining] = best
            return memo[remaining]

        result = dfs(amount)

        return result if result != float('inf') else -1