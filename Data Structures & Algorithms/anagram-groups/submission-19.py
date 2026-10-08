class Solution:
    def count(self,word):
        count_string = [0] * 26
        for char in word:
            count_string[ord(char)-ord('a')]+=1
        return count_string

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        group = defaultdict(list)

        for word in strs:
            key = tuple(self.count(word))
            group[key].append(word)
        
        for key, value in group.items():
            result.append(value)
        
        return result