# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(root):
            if not root:
                return [0,0]
            left = dfs(root.left)
            right = dfs(root.right)

            # to get max val including root, we sum its value + max excluding left and right nodes
            including_root = root.val + left[1] + right[1]
            # to get max val excluding root, we take max o
            excluding_root = max(left) + max(right)
            return [including_root, excluding_root]
        return max(dfs(root))
        

