class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def dfs(n):
            if n in memory:
                return memory[n]

            if n == 0:
                return 0
            
            if n == 1:
                return 1

            if n == 2:
                return 2
            
            # if n == 3:
            #     return 3
                    
            memory[n] = dfs(n-1) + dfs(n-2)

            return memory[n]

        return dfs(n)