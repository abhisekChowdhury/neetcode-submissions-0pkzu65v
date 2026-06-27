class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # get the last occurrence of each character
        last_occur = {}
        for i,char in enumerate(s):
            last_occur[char] = i
        
        res=[]
        farthest = 0
        start = 0

        for i in range(len(s)):
            farthest = max(farthest, last_occur[s[i]])

            if i == farthest:
                res.append(i-start+1)
                start = i+1
            
        return res