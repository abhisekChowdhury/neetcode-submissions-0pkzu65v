class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        #just store each word into its key
        map = defaultdict(list)

        for word in strs:
            key = tuple(sorted(word))
            map[key].append(word)
        
        return [word for key, word in map.items()]