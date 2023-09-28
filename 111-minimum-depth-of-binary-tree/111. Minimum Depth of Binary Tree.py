# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ans = 0
        # level order traversal
        queue = collections.deque()
        queue.append(root)
        while queue:
            ans += 1
            for i in range(len(queue)):
                cur = queue.popleft()
                if cur.left is None and cur.right is None:
                    return ans
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return ans