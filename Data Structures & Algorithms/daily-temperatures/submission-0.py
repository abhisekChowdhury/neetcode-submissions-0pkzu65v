class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        coldTempIndexStack = []
        answer = [0] * len(temperatures)

        for i in range(len(temperatures)):
            currentTemperature = temperatures[i]

            while coldTempIndexStack and currentTemperature > temperatures[coldTempIndexStack[-1]]:
                coldTempIndexTop = coldTempIndexStack.pop()
                answer[coldTempIndexTop] = i - coldTempIndexTop
            coldTempIndexStack.append(i)
            
        return answer