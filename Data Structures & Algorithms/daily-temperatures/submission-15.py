class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Time - O(n) since every element is visited once
        #Space - O(n) for the result and to_resolve_stack being size n
        to_resolve_stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while to_resolve_stack and temperatures[to_resolve_stack[-1]] < temp:
                to_resolve_idx = to_resolve_stack.pop()
                result[to_resolve_idx] = i-to_resolve_idx
            to_resolve_stack.append(i)
        
        return result