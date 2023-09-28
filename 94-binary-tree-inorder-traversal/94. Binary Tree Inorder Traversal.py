# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        ans = []
        def dfs(node, ans):
            if node is None:
                return
            
            dfs(node.left, ans)
            ans.append(node.val)
            dfs(node.right, ans)
        dfs(root, ans)
        return ans
            