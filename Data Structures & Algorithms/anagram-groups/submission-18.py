class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def count(word):
            word_count = [0] * 26
            for char in word:
                word_count[ord(char) - ord('a')]+=1
            
            return word_count
        
        result = []
        group = defaultdict(list)

        for i in range(len(strs)):
            key = tuple(count(strs[i])) #should return something like [0010110 etc.]
            group[key].append(strs[i])

        for word in group.values():
            result.append(word)
        
        return result