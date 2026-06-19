class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved_stack = []
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while unresolved_stack and temp > temperatures[unresolved_stack[-1]]:
                to_resolve_idx = unresolved_stack.pop()
                res[to_resolve_idx] = i - to_resolve_idx
            unresolved_stack.append(i)
        
        return res