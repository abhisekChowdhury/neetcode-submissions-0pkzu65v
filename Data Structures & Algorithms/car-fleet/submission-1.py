class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        cars = sorted(zip(position, speed))

        for position, speed in reversed(cars):
            t = (target - position)/speed

            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)