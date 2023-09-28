class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        for num, freq in counts.items():
            if freq > (n/2):
                return num
        return -1