class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        p_sum = [0] * n 
        p_sum[0] = nums[0]
        for i in range(1, n):
            p_sum[i] = p_sum[i-1] + nums[i]
        return p_sum