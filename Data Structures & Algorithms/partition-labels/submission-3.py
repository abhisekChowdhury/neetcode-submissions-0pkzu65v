class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        last_occur = {}

        for i, c in enumerate(s):
            last_occur[c] = i
        
        start = end = 0
        
        for i in range(len(s)):
            end = max(end, last_occur[s[i]])
            start += 1

            if i == end:
                res.append(start)
                start = 0
        
        return res