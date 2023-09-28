class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        cur_sum = left = res = 0
        nums.sort()
        for right in range(len(nums)):
            cur_sum += nums[right]
            if nums[right] * (right-left+1) > cur_sum + k:
                cur_sum -= nums[left]
                left += 1
            res = max(right-left+1, res)
        return res

