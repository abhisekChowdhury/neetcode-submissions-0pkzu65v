class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # grouping problem
        # use sorting first as key

        res = defaultdict(list)
        n = len(strs)

        for w in strs:
            key = tuple(sorted(w))
            res[key].append(w)
        
        return list(res.values())