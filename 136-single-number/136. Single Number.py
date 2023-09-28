class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for num, c in count.items():
            if c != 2:
                return num
        return float(-inf)