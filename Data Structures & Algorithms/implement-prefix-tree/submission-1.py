class Node:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class PrefixTree:

    def __init__(self):
        self.start = Node()

    def insert(self, word: str) -> None:
        cur = self.start

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.isEnd = True
        

    def search(self, word: str) -> bool:
        cur = self.start
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        if cur.isEnd:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.start
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)