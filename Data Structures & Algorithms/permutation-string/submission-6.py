class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)

        if s1_length == 0:
            return True
        
        if s1_length > s2_length:
            return False
        
        s1_counts = [0] * 26
        for letter in s1:
            s1_counts[ord(letter)-ord('a')] += 1
        
        window_counts = [0]*26

        for right_index in range(s2_length):
            new_letter = s2[right_index]
            window_counts[ord(new_letter) - ord('a')] += 1

            if right_index >= s1_length:
                old_letter = s2[right_index - s1_length]
                window_counts[ord(old_letter) - ord('a')] -= 1
            
            if window_counts == s1_counts:
                return True
        return False