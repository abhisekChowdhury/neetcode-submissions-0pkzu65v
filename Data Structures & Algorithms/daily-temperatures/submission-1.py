class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            # currentTemperature = temperatures[i]

            while stack and temperatures[stack[-1]]<temperatures[i]:
                tempIndex = stack.pop()
                answer[tempIndex] = i - tempIndex
            stack.append(i)
        
        return answer