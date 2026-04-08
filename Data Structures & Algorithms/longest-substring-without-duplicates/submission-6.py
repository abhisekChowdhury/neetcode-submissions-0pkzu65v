class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charSet = set()
        result = 0

        for right in range(len(s)):
            #expand
            while s[right] in charSet:
                charSet.remove(s[left]) # remove duplicates
                left+=1
            
            charSet.add(s[right])

            result = max(result, right-left+1)
        
        return result