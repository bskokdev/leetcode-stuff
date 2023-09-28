/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        if (root == null) {
            return -1;
        }
        Queue<TreeNode> q = new ArrayDeque<>();
        Map<TreeNode, Integer> nodePos = new HashMap<>();
        q.add(root);
        nodePos.put(root, 0);
        int res = -1;
        while (!q.isEmpty()) {
            int size = q.size();
            int firstIdx = nodePos.get(q.peek());
            int lastIdx = -1;
            for (int i = 0; i < size; i++) {
                TreeNode cur = q.remove();
                int cur_pos = nodePos.get(cur);
                if (cur.left != null) {
                    q.add(cur.left);
                    nodePos.put(cur.left, 2*cur_pos);
                }
                if (cur.right != null) {
                    q.add(cur.right);
                    nodePos.put(cur.right, 2*cur_pos+1);
                }
                lastIdx = cur_pos;
            }
            res = Math.max(res, lastIdx-firstIdx+1);
        }
        return res;
    }
}