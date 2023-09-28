class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i, num in enumerate(nums):
            if i > reachable:
                return False
            reachable = max(reachable, i + num)
        return True
            