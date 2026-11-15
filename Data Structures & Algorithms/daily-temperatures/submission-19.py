class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        temp_idx = []

        for i in range(len(temperatures)):
            while temp_idx and temperatures[temp_idx[-1]] < temperatures[i]:
                to_resolve_idx = temp_idx.pop()
                result[to_resolve_idx] = i - to_resolve_idx
            temp_idx.append(i)
        
        return result