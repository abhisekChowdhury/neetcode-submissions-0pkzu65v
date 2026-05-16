class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '{':'}',
            '[':']',
            '(':')'
        }

        stack = []

        for c in s:
            if c in bracket_map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif bracket_map[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        
        return len(stack)==0
