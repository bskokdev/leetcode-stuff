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
    public boolean isCompleteTree(TreeNode root) {
        int count = countNodes(root);
        return dfs(root, 1, count);
    }

    private int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return 1 + countNodes(root.left) + countNodes(root.right);
    }

    private boolean dfs(TreeNode root, int i, int totalCount) {
        if (root == null) {
            return true;
        }
        if (i > totalCount) {
            return false;
        }

        return dfs(root.left, i*2, totalCount) && dfs(root.right, i*2+1, totalCount);
    }
}