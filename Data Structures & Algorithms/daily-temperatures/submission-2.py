class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j-i
                    break
        
        return result

# [30,38,30,36,35,40,28]
# i = 30
# j = 30

# i=30
# j=30
# i=38
# j=30

# answer[i] = i-j

# i = 38
# j = 38

