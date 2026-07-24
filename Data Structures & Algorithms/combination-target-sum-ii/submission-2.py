class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        result, path = [],[]

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(path.copy())
                return
            
            if remaining < 0:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i+1, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return result