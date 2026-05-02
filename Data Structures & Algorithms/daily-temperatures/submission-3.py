class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        
        for idx_current in range(len(temperatures)):
            for idx_future in range(idx_current+1,len(temperatures)):
                if temperatures[idx_future] > temperatures[idx_current]:
                    #we want the first hot day
                    answer[idx_current] = idx_future - idx_current
                    break
        
        return answer