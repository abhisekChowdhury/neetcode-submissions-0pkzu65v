class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        left = 0
        count1 = {}
        count2 = {}
        result = 0

        for right in range(len(s1)):
            count1[s1[right]] = count1.get(s1[right],0) + 1

        for right in range(len(s2)):
            #expand
            count2[s2[right]] = count2.get(s2[right], 0) + 1

            #shrink
            if (right-left+1) > len(s1):
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left+=1

            #compare
            if count1 == count2:
                return True
        return False
