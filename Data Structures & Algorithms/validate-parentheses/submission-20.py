class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for char in s:
            if char in map: #this means },],)
                if stack and stack[-1] == map[char]:
                    stack.pop()
                else:
                    return False
            else: #this means (,[,{
                stack.append(char)
        return len(stack) == 0

