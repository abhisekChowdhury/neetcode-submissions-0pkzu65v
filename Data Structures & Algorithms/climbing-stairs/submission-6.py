class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def dfs(n):
            if n in memory:
                return memory[n]

            if n <= 2:
                return n
                    
            memory[n] = dfs(n-1) + dfs(n-2)

            return memory[n]

        return dfs(n)