class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(nums[:])
                return
            seen = set()
            for j in range(i, n):
                if nums[j] not in seen:
                    nums[i], nums[j] = nums[j], nums[i]
                    dfs(i+1)
                    nums[i], nums[j] = nums[j], nums[i]
                seen.add(nums[j])
        
        dfs(0)
        return res
            