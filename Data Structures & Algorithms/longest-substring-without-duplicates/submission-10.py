class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]]+=1
            # print(count[s[right]])
            while count[s[right]] > 1:
                count[s[left]]-=1
                left+=1
                if count[s[right]] == 0:
                    del count[s[right]]
            
            max_len = max(max_len, right-left+1)
            

        return max_len