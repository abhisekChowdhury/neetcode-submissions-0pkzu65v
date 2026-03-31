class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        print("pushed: ", self.stack[-1])
        

    def pop(self) -> None:
        self.stack.pop()
        # print("popped: ", self.stack[-1])
        

    def top(self) -> int:
        return self.stack[-1]
        print("top: ", self.stack[-1])
        

    def getMin(self) -> int:
        lowest = self.stack[0]
        for val in self.stack:
            lowest = min(lowest, val)
        print("min: ", lowest)
        return lowest
