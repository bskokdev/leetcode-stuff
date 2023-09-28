class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n-1) // 2
        good = 0
        lookup = defaultdict(int)
        for i, num in enumerate(nums):
            cur_pair = i - num
            good += lookup[cur_pair]
            lookup[cur_pair] += 1
        return total - good
