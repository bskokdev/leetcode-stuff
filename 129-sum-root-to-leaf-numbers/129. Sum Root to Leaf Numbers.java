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
    public int sumNumbers(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return sumNumbers(root, "");
    }

    private int sumNumbers(TreeNode curNode, String curNum) {
        if (curNode == null) {
            return 0;
        }
        curNum += curNode.val;
        if (curNode.left == null && curNode.right == null) {
            return Integer.parseInt(curNum);
        }
        return sumNumbers(curNode.left, curNum) + sumNumbers(curNode.right, curNum);
    }
}