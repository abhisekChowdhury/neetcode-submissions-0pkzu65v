class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        def count_me(word):
            count = [0] * 26
            for c in word:
                count[ord(c)-ord('a')]+=1
            return count
        for word in strs:
            key = tuple(count_me(word))
            map[key].append(word)
        return list(map.values())

