class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sol = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(sol.copy())
                return
            
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # take
                sol.append(candidates[i])

                # don't take
                backtrack(i + 1, remaining - candidates[i])
                sol.pop()
        
        backtrack(0, target)
        return res