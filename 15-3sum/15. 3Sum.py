class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # Handle ith index duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
            cur_target = -num
            left, right = i+1, n-1
            while left < right:
                cur_sum = nums[left] + nums[right]
                # Found a valid triplet
                if cur_sum == cur_target:
                    res.append([num, nums[left], nums[right]])
                    # Skip left index duplicates
                    while left+1 < n and nums[left] == nums[left+1]:
                        left += 1
                    # Skip right index duplicates
                    while right-1 >= 0 and nums[right] == nums[right-1]:
                        right -= 1
                if cur_sum > cur_target:
                    right -= 1
                else:
                    left += 1
        return res
