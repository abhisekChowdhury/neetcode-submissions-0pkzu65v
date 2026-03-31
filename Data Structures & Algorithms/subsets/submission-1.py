class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(index):
            if len(nums) == index:
                res.append(sol.copy())
                return
            
            #don't take
            backtrack(index + 1)
            
            #take
            sol.append(nums[index])
            backtrack(index + 1)
            sol.pop()
        
        backtrack(0)
        return res