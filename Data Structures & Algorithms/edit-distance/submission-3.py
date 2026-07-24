class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def min_ops(i,j):

            if i == len(word1) and j == len(word2):
                return 0
            
            if i == len(word1):
                return len(word2)-j
            
            if j == len(word2):
                return len(word1)-i
            
            if (i,j) in memo:
                return memo[(i,j)]
                
            if word1[i] == word2[j]:
                memo[(i,j)] = min_ops(i+1,j+1)
                return memo[(i,j)]
            
            insert = 1 + min_ops(i,j+1)
            delete = 1 + min_ops(i+1,j)
            replace = 1 + min_ops(i+1,j+1)

            memo[(i,j)] = min(insert,delete,replace)

            return memo[(i,j)]

        return min_ops(0,0)