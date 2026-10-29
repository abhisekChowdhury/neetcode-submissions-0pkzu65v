class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                to_resolve_idx = stack.pop()
                result[to_resolve_idx] = i - to_resolve_idx
            stack.append(i)
        return result
