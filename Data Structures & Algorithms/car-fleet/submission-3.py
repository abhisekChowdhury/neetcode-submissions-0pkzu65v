class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # t=d/s

        # t = (10-1)/3 -> farther car
        # t = 3

        # t = (10-4)/3 -> closer car
        # t = 2
        stack = []
        for (position,speed) in sorted(zip(position,speed),reverse = True):
            time = (target-position)/speed

            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)