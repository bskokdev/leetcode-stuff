class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestions = []

    def add_suggestion(self, product):
        if len(self.suggestions) < 3:
            self.suggestions.append(product)

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        trie = TrieNode()
        for product in products:
            # add suggestions for each letter in product
            cur = trie
            for char in product:
                cur = cur.children[char]
                cur.add_suggestion(product)

        res, cur = [], trie
        for char in searchWord:
            cur = cur.children[char]
            res.append(cur.suggestions)
        return res
    