class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        left = 0
        best = 0

        for right in range(len(s)):
            #expand
            count[s[right]]+=1

            max_freq = max(max_freq,count[s[right]])

            while (right-left+1) - max_freq > k:
                count[s[left]] -= 1
                if count[s[left]] == 0:
                    del count[s[left]]
                left += 1

            best = max(best, right-left+1)
        return best