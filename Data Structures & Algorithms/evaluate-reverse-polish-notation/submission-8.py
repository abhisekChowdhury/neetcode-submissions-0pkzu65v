class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                stack.append(token)
            else:
                if len(stack) > 1:
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    if token == '+':
                        stack.append(num2+num1)
                    elif token == '-':
                        stack.append(num2-num1)
                    elif token == '*':
                        stack.append(num2*num1)
                    else:
                        stack.append(num2/num1)
        return int(stack[-1])