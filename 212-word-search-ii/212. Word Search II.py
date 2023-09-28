class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.insert_word(word)
    
    def insert_word(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M, N = len(board), len(board[0])
        # O(n)
        trie = Trie(words)
        res = []
        def dfs(row, col, node, cur_word):
            temp = board[row][col]
            node = node.children.get(temp)
            if not node:
                return
            cur_word += temp
            if node.is_word:
                res.append(cur_word)
                node.is_word = False

            board[row][col] = '#'
            # O(4^n), n = longest word length
            for dx, dy in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr, nc = row + dx, col + dy
                if 0 <= nr < M and 0 <= nc < N:
                    dfs(nr, nc, node, cur_word) 
            board[row][col] = temp
        
        # O(m * n)
        for r in range(M):
            for c in range(N):
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root, "")
        return res