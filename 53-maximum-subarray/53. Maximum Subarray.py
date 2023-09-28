class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = res = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_sum = max(cur_sum + num, num)
            res = max(cur_sum, res)
        return res