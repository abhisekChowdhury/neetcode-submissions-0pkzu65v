class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c in enumerate(s)}

        res = []
        size = 0
        end = 0

        for i in range(len(s)):
            end = max(end, last[s[i]])
            size += 1

            if i == end:
                res.append(size)
                size = 0
        
        return res