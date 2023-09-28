# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(node):
            if not node:
                return 0
            l_depth = depth(node.left)
            r_depth = depth(node.right)
            return 1 + max(l_depth, r_depth)

        if not root:
            return True
        left_height = depth(root.left)
        right_height = depth(root.right)
        if abs(left_height-right_height) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)