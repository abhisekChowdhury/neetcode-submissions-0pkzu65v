class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []

        for char in s:
            if char in bracketMap:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif bracketMap[stack[-1]] == char:
                stack.pop()
            else:
                return False
            
        return len(stack) == 0