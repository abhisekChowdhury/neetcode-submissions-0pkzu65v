class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #speed = d/t
        # t = d/s

        time_stack = []
        res_stack = []

        if len(position) == 0:
            return 0

        cars = sorted(zip(position, speed))

        for position, speed in cars:
            t = (target - position)/speed
            time_stack.append(t)
        
        for t in reversed(time_stack):
            if not res_stack:
                res_stack.append(t)
            else:
                if res_stack[-1] < t:
                    res_stack.append(t)
                    # time_stack.pop()

        return len(res_stack)