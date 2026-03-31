class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # grouping problem
        # use sorting first as key

        res = defaultdict(list)
        n = len(strs)

        for w in strs:
            key = tuple(self.count(w))
            res[key].append(w)
        
        return list(res.values())

    def count(self, word):
        count = 26 * [0]
        for c in word:
            count[ord(c) - ord('a')]+=1
        return count