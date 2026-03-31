class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_count = 26 * [0]
        t_count = 26 * [0]
        
        str_buddies = zip(s,t)

        for s, t in str_buddies:
            s_count[ord(s) - ord('a')] += 1
            t_count[ord(t) - ord('a')] += 1
        
        return s_count == t_count