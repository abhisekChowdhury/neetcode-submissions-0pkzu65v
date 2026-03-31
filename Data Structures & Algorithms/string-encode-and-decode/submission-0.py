class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        # read the length
        while i < len(s):
            j = i

            while s[j]!="#":
                j+=1
            
            length = int(s[i:j])

            # read the word
            i = j + 1
            word = s[i : i + length]

            res.append(word)

            # move forward
            i = i + length

        return res

