# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # do level order traversal
        # for each level store queue[-1] to the ans list
        if root is None:
            return []
        
        ans = []
        queue = collections.deque([root])
        while queue:
            # queue holds nodes in the level
            ans.append(queue[-1].val)
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return ans