class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for w in strs:
            key = tuple(self.count(w))
            groups.setdefault(key, []).append(w)

        return list(groups.values())
    
    def count(self, word):
        seen_count = [0] * 26
        for i, c in enumerate(word):
            seen_count[ord(c) - ord('a')]+=1
        return seen_count