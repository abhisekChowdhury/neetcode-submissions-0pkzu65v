class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_dict = {'}':'{', ']':'[', ')':'('}

        for c in s:
            if c in bracket_dict:
                if not stack or stack.pop()!=bracket_dict[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0