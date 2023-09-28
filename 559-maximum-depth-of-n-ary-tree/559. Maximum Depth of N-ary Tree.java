/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public int maxDepth(Node root) {
        int depth = 0;
        if(root == null) return depth;
        Queue<Node> q = new LinkedList();
        q.offer(root);
        while(!q.isEmpty()) {
            depth++;
            int levelSize = q.size();
            for(int i = 0; i < levelSize; i++) {
                Node curr = q.poll();
                for(Node n : curr.children) {
                    if(n != null) q.offer(n);
                }
            }

        }
        return depth;
    }
}