class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum = 0
        r_sum = sum(nums)
        for i, num in enumerate(nums):
            r_sum -= num
            if l_sum == r_sum:
                return i
            l_sum += num
        return -1