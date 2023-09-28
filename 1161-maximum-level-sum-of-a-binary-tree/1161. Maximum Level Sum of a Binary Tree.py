# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        max_sum = float("-inf")
        cur_level = max_sum_level = 0
        while q:
            level_sum = 0
            cur_level += 1
            for _ in range(len(q)):
                cur = q.popleft()
                level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = cur_level
        return max_sum_level