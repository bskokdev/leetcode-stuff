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

    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        List<TreeNode> res = new ArrayList<>();
        serialize(root, new HashMap<>(), res);
        return res;
    }

    public String serialize(TreeNode node, Map<String, Integer> occs, List<TreeNode> res) {
        if (node == null) {
            return "#";
        }
        String hash = "(" + serialize(node.left, occs, res) + node.val + serialize(node.right, occs, res) + ")";

        int count = occs.getOrDefault(hash, 0) + 1;
        occs.put(hash, count);
        if (occs.get(hash) == 2) {
            res.add(node);
        }
        return hash;
    }
}