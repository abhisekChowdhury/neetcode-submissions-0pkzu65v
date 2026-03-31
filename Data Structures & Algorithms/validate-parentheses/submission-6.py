class Solution:
    def isValid(self, s: str) -> bool:
        bracketmap = {'(':')', '{':'}', '[':']'}
        res = []

        for char in s:
            if char in bracketmap:
                res.append(char)
            else:
                if len(res) == 0:
                    return False
                if bracketmap[res[-1]] == char:
                    res.pop()
                else:
                    return False
        return len(res) == 0
