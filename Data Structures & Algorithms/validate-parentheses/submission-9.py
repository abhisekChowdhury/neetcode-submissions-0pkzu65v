class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracketMap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        for char in s:
            if char in bracketMap:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elif char == bracketMap[stack[-1]]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0