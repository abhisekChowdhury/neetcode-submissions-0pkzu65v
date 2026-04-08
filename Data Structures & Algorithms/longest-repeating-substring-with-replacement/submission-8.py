class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        result = 0
        max_freq = 0

        for right in range(len(s)):
            #expand
            count[s[right]] = count.get(s[right], 0) + 1

            #update max freq
            max_freq = max(max_freq, count[s[right]])

            #shrink
            while (right-left+1) - max_freq > k:
                count[s[left]]-=1
                left+=1

            #update result
            result = max(result, right-left+1)
        return result