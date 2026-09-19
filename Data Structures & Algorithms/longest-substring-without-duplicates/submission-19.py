class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right = 0,0
        visited = set()
        longest_substring = 0
        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            longest_substring = max(longest_substring, right-left+1)
            right += 1
        return longest_substring
