class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                temp_index = stack.pop()
                result[temp_index] = i-temp_index
            stack.append(i)
        
        return result
