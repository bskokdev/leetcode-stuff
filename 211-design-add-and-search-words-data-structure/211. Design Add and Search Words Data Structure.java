class TrieNode {
    public char c;
    public TrieNode[] children;
    public boolean isWord;
    
    public TrieNode(char c) {
        this.c = c;
        this.children = new TrieNode[26];
        this.isWord = false;
    }
}

class WordDictionary {
    private TrieNode root;
    
    public WordDictionary() {
        this.root = new TrieNode('\0');
    }
    
    public void addWord(String word) {
        TrieNode cur = this.root;
        for (char c : word.toCharArray()) {
            if (cur.children[c - 'a'] == null) {
                cur.children[c - 'a'] = new TrieNode(c);
            }
            cur = cur.children[c - 'a'];
        }
        cur.isWord = true;
    }
    
    public boolean search(String word) {
        return searchHelper(word, 0, this.root);
    }
    
    public boolean searchHelper(String word, int i, TrieNode cur) {
        if (word.length() == i) {
            return cur.isWord;
        }
        
        char curChar = word.charAt(i);
        if (curChar == '.') {
            for (TrieNode child : cur.children) {
                if (child != null && searchHelper(word, i+1, child)) {
                    return true;
                }
            }
            return false;
        }
        TrieNode next = cur.children[curChar - 'a'];
        return next != null && searchHelper(word, i+1, next);
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary obj = new WordDictionary();
 * obj.addWord(word);
 * boolean param_2 = obj.search(word);
 */