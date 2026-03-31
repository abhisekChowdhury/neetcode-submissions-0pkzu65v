class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def is_palindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True


        def backtrack(start):
            if start == len(s):
                res.append(sol[:])
                return
            
            for end in range(start, len(s)):
                if is_palindrome(start, end):
                    sol.append(s[start:end + 1])
                    backtrack(end + 1)
                    sol.pop()
                    
        backtrack(0)
        return res