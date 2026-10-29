class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        best = 0
        visited = set()

        while right < len(s):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            best = max(best,right-left+1)
            right += 1
        
        return best