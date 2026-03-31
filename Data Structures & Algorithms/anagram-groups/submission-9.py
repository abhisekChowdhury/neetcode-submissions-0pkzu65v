class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for iterator, word in enumerate(strs):
            key = tuple(sorted(word))
            group[key].append(word)
        
        return list(group.values())