class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n

        for current_day in range(n):
            for future_day in range(current_day+1, n):
                if temperatures[future_day]>temperatures[current_day]:
                    result[current_day] = future_day - current_day
                    break

        return result