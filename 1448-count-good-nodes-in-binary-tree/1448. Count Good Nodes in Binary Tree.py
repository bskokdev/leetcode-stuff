# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # a node is good if there's a path from root to the node which doesn't contain values > nodel.val (equal val is ok)

        # go left and right using dfs
        # keep track of the largest node value
        # if the cur.val >= largest_val -> ans +=1
        self.ans = 0
        def dfs(node: TreeNode, path_max: int):
            if node is None: return

            if node.val >= path_max:
                self.ans += 1
                path_max = node.val
            
            dfs(node.left, path_max)
            dfs(node.right, path_max)

        dfs(root, root.val)
        return self.ans
            
