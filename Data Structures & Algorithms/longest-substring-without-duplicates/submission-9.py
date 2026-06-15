class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        charset = set()

        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left += 1
            else:
                charset.add(s[right])
                max_len = max(max_len, right-left+1)
        
        return max_len