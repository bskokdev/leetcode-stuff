class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n+1)
        for i in range(1, n+1):
            prefix_sum[i] = prefix_sum[i-1] + nums[i-1]

        pre_occs = defaultdict(int)
        res = 0
        for p_sum in prefix_sum:
            if p_sum - k in pre_occs:
                res += pre_occs[p_sum-k]
            pre_occs[p_sum] += 1
        return res
