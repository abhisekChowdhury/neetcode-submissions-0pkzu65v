class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord,1)])

        visited = set([beginWord])

        while queue:
            word, steps = queue.popleft()

            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    
                    new_word = word[:i] + c + word[i+1:]

                    if new_word == endWord:
                        return steps + 1
                    
                    if new_word in wordSet and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, steps + 1))
        
        return 0