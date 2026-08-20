class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #variable window problem. Trying to find the longest substring
        #maintain a left pointer set to 0 and a right pointer incrementing up to len(s)
        #maintain a seen set, which stores all the values and decides whether a window will continue or not
        #if a character is seen in seen, while that character exists in seen, left will keep increasing until that character doesn't exist in seen anymore while these characters are being removed from seen. Both O(1) operations
        #Since I will be storing characters in a seen set, the worst case space will be O(n) and time will be O(n) as well for iterating through all the charaters.

        seen = set()
        best = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best,(right-left+1))
        return best

        # right = 0 val = p seen? No; best = 1 seen = {p}
        # right = 1 val = w seen? No; best = (1-0)+1 = 2 seen = {pw}
        # right = 2 val = w  seen? Yes
            #remove p left=1 ; remove w left = 2; seen = {w}; best = 1
        # right = 3 val = k seen? No; seen = {wk}; best = 2
        # right = 4 val = e seen? No; seen = {wke}; best = 3
        # right = 5 val = w seen? Yes;
            #remove e,k,w; left = 2+1+1+1 = 5; best = 3
        # best should be 3