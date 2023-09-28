# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root, None)
        queue = collections.deque([root])
        level = 1
        while queue:
            if level == depth - 1:
                for node in queue:
                    cur_left = node.left
                    cur_right = node.right

                    node.left = TreeNode(val, cur_left, None)
                    node.right = TreeNode(val, None, cur_right)
                break
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            level += 1

        return root

