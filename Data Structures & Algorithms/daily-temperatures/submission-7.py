class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        unresolved_stack = []

        for current_day in range(n):
            while unresolved_stack and temperatures[unresolved_stack[-1]] < temperatures[current_day]:
                temp_index = unresolved_stack.pop()
                result[temp_index] = current_day - temp_index
            unresolved_stack.append(current_day)
        return result