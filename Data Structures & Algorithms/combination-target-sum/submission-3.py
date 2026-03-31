class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(sol.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                sol.append(nums[i])
                backtrack(i, remaining - nums[i])
                sol.pop()
        
        backtrack(0, target)
        return res