class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = {}
        L = 0
        res = 0

        for R in range(len(s)):
            #expand
            count[s[R]] = count.get(s[R], 0) + 1

            #shrink
            while count[s[R]] > 1:
                count[s[L]] -= 1
                L+=1 

            #update
            res = max(res, R-L+1)
        return res