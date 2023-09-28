# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def dfs(root, rem):
            if not root:
                return False
            if rem == 0 and not root.left and not root.right:
                return True
            has_left = False
            if root.left:
                has_left = dfs(root.left, rem-root.left.val)
            has_right = False
            if root.right:
                has_right = dfs(root.right, rem-root.right.val)
            return has_left or has_right

        return dfs(root, targetSum-root.val)