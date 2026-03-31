class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        visited = [False] * len(nums)

        def backtrack(index):
            if len(nums) == index:
                res.append(sol[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                sol.append(nums[i])
                visited[i] = True

                backtrack(index + 1)

                sol.pop()
                visited[i] = False
        
        backtrack(0)

        return res
