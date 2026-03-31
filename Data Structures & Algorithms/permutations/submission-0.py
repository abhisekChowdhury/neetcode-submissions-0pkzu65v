class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        visited = [False] * len(nums)

        def backtrack(index):
            if index == len(nums):
                res.append(sol[:])
                return
            
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                # take
                sol.append(nums[i])
                visited[i] = True

                # explore
                backtrack(index + 1)
                
                # don't take
                sol.pop()
                visited[i] = False
        
        backtrack(0)
        return res