class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        # self.is_dot = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            # base:
            if index == len(word):
                return node.is_end
            
            c = word[index]

            # c=="."
            if c == ".":
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            
            # c is normal character
            if c not in node.children:
                return False

            return dfs(index + 1, node.children[c])
        
        return dfs(0, self.root)
            

