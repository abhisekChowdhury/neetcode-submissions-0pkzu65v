class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        #just store each word into its key
        map = defaultdict(list)

        for word in strs:
            key = tuple(self.count(word))
            map[key].append(word)
        
        return [word for key, word in map.items()]
    
    def count(self,word):
        word_count = [0] * 26

        for char in word:
            word_count[ord(char)-ord('a')]+=1
        
        return word_count