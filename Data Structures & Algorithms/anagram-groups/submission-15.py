class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        result = []
        for word in strs:
            key = tuple(sorted(word))
            word_map[key].append(word)

        for word_list in word_map.values():
            result.append(word_list)
        
        return result