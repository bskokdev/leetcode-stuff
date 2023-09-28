class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = 0, n-1
        res_idx = n-1
        res = [0] * n 
        while left <= right:
            left_pow = nums[left]**2
            right_pow = nums[right]**2
            if left_pow > right_pow:
                res[res_idx] = left_pow
                res_idx -= 1
                left += 1
            else:
                res[res_idx] = right_pow
                res_idx -= 1
                right -= 1
        return res
