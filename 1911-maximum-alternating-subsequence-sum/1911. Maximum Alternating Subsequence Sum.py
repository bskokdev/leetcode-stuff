class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        add, sub = nums[0], 0
        for i in range(1, n):
            add = max(add, nums[i]+sub)
            sub = max(sub, add-nums[i])
        return max(add, sub)