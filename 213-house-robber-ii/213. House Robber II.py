class Solution:
    def rob_acyclic(self, nums):
        memo = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = max(dfs(i+2) + nums[i], dfs(i+1))
            return memo[i]
        return dfs(0)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_acyclic(nums[1:]), self.rob_acyclic(nums[:-1]))