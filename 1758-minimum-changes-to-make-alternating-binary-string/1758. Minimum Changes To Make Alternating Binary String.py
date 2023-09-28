class Solution:
    def minOperations(self, s: str) -> int:
        a = b = 0
        for i, num in enumerate(s):
            if int(num) == i % 2:
                a += 1
            else:
                b += 1
        return min(a, b)

        