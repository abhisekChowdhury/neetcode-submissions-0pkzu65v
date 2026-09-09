class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts1 = [0] * 26

        for char in s1:
            counts1[ord(char) - ord('a')]+=1
        
        left = 0
        right = len(s1)-1

        while right < len(s2):
            counts2 = [0] * 26
            for i in range(left,right+1):
                counts2[ord(s2[i])-ord('a')]+=1
            if counts1 == counts2:
                return True
            
            right += 1
            left += 1
        return False
