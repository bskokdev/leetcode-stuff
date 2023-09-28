class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k > 0 and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        
        # pop while k is valid
        stack = stack[:len(stack)-k]
        return "".join(stack).lstrip("0") or "0"