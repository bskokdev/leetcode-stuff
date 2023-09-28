class Solution:
    def partition(self, nums, lo, hi) -> int:
        pivot = nums[hi]
        idx = lo-1
        for i in range(lo, hi):
            if nums[i] <= pivot:
                idx += 1
                nums[i], nums[idx] = nums[idx], nums[i]
        
        idx += 1
        nums[hi] = nums[idx]
        nums[idx] = pivot
        return idx

    def qs(self, nums, lo, hi) -> None:
        if lo >= hi:
            return
        pivot = self.partition(nums, lo, hi)
        self.qs(nums, pivot+1, hi)
        self.qs(nums, lo, pivot-1)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.qs(nums, 0, len(nums)-1)
        return nums