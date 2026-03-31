class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.is_end = False

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
        def dfs(node, index):
            if len(word) == index:
                return node.is_end
            
            c = word[index]

            if c == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False
            
            if c not in node.children:
                return False
            
            return dfs(node.children[c], index + 1)
        
        return dfs(self.root, 0)