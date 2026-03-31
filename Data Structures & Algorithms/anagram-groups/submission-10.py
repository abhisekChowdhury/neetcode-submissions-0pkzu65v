class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for i, word in enumerate(strs):
            key = tuple(sorted(word))
            group[key].append(word)
        
        return list(group.values())