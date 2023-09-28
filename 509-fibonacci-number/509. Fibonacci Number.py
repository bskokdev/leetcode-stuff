class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        
        prev_prev, prev = 0, 1
        for i in range(n-1):
            prev_prev, prev = prev, prev_prev + prev
        return prev