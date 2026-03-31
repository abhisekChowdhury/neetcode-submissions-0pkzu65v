class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # if it is a number, append to stack
        # if it is an operator:
            # operator = s (or '+' for example)
            # operand2 = s.pop()
            # operand1 = s.pop()
            # s.append(operand1, operator, operand1)
        # return s.pop()

        stack = []

        for s in tokens:
            if s not in "+-*/":
                stack.append(int(s))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if s == '+':
                    stack.append(int(operand2 + operand1))
                elif s == '-':
                    stack.append(int(operand2 - operand1))
                elif s == '*':
                    stack.append(int(operand2 * operand1))
                else:
                    stack.append(int(operand2 / operand1))
        return stack.pop()