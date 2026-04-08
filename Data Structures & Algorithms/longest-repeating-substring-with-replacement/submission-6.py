class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_freq = 0
        count = {}
        res = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right],0)

            max_freq = max(max_freq, count[s[right]])

            while (right-left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res