class Solution:
    def climbStairs(self, n: int) -> int:
        prev_prev = prev = 1
        for i in range(2, n+1):
            prev, prev_prev = prev_prev + prev, prev
        return prev