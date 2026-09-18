class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            current_min = min(self.min_stack[-1],val)
        else:
            current_min = val
        self.min_stack.append(current_min)
        
    def pop(self) -> None:
        if self.stack and self.min_stack:
            self.stack.pop()
            self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]        
