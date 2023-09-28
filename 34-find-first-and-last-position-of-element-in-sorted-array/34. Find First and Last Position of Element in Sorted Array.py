class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        def find_left():
            left, right = 0, n-1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                if target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        
        def find_right():
            left, right = 0, n-1
            index = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                if target >= nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return index

        start = find_left()
        end = find_right()
        return [start, end]
        
