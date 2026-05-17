class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        unresolved_stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while unresolved_stack and temperatures[unresolved_stack[-1]] < temperatures[i]:
                to_resolve = unresolved_stack.pop()
                res[to_resolve] = i-to_resolve
            unresolved_stack.append(i)
        return res