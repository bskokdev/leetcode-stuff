class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            # elements are decreasing to the right
            # we need to search to the left
            if nums[mid] > nums[mid+1]:
                right = mid
            # elements are increasing to the right
            # we need to search to the right
            else:
                left = mid + 1
        return left
