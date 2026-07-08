class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved_idx = []
        res = [0] * len(temperatures)

        for curr_idx, temp in enumerate(temperatures):
            while unresolved_idx and temperatures[unresolved_idx[-1]] < temp:
                to_resolve_idx = unresolved_idx.pop()
                res[to_resolve_idx] = curr_idx-to_resolve_idx
            
            unresolved_idx.append(curr_idx) 
        
        return res