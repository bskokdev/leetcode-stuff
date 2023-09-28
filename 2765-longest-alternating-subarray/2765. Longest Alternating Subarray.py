class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for l in range(n):
            dif = 1
            for r in range(l+1, n):
                if nums[r] - nums[r-1] == dif:
                    res = max(res, r-l+1)
                else:
                    break
                dif = -dif
        return -1 if res == 0 else res
            
        