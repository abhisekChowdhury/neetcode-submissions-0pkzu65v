class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for k in range(i+1,len(temperatures)):
                if temperatures[k]>temperatures[i]:
                    result[i] = k-i
                    break
        
        return result