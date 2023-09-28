class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_word = True

    def search(self, word: str) -> bool:
        node = self.find_node(word)
        return node and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self.find_node(prefix)

    def find_node(self, string) -> Optional[TrieNode]:
        current = self.root
        for char in string:
            if char not in current.children:
                return None
            current = current.children[char]
        return current
      


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)