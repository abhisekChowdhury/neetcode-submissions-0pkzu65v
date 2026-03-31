class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(i):
            if len(nums) == i:
                res.append(sol[:]) # copy of sol
                return
            
            # don't append
            backtrack(i + 1)
        
            # append
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)

        return res
