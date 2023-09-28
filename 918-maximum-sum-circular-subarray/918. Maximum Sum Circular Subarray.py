class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        cur_min = cur_max = 0
        min_sum = max_sum = nums[0]
        for num in nums:
            cur_max = max(cur_max + num, num)
            cur_min = min(cur_min + num, num)
            max_sum = max(max_sum, cur_max)
            min_sum = min(min_sum, cur_min)
        
        if max_sum > 0:
            return max(max_sum, sum(nums) - min_sum)
        return max_sum
