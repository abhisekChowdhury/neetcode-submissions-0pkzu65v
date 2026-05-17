class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s not in '+-*/':
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
                elif s == '/':
                    stack.append(int(operand2 / operand1))
        return stack.pop()