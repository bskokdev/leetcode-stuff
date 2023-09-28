class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        peak = float('-inf')
        stack = []
        for num in nums[::-1]:
            if num < peak:
                return True
            while stack and num > stack[-1]:
                peak = stack.pop()
            stack.append(num)
        return False