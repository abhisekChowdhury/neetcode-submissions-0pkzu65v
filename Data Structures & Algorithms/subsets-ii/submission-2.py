class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(start):
            res.append(sol.copy())
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                backtrack(i+1)
                sol.pop()
        
        nums.sort()
        backtrack(0)
        return res